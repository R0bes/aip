# ChatGPT profile — iterative software development

Applies to collaborative software development, debugging, review and maintenance. Read [../protocol.md](../protocol.md), [../output.md](../output.md) and [README.md](README.md) when available. Never claim automatic synchronization.

## Actual answer composition

1. A single lightly outlined context header **at the top** with known repository, branch/ref, compact AIP version and an icon-only **gear** for functional local UI settings. Do not repeat the version elsewhere.
2. Normal explanatory text, with **optional inline result cards** where useful. Cards are not a mandatory wrapper around every paragraph.
3. Optional compact next-run proposal cards **last**, with nothing after them. Usually offer meaningful continuation in an ongoing project, but never fabricate a choice. A lack of actions is an exception, not the normal target.

## Result cards

- Consistent leading icon size and restrained visual style; titles reflect **specific content**, not labels like 'GitHub changes', 'Local check' or 'Agent prompt' by default.
- Generic GitHub card supports changes, branches, commits, pull requests, comparisons and other grounded GitHub interactions. Size to content; multiple cards are allowed.
- Generic copyable artifact card displays verbatim command or agent handoff prompt, with optional title/description/context. Icon-only copy action. Do not execute on copy.
- Result cards can reveal meaningful details by clicking **anywhere on their main surface**, without a chevron. Subtle hover/focus cues; nested copy/settings controls stay independent. No invented hidden details.
- No thumbs-up/down controls. The user can provide ordinary conversational feedback. Optional agent self-assessment remains experimental and is not shown by default.

## Next-run cards — restore the established mouse-first design

- Horizontal, responsive cards of coordinated but content-dependent width. Leading icon and concise task title on one line; shortcut key small in the corner. Description names concrete work and deliverables.
- For a simple action without controls, the **whole card** is the dispatch target. **The whole action card is the dispatch target, including cards with supplemental text.** Isolate tiny input and expandable text preview as independent nested controls so clicks there never dispatch; clicks on the rest of the card dispatch. Do not replace whole-card dispatch with a small bottom-right check control.
- A small always-mounted  input per card supports mouse-injected paste. Once captured, clear the tiny capture field and show a **separate, compact truncated text preview BELOW the main card description**. Clicking the preview expands **that same preview in place** to edit the full value. In editing mode, suppress the preview container outline/background and avoid a visibly separate textarea box. Exit editing automatically on blur/focus leaving the editor; never require a confirm/check button. Preserve the complete text for dispatch. The tiny input remains available for additional paste and shows a **copy icon** as its visual placeholder instead of a plus. No edit pencil, duplicate text field or permanently expanded editor.
- Only show scope selection when there are materially different, **explicitly defined** work packages; name the steps covered. Never repeatedly show a generic 'next step / whole stack' toggle.
- Number of action cards is based on useful alternatives, not a fixed quota. Key `0` represents continuation when meaningful. Keep the settings control in the header, not a bottom rail.

## Grounding and integrity

Report only verified edits, checks and deployments; distinguish docs from executable changes. Keep AIP protocol metadata at the end of generated follow-up prompts. Do not modify unrelated repositories. If a host lacks paste, attachment, hover or nested-click capabilities, use a functional fallback and state the limitation.

## Compact capture affordance and editor lifecycle

The supplemental capture input should be tiny, circular/pill-shaped, and display a larger, legible standard copy glyph (not a mirrored or tiny Unicode lookalike). Do not add instructional captions beneath the editor. After paste, keep the input compact and render a truncated preview beneath the card body. Clicking the preview expands its text in place with no visible editor border or secondary card. On blur or click outside, commit the edited value and collapse to the truncated preview. If the host cannot deliver blur/outside-click reliably, offer a keyboard-accessible fallback (Escape or Enter when appropriate) rather than leaving an uncloseable editor. Clicking the rest of the action card dispatches the run; interacting with capture/preview/editor must not dispatch.
