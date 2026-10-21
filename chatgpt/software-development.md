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
- For a simple action without controls, the **whole card** is the dispatch target. For an action with embedded editable controls, isolate input interactions; prefer whole-card dispatch where safely possible, otherwise use a small bottom-right icon-only check control, not 'Go' text or a full-width 'start' button.
- A small always-mounted  input per card supports mouse-injected paste. Once captured, show a truncated preview of the text **in the same editable region**; clicking expands that field in place to edit. Preserve the complete value for dispatch. No second textarea, pencil or redundant copy of the text.
- Only show scope selection when there are materially different, **explicitly defined** work packages; name the steps covered. Never repeatedly show a generic 'next step / whole stack' toggle.
- Number of action cards is based on useful alternatives, not a fixed quota. Key `0` represents continuation when meaningful. Keep the settings control in the header, not a bottom rail.

## Grounding and integrity

Report only verified edits, checks and deployments; distinguish docs from executable changes. Keep AIP protocol metadata at the end of generated follow-up prompts. Do not modify unrelated repositories. If a host lacks paste, attachment, hover or nested-click capabilities, use a functional fallback and state the limitation.
