# ChatGPT profile — iterative software development

Use for collaborative development, debugging, review and maintenance. Read [../protocol.md](../protocol.md), [../output.md](../output.md), and [README.md](README.md) when available. No automatic profile loading or synchronization is guaranteed.

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
