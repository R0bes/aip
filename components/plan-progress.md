# Plan / Progress card — multi-run work

Read [AGENTS.md](../AGENTS.md) first. Use this card for work spanning multiple runs, not for a trivial one-step task. This is a **presentation and handoff template**, not a plan database, workflow engine or scheduler.

## Semantics

- Show the **goal**, a short explanation of the plan, and numbered actionable work packages with concrete deliverables. Optionally group packages into phases.
- Status vocabulary: **open** (circle, neutral), **active** (play/circle-dot, accent), **done** (check, success), **blocked** (alert, warning). Use **both symbol and text**, not color alone. Distinguish confirmed work from unverified claims; completed means evidenced, not just previously requested.
- Progress is `done / total` for the explicitly enumerated packages; active and blocked do **not** count as done. Do not guess a percentage when the scope is unknown. State if the plan is provisional or changed.
- The plan is **not automatically persisted across chats**. For continuity, cite the existing issue/document/branch when one exists, or include a compact self-contained plan snapshot in the next-run handoff. If no durable source exists, never claim one.
- A plan row can be the basis of a **Next Run** choice: continue the whole plan, do a specific package, review blockers, or replan. **Selection of a plan row alone never starts work**; use the established shared Next Run input + native rocket. Handoff must identify the package, plan context and remaining statuses. A plan is not authorization for unsupervised background execution.
- Do not mark a package done merely because a new run was requested. Update statuses only after work and verification. If steps are parallelizable, mention it but don't pretend they have started.

## Compact native DIL example

```jsx
<box border={{size:1,color:"default"}} radius="xl" padding={3} gap={3}>
  <row align="center" justify="between">
    <row align="center" gap={2}><icon name="list-checks"/><text strong>Plan · AIP Kartenfamilie</text></row>
    <text color="secondary" size="xs">2 / 5 erledigt</text>
  </row>
  <text size="sm" color="secondary">GitHub-Ansichten und eine verlässliche Fortschrittsanzeige für mehrere Entwicklungsruns etablieren.</text>
  <box gap={2}>
    <row align="start" gap={2}><icon name="check-circle-2" color="success"/><box flex="1" gap={1}><text weight="medium" size="sm">AP1 · Anforderungen</text><text size="xs" color="secondary">Kartenarten und Statusmodell festlegen · Erledigt</text></box></row>
    <row align="start" gap={2}><icon name="check-circle-2" color="success"/><box flex="1" gap={1}><text weight="medium" size="sm">AP2 · Vorlagen</text><text size="xs" color="secondary">DIL-Muster erstellen · Erledigt</text></box></row>
    <row align="start" gap={2}><icon name="circle-dot" color="info"/><box flex="1" gap={1}><text weight="medium" size="sm">AP3 · Interaktion</text><text size="xs" color="secondary">Planpunkt als Next Run übergeben · In Arbeit</text></box></row>
    <row align="start" gap={2}><icon name="circle" color="secondary"/><box flex="1" gap={1}><text weight="medium" size="sm">AP4 · Integration</text><text size="xs" color="secondary">GitHub- und Plan-Karten zusammen anzeigen · Offen</text></box></row>
    <row align="start" gap={2}><icon name="alert-circle" color="warning"/><box flex="1" gap={1}><text weight="medium" size="sm">AP5 · Abnahme</text><text size="xs" color="secondary">End-to-End-UI prüfen · Blockiert bis AP4</text></box></row>
  </box>
</box>
```

The five packages and statuses above are **demonstration data**, not claims about actual project progress. Replace with grounded current plan data; avoid arbitrary decorative progress. For progress, the verified `done / total` counter is sufficient. Add a visual bar only when supported and grounded in the same counts.

## Example next-run handoff

Use the established Next Run component in [next-run.md](next-run.md), e.g. choices `0 = Plan fortsetzen`, `1 = AP3 umsetzen`, `2 = Blocker prüfen`. Pass a self-contained plan snapshot with package IDs, deliverables, statuses and source ref in **Proposal context**; include the selected package in **Proposed task**, and preserve the shared input verbatim. No second dispatch button in the plan card.
