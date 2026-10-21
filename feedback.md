# AIP feedback and guidance continuity (draft)

## User feedback

Ordinary conversational feedback is the default. **Do not render per-card thumbs-up/down** in the current ChatGPT software-development profile. No implicit telemetry, persistence or inferred rating is allowed.

## Optional improvement proposals

Offer a concrete improvement proposal for the active project or AIP only when it is worth the user's attention. Include expected benefit and trade-off, without quotas. No proposal is preferable to filler.

## Experimental calibration (opt-in)

During AIP development, an agent MAY offer explicitly labeled, subjective self-assessment of result quality, action relevance or suggestion value. Human and agent judgments are distinct; an overall rating must not be silently interpreted as a rating of individual cards. The current profile does not render ratings by default.

## Guidance continuity

Follow-up requests may carry a compact AIP version/profile footer. Refresh instructions on explicit request, version change, or suspected drift when retrieval is available. Do not claim automatic reloading, persistent settings or remote feedback storage without evidence.

## Drift-aware next-run handoff

Generated follow-up prompts SHOULD include the AIP repository and profile reference plus a short conditional refresh instruction: if AIP rules are unavailable, uncertain, or inconsistent with the current task, re-read the relevant repository instructions before continuing. This is **not** a requirement to fetch the repository on every run. A refresh must only be reported as performed when actually executed. Do not introduce background synchronization, version polling, or a new service for this purpose.
