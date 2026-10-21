# AIP run output elements (draft)

AIP covers both **run output** (what happened) and **next-run proposals** (what to do next). Elements are optional, composable, and independent of a specific renderer.

## Context header

When grounded, show repository, branch/ref, agent/run reference and protocol version. Never guess repository or branch. If the run spans multiple repositories or branches, label each scope explicitly. The agent/run reference should be a portable identifier supplied by the host or explicitly assigned by the agent, not an invented globally unique ID.

## Change summary

Show a distinctive compact change indicator **only when actual changes are confirmed**. Summarize what changed, affected files/areas, verification performed, and **observable behavior to expect when testing**. Distinguish local edits, commits, pushes, and deployments. Do not imply a UI-visible change for documentation-only edits.

## Command artifact

Represent local commands as copyable artifacts with a short purpose, expected environment, working directory, safety notes if applicable, and an exact command string. Copy must preserve the command verbatim. Commands do not execute on copy or on render.

## Agent handoff artifact

A prompt intended for another agent is a distinct copyable artifact. Include task, repository/branch, relevant constraints, evidence, and what the receiving agent should deliver. Keep it self-contained. Never include hidden secrets or unsupported claims.

## Copyable report

Offer an optional **plain-text/Markdown export** of the full run report for cross-agent review. The exported report includes context, actual changes, verification status, outstanding work and relevant commands/prompts. Interactive widgets are converted to text descriptions with current values when available. Do not assume the host's native “copy response” action serializes interactive components; provide a dedicated explicit copy action. Avoid embedding credentials or other sensitive data.

## Rendering

Adapters may implement these elements as compact graphical panels with copy controls. The core specifies meaning and fidelity, not visual layout.
