# ChatGPT run-output components

Prefer a concise context header (repository, branch, optional agent/run reference), then a visually distinct change summary when actual edits occurred. Show **what the user should notice when testing**, not just a file list.

Render local commands in a code block or compact command panel with an explicit copy control. Render prompts for another agent as separate copyable artifacts. Offer a dedicated **Copy report** action for a faithful, self-contained Markdown/text export. Do not rely on ChatGPT's native Copy Response button to preserve interactive widget state or buttons.

All copy actions copy only; never execute commands or submit agent prompts. Be accurate about the current working directory and environment. Omit elements without grounded data.

Run proposal cards remain the final section of the answer. Prefer horizontal arrangements, clean coordinated visual language and variable card widths. Each card may have a tiny **always-mounted text input** so mouse-driven paste targets the field on the first click; keep a visible focus state and accessible label. The host may still route special mouse events elsewhere: test with the actual input controller rather than promise universal behavior.
