# AIP — Agent Interaction Protocol

**Scope:** iterative ChatGPT collaboration on the user's own GitHub repositories. **Version:** experimental 0.3.0.

AIP is a small interaction convention, not a general agent framework. Every run should show verified GitHub work and offer practical ways to continue without losing context.

## Only three UI components

1. **GitHub change cards:** verified edits, commits, checks and blockers.
2. **Next-run action cards:** user-selectable follow-up tasks, with optional verbatim supplemental text; key `0` continues agreed work.
3. **Agent improvement proposals:** high-impact suggestions, accepted with 👍 for implementation on the next run.

Keep cards compact and native to ChatGPT. No invented status, filler actions or implicit execution.

## How to use

The operative profile is [`chatgpt/quick.md`](chatgpt/quick.md). Read and **apply** it at the start of each run when accessible. Every next-run prompt must instruct the following run to do the same.

## Out of current scope

General-purpose adapters, standalone HTML reports, JSON report protocols, settings, ratings, exports and synchronization are not product goals. Obsolete experimental renderer, schemas, examples, settings and feedback files have been removed.

See [`AGENTS.md`](AGENTS.md) for repository maintenance guidance.
