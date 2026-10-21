# Next Run — accepted hybrid UI

Read [AGENTS.md](../AGENTS.md). This is the **only current Next Run template**. The former HTML experiment is superseded and must not be used. Preserve the agreed visual and interaction model rather than replacing it with a plain DIL input.

## Contract

- Offer a curated number of compact selectable action cards, with 20px icon beside title, small numeric key, useful description and optional action-specific controls. Equal-height siblings; selected card gets only an accent outline and subtle glow. Key `0` continues useful work. Use a scoped HTML AppBlock for cards when needed.
- **One shared real HTML textarea**, initially a **40×40px circular icon**. The idle SVG contains **three audio bars, an I-beam cursor, and a separate lower arrow**. Focusing the textarea expands the *same element* into a normal editable multi-line field. Empty + blurred collapses; nonempty + blurred stays expanded. Normal selection, paste, caret and input must work. A permanently visible DIL `<input>`/`<textarea>` is **not equivalent**.
- To its right, keep **one native DIL `<pressable>`**, 44px circle, with the custom circular-arrow/play SVG in [assets/next-run.svg](../assets/next-run.svg). Only this native control calls `GenUI.issueNewTurn`; AppBlock HTML cannot dispatch a ChatGPT turn.
- DIL owns shared selection, text, action parameters and theme state. Bind AppBlocks through `bind={{value,setValue}}`; `globalThis.__bindings?.…` and `globalThis.__effect?.(…)` must always be optional-chained.
- Include the theme chosen in the header gear panel in the next-run parameters, e.g. `{theme:"Neutral"}`. Theme changes recolor all theme-aware components immediately, using [themes/tokens.csv](../themes/tokens.csv); no persistent settings.
- Dispatch a self-contained request: repository/ref, proposed task, action/key, parameters, proposal context, exact `User instruction (verbatim)` textarea content, AIP footer and the required AGENTS.md refresh instruction. A leading valid `N:` selects that action **without altering the original textarea text**. Never claim HTML-only Enter sends or that file attachments can be forwarded.

## DIL composition (generation template)

This snippet shows the important binding boundary. Replace `UNIQUE` consistently; provide concrete action definitions and actual HTML for the two AppBlocks. The SVG path is identical to `assets/next-run.svg`.

```jsx
{@body const [selection,setSelection]=DIL.useState({selected:"0",params:{"0":{}}})}
{@body const [instruction,setInstruction]=DIL.useState("")}
{@body const [theme,setTheme]=DIL.useState("Neutral")}
{@body const actions=[{id:"0",title:"Weiter",task:"Continue the agreed task.",context:"Preserve approved UI."}]}
<box gap={2}>
  <AppBlock app_block_id="aip-cards-UNIQUE" title="Next Run" variant="inline"
    bind={{value:selection,setValue:setSelection,theme}}>
    <!-- Use the compact accessible cards pattern below. -->
  </AppBlock>
  <row align="center" gap={2}>
    <box flex="1">
      <AppBlock app_block_id="aip-input-UNIQUE" title="Anweisung" variant="inline"
        bind={{value:instruction,setValue:setInstruction,theme}}>
        <!-- Use the complete morphing textarea below. -->
      </AppBlock>
    </box>
    <pressable width="44px" height="44px" background="#F4F5F7"
      border={{size:1,color:"#4B647D"}} radius="full" align="center"
      justify="center" tooltip="Nächsten Run starten" onClick={()=>{
        const prefix=instruction.match(/^\s*([0-9])\s*:/);
        const key=prefix&&actions.some(a=>a.id===prefix[1])?prefix[1]:selection.selected;
        const action=actions.find(a=>a.id===key);
        if(!action)return;
        const params={...(selection.params[key]||{}),theme};
        GenUI.issueNewTurn(
          "Repository: R0bes/aip\nBranch: main\nProposed task: "+action.task+
          "\nAction: "+action.title+"\nKey: "+key+
          "\nParameters: "+JSON.stringify(params)+
          "\nProposal context: "+action.context+
          "\n\nUser instruction (verbatim):\n"+instruction+
          "\n\n[aip: 0.3.0; repo: R0bes/aip; instructions: AGENTS.md]"+
          "\nRead R0bes/aip/AGENTS.md at run start if accessible; apply it throughout this run and carry this instruction into every next-run prompt. If unavailable, say so; never claim an unperformed refresh."
        );
      }}>
      <svg viewBox="0 0 24 24" width="24px" height="24px" fill="none"
        stroke="#4B647D" strokeWidth={1.8} strokeLinecap="round" strokeLinejoin="round">
        <path d="M19.4 8.5A8 8 0 1 0 20 12"/>
        <path d="M19.4 3.9v4.6h-4.6"/>
        <path d="m10 8.8 5 3.2-5 3.2z"/>
      </svg>
    </pressable>
  </row>
</box>
```

Colors above are the Neutral illustration only. Bind the selected theme from the shared header state in the real response; never create a second independent theme state.

## Shared morphing input — AppBlock HTML

```html
<div id="aip-input-UNIQUE">
<style>
#aip-input-UNIQUE .shell{position:relative;box-sizing:border-box;width:40px;height:40px;max-width:100%;overflow:hidden;border:1px solid var(--aip-accent);border-radius:50%;background:var(--aip-surface);transition:width .3s ease,border-radius .3s ease}
#aip-input-UNIQUE .shell.expanded{width:100%;min-height:72px;border-radius:12px}
#aip-input-UNIQUE .symbol{position:absolute;inset:0;display:grid;place-items:center;color:var(--aip-accent);pointer-events:none}
#aip-input-UNIQUE .symbol svg{width:23px;height:23px}
#aip-input-UNIQUE .expanded .symbol{display:none}
#aip-input-UNIQUE textarea{position:absolute;inset:0;box-sizing:border-box;width:100%;height:100%;border:0!important;outline:0!important;background:transparent!important;box-shadow:none!important;resize:none;padding:10px 12px;color:var(--aip-text)!important;font:13px/1.5 system-ui;caret-color:var(--aip-accent);opacity:0;cursor:text}
#aip-input-UNIQUE .expanded textarea{opacity:1}
@media(prefers-reduced-motion:reduce){#aip-input-UNIQUE .shell{transition:none}}
</style>
<div class="shell">
  <div class="symbol"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <path d="M3 8v5 M6 5v11 M9 8v5"/>
    <path d="M12 5h5 M14.5 5v11 M12 16h5"/>
    <path d="M2 20h20 M19 17l3 3-3 3"/>
  </svg></div>
  <textarea aria-label="Zusätzliche Anweisung" placeholder="Zusätzliche Anweisung …"></textarea>
</div>
<script>
(()=>{
const root=document.getElementById("aip-input-UNIQUE");
const shell=root.querySelector(".shell"),field=root.querySelector("textarea");
const palettes={
  Pastel:["#EEE5FA","#35374D","#866ACB"],
  Cyberpunk:["#141824","#EEF5FF","#50E4DD"],
  Neutral:["#F4F5F7","#232833","#4B647D"]
};
function render(){
  const p=palettes[globalThis.__bindings?.theme]||palettes.Pastel;
  ["--aip-surface","--aip-text","--aip-accent"].forEach((name,i)=>root.style.setProperty(name,p[i]));
  shell.classList.toggle("expanded",document.activeElement===field||field.value.length>0);
}
field.addEventListener("focus",render);
field.addEventListener("blur",render);
field.addEventListener("input",()=>{render();globalThis.__bindings?.setValue?.(field.value)});
globalThis.__effect?.(()=>{
  const v=globalThis.__bindings?.value;
  if(typeof v==="string"&&v!==field.value)field.value=v;
  render();
});
render();
})();
</script>
</div>
```

The inline palette literals are generated examples copied from the authoritative CSV; update them whenever `themes/tokens.csv` changes. They are not an independent token source.

## Compact selectable cards — AppBlock HTML

```html
<div id="aip-cards-UNIQUE">
<style>
#aip-cards-UNIQUE .cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:9px;align-items:stretch}
#aip-cards-UNIQUE .card{position:relative;box-sizing:border-box;min-width:0;padding:13px;border:1px solid var(--aip-border);border-radius:10px;background:var(--aip-surface);color:var(--aip-text);cursor:pointer;font-family:system-ui}
#aip-cards-UNIQUE .card[aria-pressed=true]{border:2px solid var(--aip-accent);padding:12px;box-shadow:0 0 10px var(--aip-glow)}
#aip-cards-UNIQUE .head{display:flex;align-items:center;gap:8px;font-size:13px;font-weight:650}
#aip-cards-UNIQUE .head svg{width:20px;height:20px;flex-shrink:0;color:var(--aip-accent)}
#aip-cards-UNIQUE .key{position:absolute;right:10px;top:9px;font-size:10px;color:var(--aip-muted)}
#aip-cards-UNIQUE .desc{font-size:11px;line-height:1.5;color:var(--aip-muted);margin-top:7px}
@media(max-width:390px){#aip-cards-UNIQUE .cards{grid-template-columns:1fr}}
</style>
<div class="cards">
  <div class="card" role="button" tabindex="0" data-key="0" aria-pressed="true">
    <span class="key">0</span><div class="head"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>Weiter</div>
    <div class="desc">Nächsten vereinbarten Schritt ausführen.</div>
  </div>
  <div class="card" role="button" tabindex="0" data-key="1" aria-pressed="false">
    <span class="key">1</span><div class="head"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="11" cy="11" r="7"/><path d="m16 16 5 5"/></svg>Prüfen</div>
    <div class="desc">Aktuellen Stand und Risiken prüfen.</div>
  </div>
</div>
<script>
(()=>{
const root=document.getElementById("aip-cards-UNIQUE");
const palettes={
  Pastel:["#EEE5FA","#35374D","#626B81","#B8ACCE","#866ACB","#8E78C650"],
  Cyberpunk:["#141824","#EEF5FF","#A7B7C9","#4D6075","#50E4DD","#50E4DD50"],
  Neutral:["#F4F5F7","#232833","#626B76","#C5CAD2","#4B647D","#4B647D20"]
};
let state={selected:"0",params:{"0":{},"1":{}}};
function render(){
 const p=palettes[globalThis.__bindings?.theme]||palettes.Pastel;
 ["--aip-surface","--aip-text","--aip-muted","--aip-border","--aip-accent","--aip-glow"].forEach((name,i)=>root.style.setProperty(name,p[i]));
 root.querySelectorAll(".card").forEach(c=>c.setAttribute("aria-pressed",String(c.dataset.key===state.selected)));
}
function select(key){state={...state,selected:key};render();globalThis.__bindings?.setValue?.(state)}
root.querySelectorAll(".card").forEach(c=>{
 c.addEventListener("click",()=>select(c.dataset.key));
 c.addEventListener("keydown",e=>{if(e.key==="Enter"||e.key===" "){e.preventDefault();select(c.dataset.key)}});
});
globalThis.__effect?.(()=>{const v=globalThis.__bindings?.value;if(v&&typeof v==="object"&&v.params)state=v;render()});
render();
})();
</script>
</div>
```

Replace example actions and card content together; only include meaningful choices. More elaborate action-specific controls are optional and must update their own parameter state without changing other actions.

## Verification checklist

- [ ] Empty, unfocused textarea is the 40px circle with the approved SVG.
- [ ] Focus expands the **same** textarea; typing, paste, selection and multiline editing work.
- [ ] Blur preserves nonempty text and expanded state; empty blur collapses.
- [ ] Theme selection changes header, cards, textarea and native pressable consistently.
- [ ] Card selection is exclusive and keyboard accessible.
- [ ] Native pressable dispatches the selected key, selected theme and unchanged instruction.
- [ ] No AppBlock send button, no personal agent rules and no persistent settings.

Repository text review is not equivalent to a successful live UI interaction test.
