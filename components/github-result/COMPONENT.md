# GitHub cards — verified repository views

## Shared theme

Apply [themes/themes.css](../../themes/themes.css) to **all three** GitHub views (verified result, PRs, branches). Use the same semantic surface, text, muted, border, accent and radius tokens as Next Run and Plan. For native DIL, map to supported presentation props; AppBlock CSS cannot style native cards. Cyberpunk uses dark surfaces and cyan accents, but repository facts, link targets and verification states remain unchanged. Informational GitHub cards have **no selection glow**. Use status text and icons, not color alone. The DIL examples below MUST use the selected theme tokens explicitly, including surface, foreground, muted, border, accent and radius. Do not fall back to unthemed `border`, `color="#626B76"` or default card styling. The examples illustrate Neutral; use shared DIL theme state for the active response.

Read [AGENTS.md](../../AGENTS.md) first. **GitHub cards are a family of contextual views**, not one oversized card. Render only the views relevant to the run. This is DIL generation guidance, not an importable component. Match the existing compact visual language without imposing Next Run's selection controls on read-only results.

## Shared rules

- Repository and ref must be grounded in fetched data. Distinguish **verified**, **pending/unverified**, and **blocked**; never invent a check result, PR state, branch relationship or commit.
- Choose from **Change result**, **Open pull requests**, **Branches**. The latter two are repository snapshots, not automatically complete: show retrieval scope/time when relevant, and say when pagination or access limits prevent completeness.
- Each card has a clear icon, specific title, concise useful rows and small secondary metadata. Link PRs/branches/commits to verified GitHub URLs where available. Use small neutral labels; avoid a rainbow of statuses.
- Use separate cards when information differs in purpose. Avoid empty sections. The **Plan / Progress** card is a separate component in [Plan / Progress](../plan-progress/COMPONENT.md).
- Prefer native DIL components for simple cards; no custom HTML, duplicated renderers, or additional persistence.

## Variant A: verified change result

```jsx
<box background="#F4F5F7" border={{size:1,color:"#C5CAD2"}} radius="lg" padding={3} gap={2}>
  <row align="center" justify="between">
    <row align="center" gap={2}><icon name="github" color="#4B647D"/><text strong color="#232833">Next Run · Vorlage konsolidiert</text></row>
    <badge color="success">Committed</badge>
  </row>
  <text color="#626B76" size="xs">R0bes/aip · main</text>
  <divider color="#C5CAD2"/>
  <text size="sm" color="#232833">• Vollständiges Beispiel ergänzt</text>
  <text size="sm" color="#232833">• Parameterübergabe dokumentiert</text>
  <row align="center" justify="between">
    <text size="xs" color="#626B76">Commit: <code>9e56e54</code></text>
    <text size="xs" color="#626B76">UI-Test: nicht ausgeführt</text>
  </row>
</box>
```

The values above illustrate a previously verified change. Replace them with **current, independently verified facts**; omit badges and fields without evidence.

## Variant B: open pull requests

```jsx
<box background="#F4F5F7" border={{size:1,color:"#C5CAD2"}} radius="lg" padding={3} gap={2}>
  <row align="center" gap={2}><icon name="git-pull-request" color="#4B647D"/><text strong color="#232833">Offene Pull Requests</text></row>
  <text size="xs" color="#626B76">Repository · Abfrageumfang und Zeitpunkt</text>
  <divider color="#C5CAD2"/>
  <row justify="between" align="center">
    <box gap={1}><text weight="medium" color="#232833">#25 · Calendar Read Gateway</text><text size="xs" color="#626B76">feat/calendar-read-gateway → integration/phase2</text></box>
    <badge>Draft</badge>
  </row>
  <row justify="between" align="center">
    <box gap={1}><text weight="medium" color="#232833">#26 · CI vereinfachen</text><text size="xs" color="#626B76">chore/affected-ci → main</text></box>
    <badge>Open</badge>
  </row>
</box>
```

**Illustrative rows only, not a live PR lookup.** Populate from actual GitHub results; link PRs when URL is verified. Useful fields: number/title, source → target, draft/open, review/check state **only if retrieved**, and the total when the query is complete. No speculative mergeability.

## Variant C: branches

```jsx
<box background="#F4F5F7" border={{size:1,color:"#C5CAD2"}} radius="lg" padding={3} gap={2}>
  <row align="center" gap={2}><icon name="git-branch" color="#4B647D"/><text strong color="#232833">Branches</text></row>
  <text size="xs" color="#626B76">Repository · Stand der letzten Abfrage</text>
  <divider color="#C5CAD2"/>
  <row align="center" justify="between"><text size="sm" color="#232833"><code>main</code></text><badge>Default</badge></row>
  <row align="center" justify="between"><text size="sm" color="#232833"><code>integration/phase2</code></text><text size="xs" color="#626B76">Integration</text></row>
  <row align="center" justify="between"><text size="sm" color="#232833"><code>feat/calendar-read-gateway</code></text><text size="xs" color="#626B76">Feature</text></row>
</box>
```

**Illustrative rows only.** Show branches actually returned; never infer their existence, freshness, or relationship from previous conversations. When branch lists are partial, explicitly label them as partial. For large repositories, filter to relevant branches and offer a more comprehensive lookup instead of a huge card.

## Choosing the view

A completed edit usually calls for **Change result**. A request about review/merge work calls for **Open PRs**. A request about integration or active development lines calls for **Branches**. Combine PRs and branches as two adjacent cards when both matter; do not make every response a GitHub dashboard.
