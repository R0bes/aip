# AIP repository instructions

## Product priority

Optimize for collaborative ChatGPT development work on GitHub repositories: clear verified result presentation, meaningful next-run cards, and reliable context/profile handoff across runs and conversations. Do not treat generic agent runtimes, multi-platform adapters, background synchronization, or standalone protocol infrastructure as goals. Prefer the smallest change that improves this workflow.

## Development process

- Start with the actual user-facing failure or friction; avoid speculative architecture expansion.
- Maintain `chatgpt/software-development.md` as the primary behavioral profile and `chatgpt/README.md` as its adapter guidance.
- For changes to next-run prompts, verify that task, action, context, parameters, and verbatim supplemental text survive and that the conditional AIP refresh footer remains last.
- For UI changes, preserve the clickable card and independent supplemental field; check presentation and interactions where possible.
- Run relevant tests when possible and report exact results or clearly state what could not be executed.
- Avoid mandatory per-run GitHub fetching; refresh on explicit request, version change, or suspected rule drift.

## Repository maintenance

- Read `protocol.md` before changing protocol semantics or its schema.
- Keep platform-neutral rules separate from adapters under `chatgpt/` and future platform folders.
- The initial workflow profile is `chatgpt/software-development.md`.
- Prefer maintained standards and existing libraries before custom infrastructure.
- Keep schema, examples, and documentation aligned. Validate JSON and semantic invariants.
- Do not claim tests, commits, or integration outcomes that were not verified.
- Work only in the repository the user authorizes; do not introduce unrelated project-specific names into the spec.
