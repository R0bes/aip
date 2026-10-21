# AIP — Agent Interaction Protocol

AIP is a lightweight convention for **iterative ChatGPT collaboration on user-owned GitHub repositories** (experimental version 0.3.0). It is a set of generation instructions and examples, **not** an installable renderer or component library.

- [AGENTS.md](AGENTS.md) — authoritative interaction and handoff rules. Read this first at the start of an AIP run.
- [Theme tokens](themes/themes.css) — canonical CSS custom properties for Pastel, Cyberpunk and Neutral.
- [Identity header](components/identity-header/COMPONENT.md) — repository/ref orientation and expandable theme gear.
- [Next Run](components/next-run/COMPONENT.md) — **sole accepted hybrid template**, with selectable cards, circular morphing real HTML textarea and native circular-arrow/play dispatch.
- [GitHub results](components/github-result/COMPONENT.md) — verified changes, pull requests and branches.
- [Plan / Progress](components/plan-progress/COMPONENT.md) — numbered multi-run work packages, gates and grounded status.
- [Agent proposal](components/proposal/COMPONENT.md) — experimental improvement suggestion.
- [Next Run SVG](assets/next-run.svg) — accepted native dispatch icon.
- [Transcription input SVG](assets/transcription-input.svg) — accepted idle icon of the morphing text input.

Each component has a `COMPONENT.md` entry point. The Next Run component additionally separates DIL composition guidance and reusable HTML sources; simple components keep short examples in their own definition. These are agent-facing references, not a runtime or tool-call API.

Themes are ephemeral and propagated via next-run parameters. No AIP settings persistence, personal agent-rule controls, additional runtime or infrastructure.
