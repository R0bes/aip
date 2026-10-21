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
  <row align="end" gap={2}>
    <box flex="1">
      <textarea value={extra} onChange={setExtra} placeholder="⧉" rows={1} autoResize/>
    </box>
    <button size="sm" uniform label="Run next action" onClick={() => GenUI.issueNewTurn(handoff(extra))}>
      <icon name="rocket"/>
    </button>
  </row>
</box>
```

Native UI limitation: the current `textarea` API has no borderless/transparent styling property and no keyboard event handler. Do not claim that Enter submits or Shift+Enter inserts a newline; these behaviors require host support or a separately approved embedded HTML implementation. Keep the native textarea and explicit rocket button rather than adding a fake shortcut.

Only the icon-only 🚀 button dispatches. `handoff(extra)` labels the unchanged textarea value as `User instruction (verbatim)` and treats it as the primary user instruction, while the card's proposed task is context/default. Follow the self-contained request format and AGENTS.md propagation rule. Key `0` is continuation.
