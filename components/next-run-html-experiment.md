# Next Run · experimental light HTML/CSS input

Experimental presentation only. Read `AGENTS.md` first. The **native** `components/next-run.md` remains the supported dispatch implementation. Do not claim this HTML input can directly call `GenUI.issueNewTurn`: an embedded AppBlock cannot invoke that host action. A native button outside AppBlock can dispatch its bound text on a user click; Enter inside AppBlock cannot trigger the native button. Do not use simulated dispatch.

The following snippet is for an **AppBlock** visualization. Pair it with `{@body const [instruction,setInstruction]=DIL.useState("")}`, `bind={{value:instruction,setValue:setInstruction}}`, and a separate native rocket button calling `GenUI.issueNewTurn(handoff(instruction))`. Use a unique AppBlock ID per card. Preserve user text verbatim and identify it as `User instruction (verbatim)`.

```html
<div id="aip-next-html" class="w-full">
  <style>
    #aip-next-html .surface{background:linear-gradient(125deg,#f9f8ff,#f0f8fc);border:1px solid #c9c6e5;border-radius:14px;padding:14px;color:#29334a;box-shadow:0 2px 12px #6173a012}
    #aip-next-html .heading{font:600 14px system-ui;margin:0 0 5px}
    #aip-next-html .detail{font:12px system-ui;color:#67728b;margin:0 0 10px}
    #aip-next-html textarea{display:block;box-sizing:border-box;width:100%;min-height:35px;max-height:160px;padding:8px 2px;border:0;outline:0;box-shadow:none;background:transparent;color:#29334a;font:13px system-ui;resize:none;overflow-y:auto}
    #aip-next-html textarea::placeholder{color:#8c94ac}
  </style>
  <div class="surface">
    <p class="heading">Next Run</p>
    <p class="detail">Deine Anweisung · Enter versucht abzusenden, Shift+Enter neue Zeile</p>
    <textarea aria-label="Deine Anweisung" rows="1" placeholder="⧉"></textarea>
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

The rocket can be a **native** `<button>` with an `<icon name="rocket"/>` and working click callback. Native button appearance cannot be styled with arbitrary CSS from the AppBlock. A colored SVG rocket **inside** the HTML is possible, but its click cannot directly dispatch to ChatGPT; it would be demonstration-only. Avoid showing a misleading fake-send button. This experiment is intentionally light rather than dark and introduces no runtime, files, or dependencies beyond this template.
