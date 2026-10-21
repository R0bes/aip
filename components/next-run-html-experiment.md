# Next Run · experimental light HTML/CSS input

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
