# AIP — Agent Interaction Protocol

AIP's primary use case is collaborative software development with ChatGPT on GitHub repositories. It makes verified results easy to read, presents meaningful next-step suggestions as compact interactive cards, and preserves task context and presentation guidance across follow-up runs and separate ChatGPT conversations.

**Status:** experimental draft v0.3.0. **Priority:** the ChatGPT software-development profile, clear results, useful next-run cards, and reliable handoff. Protocol schemas and the standalone renderer support this experience; they are not ends in themselves. Agent runtimes, cross-platform synchronization, and general infrastructure are not project goals.

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
- [chatgpt/quick.md](chatgpt/quick.md) — minimal per-run rules.
- [chatgpt/software-development.md](chatgpt/software-development.md) — initial profile for collaborative iterative software development.
- [chatgpt/settings.md](chatgpt/settings.md) — settings interaction (draft; no persistence/sync yet).
- [AGENTS.md](AGENTS.md) — maintenance instructions.

The current product focus is ChatGPT conversations working on arbitrary GitHub repositories. Keep per-run rules in `chatgpt/quick.md`, full reference in `chatgpt/software-development.md`, and instruct every next run to re-read the quick profile when GitHub access is available. Do not expand toward generic agent infrastructure unless a concrete user need warrants it.

## Feedback and continuity

See [feedback.md](feedback.md) for optional improvement proposals, experimental agent self-assessment during AIP development, human calibration, and guidance refresh semantics. Proposals and self-ratings are not mandatory.


## Standalone HTML report renderer (experimental)

`python scripts/render_report.py examples/report.json /tmp/aip-report.html` renders a schema-validated report to a standalone interactive HTML file. Open it in a browser. Result cards expand on click; copyable artifacts use the browser clipboard when permitted; next-run cards contain one always-visible supplemental-text field with a copy-glyph placeholder. Clicking a next-run card's main surface emits the `aip:invoke` browser event and displays its JSON payload for inspection; it **does not** run an agent or call ChatGPT. An embedding host must explicitly handle this event to dispatch a new request. Run `python -m unittest discover -s tests -v` and `python scripts/validate.py` for checks. Browser interaction and clipboard permissions require browser testing.
