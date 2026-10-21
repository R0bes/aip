# ChatGPT adapter

ChatGPT is AIP's first concrete rendering/dispatch target, **not** part of the core protocol.

When available, render compact buttons and action-local checkbox, select, slider, and multiline text controls. On an explicit user action, send a new self-contained turn containing the chosen action ID, complete instruction, explicit parameter values, verbatim additional user text, and necessary project context.

Use numbered text fallback if controls are unavailable. Never silently invoke an action. The action selector belongs at the end of the response.

Available UI capabilities vary by ChatGPT client; a repository file or global instruction cannot guarantee that every agent loads this specification.

See [software-development.md](software-development.md) for the initial domain profile. Future profiles and renderers may coexist.
