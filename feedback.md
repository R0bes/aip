# AIP feedback and guidance continuity (draft)

## User feedback

Ordinary conversational feedback is the default. **Use thumbs-up/down only on dedicated agent improvement proposal cards**, never on ordinary action or result cards. No implicit telemetry, persistence or inferred rating is allowed.

## Scope discipline

Judge suggestions by whether they improve the ChatGPT GitHub-development experience: verified results, helpful next-run cards, or continuity across runs and conversations. Prefer small usability fixes over generic protocol or runtime infrastructure. Do not invent proposals just to populate cards.

## Optional improvement proposals

Offer a concrete agent-originated improvement proposal for the active project or AIP only when it is worth the user's attention. Use a distinct proposal card with expected benefit/trade-off and functional 👍/👎 controls. 👍 expresses interest or approval for discussion, **not authorization to change code**; 👎 rejects the idea for now. Each control sends explicit conversational feedback; never silently persist votes or infer consent to implement. No proposal is preferable to filler.

## Experimental calibration (opt-in)

During AIP development, an agent MAY offer explicitly labeled, subjective self-assessment of result quality, action relevance or suggestion value. Human and agent judgments are distinct; an overall rating must not be silently interpreted as a rating of individual cards. The current profile does not render ratings by default.

## Guidance continuity

Follow-up requests may carry a compact AIP version/profile footer. For the ChatGPT GitHub-development profile, re-read the compact primary profile at the start of each run when retrieval is available; other supporting documentation can be refreshed on explicit request, version change, or suspected drift. Do not claim automatic reloading, persistent settings or remote feedback storage without evidence.

## Drift-aware next-run handoff

Generated follow-up prompts SHOULD include the AIP repository and profile reference plus a short conditional refresh instruction: if AIP rules are unavailable, uncertain, or inconsistent with the current task, re-read the relevant repository instructions before continuing. This is **not** a requirement to fetch the repository on every run. A refresh must only be reported as performed when actually executed. Do not introduce background synchronization, version polling, or a new service for this purpose.
