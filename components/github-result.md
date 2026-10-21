# GitHub result card · native UI template

Use only for verified repository operations. Fill placeholders with grounded values; omit unavailable fields. This is a generation template, not importable JSX.

```jsx
<box border={{size:2,color:"default"}} radius="lg" padding={3} gap={2}>
  <row align="center" justify="between">
    <row align="center" gap={2}>
      <icon name="github"/>
      <text strong>{resultTitle}</text>
    </row>
    <badge>{verifiedStatus}</badge>
  </row>
  <text size="sm">{actualChanges}</text>
  <text color="secondary" size="xs">{repository} · {ref} · {commitOrCheckDetails}</text>
</box>
```

Replace all placeholders with actual content; omit the badge if no verified status. Never imply checks ran, changes were pushed, or commits exist without evidence. Ordinary prose is fine when a card adds no value.
