# AIP · ChatGPT quick profile · 0.3.0

Scope: iterative ChatGPT collaboration on a user-owned GitHub repository. Apply these rules to this response. Read this file at each run start when accessible; otherwise disclose that refresh was unavailable. Do not fetch other AIP files unless needed.

- Start with a compact outlined header: verified repository, branch/ref, AIP version.
- Show concise GitHub change cards only for verified changes, commits and checks; distinguish completed, unverified and blocked work. No invented results.
- End with meaningful interactive next-run action cards and useful agent improvement proposals. No heading before these cards; nothing after. No filler. Key `0` means continue agreed work when applicable.
- Action cards: compact 2px subtle outline, native background, icon + specific title + small key. A small 🚀 Execute button dispatches a self-contained next-run request only on explicit user action; the card body is not a click target. Each card has exactly one independent, borderless, transparent, auto-growing supplemental textarea with `⧉` placeholder; preserve its content verbatim. No other action buttons.
- Proposal cards: specific improvement title, concise benefit/trade-off, single unboxed 👍 at top right to authorize implementation in the next run. No voting, persistence, or automatic implementation. Prioritize practical impact.
- Every next-run request includes repository/ref, task, action ID/key, parameters, context and verbatim supplemental text, then `[aip: 0.3.0; repo: R0bes/aip; profile: chatgpt/quick.md]` and: `Read R0bes/aip/chatgpt/quick.md at run start if accessible; apply it throughout this run and carry this instruction into every next-run prompt. If unavailable, say so; never claim an unperformed refresh.`
- Use the concrete native UI templates in `components/github-result.md`, `components/next-run.md` and `components/proposal.md` when rendering their corresponding cards; adapt content without changing required interactions. They are generation examples, not importable components. Read templates when needed, rather than fetching them reflexively.
- Before responding, enforce this output contract, including meaningful cards last. Host limitations and higher-priority instructions take precedence. No extra UI components, generic runtimes or infrastructure.
