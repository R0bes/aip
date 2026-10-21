# AIP — Agent Interaction Protocol

AIP is a minimal convention for **iterative ChatGPT work on user-owned GitHub repositories** (experimental v0.3.0). It reports verified work and provides explicit next-run controls.

The sole runtime instruction source is [`chatgpt/quick.md`](chatgpt/quick.md). Three native ChatGPT UI generation templates supply concrete structures:

- [GitHub result](components/github-result.md) — verified changes, commits and checks
- [Next run](components/next-run.md) — editable supplemental text and 🚀 Execute
- [Agent proposal](components/proposal.md) — practical improvements accepted with 👍

Templates are declarative source examples for ChatGPT to adapt, **not** importable JSX components or a standalone renderer. Read and apply the quick profile at each run start if accessible. Every next-run request propagates that instruction.

No HTML renderer, JSON schemas, settings, ratings, report exports or general-purpose agent infrastructure.
