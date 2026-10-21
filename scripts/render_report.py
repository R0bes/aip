#!/usr/bin/env python3
"""Standalone AIP 0.3 report renderer: JSON report -> interactive HTML.

Usage: python scripts/render_report.py examples/report.json /tmp/aip-report.html
Requires jsonschema and referencing; no browser framework or network calls.
"""
import argparse
import html
import json
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]


def validate(report):
    selector = json.loads((ROOT / "run-ui.schema.json").read_text())
    schema = json.loads((ROOT / "report.schema.json").read_text())
    registry = Registry().with_resource(selector["$id"], Resource.from_contents(selector))
    Draft202012Validator(schema, registry=registry).validate(report)
    if "next_run" in report:
        # The validator's semantic invariants apply equally to embedded selectors.
        from validate import validate_semantics
        validate_semantics(report["next_run"])


def render(report):
    validate(report)
    safe = lambda value: html.escape(str(value), quote=True)
    header = report["header"]
    context = " · ".join(safe(header[k]) for k in ("repository", "ref", "run_id") if k in header)
    parts = ['<!doctype html><html lang="en"><meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width,initial-scale=1">',
             '<title>AIP run report</title>',
             '<style>body{font:15px system-ui;max-width:950px;margin:30px auto;padding:0 16px;background:#10131a;color:#e9edf5}',
             '.header,.card{border:2px solid #414756;border-radius:15px;padding:14px;margin:12px 0;background:transparent}',
             '.action{border-color:#3c6670}.action:nth-child(2n){border-color:#695578}.action strong{color:#59cadb}.action:nth-child(2n) strong{color:#bd94e8}',
             '.header{display:flex;justify-content:space-between}.cards{display:flex;flex-wrap:wrap;gap:12px}',
             '.cards .card{flex:1 1 260px;margin:0;cursor:pointer}.muted{color:#a8afc0}',
             'button{cursor:pointer;background:#292f3c;color:inherit;border:1px solid #596073;border-radius:9px;padding:7px}',
             'textarea{box-sizing:border-box;width:100%;background:transparent;color:inherit;border:0;outline:0;box-shadow:none;border-radius:0;padding:3px 0;font:12px/1.35 system-ui;resize:vertical;min-height:24px}',
             'textarea::placeholder{font-size:17px;color:#bec7db}textarea:focus{background:transparent;border:0;outline:0;box-shadow:none}pre{white-space:pre-wrap;overflow-wrap:anywhere}',
             'details{margin-top:8px}summary{cursor:pointer} .result{cursor:pointer} .result pre{cursor:text}',
             '</style><header class="header"><span>⌘ '+context+'</span><span class="muted">AIP '+safe(report["protocol_version"])+'</span></header>']
    for block in report["blocks"]:
        kind = block["type"]
        if kind == "text":
            parts.append('<p>'+safe(block["text"])+'</p>')
            continue
        icon = {"github":"⌁","artifact":"▣","notice":"ⓘ"}[kind]
        title = block.get("title") or (block.get("summary") if kind=="github" else block.get("kind",kind))
        desc = block.get("description") or block.get("summary","") if kind=="github" else block.get("description","")
        parts.append('<section class="card result" tabindex="0" role="button" aria-expanded="false"><strong>'+icon+' '+safe(title)+'</strong>')
        if desc and desc!=title:
            parts.append('<p class="muted">'+safe(desc)+'</p>')
        if kind=="artifact":
            parts.append('<button class="copy" type="button" aria-label="Copy artifact" data-copy="'+safe(block["content"])+'">⧉</button><pre>'+safe(block["content"])+'</pre>')
        details = block.get("details") or block.get("verification") or block.get("text","")
        if details:
            parts.append('<div class="detail" hidden><pre>'+safe(details)+'</pre></div>')
        parts.append('</section>')
    if "next_run" in report and report["next_run"]["actions"]:
        parts.append('<section class="cards" aria-label="Next run actions">')
        for action in report["next_run"]["actions"]:
            parts.append('<article class="card action" tabindex="0" role="button" data-action="'+safe(action["id"])+'"><strong>▷ '+safe(action["title"])+'</strong><span class="muted" style="float:right">'+safe(action["key"])+'</span>')
            if action.get("description"):
                parts.append('<p class="muted">'+safe(action["description"])+'</p>')
            parts.append('<textarea rows="1" aria-label="Supplemental text" placeholder="⧉"></textarea></article>')
        parts.append('</section>')
    # Avoid embedding raw user data into JS: use a JSON script node with escaped '<'.
    data = json.dumps(report, ensure_ascii=False).replace("<", "\\u003c").replace("&", "\\u0026")
    parts.append('<script id="aip-data" type="application/json">'+data+'</script>')
    parts.append("""<script>
const report=JSON.parse(document.getElementById('aip-data').textContent);
document.querySelectorAll('.result').forEach(card=>{
 const toggle=()=>{const detail=card.querySelector('.detail');if(!detail)return;detail.hidden=!detail.hidden;card.setAttribute('aria-expanded',String(!detail.hidden));};
 card.addEventListener('click',e=>{if(e.target.closest('button,pre'))return;toggle();});
 card.addEventListener('keydown',e=>{if((e.key==='Enter'||e.key===' ')&&e.target===card){e.preventDefault();toggle();}});
});
document.querySelectorAll('.copy').forEach(button=>button.addEventListener('click',async e=>{
 e.stopPropagation();try{await navigator.clipboard.writeText(button.dataset.copy);}catch(err){alert('Clipboard unavailable; select the artifact text to copy.');}
}));
document.querySelectorAll('.action').forEach(card=>{
 const run=()=>{
  const action=report.next_run.actions.find(a=>a.id===card.dataset.action);
  const supplemental_text=card.querySelector('textarea').value;
  const payload={protocol_version:report.protocol_version,context:report.next_run.context,action_id:action.id,key:action.key,instruction:action.instruction,parameters:Object.fromEntries((action.parameters||[]).map(p=>[p.id,p.default])),supplemental_text};
  const repoName=report.header.repository||'unspecified';
  const profile='chatgpt/software-development.md';
  const refresh='Read the AIP ChatGPT profile from the repository at the start of this run when access is available. Do not claim a refresh unless performed.';
  const promptParts=[`Repository: ${repoName}`,report.header.ref?`Branch: ${report.header.ref}`:'',`Task: ${action.instruction}`,`Action: ${action.id} (key ${action.key})`,`Context: ${report.next_run.context}`,`Parameters: ${JSON.stringify(payload.parameters)}`,`Supplemental text (verbatim):\\n${supplemental_text}`,`[aip: ${report.protocol_version}; repo: ${repoName}; profile: ${profile}]`,refresh];
  payload.prompt=promptParts.filter(Boolean).join('\\n');
  // No implicit agent execution: host must handle this explicit event.
  card.dispatchEvent(new CustomEvent('aip:invoke',{bubbles:true,detail:payload}));
  document.getElementById('invocation').textContent=JSON.stringify(payload,null,2);
 };
 card.addEventListener('click',e=>{if(e.target.closest('textarea,button'))return;run();});
 card.addEventListener('keydown',e=>{if((e.key==='Enter'||e.key===' ')&&e.target===card){e.preventDefault();run();}});
});
</script><pre id="invocation" aria-live="polite"></pre></html>""")
    return "\n".join(parts)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.write_text(render(json.loads(args.report.read_text())), encoding="utf-8")


if __name__ == "__main__":
    main()
