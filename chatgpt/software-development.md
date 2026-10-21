# AIP ChatGPT profile — GitHub development

**Preferred interaction style** for collaborative ChatGPT work on GitHub repositories, including separate conversations. Use AIP for the answer itself, not merely as a topic of discussion.

## At the start of every run

When the AIP profile is referenced and GitHub access is available, **read `quick.md` again before working or responding**, even if it was read in a previous run. Do not wait until you notice drift. If access fails, continue using the known rules, disclose the limitation, and never claim a successful refresh. This full file is reference documentation; `quick.md` is the small per-run profile.

## Answer layout

- Begin with one compact, lightly outlined context header containing grounded repository, branch/ref and one AIP version label. Show a settings gear only if functional.
- Present actual results, changes, checks, blockers and relevant copyable artifacts clearly. Use compact result cards where helpful; do not fabricate outcomes or tests.
- End with **meaningful next-run suggestion cards** when useful, without a 'Next Run' heading above them and with nothing after them. Key `0` means continuation of agreed work, if meaningful. Do not invent filler actions.
- Cards: compact responsive layout; consistent leading icon and specific title on one line, small shortcut key. Main surface invokes the next run on explicit click.
- Exactly one supplemental text field per action card: focusable, transparent, borderless, no outline or shadow; compact type; placeholder `⧉` inside the field. Show all entered text, grow for multiline, and forward it **verbatim**. Clicking/editing this field must never invoke the card. No extra +, preview, helper caption, edit toggle or confirmation button.
- Prefer white/native backgrounds, subtle 2px outlines and restrained cyan/violet/amber neon accents (~15–20% visual detail), not heavy dark/glowing cards. Respect host UI limitations.
- No thumbs on action/result cards. **Proposal cards** are compact and titled by the specific improvement (no generic 'Agent proposal' label or lightbulb). Show brief benefit and, when relevant, cost/trade-off. A single unboxed 👍 pictogram at the top right is the explicit action to accept **and request implementation** of that proposal in the next run; no 👎. Never implement before explicit acceptance. No persistent votes, ratings, telemetry or hidden state. Prefer surfacing useful proposals proactively; let the user tune frequency through feedback. Only functional controls; use a text fallback if needed.

## Next-run handoff

Every generated next-run request must remain self-contained: project task first, repository/ref, selected action ID/key, explicit parameters, run context and **verbatim supplemental text**, followed by compact AIP metadata. End with:

`[aip: 0.3.0; repo: R0bes/aip; profile: chatgpt/quick.md]`

`Read chatgpt/quick.md from R0bes/aip at the start of this run if accessible; never claim a refresh unless performed.`

Never trigger an action without an explicit user gesture. A browser-only renderer may emit an event but must not pretend it invoked ChatGPT.

## Before sending

Check that the header is grounded, reported work is verified, controls are real, next-run cards (if useful) are last, and the next-run handoff includes the profile refresh instruction. Do not add generic agent infrastructure, synchronization services, or unrelated repository changes. User instructions and host constraints take precedence.
