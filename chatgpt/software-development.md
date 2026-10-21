# ChatGPT profile — iterative software development

## Activation

Use this profile for collaborative, iterative software/digital-project development, review, debugging, and maintenance; not for ordinary questions or unrelated domains.

## End of run

1. Report actual changes, verification, blockers, and remaining work first.
2. Finish with compact next-run choices; `0` always means continue the agreed plan.
3. Present a small number of distinct, useful alternatives.
4. Support action-local boolean, enum, bounded integer, and multiline free-text inputs when needed; keep generic supplemental text visually collapsed to a small, always-mounted input by default.
5. Preserve extra user text verbatim and dispatch a self-contained new user message.
6. Never imply tests, commits, or deployment happened unless verified.
7. Check maintained existing standards/libraries before building replacements.
8. Do not modify unrelated repositories.
9. Use numbered text fallback when interactive controls are unavailable.

## Repository discovery

When working on an iterative software project, the agent may check the public AIP repository for current instructions, or the user can provide its URL. Read the protocol and this profile before claiming to follow them. Do not assume an agent can autonomously load global rules or detect repository updates.

## UI preferences

Prefer a **horizontal, responsive row** of compact, information-rich **run proposal cards** rather than a vertical list or plain button row. Keep the visual language clean, elegant and restrained; avoid clutter and decorative controls. A simple card is itself clickable. A card with editable parameters has a separate explicit Go control so adjusting controls cannot accidentally dispatch the run. Cards may use restrained color/accent and short descriptions. Give each card its **own tiny, always-mounted, focusable text input** (visually about the size of a plus icon, with no placeholder prose or visible border until focused), and isolated supplemental text state. Clicking the field must not dispatch the card. Paste on one card must never be forwarded with another card. When text or other parameters are present, use an explicit Go control; avoid ambiguous parent-card click handling. Put only the icon-only Settings control and a small version label in a right-aligned, bottom-aligned utility rail. Keep action-local controls inside their card. Do not assume every action needs parameters. The selector is the final response element.

## Card refinements

- Put icon and action title on the same header line; render the numeric key small and secondary in a corner (mouse-first, keyboard fallback).
- Allow variable card widths based on content, with responsive wrapping.
- Describe the **specific next work** and expected boundary/deliverable, not tautologies such as 'continue the agreed plan'.
- When useful, offer a scoped parameter such as `next_step` versus `complete_work_block`, with clear consequences.
- Treat paste-on-click as an adapter capability, not an assumed feature. In mouse-injection workflows, creating an input *after* a paste-triggering click is too late and can send text to the host composer. Prefer an actual host-supported clipboard-read action, otherwise disclose the limitation and use a user-controlled fallback. Do not claim the paste button works as one-click clipboard ingestion unless verified.

## Additional run output

Use [output.md](output.md) for context headers, distinct change summaries with observable testing expectations, copyable local commands, agent handoff prompts, and a dedicated copyable report. Use only elements grounded in the actual run. Prefer a small always-mounted per-card input over an input created after the mouse paste gesture; do not assume it works with every mouse controller. Compact controls should use icons and shape where clear, with accessible labels and tooltips; avoid long segmented-control labels.

## Clean output grammar and feedback

Use a GitHub icon for repository change summaries, not a generic checkmark. Apply the same restrained card design to output elements: icon-only Copy controls (with accessible names), concise text, and consistent geometry within each run. Agent handoff may be labeled `Agent prompt` with a robot icon. The compact input should show only `+` at rest; focus can expand it for readable editing. Avoid unnecessary labels, explanatory filler, and default controls that do not change the outcome.

Offer **optional** improvement suggestions only when concrete and worthwhile, for the project or AIP itself. Never manufacture suggestions or follow-up options to fill space. During AIP design iterations, an optional compact self-assessment can score output quality and suggestion relevance, explicitly as a subjective estimate rather than measured fact; invite the user's independent rating to calibrate thresholds. See [feedback.md](feedback.md).

Before generating a selector, check whether the current AIP guidance is available and coherent. If the profile appears missing or contradictory, reload the pinned profile if accessible or ask for it. Do not silently claim fresh sync. A lightweight revision marker can travel in self-contained follow-up prompts; periodic rechecks may be configured later, but a decrementing counter is not required.

## Updated composition

Keep a **single** AIP version reference in the top context header, with an icon-only Settings control in that header; remove the bottom-right utility rail. Number of next-run cards is **zero or more**, driven by meaningful choices; never force exactly two. Prefer mouse-first clean coordinated cards, with flexible widths and optional expanded detail.

For each card, a tiny round `+` is the visible face of an always-mounted focusable input. On input, render the user-supplied text as a **non-editable preview** elsewhere in that card; keep the input accessible for editing and show a clear focused state. A host may not permit an input to be truly icon-sized and still reliably accept mouse paste; test actual focus/paste behavior and use a slightly larger focus target if necessary. Text remains isolated to that action.

AIP is third-party UI infrastructure in other projects: generated follow-up requests put the project task and its scope first, and a short unobtrusive AIP metadata footer last. Do not make AIP the subject of an unrelated project's prompt.
