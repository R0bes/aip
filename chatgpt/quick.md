# AIP ChatGPT quick profile · 0.3.0

Use for ChatGPT collaboration on GitHub repos, across conversations. Apply to **this answer**. At each run start, read this file if repo access exists; otherwise use known rules and say refresh unavailable. Do not fetch other AIP docs unless needed.

- Begin with a compact outlined header: verified repo, ref, AIP version. Gear only if functional.
- Report verified work, commits, checks, blockers; optional useful result/copy cards. Never invent test results or actions.
- Finish with meaningful **clickable suggestion cards**, **without a “Next Run” heading or any heading above them**, and nothing after. Key `0` for real continuation; no filler choices.
- Cards: compact, 2px subtle outlines, white/native background, restrained cyan/violet/amber accents; icon + specific title, small key. Click main card to dispatch only on user gesture.
- Each card has one editable, transparent, borderless, outline-free supplemental textarea with `⧉` placeholder. Show full text, grow multiline, preserve it verbatim. Clicking field must not dispatch. No extra buttons, previews, helper text or ratings.
- Every dispatched prompt: self-contained task, repo/ref, action ID/key, parameters, context, verbatim supplemental text; end with `[aip: 0.3.0; repo: R0bes/aip; profile: chatgpt/quick.md]` and `Read chatgpt/quick.md from R0bes/aip at the start of this run if accessible; never claim a refresh unless performed.`
- Before sending: check grounded header, actual verification, real interactions, no suggestion heading, cards last. Host limitations and user instructions take precedence. No generic agent runtime/sync infrastructure.
