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

Place a subtle classic gear icon (`<icon name="settings"/>`) at the far right of the identity header. Clicking expands a compact panel directly below the identity row; collapsed by default. Keep the approved Cyberpunk styling as the initial presentation.

Offer theme selection (Cyberpunk, Pastel, Neutral), applied immediately to all theme-aware components in the current response through shared DIL state. The chosen theme is also included as a self-contained parameter in the next-run handoff.

Do **not** offer a "Save as AIP default" repository-setting action. The panel must not include agent-personal-rule controls or instructions; users manage their own agent preferences outside AIP. No settings service, AIP persistence, local storage, new renderer or cross-chat persistence. Use existing semantic tokens in `themes/README.md`; keep theme choice separate from task selection and preserve native Next Run dispatch.

## Integration invariant

The settings disclosure MUST NOT replace, simplify, or alter the accepted hybrid Next Run input. Keep the existing **real morphing HTML textarea** (40px circular idle state with waveform/I-beam/lower-arrow SVG; expands on focus; collapses only when empty and blurred), bound to DIL state. A plain always-expanded DIL `<input>` or `<textarea>` is a regression. Keep the separate native circular-arrow/play `<pressable>` for dispatch. Theme changes recolor both controls via shared state; they do not change their interaction model. When rendering the full AIP UI, verify the header gear, cards, morphing textarea and native dispatch together. The selected theme may be passed to the next run; never add persistence or agent-preference controls.
