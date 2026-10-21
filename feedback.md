# Feedback and guidance continuity (draft)

## Optional improvement proposals

After a run, propose an improvement only if it is specific, actionable, and likely worth the user's attention. Scope can be the active project or AIP itself. Each proposal identifies its target, expected benefit, cost or trade-off, and a possible next action. Do not generate proposals merely to satisfy a quota. Do not confuse a recommendation with work already completed.

## Experimental self-assessment (AIP development only)

During AIP interface development, a compact agent estimate MAY show:
- **Output quality** (0–5): how useful, grounded, and complete the result seems.
- **Option relevance** (0–5): whether the offered next actions are distinct and worth showing.
- **Suggestion value** (0–5): whether any proposed improvement is worth the visual space; omit this score if no suggestion is offered.
- **Confidence** (low / medium / high): confidence in those estimates.

These are subjective self-assessments, not verified metrics. A separate human rating can be collected optionally, and disagreement used to tune when cards, suggestions, or extra controls appear. Keep the visual display tiny (e.g. dots, compact bar, or icons), but preserve accessible text labels. Avoid numeric false precision.

## Guidance continuity

Each self-contained follow-up request SHOULD identify the AIP version and the relevant profile or pinned revision. A host that supports retrieving rules may refresh them when a version changes, on explicit request, or when instructions seem to drift. Do not claim automatic reload, freshness, or persistent memory without actual evidence. A configurable periodic recheck or countdown may be explored later, but is not required by the protocol.
