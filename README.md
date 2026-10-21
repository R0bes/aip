# AIP — Agent Interaction Protocol

AIP is a lightweight convention for **iterative ChatGPT collaboration on user-owned GitHub repositories** (experimental version 0.3.0). It is a set of generation instructions and examples, **not** an installable renderer or component library.

- [AGENTS.md](AGENTS.md) — authoritative interaction and handoff rules. Read this first at the start of an AIP run.
- [Next Run prompt template](prompts/next-run.md) — minimal stateless action handoff; no plan or history serialization.\n- [Theme tokens](themes/themes.css) — canonical CSS custom properties for Pastel, Cyberpunk and Neutral.
- [Identity header](components/identity-header/COMPONENT.md) — repository/ref orientation and expandable theme gear.
- [Next Run](components/next-run/COMPONENT.md) — **sole accepted hybrid template**, with selectable cards, circular morphing real HTML textarea and native circular-arrow/play dispatch.
- [GitHub results](components/github-result/COMPONENT.md) — verified changes, pull requests and branches.
- [Plan / Progress](components/plan-progress/COMPONENT.md) — numbered multi-run work packages, gates and grounded status.
- [Agent proposal](components/proposal/COMPONENT.md) — experimental improvement suggestion.
- [Next Run SVG](assets/next-run.svg) — accepted native dispatch icon.
- [Transcription input SVG](assets/transcription-input.svg) — accepted idle icon of the morphing text input.

Each component has a `COMPONENT.md` entry point. Each component separates its `COMPONENT.md` contract from a `.dil` generation reference. Next Run additionally includes reusable HTML sources for cards and the morphing input. The `.dil` suffix is a source convention, not a standalone executable format. These are agent-facing references, not a runtime or tool-call API.

AIP components are views over existing agent/tool state, not independent stores: GitHub tools supply GitHub facts, an agent plan tool or project plan supplies progress, and the header reflects known repository/ref context. Next Run sends selected intent only.\n\nThemes are ephemeral and propagated via next-run parameters. No AIP settings persistence, personal agent-rule controls, additional runtime or infrastructure.
