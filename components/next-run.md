# Next Run — accepted hybrid template

## Shared theme application

Use the semantic tokens from [themes/README.md](../themes/README.md). The accepted Cyberpunk variant uses cyan (#50E4DD), dark translucent surfaces, and subtle glow. The shared textarea itself morphs between a circular 40×40 icon state and an expanded editing state. Its circular shell and the native Next Run button should appear visually coordinated; host-native Next Run trigger colors cannot be forced by AppBlock CSS. Do not pretend CSS crosses AppBlock/native boundaries.

The circular icon is an SVG with three audio bars, a nearby I-beam cursor and a separate horizontal arrow beneath both. It is decorative: **the circle is the actual textarea, not a separate insert or expand button**. Focusing it expands the same textarea; typing and clipboard paste use ordinary browser caret/selection behavior. When empty and unfocused it collapses. Preserve text when blurred; a nonempty field stays expanded.

The final preview was Cyberpunk; Pastel and Neutral can reuse the same interaction with theme-specific colors. Avoid extra renderers, state persistence or infrastructure.

## Contract

- Curate a meaningful single-digit number of actions; do not pad to a fixed count. Key `0` is useful continuation where applicable. Each card has a small key in the corner, a consistently sized **20px icon** beside the title, a concise description and specific bullet points or numbered steps.
- Cards in a **horizontal group share height**; cards in a **vertical group share width**. Nested horizontal/vertical groups are permitted (one tall card next to two stacked cards). Prefer content-aware grouping and concise copy; avoid artificial minimum heights and `margin-top:auto` on controls. A row may have modest empty space to preserve equal height; avoid large unused areas.
- All cards share the same basic composition. Add controls **only when meaningful**: a fine-line slider with *visible* step labels, checkboxes, radio buttons, round color pickers without hex labels, selectable editable color palettes, or a single base color for palette generation on the next run. Controls belong **inside** their card and select that action when changed. Use accessible native HTML input semantics.
- Selection is exclusive and indicated **only** by a stronger outline and subtle glow. Do not add selection dots, checkmarks or badges. Keep softly tinted lavender/cyan surfaces.
- Use one shared real HTML textarea inside a morphing 40px circular shell. Empty/unfocused: show the agreed SVG centered, hide the caret and text. Focused or nonempty: smoothly expand to available width, hide the icon, expose normal text and caret; support direct typing, selection, Ctrl+V and multiple lines. Keep a single **native** icon-only Next Run pressable to its right, with the custom circular-arrow/play SVG from [`assets/next-run.svg`](../assets/next-run.svg). HTML may update bound text but **cannot dispatch** a ChatGPT turn. Only the native Next Run trigger invokes `GenUI.issueNewTurn`.
- Keep selected key, parameter values and input text in DIL state. A valid leading `N:` prefix in the shared text overrides the clicked card at dispatch, without stripping or altering **any** text from `User instruction (verbatim)`. Include only the effective action's parameters in the handoff.
- No file attachments or Enter-to-send through AppBlock. Do not claim runtime verification merely because a template is committed.

## Complete example: four cards with different controls

The example intentionally demonstrates **one slider, checkboxes, radio buttons and an editable five-color palette**. These are independent optional card capabilities, not a mandatory set. For fewer or more choices, change the markup and action definitions together; use a row, stack, or nested composition as appropriate.

### DIL response structure\n\nThe native pressable uses the same SVG paths as [`assets/next-run.svg`](../assets/next-run.svg), inlined as a DIL `<svg>` child. Preserve the native `<pressable>` and its `GenUI.issueNewTurn` callback. The icon uses the explicit Cyberpunk accent `#50E4DD`; the native pressable uses a 44px circular dark-blue surface and cyan border. Do not substitute an HTML button.\n

```jsx
{@body const [choiceState,setChoiceState]=DIL.useState({
  selected:"0",
  params:{
    "0":{research_depth:2},
    "1":{optional_work:["tests"]},
    "2":{strategy:"reuse"},
    "3":{palette:"Neon Mist",colors:["#9478d6","#54b5c6","#f3a86a","#252b43","#e9e7f5"]}
  }
})}
{@body const [instruction,setInstruction]=DIL.useState("")}
{@body const actions=[
  {id:"0",title:"Weiter recherchieren",task:"Review existing maintained solutions and relevant repository code to the selected depth.",context:"Reuse before build."},
  {id:"1",title:"Hybrid-UI erweitern",task:"Implement the agreed AIP Next Run enhancements with the selected optional work.",context:"Keep accepted visuals."},
  {id:"2",title:"Ansatz prüfen",task:"Evaluate the chosen implementation strategy and its maintenance tradeoffs.",context:"Avoid unnecessary infrastructure."},
  {id:"3",title:"Farbkonzept testen",task:"Explore the selected editable five-color palette without changing the accepted default.",context:"Experimental palette only."}
]}
<box gap={2}>
  <AppBlock app_block_id="aip-cards-UNIQUE" title="Next Run" variant="inline"
    bind={{value:choiceState,setValue:setChoiceState}}>
    <!-- Paste the complete card HTML below; replace UNIQUE in all IDs. -->
  </AppBlock>
  <row align="center" gap={2}>
    <box flex="1">
      <AppBlock app_block_id="aip-input-UNIQUE" title="Anweisung" variant="inline"
        bind={{value:instruction,setValue:setInstruction}}>
        <!-- Paste the shared-input HTML below; replace UNIQUE in all IDs. -->
      </AppBlock>
    </box>
    <pressable width="44px" height="44px" background="#1B3746" border={{size:1,color:"#50E4DD"}} radius="full" align="center" justify="center" tooltip="Ausgewählten nächsten Run starten"
      onClick={()=>{
        const prefix=instruction.match(/^\s*([0-9])\s*:/);
        const key=prefix&&actions.some(a=>a.id===prefix[1])?prefix[1]:choiceState.selected;
        const action=actions.find(a=>a.id===key);
        if(!action)return;
        const parameters=choiceState.params[key]||{};
        GenUI.issueNewTurn(
          "Repository: R0bes/aip\nBranch: main\nProposed task: "+action.task+
          "\nAction: "+action.title+"\nKey: "+key+
          "\nParameters: "+JSON.stringify(parameters)+
          "\nProposal context: "+action.context+
          "\n\nUser instruction (verbatim):\n"+instruction+
          "\n\n[aip: 0.3.0; repo: R0bes/aip; instructions: AGENTS.md]"+
          "\nRead R0bes/aip/AGENTS.md at run start if accessible; apply it throughout this run and carry this instruction into every next-run prompt. If unavailable, say so; never claim an unperformed refresh."
        );
      }}>
      <svg viewBox="0 0 24 24" width="23px" height="23px" fill="none" stroke="#50E4DD" strokeWidth={1.8} strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">\n        <path d="M19.4 8.5A8 8 0 1 0 20 12"/>\n        <path d="M19.4 3.9v4.6h-4.6"/>\n        <path d="m10 8.8 5 3.2-5 3.2z"/>\n      </svg>
    </pressable>
  </row>
</box>
```

### Cards AppBlock HTML

```html
<div id="aip-cards-UNIQUE">
<style>
#aip-cards-UNIQUE{font-family:system-ui;color:#37384c;padding:3px}
#aip-cards-UNIQUE .cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px;align-items:stretch}
#aip-cards-UNIQUE .card{min-width:0;display:flex;flex-direction:column;gap:8px;padding:13px;border:1.5px solid #b8acce;border-radius:14px;background:linear-gradient(145deg,#eee5fa,#dfe9f6)}
#aip-cards-UNIQUE .card:nth-child(2){background:linear-gradient(145deg,#e1f0f4,#e4e8f8)}
#aip-cards-UNIQUE .card:nth-child(3){background:linear-gradient(145deg,#e6eaf8,#dcebf2)}
#aip-cards-UNIQUE .card:nth-child(4){background:linear-gradient(145deg,#f1e5f0,#eae9f8)}
#aip-cards-UNIQUE .card[aria-pressed=true]{border:2px solid #866acb;box-shadow:0 0 0 2px #a58de639,0 4px 16px #8e78c650}
#aip-cards-UNIQUE .head{display:flex;align-items:center;gap:7px;cursor:pointer}
#aip-cards-UNIQUE .glyph{width:23px;height:23px;display:grid;place-items:center;flex:none;color:#7654a5;font-size:20px}
#aip-cards-UNIQUE .name{font-size:12px;font-weight:700;line-height:1.3;flex:1}
#aip-cards-UNIQUE .key{font-size:10px;color:#8a7a9f;font-weight:700;align-self:flex-start}
#aip-cards-UNIQUE .desc{font-size:11px;line-height:1.45;color:#626b81}
#aip-cards-UNIQUE ul,#aip-cards-UNIQUE ol{padding-left:17px;margin:0;color:#59627a;font-size:10.5px;line-height:1.6}
#aip-cards-UNIQUE .control{border-top:1px solid #9582b744;padding-top:8px}
#aip-cards-UNIQUE .control-title{font-size:10.5px;font-weight:700;color:#665887;margin-bottom:7px}
#aip-cards-UNIQUE .range{width:100%;appearance:none;-webkit-appearance:none;background:transparent;cursor:pointer;margin:4px 0 7px}
#aip-cards-UNIQUE .range::-webkit-slider-runnable-track{height:2px;background:#a698c4;border-radius:10px}
#aip-cards-UNIQUE .range::-moz-range-track{height:2px;background:#a698c4;border-radius:10px}
#aip-cards-UNIQUE .range::-webkit-slider-thumb{-webkit-appearance:none;width:12px;height:12px;border-radius:50%;background:#866acb;border:2px solid #fff;margin-top:-5px}
#aip-cards-UNIQUE .range::-moz-range-thumb{width:10px;height:10px;border-radius:50%;background:#866acb;border:2px solid #fff}
#aip-cards-UNIQUE .steps{display:flex;justify-content:space-between;gap:3px}
#aip-cards-UNIQUE .step{font-size:9px;color:#7a7c91;text-align:center;cursor:pointer;flex:1}
#aip-cards-UNIQUE .step.current{color:#6a4fa7;font-weight:800}
#aip-cards-UNIQUE .opt{display:flex;align-items:center;gap:7px;font-size:11px;margin:5px 0;cursor:pointer}
#aip-cards-UNIQUE input[type=checkbox],#aip-cards-UNIQUE input[type=radio]{accent-color:#886ac5}
#aip-cards-UNIQUE .palettes{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px;margin-bottom:8px}
#aip-cards-UNIQUE .palette{border:1px solid #b9b0c9;border-radius:8px;padding:6px 3px;background:#ffffff60;cursor:pointer}
#aip-cards-UNIQUE .palette[aria-pressed=true]{outline:2px solid #886ac5}
#aip-cards-UNIQUE .swatches{display:flex;gap:2px;justify-content:center}
#aip-cards-UNIQUE .swatches i{width:14px;height:14px;border-radius:3px}
#aip-cards-UNIQUE .palette-name{display:block;font-size:9px;margin-top:5px;color:#64647d}
#aip-cards-UNIQUE .pickers{display:flex;justify-content:space-between;gap:4px}
#aip-cards-UNIQUE .picker-item{display:flex;flex-direction:column;align-items:center;gap:4px;min-width:0}
#aip-cards-UNIQUE .picker-item span{font-size:9px;color:#64647d}
#aip-cards-UNIQUE .picker{appearance:none;-webkit-appearance:none;width:28px;height:28px;border:2px solid white;border-radius:50%;padding:0;overflow:hidden;cursor:pointer;box-shadow:0 0 0 1px #a7a0bc;background:transparent}
#aip-cards-UNIQUE .picker::-webkit-color-swatch-wrapper{padding:0}
#aip-cards-UNIQUE .picker::-webkit-color-swatch{border:0;border-radius:50%}
#aip-cards-UNIQUE .picker::-moz-color-swatch{border:0;border-radius:50%}
</style>
<div class="cards">
<section class="card" data-id="0" role="button" tabindex="0" aria-pressed="true">
 <div class="head"><span class="glyph" aria-hidden="true">⌕</span><span class="name">Weiter recherchieren</span><span class="key">0</span></div>
 <div class="desc">Vorhandene Ansätze vergleichen, bevor wir eigene Logik entwickeln.</div>
 <ul><li>Repository prüfen</li><li>Libraries vergleichen</li><li>Reuse-vs-Build-Empfehlung</li></ul>
 <div class="control"><div class="control-title">Research Depth</div>
 <input class="range" type="range" min="1" max="4" step="1" value="2" aria-label="Research Depth" data-depth/>
 <div class="steps"><span class="step" data-step="1">Schnell</span><span class="step current" data-step="2">Standard</span><span class="step" data-step="3">Gründlich</span><span class="step" data-step="4">Tiefgehend</span></div></div>
</section>
<section class="card" data-id="1" role="button" tabindex="0" aria-pressed="false">
 <div class="head"><span class="glyph" aria-hidden="true">⌘</span><span class="name">Hybrid-UI erweitern</span><span class="key">1</span></div>
 <div class="desc">Die vereinbarte Vorlage gezielt ergänzen.</div>
 <ul><li>Parameter korrekt übergeben</li><li>Bestehendes Design bewahren</li></ul>
 <div class="control"><div class="control-title">Zusätzliche Arbeiten</div>
 <label class="opt"><input type="checkbox" data-check="tests" checked/> Regressionstests</label>
 <label class="opt"><input type="checkbox" data-check="docs"/> Dokumentation</label>
 <label class="opt"><input type="checkbox" data-check="review"/> Code-Review</label></div>
</section>
<section class="card" data-id="2" role="button" tabindex="0" aria-pressed="false">
 <div class="head"><span class="glyph" aria-hidden="true">◇</span><span class="name">Ansatz prüfen</span><span class="key">2</span></div>
 <div class="desc">Integrationsstrategie mit klaren Vor- und Nachteilen festlegen.</div>
 <ol><li>Alternativen bewerten</li><li>Aufwand vergleichen</li><li>Entscheidung begründen</li></ol>
 <div class="control"><div class="control-title">Strategie</div>
 <label class="opt"><input type="radio" name="aip-strategy-UNIQUE" value="reuse" checked/> Bausteine nutzen</label>
 <label class="opt"><input type="radio" name="aip-strategy-UNIQUE" value="custom"/> Eigenbau</label>
 <label class="opt"><input type="radio" name="aip-strategy-UNIQUE" value="compare"/> Ergebnisoffen</label></div>
</section>
<section class="card" data-id="3" role="button" tabindex="0" aria-pressed="false">
 <div class="head"><span class="glyph" aria-hidden="true">✧</span><span class="name">Farbkonzept testen</span><span class="key">3</span></div>
 <div class="desc">Eine vorgeschlagene Palette auswählen und individuell anpassen.</div>
 <div class="control"><div class="control-title">Vorgeschlagene Paletten</div>
 <div class="palettes">
 <button type="button" class="palette" data-palette="0" aria-pressed="true"><span class="swatches"><i style="background:#9478d6"></i><i style="background:#54b5c6"></i><i style="background:#f3a86a"></i><i style="background:#252b43"></i><i style="background:#e9e7f5"></i></span><span class="palette-name">Neon Mist</span></button>
 <button type="button" class="palette" data-palette="1" aria-pressed="false"><span class="swatches"><i style="background:#ff6b9a"></i><i style="background:#54d6bc"></i><i style="background:#f5c36b"></i><i style="background:#20263c"></i><i style="background:#dce6f5"></i></span><span class="palette-name">Synthwave</span></button>
 <button type="button" class="palette" data-palette="2" aria-pressed="false"><span class="swatches"><i style="background:#7c9e85"></i><i style="background:#d7a56d"></i><i style="background:#b983a7"></i><i style="background:#303c3a"></i><i style="background:#ede8dc"></i></span><span class="palette-name">Mineral</span></button>
 </div><div class="control-title">Einzelfarben</div><div class="pickers">
 <label class="picker-item"><input class="picker" type="color" data-color="0" value="#9478d6" aria-label="Primärfarbe"/><span>Primär</span></label>
 <label class="picker-item"><input class="picker" type="color" data-color="1" value="#54b5c6" aria-label="Sekundärfarbe"/><span>Sekundär</span></label>
 <label class="picker-item"><input class="picker" type="color" data-color="2" value="#f3a86a" aria-label="Akzentfarbe"/><span>Akzent</span></label>
 <label class="picker-item"><input class="picker" type="color" data-color="3" value="#252b43" aria-label="Textfarbe"/><span>Text</span></label>
 <label class="picker-item"><input class="picker" type="color" data-color="4" value="#e9e7f5" aria-label="Flächenfarbe"/><span>Fläche</span></label>
 </div></div>
</section>
</div>
</div>
<script>
(()=>{
const root=document.getElementById("aip-cards-UNIQUE");
const cards=[...root.querySelectorAll(".card")];
const palettes=[
 {name:"Neon Mist",colors:["#9478d6","#54b5c6","#f3a86a","#252b43","#e9e7f5"]},
 {name:"Synthwave",colors:["#ff6b9a","#54d6bc","#f5c36b","#20263c","#dce6f5"]},
 {name:"Mineral",colors:["#7c9e85","#d7a56d","#b983a7","#303c3a","#ede8dc"]}
];
let state={selected:"0",params:{"0":{research_depth:2},"1":{optional_work:["tests"]},"2":{strategy:"reuse"},"3":{palette:"Neon Mist",colors:[...palettes[0].colors]}}};
const emit=()=>globalThis.__bindings?.setValue?.({selected:state.selected,params:state.params});
const select=id=>{state.selected=id;render();emit()};
function render(){
 cards.forEach(c=>c.setAttribute("aria-pressed",String(c.dataset.id===state.selected)));
 root.querySelector("[data-depth]").value=state.params["0"].research_depth;
 root.querySelectorAll("[data-step]").forEach(e=>e.classList.toggle("current",Number(e.dataset.step)===state.params["0"].research_depth));
 root.querySelectorAll("[data-check]").forEach(e=>e.checked=state.params["1"].optional_work.includes(e.dataset.check));
 root.querySelectorAll('input[type="radio"]').forEach(e=>e.checked=e.value===state.params["2"].strategy);
 root.querySelectorAll("[data-palette]").forEach(e=>e.setAttribute("aria-pressed",String(palettes[Number(e.dataset.palette)].name===state.params["3"].palette)));
 root.querySelectorAll("[data-color]").forEach(e=>e.value=state.params["3"].colors[Number(e.dataset.color)]);
}
cards.forEach(c=>{
 c.addEventListener("click",e=>{if(e.target.closest("input,label,button,[data-step]"))return;select(c.dataset.id)});
 c.addEventListener("keydown",e=>{if(e.target===c&&(e.key==="Enter"||e.key===" ")){e.preventDefault();select(c.dataset.id)}});
});
root.querySelector("[data-depth]").addEventListener("input",e=>{state.params["0"]={research_depth:Number(e.target.value)};select("0")});
root.querySelectorAll("[data-step]").forEach(e=>e.addEventListener("click",()=>{state.params["0"]={research_depth:Number(e.dataset.step)};select("0")}));
root.querySelectorAll("[data-check]").forEach(e=>e.addEventListener("change",()=>{state.params["1"]={optional_work:[...root.querySelectorAll("[data-check]:checked")].map(x=>x.dataset.check)};select("1")}));
root.querySelectorAll('input[type="radio"]').forEach(e=>e.addEventListener("change",()=>{state.params["2"]={strategy:e.value};select("2")}));
root.querySelectorAll("[data-palette]").forEach(e=>e.addEventListener("click",()=>{const p=palettes[Number(e.dataset.palette)];state.params["3"]={palette:p.name,colors:[...p.colors]};select("3")}));
root.querySelectorAll("[data-color]").forEach(e=>e.addEventListener("input",()=>{state.params["3"]={palette:"custom",colors:state.params["3"].colors.map((v,i)=>i===Number(e.dataset.color)?e.value:v)};select("3")}));
globalThis.__effect?.(()=>{const v=globalThis.__bindings?.value;if(v&&typeof v==="object"&&v.params){state={selected:v.selected,params:v.params};render()}});
render();
})();
</script>
```

### Shared morphing textarea AppBlock HTML

The circular shell is **not a button**. The textarea is present in both states. Its native focus is the only expansion trigger; no clipboard API, clipboard interception or fake insertion action is necessary.

```html
<div id="aip-input-UNIQUE">
<style>
#aip-input-UNIQUE .space{display:flex;min-width:0}
#aip-input-UNIQUE .morph{position:relative;box-sizing:border-box;width:40px;height:40px;flex:0 0 40px;overflow:hidden;border-radius:50%;border:1px solid #50e4dd99;background:linear-gradient(145deg,#1b3746,#18243a);box-shadow:0 0 10px #50e4dd25;transition:width .32s ease,flex-basis .32s ease,border-radius .32s ease}
#aip-input-UNIQUE .morph.expanded{width:100%;flex:1 1 100%;border-radius:16px}
#aip-input-UNIQUE .glyph{position:absolute;left:8px;top:8px;width:23px;height:23px;color:#50e4dd;pointer-events:none;transition:opacity .14s}
#aip-input-UNIQUE .morph.expanded .glyph{opacity:0}
#aip-input-UNIQUE textarea{position:absolute;inset:0;box-sizing:border-box;width:100%;height:100%;border:0!important;outline:0!important;background:transparent!important;box-shadow:none!important;resize:none;overflow:auto;padding:9px 12px;color:#eef5ff;font:14px/20px system-ui;caret-color:#50e4dd;opacity:0;cursor:text}
#aip-input-UNIQUE .morph.expanded textarea{opacity:1;transition:opacity .12s .12s}
@media(prefers-reduced-motion:reduce){#aip-input-UNIQUE .morph,#aip-input-UNIQUE .glyph,#aip-input-UNIQUE textarea{transition:none}}
</style>
<div class="space"><div class="morph">
<svg class="glyph" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
<path d="M3 8v5 M6 5v11 M9 8v5"/>
<path d="M12 5h5 M14.5 5v11 M12 16h5"/>
<path d="M2 20h20 M19 17l3 3-3 3"/>
</svg>
<textarea rows="1" aria-label="Zusätzliche Anweisung"></textarea>
</div></div>
</div>
<script>
(()=>{
const root=document.getElementById("aip-input-UNIQUE");
const shell=root.querySelector(".morph"),field=root.querySelector("textarea");
const sync=()=>{
 const active=document.activeElement===field||field.value.length>0;
 shell.classList.toggle("expanded",active);
 shell.style.height=Math.min(150,Math.max(40,field.scrollHeight+2))+"px";
};
field.addEventListener("focus",sync);
field.addEventListener("blur",sync);
field.addEventListener("input",()=>{sync();globalThis.__bindings?.setValue?.(field.value)});
globalThis.__effect?.(()=>{const v=globalThis.__bindings?.value;if(typeof v==="string"&&field.value!==v){field.value=v;sync()}});
sync();
})();
</script>
```

**Host limitation:** The Next Run trigger remains a native DIL button with the existing `GenUI.issueNewTurn` callback. The AppBlock can render a matching cyan circle but cannot trigger that host action. If the host cannot give the native pressable the exact cyan styling, preserve working dispatch and accessibility rather than substituting a nonfunctional HTML rocket. The example's surrounding `row` and button stay as defined above.

## Adaptation checklist

- Replace all `UNIQUE` IDs consistently per response, and adapt the action definitions, HTML cards, and parameter defaults together.
- Use meaningful action-specific parameter keys; only send the effective action's values.
- Keep every `globalThis.__bindings` and `globalThis.__effect` access optional-chained.
- In mixed/nested layouts, preserve the same card anatomy and exclusive selection. CSS Grid with equal-height row items and nested flex/grid columns is sufficient; do not build a general layout engine.
- This file is the authoritative **Next Run example**; historical experiments in `next-run-html-experiment.md` are superseded. GitHub Result remains to be redesigned; Proposals remain experimental.
