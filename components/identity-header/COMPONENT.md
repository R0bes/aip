# Work identity header

Read [AGENTS.md](../../AGENTS.md) first. The header identifies the **agent's current work**, not the AIP integration. Render it exactly once at the start of an AIP response.

## Visible identity

- **Agent label:** Use an explicitly assigned agent name or role when provided. Otherwise choose a short descriptive label based on the actual task (for example, `JSON Analyzer` or `UI Engineer`). A self-chosen label is a description, not a claim of a formal assignment.
- **Work repository:** Show the actual target repository from the user's task or verified context. Never substitute `R0bes/aip` merely because AIP supplies the UI. If no work repository is known, omit this field rather than invent one.
- **Current task:** Show a concise, grounded task title, preferably with the existing plan identifier (e.g. `AP2 · Define metrics`) when one is available. If no plan exists, derive a truthful task title from the current request; do not invent progress or IDs.
- **Branch/ref:** Optional secondary context when known; never invent it.

Preferred compact layout: first row **agent label · work repository** with a subtle settings gear at the right; second row **current task**. Omit unavailable optional fields cleanly. Do not show `AIP` as the agent name or the AIP source repository as the work repository. AIP version belongs in handoff metadata, not the visible identity. Keep commits, test results, status and progress in their own views.

Use [themes/themes.css](../../themes/themes.css) as the token source and [header.dil](header.dil) as an illustrative native DIL rendering reference. No glow in the header. Native DIL requires explicit token values; HTML/AppBlock CSS does not style it.

## Theme settings

The header owns the single compact gear/theme selector, collapsed by default. Offer Pastel, Cyberpunk and Neutral. Use the incoming theme when present, otherwise Pastel. Apply theme changes immediately across the **whole response**, including additional native DIL components beyond the AIP-specific views where styling is supported, and carry the ephemeral theme in Next Run. Theme affects appearance only, never facts or actions. Do not add persistence or agent-preference settings.

## Integration invariant

The settings disclosure must not replace or change the accepted hybrid Next Run input: a real morphing HTML textarea (40px circular idle icon, expands on focus, remains expanded when nonempty) plus a separate native circular-arrow/play dispatch pressable. See [Next Run](../next-run/COMPONENT.md).