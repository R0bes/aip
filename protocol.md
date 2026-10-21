# AIP — Agent Interaction Protocol

Version: **0.3.0 (draft)**

## Purpose

A portable contract for human selection and configuration of follow-up agent actions after a run. AIP is not an agent-to-agent transport, GUI toolkit, or authorization mechanism.

## Run output

AIP also defines optional run-output elements: context header, change summary, local command, agent handoff, and copyable report. See [output.md](output.md). A report is not required to contain every element; use only elements grounded in actual work.

## Run completion

Report completed work, verification actually performed, blockers, and remaining work. If useful next actions exist, place the selector last; **nothing** follows it. Result artifacts may be interleaved with prose before the selector. Do not force any fixed number of options; omit the selector when no meaningful next action exists.

## Actions

- Every action has a stable `id`, unique display `key`, concise `title`, and self-contained `instruction`.
- Key `0` is reserved for `continue`: continue the agreed plan without unrequested scope expansion. Do not invent continuation when no work remains.
- Other actions must represent materially different choices. No fixed count is required.
- At most one action may be marked `recommended`; this is advisory only.
- Action IDs, keys, and parameter IDs within an action must be unique. If key `0` exists, its ID MUST be `continue`; any `continue` action MUST use key `0`. For this development profile, key `0` is required when continuation is meaningful.
- A selector may include optional `meta` information such as a `settings` action and a version reference. Meta actions are not numbered workflow choices; they must still be explicitly invoked.
- Optional descriptions/icons are presentation hints. Preconditions do not grant authorization.
- Action-local parameters may be `boolean`, bounded `integer`, `enum`, or `text`. Text can be multiline, optional, and defaults to an empty string.

## Invocation

Only a genuine user gesture invokes an action. Capture the selected action and its current parameters, then dispatch a **new, self-contained user request** with stable action ID, display key, complete instruction, explicit parameter values, verbatim extra user text, and enough project/run context to resume independently. Keep the actual project task first; place compact AIP protocol/profile/version metadata at the end as machine-readable or otherwise unobtrusive context. Never rely on hidden widget state. The host's safety, permissions, and confirmation requirements still apply.

## Optional supplemental text

A selector MAY carry user-supplied supplemental text per action. An adapter may keep a tiny always-mounted input visible as a `+` affordance to support mouse-driven paste; this input must be focusable, editable, and scoped to its own action. A renderer MAY expose a compact paste affordance and attach the captured text verbatim to the next invocation. It MUST NOT claim clipboard access unless the host actually grants it; if direct paste is unavailable, it SHOULD provide an explicit user-controlled paste field. Never access clipboard contents automatically or without a user gesture. The text must remain reviewable before dispatch. Future attachment types are not defined in this draft.

## Version reference and settings

An optional single compact version reference in the context header can identify the exact protocol release or revision used (e.g. `AIP 0.3.0 · abc1234`). It is informational, not evidence that the agent fetched the latest release. An optional settings entry may request a separate settings interaction; changing preferences does not itself perform repository updates or grant access. Live synchronization, persistence and automatic updates are out of scope for this draft.

## Text fallback

Show numbered actions. Bare `0` or `1` selects defaults; accept `1 depth=4` and `0 prioritize_checks=true` for configured actions. For short text accept `1 notes="..."`; for multiline text accept a key followed by a text block or the platform's text input. Clarify invalid or ambiguous values. Keys are unique within the current selector; stable IDs remain meaningful after reordering.

## Rendering recommendations (non-normative)

Prefer compact, information-rich action cards for parameterless actions and compact action-specific controls (checkboxes, sliders, selects, multiline text) where needed. Avoid ambiguous click targets. Provide accessible labels, keyboard interaction, visible defaults, and responsive wrapping.

## Portability and versioning

The same descriptor may be rendered by ChatGPT, CLI/text, or a future A2UI adapter. JSON Schema validates shape, not all semantic constraints (e.g. uniqueness, recommendation count, continuation meaning). Use semantic versions: compatible additions bump minor, breaking semantics bump major. Conformance is not claimed without dedicated tests.
