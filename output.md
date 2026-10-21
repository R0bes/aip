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

## Improvement proposal and feedback

An agent MAY offer a concise, actionable improvement proposal after a run if there is a substantive reason. Proposals can target the active project or AIP itself and should include expected benefit and trade-off. No proposal is better than a low-value proposal. An optional agent self-rating is explicitly subjective and should not masquerade as external evaluation. Human ratings may be compared to calibrate recommendation thresholds. See [feedback.md](feedback.md).

## Structured report payload

The experimental [report.schema.json](report.schema.json) describes one top header, an ordered array of optional inline blocks (text, generic GitHub interactions, copyable artifacts, and notices), and an optional `next_run` action descriptor. The `next_run` element is **last in rendering order** regardless of how blocks are laid out. An absent `next_run` is exceptional but valid when no meaningful continuation exists. This does not mean the normal project workflow should hide continuation options.

Generic GitHub blocks identify their operation; titles describe the specific event, not the block type. Generic artifact blocks have optional titles/descriptions and verbatim copyable content. UI expansion and clipboard behavior belong to the adapter; the payload is not itself a renderer.
