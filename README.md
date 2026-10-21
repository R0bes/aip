# AIP — Agent Interaction Protocol

AIP is a lightweight convention for **iterative ChatGPT collaboration on user-owned GitHub repositories** (experimental version 0.3.0). It is a set of generation instructions and examples, **not** an installable renderer or component library.

- [AGENTS.md](AGENTS.md) — authoritative interaction and handoff rules. Read this first at the start of an AIP run.
- [Theme tokens](themes/tokens.csv) — single CSV table of Pastel, Cyberpunk and Neutral values; [application guidance](themes/README.md).
- [Identity header](components/identity-header.md) — repository/ref orientation and expandable theme gear.
- [Next Run](components/next-run.md) — **sole accepted hybrid template**, with selectable cards, circular morphing real HTML textarea and native circular-arrow/play dispatch.
- [GitHub results](components/github-result.md) — verified changes, pull requests and branches.
- [Plan / Progress](components/plan-progress.md) — numbered multi-run work packages, gates and grounded status.
- [Agent proposal](components/proposal.md) — experimental improvement suggestion.
- [Next Run SVG](assets/next-run.svg) — accepted native dispatch icon.

Themes are ephemeral and propagated via next-run parameters. No AIP settings persistence, personal agent-rule controls, additional runtime or infrastructure.
