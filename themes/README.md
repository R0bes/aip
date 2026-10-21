# AIP visual themes

**Authoritative theme values:** [tokens.csv](tokens.csv). The CSV has one row per theme and columns for `surface`, `surface_alt`, `text`, `muted`, `border`, `accent`, `accent_soft`, `glow`, `radius`, `density`. Do not maintain a second table of values in Markdown.

## Application

- The theme is **presentation only**. It never changes repository facts, action keys, authorization or plan status.
- Read a passed `theme` next-run parameter first. Otherwise use **Pastel** as the fallback. A header gear icon exposes a compact, initially collapsed selector for Pastel, Cyberpunk and Neutral. Theme selection is ephemeral; carry the selected name in the next-run handoff.
- Apply the selected row consistently to the header, Next Run cards, morphing textarea shell and native pressable, GitHub results, Plan and Proposal. Use `surface` for main cards and `surface_alt` for nested controls; use `text` for primary copy and `muted` for descriptions. Reserve `accent` and `glow` for interactive focus and selected actions, not informational results.
- Native DIL props and scoped AppBlock CSS are separate rendering surfaces. Map the same token semantics to each; a global CSS file cannot style native DIL from an AppBlock. Explicitly style AppBlock root, headings and descriptions for contrast.
- Preserve the accepted **40px circular morphing real HTML textarea** and native circular-arrow/play dispatch described in [next-run.md](../components/next-run.md). The theme may recolor them, not replace their behavior.
- Semantic statuses (`done`, `active`, `open`, `blocked`) must include labels or icons, never color alone. Keep layouts compact and content-aware.
- No settings service, persistence, agent personal-rule controls, new renderer or CSS injection infrastructure.

The CSV is a **repository design reference for agents**, not a runtime file automatically loaded by ChatGPT. Each response maps the chosen row into its native and HTML components.
