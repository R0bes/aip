# ChatGPT run-output components

Prefer a concise context header (repository, branch, optional agent/run reference), then a visually distinct change summary with a **GitHub icon** when actual edits occurred. Show **what the user should notice when testing**, not just a file list.

Render local commands in a code block or compact command panel with an icon-only Copy control (accessible label and tooltip). Render prompts for another agent as separate copyable `Agent prompt` artifacts (robot icon and icon-only Copy control). Offer a dedicated **Copy report** action for a faithful, self-contained Markdown/text export. Do not rely on ChatGPT's native Copy Response button to preserve interactive widget state or buttons.

All copy actions copy only; never execute commands or submit agent prompts. Be accurate about the current working directory and environment. Omit elements without grounded data.

Run proposal cards remain the final section of the answer. Prefer horizontal arrangements, clean coordinated visual language and variable card widths. Each card may have a tiny **always-mounted text input** so mouse-driven paste targets the field on the first click; keep a visible focus state and accessible label. The host may still route special mouse events elsewhere: test with the actual input controller rather than promise universal behavior.

## Layout and scope

Use one top header for repository/ref, optional run reference, AIP version and icon-only Settings. Do not duplicate the version in a bottom rail. GitHub change cards may expand/collapse details as warranted, and may be repeated for different repositories/branches or combined into an explicit comparison card. Distinguish edited, committed, pushed and deployed states. Next-run options are optional and have no fixed count.
