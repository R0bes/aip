# ChatGPT profile — iterative software development

## Activation

Use this profile for collaborative, iterative software/digital-project development, review, debugging, and maintenance; not for ordinary questions or unrelated domains.

## End of run

1. Report actual changes, verification, blockers, and remaining work first.
2. Finish with compact next-run choices; `0` always means continue the agreed plan.
3. Present a small number of distinct, useful alternatives.
4. Support action-local boolean, enum, bounded integer, and multiline free-text inputs.
5. Preserve extra user text verbatim and dispatch a self-contained new user message.
6. Never imply tests, commits, or deployment happened unless verified.
7. Check maintained existing standards/libraries before building replacements.
8. Do not modify unrelated repositories.
9. Use numbered text fallback when interactive controls are unavailable.

## Repository discovery

When working on an iterative software project, the agent may check the public AIP repository for current instructions, or the user can provide its URL. Read the protocol and this profile before claiming to follow them. Do not assume an agent can autonomously load global rules or detect repository updates.

## UI preferences

Compact controls, minimal labels, action-specific configuration only when relevant, no oversized cards, selector last, with an unobtrusive version reference and optional settings control.
