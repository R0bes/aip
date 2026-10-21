# ChatGPT adapter — AIP 0.3.0 draft

ChatGPT collaboration on GitHub repositories is AIP's primary target experience, including across separate conversations. The goal is readable verified results and practical next-run suggestions, not an agent runtime or background synchronization system. See [protocol.md](../protocol.md), [output.md](../output.md), and [software-development.md](software-development.md). Repository instructions are not automatically loaded or synchronized. When AIP is invoked, read the compact `quick.md` profile at the start of every run if GitHub access is available.

## Rendering

Start with one outlined context header, including known repository/ref, one version label, and an icon-only settings gear **only if functional**. Interleave normal prose and optional inline result cards with content-specific titles and consistently sized icons. Result-card main surfaces may expand grounded details; nested copy actions remain independent.

Render GitHub interactions and generic copyable commands/prompts when relevant. Offer a dedicated faithful report export when useful. Copy controls never execute. Do not invent hidden details, unsupported attachments, or clipboard access.

Put compact next-run cards at the **very end**, with no 'Next Run' heading; nothing follows. The whole main card surface dispatches on an explicit click. Inputs must be isolated from dispatch. Do not force a fixed number of choices or generic scope switches. Distinguish next-action cards from optional agent improvement proposal cards; proposal cards have one unboxed 👍 at top right that explicitly dispatches an implementation request for the specific proposal. No 👎, no voting state or persistence; no automatic implementation before the click. Proposal cards use their idea as the title, no generic label or lightbulb, and show brief benefit/optional trade-off.

## Supplemental text

Use **one** focusable text field inside each next-run card. Empty state: a large copy icon displayed **inside** the field as a paste cue. Filled state: **all text remains visible and directly editable**, with multiline growth as needed. Style this field with a transparent background, no border or outline, and smaller compact typography. No separate + control, shortened preview, expand/collapse state, confirm button, or helper caption. The text is forwarded verbatim in a self-contained next-turn request.

## Settings and fallback

The gear can adjust only real, local presentation options supported by the current host. Never pretend to change account settings or persist preferences. If no real options exist, omit/disable it. Use numbered text fallback if graphical controls are unavailable. Never dispatch without an explicit user action.
