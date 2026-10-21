# AIP feedback and guidance continuity (draft)

## User feedback

Ordinary conversational feedback is the default. **Use a single thumbs-up acceptance control only on dedicated agent improvement proposal cards**, never on ordinary action or result cards. No implicit telemetry, persistence or inferred rating is allowed.

## Scope discipline

Judge suggestions by whether they improve the ChatGPT GitHub-development experience: verified results, helpful next-run cards, or continuity across runs and conversations. Prefer small usability fixes over generic protocol or runtime infrastructure. Do not invent proposals just to populate cards.

## Optional improvement proposals

Proactively offer concrete agent-originated improvement ideas for the active project or AIP, initially favoring more useful proposals over excessive restraint; adjust frequency from user feedback. Use a compact card titled by the idea itself, with benefit and optional cost/trade-off. No generic label or lightbulb. One unboxed 👍 at top right explicitly requests implementation of the described proposal in the next run; no thumbs-down. Never implement without the click or persist a rating/vote. Avoid filler.

## Experimental calibration (opt-in)

During AIP development, an agent MAY offer explicitly labeled, subjective self-assessment of result quality, action relevance or suggestion value. Human and agent judgments are distinct; an overall rating must not be silently interpreted as a rating of individual cards. The current profile does not render ratings by default.

## Guidance continuity

Follow-up requests may carry a compact AIP version/profile footer. For the ChatGPT GitHub-development profile, re-read the compact primary profile at the start of each run when retrieval is available; other supporting documentation can be refreshed on explicit request, version change, or suspected drift. Do not claim automatic reloading, persistent settings or remote feedback storage without evidence.

## Drift-aware next-run handoff

Generated follow-up prompts SHOULD include the AIP repository and profile reference plus a short conditional refresh instruction: if AIP rules are unavailable, uncertain, or inconsistent with the current task, re-read the relevant repository instructions before continuing. This is **not** a requirement to fetch the repository on every run. A refresh must only be reported as performed when actually executed. Do not introduce background synchronization, version polling, or a new service for this purpose.
