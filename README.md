# AIP — Agent Interaction Protocol

AIP is a small convention for **iterative ChatGPT collaboration on user-owned GitHub repositories** (experimental version 0.3.0).

The [`AGENTS.md`](AGENTS.md) file is the **single authoritative instruction source**. The native UI component templates are:

- [GitHub result](components/github-result.md)
- [Next Run](components/next-run.md)
- [Agent proposal](components/proposal.md)

They are declarative JSX-like examples for ChatGPT to adapt, not an importable component library or a standalone renderer. No extra runtime infrastructure is required.
