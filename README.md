# AIP — Agent Interaction Protocol

AIP defines portable run-output artifacts and structured human decisions between iterative agent runs: results, changes, copyable commands and handoffs, next actions, parameters, and self-contained follow-up invocations.

**Status:** experimental draft v0.3.0. **Scope:** platform-neutral interaction semantics; not a GUI framework, transport protocol, or authorization system.

## Layout

- [protocol.md](protocol.md) — core interaction rules.
- [output.md](output.md) — run context, change summaries and copyable artifacts.
- [run-ui.schema.json](run-ui.schema.json) — JSON Schema for action descriptors.
- [report.schema.json](report.schema.json) — JSON Schema for complete reports.
- [examples/report.json](examples/report.json) — structured full-report example.
- [examples/development-run.json](examples/development-run.json) — sample descriptor.
- [chatgpt/README.md](chatgpt/README.md) — ChatGPT rendering/dispatch guidance.
- [chatgpt/output.md](chatgpt/output.md) — ChatGPT run-output presentation and copy semantics.
- [chatgpt/examples.md](chatgpt/examples.md) — example report layout.
- [chatgpt/software-development.md](chatgpt/software-development.md) — initial profile for collaborative iterative software development.
- [chatgpt/settings.md](chatgpt/settings.md) — settings interaction (draft; no persistence/sync yet).
- [AGENTS.md](AGENTS.md) — maintenance instructions.

The core remains renderer-neutral. ChatGPT is the first concrete adapter; other adapters may be added later. Existing standards such as A2UI may inform future renderers, but are not required dependencies.

## Feedback and continuity

See [feedback.md](feedback.md) for optional improvement proposals, experimental agent self-assessment during AIP development, human calibration, and guidance refresh semantics. Proposals and self-ratings are not mandatory.


## Standalone HTML report renderer (experimental)

`python scripts/render_report.py examples/report.json /tmp/aip-report.html` renders a schema-validated report to a standalone interactive HTML file. Open it in a browser. Result cards expand on click; copyable artifacts use the browser clipboard when permitted; next-run cards contain one always-visible supplemental-text field with a copy-glyph placeholder. Clicking a next-run card's main surface emits the `aip:invoke` browser event and displays its JSON payload for inspection; it **does not** run an agent or call ChatGPT. An embedding host must explicitly handle this event to dispatch a new request. Run `python -m unittest discover -s tests -v` and `python scripts/validate.py` for checks. Browser interaction and clipboard permissions require browser testing.
