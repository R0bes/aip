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

## Shared speech-bubble input

The `💬` field is the **shared Next Run instruction input**, not the host's main chat composer. Keep it one transparent, borderless HTML textarea with the `💬` placeholder and native rocket to the right. Theme its placeholder, caret and text using scoped tokens in its **own** AppBlock:

```css
#aip-input-UNIQUE {
  --aip-text: #EEF5FF;
  --aip-muted: #A7B7C9;
  --aip-accent: #50E4DD;
}
#aip-input-UNIQUE textarea {
  color: var(--aip-text);
  caret-color: var(--aip-accent);
  background: transparent;
  border: 0;
  outline: 0;
  box-shadow: none;
}
#aip-input-UNIQUE textarea::placeholder {
  color: var(--aip-muted);
  opacity: 1;
}
```

This CSS is a **scoped example**, not a global stylesheet. The surrounding host surface may need a theme-compatible container for contrast; never promise to recolor the native rocket or ChatGPT's actual composer.
