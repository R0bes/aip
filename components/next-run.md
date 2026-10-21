# Next-run card · native UI template

Generate this structure in a ChatGPT response. This is illustrative DIL-like source, not an importable component. The state declaration belongs at the top level of the response, outside the card. Each card needs its own state variable. Replace all placeholders and implement `handoff` as a self-contained string before rendering.

```jsx
{@body const [extra, setExtra] = DIL.useState("")}

<box border={{size:2,color:"default"}} radius="lg" padding={3} gap={2}>
  <row align="center" justify="between">
    <row align="center" gap={2}>
      <icon name="git-branch"/>
      <text strong>{actionTitle}</text>
    </row>
    <text size="xs" color="tertiary">{actionKey}</text>
  </row>
  <text size="sm" color="secondary">{actionDescription}</text>
  <textarea value={extra} onChange={setExtra} placeholder="⧉" rows={1} autoResize/>
  <row justify="end">
    <button size="sm" onClick={() => GenUI.issueNewTurn(handoff(extra))}>
      <icon name="rocket" inline/> Execute
    </button>
  </row>
</box>
```

The card body never dispatches. Only 🚀 Execute does. `handoff(extra)` must include repository/ref, task, action ID/key, explicit parameters, context, supplemental text verbatim, then AIP metadata and the read/apply/propagate instruction from `chatgpt/quick.md`. Key `0` is continuation. Cards appear last without a heading or trailing text.
