# AIP — Agent Interaction Protocol

AIP defines structured human decisions between iterative agent runs: results, next actions, action-local parameters, optional free text, and self-contained follow-up invocations.

**Status:** experimental draft v0.3.0. **Scope:** platform-neutral interaction semantics; not a GUI framework, transport protocol, or authorization system.

## Layout

- [protocol.md](protocol.md) — normative interaction rules.
- [run-ui.schema.json](run-ui.schema.json) — JSON Schema for action descriptors.
- [examples/development-run.json](examples/development-run.json) — sample descriptor.
- [chatgpt/README.md](chatgpt/README.md) — ChatGPT rendering/dispatch guidance.
- [chatgpt/software-development.md](chatgpt/software-development.md) — initial profile for collaborative iterative software development.
- [chatgpt/settings.md](chatgpt/settings.md) — settings interaction (draft; no persistence/sync yet).
- [AGENTS.md](AGENTS.md) — maintenance instructions.

The core remains renderer-neutral. ChatGPT is the first concrete adapter; other adapters may be added later. Existing standards such as A2UI may inform future renderers, but are not required dependencies.
