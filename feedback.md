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

## Rating interpretation

A rating is not actionable without a named dimension and a defined scale. Separate **run outcome quality** from **interface relevance** (whether cards, options, and suggestions earned their space). Do not infer precise option relevance from an undifferentiated overall 4/5. Store agent estimates and human ratings as separate observations; a difference is a calibration signal, not proof that either estimate is correct. Keep both ratings optional.

## Per-card lightweight feedback

A renderer MAY expose thumbs-up/thumbs-down on each card independently. A rating means only that the particular card was useful or unhelpful, unless a different criterion is explicitly labeled. Unrated cards carry no negative signal. Keep feedback unobtrusive and never require it to proceed. A feedback click must not dispatch a next run or accidentally toggle card details. Distinguish user-provided ratings from agent self-assessment; do not claim that a click persists to a server without an actual persistence mechanism.

## Feedback interpretation

Thumbs-up/down is scoped to the particular card and its presentation/utility, not automatically to the underlying code change or full textual answer. Do not interpret unrated cards as neutral approval or rejection. Keep all per-card ratings independent, and never claim they were stored remotely without an actual write.
