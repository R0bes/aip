# Earlier Next Run experiments (superseded)\n\nThis file preserves exploratory prototypes and historical verification notes. **Do not use it as the current Next Run UI.** The accepted hybrid template is [next-run.md](next-run.md). The experiments below are retained only as reference.\n\n# Next Run · experimental light HTML/CSS input

Experimental presentation only. Preserve the complete card composition (header, description, colored accent, softly tinted background, subtle glow, input row); lighter means less saturated, **not** a blank white textarea. Read `AGENTS.md` first. The **native** `components/next-run.md` remains the supported dispatch implementation. Do not claim this HTML input can directly call `GenUI.issueNewTurn`: an embedded AppBlock cannot invoke that host action. A native button outside AppBlock can dispatch its bound text on a user click; Enter inside AppBlock cannot trigger the native button. Do not use simulated dispatch.

The following snippet is for an **AppBlock** visualization. Pair it with `{@body const [instruction,setInstruction]=DIL.useState("")}`, `bind={{value:instruction,setValue:setInstruction}}`, and a separate native rocket button calling `GenUI.issueNewTurn(handoff(instruction))`. Use a unique AppBlock ID per card. Preserve user text verbatim and identify it as `User instruction (verbatim)`.

```html
<div id="aip-next-html" class="w-full">
  <style>
    #aip-next-html .surface{background:linear-gradient(125deg,#e9e3f5,#dcecf3 78%,#d9e9ed);border:1px solid #a9a0c9;border-radius:14px;padding:16px;color:#29334a;box-shadow:inset 0 1px 0 #ffffff90,0 4px 18px #8c7fbd30}
    #aip-next-html .heading{font:600 14px system-ui;margin:0 0 5px;color:#51418c}
    #aip-next-html .detail{font:12px system-ui;color:#596a86;margin:0 0 10px}
    #aip-next-html textarea{display:block;box-sizing:border-box;width:100%;min-height:35px;max-height:160px;padding:8px 2px;border:0;outline:0;box-shadow:none;background:transparent;color:#29334a;font:13px system-ui;resize:none;overflow-y:auto}
    #aip-next-html textarea::placeholder{color:#8c94ac}
  </style>
  <div class="surface">
    <p class="heading">Next Run</p>
    <p class="detail">Deine Anweisung · Enter versucht abzusenden, Shift+Enter neue Zeile</p>
    <div style="border-top:1px solid #a99fca66;padding-top:7px"><textarea aria-label="Deine Anweisung" rows="1" placeholder="⧉  Deine Anweisung ..."></textarea></div>
    <p class="detail" role="status" id="aip-enter-note" hidden>Enter erkannt; für den tatsächlichen ChatGPT-Lauf die native Rakete verwenden.</p>
  </div>
</div>
<script>
(()=>{
  const root=document.getElementById("aip-next-html");
  const input=root.querySelector("textarea");
  const note=root.querySelector("#aip-enter-note");
  const resize=()=>{input.style.height="auto";input.style.height=Math.min(input.scrollHeight,160)+"px";};
  input.addEventListener("input",()=>{resize();globalThis.__bindings?.setValue?.(input.value);});
  input.addEventListener("keydown",event=>{
    if(event.key==="Enter"&&!event.shiftKey&&!event.isComposing){
      event.preventDefault();
      globalThis.__bindings?.setValue?.(input.value);
      note.hidden=false;
    }
  });
  globalThis.__effect?.(()=>{
    const value=globalThis.__bindings?.value;
    if(typeof value==="string"&&value!==input.value){input.value=value;resize();}
  });
  resize();
})();
</script>
```

The rocket can be a **native** `<button>` with an `<icon name="rocket"/>` and working click callback. Native button appearance cannot be styled with arbitrary CSS from the AppBlock. A colored SVG rocket **inside** the HTML is possible, but its click cannot directly dispatch to ChatGPT; it would be demonstration-only. Avoid showing a misleading fake-send button. This experiment uses a softly tinted lavender-to-cyan card, retained heading and accent rather than an empty white input and introduces no runtime, files, or dependencies beyond this template.


## Verified hybrid pattern: exclusive HTML choices, shared native input, native dispatch

Confirmed by an actual next-run handoff in the chat: selecting HTML choice `2`, entering `Okay, test-test. Das ist die optionale Anweisung.` in the **shared native textarea**, and clicking the **native** Run button yielded the expected action key and exact text in the next user message. This verifies that combination only; HTML-only input/Enter-to-dispatch remains unverified and unsupported.

For multiple choices, prefer **one shared textarea** (not one per card). Put the HTML choice group above a compact native input+rocket row. Use a separate AppBlock per group and stable choice IDs; do not put native buttons inside HTML.

```jsx
{@body const [selected,setSelected]=DIL.useState("0")}
{@body const [instruction,setInstruction]=DIL.useState("")}
{@body const choices=[
  {id:"0",title:"Weiter implementieren",task:"Implement the next agreed step."},
  {id:"1",title:"Architektur prüfen",task:"Review the architecture for simplification."},
  {id:"2",title:"UI verfeinern",task:"Improve UI styling and interactions."}
]}

<AppBlock app_block_id="aip-choices" title="Next Run choices" variant="inline"
          bind={{value:selected,setValue:setSelected}}>
  <!-- Replace with the HTML/CSS/JS selection view below. -->
</AppBlock>
<row align="end" gap={2}>
  <box flex="1">
    <textarea value={instruction} onChange={setInstruction} rows={1} autoResize placeholder="⧉"/>
  </box>
  <button size="sm" uniform label="Run selected action"
    onClick={() => {
      const choice=choices.find(x=>x.id===selected);
      GenUI.issueNewTurn(handoff(choice,instruction));
    }}>
    <icon name="rocket"/>
  </button>
</row>
```

Here `handoff(choice,instruction)` must be replaced by a **complete self-contained request** following AGENTS.md, with `choice.id` and `choice.task`, and `User instruction (verbatim)` containing `instruction` unchanged.

HTML content for the AppBlock above (one visual card per action, only the selected card highlighted):

```html
<div id="aip-choices" class="w-full">
<style>
#aip-choices .option{width:100%;display:flex;align-items:center;gap:12px;text-align:left;border-radius:13px;padding:14px 15px;margin-bottom:9px;border:1.5px solid #aaa0c6;background:linear-gradient(115deg,#eee7f7,#deedf3);color:#303750;box-shadow:0 2px 10px #7465a022;cursor:pointer}
#aip-choices .option:nth-child(2){background:linear-gradient(115deg,#e3eff5,#e4e9f7)}
#aip-choices .option:nth-child(3){background:linear-gradient(115deg,#eee4f3,#e8eaf6)}
#aip-choices .option[aria-pressed="true"]{border:2px solid #8270cf;box-shadow:0 0 0 2px #9d8ae733,0 3px 15px #8272c83d}
#aip-choices .title{font:600 13px system-ui;flex:1}
#aip-choices .detail{font:11px system-ui;color:#64708b}
#aip-choices .key{font:11px monospace;color:#756b97}
</style>
<button type="button" class="option" data-id="0" aria-pressed="true"><span class="title">⌘ Weiter implementieren <span class="detail">· Nächster Schritt</span></span><span class="key">0</span></button>
<button type="button" class="option" data-id="1" aria-pressed="false"><span class="title">◇ Architektur prüfen <span class="detail">· Vereinfachen</span></span><span class="key">1</span></button>
<button type="button" class="option" data-id="2" aria-pressed="false"><span class="title">✧ UI verfeinern <span class="detail">· Styling</span></span><span class="key">2</span></button>
</div>
<script>
(()=>{
const root=document.getElementById("aip-choices");
const cards=[...root.querySelectorAll(".option")];
function render(id){cards.forEach(card=>card.setAttribute("aria-pressed",String(card.dataset.id===id)));}
cards.forEach(card=>card.addEventListener("click",()=>{
  render(card.dataset.id);
  globalThis.__bindings?.setValue?.(card.dataset.id);
}));
globalThis.__effect?.(()=>{
  const id=globalThis.__bindings?.value;
  if(typeof id==="string")render(id);
});
})();
</script>
```

For multiple groups in the same response, change the HTML root ID and AppBlock ID to unique values. HTML is only for presentation and selection; the native button remains the sole ChatGPT dispatch mechanism.


## Agreed compact hybrid variant (2026-10-21)

This is the accepted visual baseline for the next-run experiment, **not** a decision on responsive layouts or a general design system. Use three compact horizontal cards for this variant. Each card has its icon and title on the **same row**, a short useful description, and an exclusive selected state expressed **only through a stronger outline and subtle glow** (no dots, checkmarks or other selection indicators). Use softly tinted lavender/cyan surfaces. Do not silently substitute the older vertically stacked icon/title or native card layout.

Below the cards, use **one shared HTML textarea**, with **transparent background, no border, no outline, no enclosing field surface or label**; its only placeholder is `💬`. Bind its value to DIL state. Place a single **native icon-only rocket button** immediately to its right, dispatching the selected action and the unchanged text via `GenUI.issueNewTurn`. AppBlock HTML must never claim to dispatch itself. Preserve the complete self-contained handoff and AGENTS.md refresh instruction.

Implementation sketch for the card presentation:

```css
.cards { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:10px; }
.card { display:flex; flex-direction:column; text-align:left; border:1.5px solid #b6accd; border-radius:13px; padding:13px 12px; background:linear-gradient(145deg,#eee5fa,#dfe9f6); }
.card .head { display:flex; align-items:center; gap:9px; }
.card .glyph { flex:none; display:grid; place-items:center; width:24px; height:24px; }
.card[aria-pressed="true"] { border:2px solid #866acb; box-shadow:0 0 0 2px #a58de639,0 4px 16px #8e78c650; }
.shared-instruction { width:100%; border:0; outline:0; background:transparent; box-shadow:none; resize:none; }
.shared-instruction::placeholder { color:#9887bf; opacity:1; }
```

Use accessible `aria-pressed` on each HTML card; on click update exactly one selected card and call `globalThis.__bindings?.setValue?.(id)`. Synchronize with `globalThis.__effect?.(() => ...)`; always optional-chain these globals. The instruction field uses a **separate** binding and synchronizes its input value to state. The native rocket reads both state values and sends the selected action's own task/key/context, with `User instruction (verbatim)` unchanged.

**Not yet agreed:** adaptive card counts, responsive breakpoint behavior, variable-card layout, a shared design system. Do not treat these as implemented or approved merely because exploratory prototypes were shown.
