# Minimal AIP identity header

Read [AGENTS.md](../AGENTS.md) first. This is a small **orientation strip**, not a status report. Display only `AIP · repository · branch/ref`. The AIP version is kept in the Next Run handoff metadata; it need not occupy visible header space. Never invent a repository/ref. Do not include commit, verification, progress, status badge or explanatory prose in the identity strip. Put those facts in GitHub Result or Plan cards.

Apply [theme tokens](../themes/README.md) to surface, border, foreground, muted text and radius. **No glow** (reserved for selected Next Run cards). A native DIL header is sufficient:

```jsx
<box background="#141824" border={{size:1,color:"#4D6075"}} radius="md" padding={{x:3,y:2}} theme="dark">
  <row align="center" gap={2}>
    <icon name="git-branch" color="#50E4DD" size="sm"/>
    <text size="sm" weight="medium" color="#EEF5FF">AIP</text>
    <text size="xs" color="#A7B7C9">·</text>
    <text size="sm" color="#EEF5FF">R0bes/aip</text>
    <text size="xs" color="#A7B7C9">·</text>
    <text size="sm" color="#50E4DD">main</text>
  </row>
</box>
```

This is the **Cyberpunk** preset example. Substitute verified repository/ref and chosen theme values. For native DIL, use supported style props; CSS from the HTML Next Run AppBlock does not cross into the header.

The speech-bubble icon belongs to the existing shared Next Run input, not this header. Its appearance may use the selected theme's accent color if supported, but do **not** introduce a styled input container or alter the text field itself.

## Compact header configuration (accepted interaction)

Place a subtle **classic gear** icon (`<icon name="settings"/>`) at the far right of the identity header. Clicking it expands a compact panel directly below the identity row; it is collapsed by default. Keep the approved Cyberpunk styling as the initial presentation and retain the identity line's orientation-only purpose.

The panel initially offers theme selection (Cyberpunk, Pastel, Neutral) and an explicit scope choice:

- **Current conversation:** Update all theme-aware components in this rendered response via shared DIL state, and include the chosen theme as a self-contained parameter in the next-run dispatch. Each subsequent run must apply that parameter consistently. This is handoff propagation, **not** durable global storage or a promise of automatic persistence outside the chain.
- **Save as AIP default:** Explicitly request a repository configuration change in the next run. The UI cannot directly mutate GitHub; only a subsequent authorized agent action can edit the authoritative theme default, verify the commit and report success. Do not claim that clicking a setting alone saved it.

No settings service, local storage, new renderer or cross-chat persistence. Use the existing semantic tokens in `themes/README.md`. The gear is a native DIL control, and the expanded panel can be a compact native layout. Keep theme selection separate from task selection and preserve the native Next Run pressable for dispatch.
