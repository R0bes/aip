# AIP — Agent Interaction Protocol

AIP is a small convention for **iterative ChatGPT collaboration on user-owned GitHub repositories** (experimental version 0.3.0).

The [theme tokens](themes/README.md) define a lightweight shared visual language (Pastel default; Cyberpunk and Neutral alternatives), without assuming one global CSS scope across native and HTML cards.

The [`AGENTS.md`](AGENTS.md) file is the **single authoritative instruction source**. The component templates are:

- [GitHub cards](components/github-result.md) — verified changes, open pull requests and branch overviews
- [Plan / Progress](components/plan-progress.md) — numbered multi-run work packages and grounded status
- [Next Run](components/next-run.md) — accepted hybrid HTML selection/input with native dispatch
- [Agent proposal](components/proposal.md) — experimental

They are declarative generation examples (DIL and embedded HTML/CSS/JS) for ChatGPT to adapt, not an importable component library or a standalone renderer. No extra runtime infrastructure is required.
