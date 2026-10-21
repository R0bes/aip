# Next Run · accepted hybrid UI template

This is the accepted AIP Next Run presentation. It supersedes the older native per-card textarea and the exploratory layouts in `next-run-html-experiment.md`. Read `AGENTS.md` at the start of each run. This file is a **generation template**, not an importable component or standalone renderer.

## Visual contract

- Use a curated **single-digit number of meaningful cards**, not a fixed count. Each card has the same structural principles: aligned icon/title and a small numbered key, a concise description, and concrete bullet points or numbered deliverables. Optional controls (thin labeled slider, checkboxes, radio buttons, round color pickers, editable palette swatches) appear **inside the relevant card**, not in a detached panel. Icons use consistent sizing around 20px (80% of the 25px experiment).
- Layout: cards in a horizontal row share height; cards in a vertical stack share width. Nested row/column groups are allowed (e.g. one tall card beside two stacked cards). Use content-driven sizing without arbitrary minimum heights; avoid large blank areas by keeping descriptions concise, positioning controls directly after related content, and selecting sensible grouping rather than forcing every card into a tall uniform rectangle. Do not use `margin-top:auto` on controls. A single intentional line break or concise copy can substantially improve packing.\n- Soft pastel lavender/cyan gradients, rounded corners, compact spacing. The **only selection indicator** is a stronger outline and subtle glow; no dots, checkmarks or radio indicators.
- One **shared** HTML textarea beneath the cards: entirely transparent, no field background, outline, border, label or container decoration; only the `💬` placeholder. Auto-grow as content is entered.
- One **native**, accessible, icon-only rocket button to the immediate right of that input. Only the native button dispatches to ChatGPT.
- HTML cards and HTML textarea each use an independent AppBlock with separate `bind` state. The cards binding also carries a structured `params` object for optional per-action controls. Selection is exclusive; interacting with a control selects its parent action. The native button reads selected action, matching action parameters and unchanged text. Serialize **only the selected action's parameters**.\n- Use a thin slider track with visible labeled steps; use circular color pickers without visible hex codes. Multiple pickers and selectable proposed color palettes may be shown together; choosing a palette populates editable color roles. A single base-color picker may instead request palette generation on the next run. These are optional controls, never mandatory decoration.\n- For a leading valid `N:` action prefix in the shared input, resolve that action for dispatch while preserving the complete original input in `User instruction (verbatim)`.
- The selected action determines task, key and context; preserve the user's textarea value byte-for-byte in the `User instruction (verbatim)` section. Explicit user instructions take precedence over proposed defaults, subject to higher-priority constraints.
- HTML cannot directly invoke `GenUI.issueNewTurn`, and pressing Enter inside AppBlock cannot invoke the native rocket. No fake submit control or claimed attachment support.

## Response composition (adapt the concrete choices and unique IDs)

```jsx
{@body const [selected,setSelected]=DIL.useState("0")}\n{@body const [params,setParams]=DIL.useState({})}
{@body const [instruction,setInstruction]=DIL.useState("")}
{@body const choices=[
  {id:"0",title:"Weiter",task:"Continue the agreed work.",context:"Continue the existing work."},
  {id:"1",title:"Alternative prüfen",task:"Evaluate a meaningful alternative.",context:"Compare an alternative."},
  {id:"2",title:"Verbessern",task:"Implement a specific improvement.",context:"Deliver an improvement."}
]}
<AppBlock app_block_id="aip-choice-UNIQUE" title="Next Run" variant="inline"
  bind={{value:{selected,params},setValue:v=>{if(v&&typeof v==='object'){if(typeof v.selected==='string')setSelected(v.selected);if(v.params)setParams(v.params)}}}}>
  <!-- Insert the HTML cards from below, replacing the UNIQUE root ID and card content. -->
</AppBlock>
<row align="center" gap={2}>
  <box flex="1">
    <AppBlock app_block_id="aip-input-UNIQUE" title="Anweisung" variant="inline"
      bind={{value:instruction,setValue:setInstruction}}>
      <!-- Insert the HTML input from below, replacing the UNIQUE root ID. -->
    </AppBlock>
  </box>
  <button size="lg" uniform color="primary" label="Ausgewählten nächsten Run starten"
    onClick={()=>{
      const prefix=instruction.match(/^\\s*([0-9])\\s*:/);\n      const effectiveKey=prefix&&choices.some(x=>x.id===prefix[1])?prefix[1]:selected;\n      const action=choices.find(x=>x.id===effectiveKey);
      if(!action)return;
      GenUI.issueNewTurn(
        "Repository: R0bes/aip\nBranch: main\nProposed task: "+action.task+
        "\nAction: "+action.title+"\nKey: "+action.id+
        "\nParameters: {}\nProposal context: "+action.context+
        "\n\nUser instruction (verbatim):\n"+instruction+
        "\n\n[aip: 0.3.0; repo: R0bes/aip; instructions: AGENTS.md]"+
        "\nRead R0bes/aip/AGENTS.md at run start if accessible; apply it throughout this run and carry this instruction into every next-run prompt. If unavailable, say so; never claim an unperformed refresh."
      );
    }}>
    <icon name="rocket"/>
  </button>
</row>
```

The repository/ref and AIP metadata above are examples; replace with the actual verified target repository and branch/ref. Keep the AIP source instruction pointing to `R0bes/aip/AGENTS.md`.

## HTML cards (first AppBlock)

```html
<div id="aip-choice-UNIQUE" style="font-family:system-ui;padding:3px 2px">
<style>
#aip-choice-UNIQUE .cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:9px;align-items:stretch}
#aip-choice-UNIQUE .card{display:flex;flex-direction:column;min-width:0;text-align:left;border:1.5px solid #b6accd;border-radius:13px;padding:12px 10px;color:#35374d;cursor:pointer;background:linear-gradient(145deg,#eee5fa,#dfe9f6)}
#aip-choice-UNIQUE .card:nth-child(2){background:linear-gradient(145deg,#e1f0f4,#e4e8f8)}
#aip-choice-UNIQUE .card:nth-child(3){background:linear-gradient(145deg,#f1e5f0,#eae9f8)}
#aip-choice-UNIQUE .card[aria-pressed=true]{border:2px solid #866acb;box-shadow:0 0 0 2px #a58de639,0 4px 16px #8e78c650}
#aip-choice-UNIQUE .head{display:flex;align-items:center;gap:7px}
#aip-choice-UNIQUE .glyph{font-size:20px;color:#6950a0;flex:none;display:grid;place-items:center;width:24px;height:24px}
#aip-choice-UNIQUE .name{font-size:12px;font-weight:700;line-height:1.3}
#aip-choice-UNIQUE .desc{font-size:10.5px;color:#67718b;line-height:1.4;margin-top:5px}
</style>
<div class="cards">
<button type="button" class="card" data-id="0" aria-pressed="true"><span class="head"><span class="glyph">⌘</span><span class="name">Weiter</span></span><span class="desc">Vereinbarten nächsten Schritt umsetzen</span></button>
<button type="button" class="card" data-id="1" aria-pressed="false"><span class="head"><span class="glyph">◇</span><span class="name">Alternative prüfen</span></span><span class="desc">Eine sinnvolle Alternative bewerten</span></button>
<button type="button" class="card" data-id="2" aria-pressed="false"><span class="head"><span class="glyph">✧</span><span class="name">Verbessern</span></span><span class="desc">Konkrete Verbesserung umsetzen</span></button>
</div>
</div>
<script>
(()=>{
const root=document.getElementById('aip-choice-UNIQUE');
const cards=[...root.querySelectorAll('.card')];
const render=id=>cards.forEach(c=>c.setAttribute('aria-pressed',String(c.dataset.id===id)));
cards.forEach(c=>c.addEventListener('click',()=>{render(c.dataset.id);globalThis.__bindings?.setValue?.(c.dataset.id)}));
globalThis.__effect?.(()=>{const v=globalThis.__bindings?.value;if(typeof v==='string')render(v)});
})();
</script>
```

## HTML shared input (second AppBlock)

```html
<div id="aip-input-UNIQUE">
<style>
#aip-input-UNIQUE textarea{display:block;width:100%;min-height:32px;max-height:150px;resize:none;overflow-y:auto;border:0!important;outline:0!important;background:transparent!important;box-shadow:none!important;padding:6px 2px;color:inherit;font:14px system-ui;line-height:1.5}
#aip-input-UNIQUE textarea::placeholder{color:#9887bf;opacity:1}
</style>
<textarea rows="1" placeholder="💬" aria-label="Zusätzliche Anweisung"></textarea>
</div>
<script>
(()=>{
const f=document.querySelector('#aip-input-UNIQUE textarea');
f.addEventListener('input',()=>{f.style.height='auto';f.style.height=Math.min(f.scrollHeight,150)+'px';globalThis.__bindings?.setValue?.(f.value)});
globalThis.__effect?.(()=>{const v=globalThis.__bindings?.value;if(typeof v==='string'&&f.value!==v)f.value=v});
})();
</script>
```

**The three-card HTML snippet above is a minimal illustration, not the complete parameterized card gallery.** For richer options, render bullet/ordered lists and appropriate controls within each card; bind `{selected,params}` and update the parent action on control interaction. Do not misrepresent the simple snippet as a tested fully featured renderer.\n\nDo not present the placeholders or sample tasks as real project-specific recommendations. Choose concrete useful options based on the current work. Do not claim a responsive layout or general design system is approved.
