# Next Run · native UI template

Generate this structure in a ChatGPT response. It is illustrative JSX-like source, not an importable module. Declare state at the response's top level, use a distinct state variable per card, and replace placeholders with concrete content. Implement `handoff` as a complete message string.

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

Only 🚀 Execute dispatches. `handoff(extra)` preserves the textarea value verbatim and follows the self-contained request format and AGENTS.md propagation rule. Key `0` is continuation.
