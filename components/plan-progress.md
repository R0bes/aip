# Plan / Progress card — multi-run work

Read [AGENTS.md](../AGENTS.md) first. Use this card for work spanning multiple runs, not for a trivial one-step task. This is a **presentation and handoff template**, not a plan database, workflow engine or scheduler.

## Semantics

- Show the **goal**, a short explanation of the plan, and numbered actionable work packages with concrete deliverables. Optionally group packages into phases.
- Status vocabulary: **open** (circle, neutral), **active** (play/circle-dot, accent), **done** (check, success), **blocked** (alert, warning). Use **both symbol and text**, not color alone. Distinguish confirmed work from unverified claims; completed means evidenced, not just previously requested.
- Progress is `done / total` for the explicitly enumerated packages; active and blocked do **not** count as done. Do not guess a percentage when the scope is unknown. State if the plan is provisional or changed.
- The plan is **not automatically persisted across chats**. For continuity, cite the existing issue/document/branch when one exists, or include a compact self-contained plan snapshot in the next-run handoff. If no durable source exists, never claim one.
- **Default interaction pattern: Plan is the status overview; adjacent Next Run cards are the action surface.** The agent should normally propose grounded plan-aware Next Run options: continue the next eligible package, implement a specified package or safe batch (e.g. AP3 + AP4), review/retry an unverified or failed package, resolve a blocker, or revise the plan. Only offer meaningful alternatives; don't manufacture them.
- Plan rows are informational by default, **not a second set of Next Run cards**. An optional plan-row selection may preselect a corresponding Next Run action, but must not dispatch, alter package status, or create a second rocket. Keep one shared input and one native rocket as specified in `next-run.md`.
- Every plan-aware action must identify exact package IDs and expected deliverables; a batch must mention dependencies and only group independently executable/ordered packages. **The next eligible step** means prerequisites are met, not simply the next numerical ID. A retry/review action must not silently reset verified status.
- The next-run handoff must include the plan goal, plan/source identifier if known, the numbered package definitions and statuses, selected package IDs, relevant dependencies/blockers, and the expected completion/verification criteria. If the snapshot is too large, use a verified durable plan source plus the necessary focused context; do not rely on an unexplained reference to a previous chat. A plan is not authorization for unsupervised background execution.
- Do not mark a package done merely because a new run was requested. Update statuses only after work and verification. If steps are parallelizable, mention it but don't pretend they have started.

## Presentation modes and future dependencies

- **Compact:** goal, verified `done / total`, one-line current/next package, and any critical blocker. Prefer this in ordinary development responses.
- **Detailed:** goal and explanation, full package list with deliverables, verified statuses and relevant dependencies. Use when planning, auditing, or explicitly requested.
- Keep the Plan card visually consistent with other AIP cards but **do not apply selection glow** to informational plan rows. Glow belongs to an explicitly selected Next Run action; use subtle status icons and restrained accents for plan progress.
- A **gate** is a named verification/approval condition with evidence and a pending/passed/failed status, not an automatic executor. A **branch** is a conditional dependency or alternative path. Defer complex graph rendering until needed; simple dependency text is sufficient for now. Do not silently mark gates passed or choose a branch without evidence.
- Follow the semantic theme tokens in [`../themes/README.md`](../themes/README.md); the default remains pastel until the user chooses otherwise. Theme changes presentation, never plan state.

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

Use the established Next Run component in [next-run.md](next-run.md), e.g. choices `0 = Nächstes freigegebenes AP`, `1 = AP3 und AP4 nacheinander`, `2 = AP5 überprüfen und bei Bedarf wiederholen`. Show those cards alongside the plan, not as extra dispatch buttons in each plan row. The native rocket dispatches the selected action with a plan snapshot (or grounded plan source + focused context) in **Proposal context**, exact package IDs and acceptance criteria in **Proposed task**, and the shared input verbatim. If a plan row can be selected, it may update the corresponding Next Run selection via shared DIL state; no separate send action.
