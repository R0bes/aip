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
