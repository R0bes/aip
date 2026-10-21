# AIP — Agent Interaction Protocol

Version: **0.2.0 (draft)**

## Purpose

A portable contract for human selection and configuration of follow-up agent actions after a run. AIP is not an agent-to-agent transport, GUI toolkit, or authorization mechanism.

## Run completion

Report completed work, verification actually performed, blockers, and remaining work. If useful next actions exist, place the selector last; no prose follows it.

## Actions

- Every action has a stable `id`, unique display `key`, concise `title`, and self-contained `instruction`.
- Key `0` is reserved for `continue`: continue the agreed plan without unrequested scope expansion. Do not invent continuation when no work remains.
- Other actions must represent materially different choices. No fixed count is required.
- At most one action may be marked `recommended`; this is advisory only.
- Optional descriptions/icons are presentation hints. Preconditions do not grant authorization.
- Action-local parameters may be `boolean`, bounded `integer`, `enum`, or `text`. Text can be multiline, optional, and defaults to an empty string.

## Invocation

Only a genuine user gesture invokes an action. Capture the selected action and its current parameters, then dispatch a **new, self-contained user request** with protocol version, stable action ID, display key, complete instruction, explicit parameter values, verbatim extra user text, and enough project/run context to resume independently. Never rely on hidden widget state. The host's safety, permissions, and confirmation requirements still apply.

## Text fallback

Show numbered actions. Bare `0` or `1` selects defaults; accept `1 depth=4` and `0 prioritize_checks=true` for configured actions. For short text accept `1 notes="..."`; for multiline text accept a key followed by a text block or the platform's text input. Clarify invalid or ambiguous values. Keys are unique within the current selector; stable IDs remain meaningful after reordering.

## Rendering recommendations (non-normative)

Prefer compact buttons for parameterless actions and compact action-specific controls (checkboxes, sliders, selects, multiline text) where needed. Avoid ambiguous click targets. Provide accessible labels, keyboard interaction, visible defaults, and responsive wrapping.

## Portability and versioning

The same descriptor may be rendered by ChatGPT, CLI/text, or a future A2UI adapter. JSON Schema validates shape, not all semantic constraints (e.g. uniqueness, recommendation count, continuation meaning). Use semantic versions: compatible additions bump minor, breaking semantics bump major. Conformance is not claimed without dedicated tests.
