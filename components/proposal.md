# Agent improvement proposal · native UI template

Only propose useful improvements prioritized by user benefit, effort and risk. This is a generation template, not importable JSX. Replace placeholders and build the complete proposal handoff before rendering.

```jsx
<box border={{size:2,color:"default"}} radius="lg" padding={3} gap={2}>
  <row align="start" justify="between">
    <box flex="1" gap={1}>
      <text strong>{specificIdeaTitle}</text>
      <text size="sm" color="secondary">{benefitAndTradeoff}</text>
    </box>
    <pressable tooltip="Vorschlag annehmen" onClick={() => GenUI.issueNewTurn(proposalHandoff)}>
      <icon name="thumbs-up" size="lg"/>
    </pressable>
  </row>
</box>
```

Only the unboxed 👍 accepts the proposal and authorizes its implementation in the next run. No automatic implementation, voting, ratings or persistence. `proposalHandoff` includes the specific proposal task, repo/ref, action ID/key, parameters, context, verbatim supplemental text if supplied, and the AIP footer specified in `chatgpt/quick.md`.
