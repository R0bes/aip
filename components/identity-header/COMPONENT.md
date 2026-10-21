# Minimal AIP identity header

Read [AGENTS.md](../../AGENTS.md) first. This is a small **orientation strip**, not a status report. Display only `AIP · repository · branch/ref`. The AIP version is kept in the Next Run handoff metadata; it need not occupy visible header space. Never invent a repository/ref. Do not include commit, verification, progress, status badge or explanatory prose in the identity strip. Put those facts in GitHub Result or Plan cards.

Apply [theme tokens](../../themes/themes.css) to surface, border, foreground, muted text and radius. **No glow** (reserved for selected Next Run cards). A native DIL header is sufficient:

See [header.dil](header.dil) — reference variant 1; adapt data and theme to the current run.

This is the **Cyberpunk** preset example. Substitute verified repository/ref and chosen theme values. For native DIL, use supported style props; CSS from the HTML Next Run AppBlock does not cross into the header.

The waveform/I-beam/lower-arrow icon belongs to the shared morphing Next Run input, not this header. Recolor the input through the selected theme without changing its focus, editing or collapse behavior.

## Compact header configuration (accepted interaction)

The header alone owns the gear/theme selector. It appears exactly once at the top of the full response, never directly above the Next Run action cards as an extra theme toolbar. Read the selected theme from the incoming handoff; otherwise use Pastel. Apply it across header, GitHub Result, Plan, Proposal and Next Run, and carry the chosen name in the next-run parameters. The CSS file is a design reference: native DIL styling needs explicit token values.


Place a subtle classic gear icon (`<icon name="settings"/>`) at the far right of the identity header. Clicking expands a compact panel directly below the identity row; collapsed by default. Use the theme passed to this run, falling back to Pastel when none is specified; never reset an explicitly selected theme.

Offer theme selection (Cyberpunk, Pastel, Neutral), applied immediately to all theme-aware components in the current response through shared DIL state. The chosen theme is also included as a self-contained parameter in the next-run handoff.

Do **not** offer a "Save as AIP default" repository-setting action. The panel must not include agent-personal-rule controls or instructions; users manage their own agent preferences outside AIP. No settings service, AIP persistence, local storage, new renderer or cross-chat persistence. Use existing semantic tokens in `themes/themes.css`; keep theme choice separate from task selection and preserve native Next Run dispatch.

## Integration invariant

The settings disclosure MUST NOT replace, simplify, or alter the accepted hybrid Next Run input. Keep the existing **real morphing HTML textarea** (40px circular idle state with waveform/I-beam/lower-arrow SVG; expands on focus; collapses only when empty and blurred), bound to DIL state. A plain always-expanded DIL `<input>` or `<textarea>` is a regression. Keep the separate native circular-arrow/play `<pressable>` for dispatch. Theme changes recolor both controls via shared state; they do not change their interaction model. When rendering the full AIP UI, verify the header gear, cards, morphing textarea and native dispatch together. The selected theme may be passed to the next run; never add persistence or agent-preference controls.
