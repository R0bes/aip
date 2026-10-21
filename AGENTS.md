# AIP — Agent Interaction Protocol · 0.3.0

## Scope and source of truth

AIP governs iterative ChatGPT collaboration on user-owned GitHub repositories. **This file is the single authoritative AIP instruction source.** Read and apply it at the start of each AIP run when accessible; if inaccessible, disclose that instead of claiming a refresh. Read component templates when needed. Avoid duplicate profiles, renderers, schemas or infrastructure.

## Response contract

1. Begin with a compact outlined header identifying verified repository, branch/ref and AIP version. Never invent a ref or result.
2. Use the contextual GitHub card family in `components/github-result.md`: verified change results, open PR overview and branch overview. Choose only relevant views; ground all displayed GitHub facts in actual retrieved results. Distinguish completed, unverified and blocked work; never invent PR/branch state.
3. For multi-run work, use `components/plan-progress.md` to show goal, numbered packages, concrete deliverables and grounded open/active/done/blocked status. Progress counts only verified completed packages. Plan rows may inform Next Run choices, but do not dispatch or persist anything by themselves; carry a self-contained plan snapshot or source reference forward. End with a useful, curated set of interactive Next Run cards and, where worthwhile, agent improvement proposals. **No heading before those cards and no text after them.** Key `0` means continue agreed work. Do not offer filler actions.
4. Next Run uses the accepted hybrid template in `components/next-run.md`: compact HTML choice cards with icon and title on one row, small visible action number in a corner, meaningful description and concrete expected deliverables, exclusive selection via outline/glow, one shared transparent borderless HTML textarea (`💬` placeholder), and one accessible native icon-only 🚀 button beside it. Choose a meaningful single-digit number of cards, not a fixed three. The shared input may explicitly select an action using a leading valid `N:` prefix; keep the entire original input unchanged in `User instruction (verbatim)` and resolve the selected key consistently. Only the native rocket dispatches. User instructions take precedence over proposed task defaults within higher-priority constraints.
5. Choose the number and layout of suggestions deliberately, based on meaningful distinct actions and available space; do not pad to a fixed count, impose a hard cap of three, or force verbose cards into an awkward grid. Always consider `0 = Weiter` when continuing the current work is useful. Add genuinely distinct, actionable alternatives and proactive improvements when warranted; do not manufacture options for quantity. Prefer a manageable selection rather than an exhaustive catalog. Keep still-relevant unchosen options available in subsequent runs when context permits, without inventing persistence or claiming that they were saved. Use compact summaries with explicit deliverables; expand details only when needed. Proposal cards offer specific improvements prioritized by practical benefit and impact, with concise benefit/trade-off and one unboxed 👍 at top right. Clicking it authorizes implementation **in the next run** only. No implicit acceptance, ratings, voting or persistence.
6. Every dispatched next-run request is self-contained: repository/ref, proposed task, action ID/key, parameters, proposal context, a clearly labeled primary `User instruction (verbatim)` section containing the textarea content unchanged, AIP version, and the instruction: `Read R0bes/aip/AGENTS.md at run start if accessible; apply it throughout this run and carry this instruction into every next-run prompt. If unavailable, say so; never claim an unperformed refresh.` Use `[aip: 0.3.0; repo: R0bes/aip; instructions: AGENTS.md]` as the AIP footer metadata, updating repository/ref context as appropriate. When working on a different user repository, still reference this authoritative AIP source explicitly.
7. Text-only next-run dispatch cannot attach screenshots or other files. Never claim an HTML file picker can forward attachments through `GenUI.issueNewTurn`; ask the user to attach images in the regular chat composer when visual context is needed. Follow higher-priority host instructions and actual UI capabilities. Never claim tests or interactions succeeded unless verified.

## Native UI component templates

These files contain JSX-like **generation templates**, not importable modules. Use their structure, substitute concrete values and supply working callbacks. Do not invent a separate rendering layer.

- [`components/github-result.md`](components/github-result.md) — contextual GitHub cards: verified results, open PRs and branches.
- [`components/plan-progress.md`](components/plan-progress.md) — multi-run plan/progress display and next-run handoff.
- [`components/next-run.md`](components/next-run.md) — **accepted hybrid Next Run** visual and dispatch template.
- [`components/proposal.md`](components/proposal.md) — **experimental** optional improvement proposal with 👍 acceptance.
- [`components/next-run-html-experiment.md`](components/next-run-html-experiment.md) — archived exploration, superseded by the accepted hybrid template. Enter cannot directly invoke the ChatGPT host action.

## Maintenance

Keep README descriptive, this file authoritative, and component files focused on implementation. Avoid repeating this contract in each component. No standalone HTML renderer, JSON protocol, generic adapters, settings, exports or telemetry.
