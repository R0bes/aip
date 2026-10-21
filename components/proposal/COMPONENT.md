# Agent proposal · experimental native UI template

## Shared theme

Apply [themes/themes.css](../../themes/themes.css) to Proposal cards too. Match the same surfaces, typography, spacing and border radius as Next Run, GitHub and Plan, using supported native DIL props; a global HTML stylesheet cannot reach native components. Keep the unboxed 👍 as the only proposal-acceptance control and avoid a selection glow on informational content. Theme affects appearance only, not authorization or dispatch.

**Experimental feature; design and interaction are not finalized.** Offer only specific, practical improvements. This is JSX-like generation source, not an importable module. Replace placeholders and prepare a complete self-contained acceptance handoff using the rules in AGENTS.md.

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

Only the unboxed 👍 authorizes implementation in the next run; no automatic execution, voting or persistence.
