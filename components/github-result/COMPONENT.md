# GitHub cards — verified repository views

## Shared theme

Apply [themes/themes.css](../../themes/themes.css) to **all three** GitHub views (verified result, PRs, branches). Use the same semantic surface, text, muted, border, accent and radius tokens as Next Run and Plan. For native DIL, map to supported presentation props; AppBlock CSS cannot style native cards. Cyberpunk uses dark surfaces and cyan accents, but repository facts, link targets and verification states remain unchanged. Informational GitHub cards have **no selection glow**. Use status text and icons, not color alone. The DIL examples in the linked source MUST use the selected theme tokens explicitly, including surface, foreground, muted, border, accent and radius. Do not fall back to unthemed `border`, `color="#626B76"` or default card styling. The examples illustrate Neutral; use shared DIL theme state for the active response.

Read [AGENTS.md](../../AGENTS.md) first. **GitHub cards are a family of contextual views**, not one oversized card. Render only the views relevant to the run. This is DIL generation guidance, not an importable component. Match the existing compact visual language without imposing Next Run's selection controls on read-only results.

## Shared rules

- Repository and ref must be grounded in fetched data. Distinguish **verified**, **pending/unverified**, and **blocked**; never invent a check result, PR state, branch relationship or commit.
- Choose from **Change result**, **Open pull requests**, **Branches**. The latter two are repository snapshots, not automatically complete: show retrieval scope/time when relevant, and say when pagination or access limits prevent completeness.
- Each card has a clear icon, specific title, concise useful rows and small secondary metadata. Link PRs/branches/commits to verified GitHub URLs where available. Use small neutral labels; avoid a rainbow of statuses.
- Use separate cards when information differs in purpose. Avoid empty sections. The **Plan / Progress** card is a separate component in [Plan / Progress](../plan-progress/COMPONENT.md).
- Prefer native DIL components for simple cards; no custom HTML, duplicated renderers, or additional persistence.

## Variant A: verified change result

See [result.dil](result.dil) — reference variant 1; adapt data and theme to the current run.

The values above illustrate a previously verified change. Replace them with **current, independently verified facts**; omit badges and fields without evidence.

## Variant B: open pull requests

See [result.dil](result.dil) — reference variant 2; adapt data and theme to the current run.

**Illustrative rows only, not a live PR lookup.** Populate from actual GitHub results; link PRs when URL is verified. Useful fields: number/title, source → target, draft/open, review/check state **only if retrieved**, and the total when the query is complete. No speculative mergeability.

## Variant C: branches

See [result.dil](result.dil) — reference variant 3; adapt data and theme to the current run.

**Illustrative rows only.** Show branches actually returned; never infer their existence, freshness, or relationship from previous conversations. When branch lists are partial, explicitly label them as partial. For large repositories, filter to relevant branches and offer a more comprehensive lookup instead of a huge card.

## Choosing the view

A completed edit usually calls for **Change result**. A request about review/merge work calls for **Open PRs**. A request about integration or active development lines calls for **Branches**. Combine PRs and branches as two adjacent cards when both matter; do not make every response a GitHub dashboard.
