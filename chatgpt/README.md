# ChatGPT adapter

ChatGPT is AIP's first concrete rendering/dispatch target, **not** part of the core protocol.

When available, render compact buttons and action-local checkbox, select, slider, and multiline text controls. Do not show a permanent generic additional-instructions textarea by default. Instead, provide a small paste affordance when supplemental text is useful. Prefer one-click clipboard paste only where host APIs and permission allow; otherwise reveal a field for user-driven paste (e.g. mouse context menu). Do not claim direct clipboard access in ChatGPT without verifying it. The pasted text must be visible/reviewable and forwarded verbatim. On an explicit user action, send a new self-contained turn containing the chosen action ID, complete instruction, explicit parameter values, verbatim additional user text, and necessary project context.

Use numbered text fallback if controls are unavailable. Never silently invoke an action. The action selector belongs at the end of the response.

Available UI capabilities vary by ChatGPT client; a repository file or global instruction cannot guarantee that every agent loads this specification.

See [software-development.md](software-development.md) for the initial domain profile. Future profiles and renderers may coexist.

## Discoverability

A ChatGPT agent can be asked to read `https://github.com/R0bes/aip`, starting with `README.md`, `protocol.md`, and this adapter's profile. For software-development tasks, it may consult this public repository when available and relevant; no automatic loading or live synchronization is guaranteed. If it cannot access the repository, it should say so rather than claim compliance.

## Compact footer

Show a small version reference such as `AIP 0.3.0` near the final action selector, and a visually secondary settings control (gear icon if available). The settings control starts a new, explicit settings interaction, never silently modifies host settings. See `settings.md`.

## Run-card layout (software-development profile)

Prefer horizontally arranged, responsive compact run cards with a clean, restrained aesthetic. Present next-run proposals as compact, information-rich cards. A simple proposal can be one clickable card; a proposal containing sliders, checkboxes or choices uses a separate Go button. Paste is **per-card** with independent supplemental text; clicking Paste must not activate the parent card. When supplemental text is opened, switch the card to explicit Go submission. Keep only Settings in the right-aligned, bottom-aligned utility rail alongside the version label. Use subtle accent colors and avoid excessive decoration. These are adapter/profile presentation rules, not requirements of the platform-neutral protocol.

### Mouse-first details and paste limitation

Titles and icons share the card header; keyboard shortcut numbers are secondary corner metadata. Cards may have different widths. Descriptions must name actual tasks, boundaries, or expected outputs rather than explain the button label. A clipboard-injecting mouse action can target the ChatGPT composer before an on-demand textarea appears; opening the field after that click does not solve the race. Direct clipboard capture is unsupported unless the host exposes an authorized clipboard API. Do not silently read clipboard or pretend the fallback is one-click.

For report components and reliable cross-agent copying, see [output.md](output.md). For a concrete example, see [examples.md](examples.md).
