# ChatGPT adapter

ChatGPT is AIP's first concrete rendering/dispatch target, **not** part of the core protocol.

When available, render compact buttons and action-local checkbox, select, slider, and multiline text controls. On an explicit user action, send a new self-contained turn containing the chosen action ID, complete instruction, explicit parameter values, verbatim additional user text, and necessary project context.

Use numbered text fallback if controls are unavailable. Never silently invoke an action. The action selector belongs at the end of the response.

Available UI capabilities vary by ChatGPT client; a repository file or global instruction cannot guarantee that every agent loads this specification.

See [software-development.md](software-development.md) for the initial domain profile. Future profiles and renderers may coexist.

## Discoverability

A ChatGPT agent can be asked to read `https://github.com/R0bes/aip`, starting with `README.md`, `protocol.md`, and this adapter's profile. For software-development tasks, it may consult this public repository when available and relevant; no automatic loading or live synchronization is guaranteed. If it cannot access the repository, it should say so rather than claim compliance.

## Compact footer

Show a small version reference such as `AIP 0.3.0` near the final action selector, and a visually secondary settings control (gear icon if available). The settings control starts a new, explicit settings interaction, never silently modifies host settings. See `settings.md`.
