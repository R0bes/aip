# AIP — Agent Interaction Protocol · 0.3.0

## Scope and source of truth

AIP governs iterative ChatGPT collaboration on user-owned GitHub repositories. **This file is the single authoritative AIP instruction source.** Read and apply it at the start of each AIP run when accessible; if inaccessible, disclose that instead of claiming a refresh. Read component templates when needed. Avoid duplicate profiles, renderers, schemas or infrastructure.

## Response contract

1. Begin with a compact outlined header identifying verified repository, branch/ref and AIP version. Never invent a ref or result.
2. Present concise native GitHub result cards only for verified edits, commits, checks or blockers; distinguish completed, unverified and blocked work. Include what matters to the user.
3. End with useful interactive Next Run cards and, where worthwhile, agent improvement proposals. **No heading before those cards and no text after them.** Key `0` means continue agreed work. Do not offer filler actions.
4. Next Run cards have a subtle 2px outline, native background, icon, specific title, small key, exactly one independent auto-growing supplemental textarea (`⧉` placeholder), and a small 🚀 Execute button. Only the button dispatches; preserve supplemental text verbatim. No other action buttons.
5. Proposal cards offer specific improvements prioritized by practical benefit and impact, with concise benefit/trade-off and one unboxed 👍 at top right. Clicking it authorizes implementation **in the next run** only. No implicit acceptance, ratings, voting or persistence.
6. Every dispatched next-run request is self-contained: repository/ref, task, action ID/key, parameters, context, verbatim supplemental text, AIP version, and the instruction: `Read R0bes/aip/AGENTS.md at run start if accessible; apply it throughout this run and carry this instruction into every next-run prompt. If unavailable, say so; never claim an unperformed refresh.` Use `[aip: 0.3.0; repo: R0bes/aip; instructions: AGENTS.md]` as the AIP footer metadata, updating repository/ref context as appropriate. When working on a different user repository, still reference this authoritative AIP source explicitly.
7. Follow higher-priority host instructions and actual UI capabilities. Never claim tests or interactions succeeded unless verified.

## Native UI component templates

These files contain JSX-like **generation templates**, not importable modules. Use their structure, substitute concrete values and supply working callbacks. Do not invent a separate rendering layer.

- [`components/github-result.md`](components/github-result.md) — verified GitHub result card.
- [`components/next-run.md`](components/next-run.md) — editable Next Run with explicit 🚀 Execute.
- [`components/proposal.md`](components/proposal.md) — optional improvement proposal with 👍 acceptance.

## Maintenance

Keep README descriptive, this file authoritative, and component files focused on implementation. Avoid repeating this contract in each component. No standalone HTML renderer, JSON protocol, generic adapters, settings, exports or telemetry.
