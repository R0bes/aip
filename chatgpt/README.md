# ChatGPT adapter — AIP 0.3.0 draft

ChatGPT is AIP's first renderer and dispatch adapter, not part of the platform-neutral core. Load [protocol.md](../protocol.md), [output.md](../output.md), and [software-development.md](software-development.md) when applicable. A public repository is not automatically loaded or synchronized.

## Rendering contract

- Begin the actual answer with one lightly outlined context header. Show repository/ref only when known, one compact version label, and an icon-only **gear** settings affordance.
- Use ordinary prose and inline result cards as warranted. Card titles describe the actual content, **not** the card type. Use a consistent visual weight and size for all leading icons.
- Result cards may expand on clicking their main surface; a dedicated chevron is unnecessary. Hover/focus may subtly change the border or background. Nested copy controls never toggle expansion.
- Use generic copyable artifacts with optional titles/descriptions, and optional compact GitHub cards for changes, comparisons, commits, PRs or other GitHub interactions.
- Only meaningful next-run action cards appear at the **very end**. No prose follows. Do not force exactly two cards or a scope selector.
- An action without editable controls can dispatch on whole-card click. An action with inputs must protect editing from accidental dispatch; use a compact icon-only confirm control if necessary.
- Use a small **always-mounted focusable input** per action to support first-click mouse paste. Preserve captured text verbatim; collapse it to a short in-place editable preview. Do not show a second editor or an edit pencil. Never claim clipboard-read or attachment support that the host does not provide.
- Put the actual project task first in dispatched messages and unobtrusive AIP metadata last.

## Settings

The header gear is a **local interface-preferences affordance** (e.g. density, detail expansion, copy/report formatting, optional prompts) when the host can actually change those choices. It must never silently alter repository files, platform account settings, permissions or protocol versions. If no functional settings exist, omit or disable the gear rather than displaying a fake control. Persistence and sync are not implemented.

## Copy and attachments

Copy controls use an icon with accessible label and tooltip. A report export must serialize grounded run data and selected values, not assume the platform's native copy-response preserves interactive widgets. File/screenshot attachment transfer is not implemented in this draft; do not simulate an upload button.

## Fallback

Use concise numbered text actions if the host cannot render the controls. Only an explicit user gesture dispatches a self-contained follow-up request.
