# ChatGPT profile — iterative software development

**Preferred interaction pattern for collaborative ChatGPT work on GitHub repositories, including in new/separate conversations.** Use AIP to report actual changes and checks clearly and to propose meaningful next actions as interactive cards. Do not turn this workflow into a general agent runtime, background synchronization service, or broad platform integration project.

Use for collaborative development, debugging, review and maintenance. Read [../protocol.md](../protocol.md), [../output.md](../output.md), and [README.md](README.md) when available. No automatic profile loading or synchronization is guaranteed.

## Across conversations

When a user invokes AIP in a new conversation, read this profile and relevant adapter rules when repository access is available; do not assume the repository was automatically loaded. Carry a compact profile/repository reference in next-run prompts. Refresh on explicit request, version change, or suspected drift, not necessarily on every run. AIP is the preferred interaction style for this kind of work, not a substitute for the user's immediate instructions or the host's controls.

## Report layout

1. Begin with a single lightly outlined context header containing grounded repository, branch/ref, one AIP version label, and a functional icon-only gear if actual settings exist.
2. Present normal prose and optional inline result cards. Result-card titles describe the specific result, not the card type. Use consistent, legible leading icon sizes.
3. Place meaningful next-run cards **last**, with nothing following. Usually suggest continuation for active projects, but never invent work to fill a quota.

## Result cards

- GitHub cards may represent changes, commits, branches, pull requests, comparisons or other confirmed GitHub interactions.
- Copyable artifact cards hold exact commands or agent prompts; titles and descriptions are optional. Copy does not execute.
- Clicking a result card's main surface may expand grounded details; no chevron is required. Nested copy controls do not toggle the card.
- No per-card thumbs ratings. Feedback is conversational.

## Next-run cards

- Use compact, horizontally arranged responsive cards of content-dependent width. Put a consistent icon and specific task title on the same line, with shortcut key small in a corner.
- **The main surface of each next-run card is clickable to dispatch**, including when it has supplemental text. Clicking the text field must **never** dispatch.
- Use exactly **one supplemental-text field per card**. When empty, show a prominent, correctly oriented copy glyph **as the field's placeholder text**, not a separate icon or button. This icon is a visual cue for paste; it does not read the clipboard.
- The user clicks the field and types/pastes directly into it. **Once text exists, show the complete text normally in the same field, without truncation, preview, expansion, collapse, or an editing-mode toggle.** Grow the field as needed for multiline text; preserve all text verbatim.
- No separate tiny + field, second preview, helper caption, pencil, or confirm/close button. The supplemental text field is transparent and borderless (no fill, outline, or box shadow), with smaller compact typography and minimal padding; keep a usable focus target.
- Only show a scope selector for genuinely distinct, concretely defined work packages. Do not automatically offer 'one step / whole stack'.
- Key `0` represents meaningful continuation. No fixed number of cards is required.

## Integrity and host constraints

Report only confirmed changes and checks; distinguish documentation, implementation, commits, pushes and deployments. Keep actual project tasks first and AIP metadata last in dispatched requests. No fabricated clipboard read, attachment support, or persistence. If a renderer cannot safely isolate nested input clicks from whole-card dispatch, use a functional fallback and explain the limitation. Do not modify unrelated repositories.

## Conditional refresh in dispatched prompts

Append the AIP repository and profile reference and a short conditional instruction to every generated next-run prompt: **If AIP instructions are missing, uncertain, or appear inconsistent, re-read the relevant rules from the AIP repository before continuing.** Do not require a fetch on every run or claim a refresh that did not occur. Preserve the complete project task and user supplemental text before this footer.
