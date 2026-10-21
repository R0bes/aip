# AIP — Agent Interaction Protocol

AIP is a small convention for **iterative ChatGPT collaboration on user-owned GitHub repositories** (experimental version 0.3.0).

The [`AGENTS.md`](AGENTS.md) file is the **single authoritative instruction source**. The component templates are:

- [GitHub result](components/github-result.md) — retained, design refinement pending
- [Next Run](components/next-run.md) — accepted hybrid HTML selection/input with native dispatch
- [Agent proposal](components/proposal.md) — experimental

They are declarative generation examples (DIL and embedded HTML/CSS/JS) for ChatGPT to adapt, not an importable component library or a standalone renderer. No extra runtime infrastructure is required.
