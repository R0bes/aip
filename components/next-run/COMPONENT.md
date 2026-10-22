# Next Run — accepted hybrid UI

Read [AGENTS.md](../../AGENTS.md). This is the **only current Next Run template**. The former HTML experiment has been removed. Preserve the agreed visual and interaction model rather than replacing it with a plain DIL input.

## Contract

- Offer a curated number of compact selectable action cards, with 20px icon beside title, small numeric key, useful description and optional action-specific controls. Equal-height siblings; selected card gets only an accent outline and subtle glow. Key `0` continues useful work. Use a scoped HTML AppBlock for cards when needed.
- **One shared real HTML textarea**, initially a **40×40px circular icon**. The idle SVG is [transcription-input.svg](../../assets/transcription-input.svg): **three audio bars, an I-beam cursor, and a separate lower arrow**. Focusing the textarea expands the *same element* into a normal editable multi-line field. Empty + blurred collapses; nonempty + blurred stays expanded. Normal selection, paste, caret and input must work. A permanently visible DIL `<input>`/`<textarea>` is **not equivalent**.
- To its right, keep **one native DIL `<pressable>`**, 44px circle, with the custom circular-arrow/play SVG in [assets/next-run.svg](../../assets/next-run.svg). Only this native control calls `GenUI.issueNewTurn`; AppBlock HTML cannot dispatch a ChatGPT turn.
- DIL owns shared selection, text, action parameters and theme state. Bind AppBlocks through `bind={{value,setValue}}`; `globalThis.__bindings?.…` and `globalThis.__effect?.(…)` must always be optional-chained.
- Carry the theme chosen in the header gear panel as separate AIP presentation metadata (not a task parameter), e.g. `AIP theme: Neutral` before the final bootstrap line. Theme changes recolor all theme-aware components immediately, using [themes/themes.css](../../themes/themes.css); no persistent settings.
- Dispatch the minimal action handoff from [prompts/next-run.md](../../prompts/next-run.md): optional **work** project/ref, concise task, action/key, task-only parameters, exact `User instruction (verbatim)` textarea content, separate optional AIP theme metadata and the reusable `Obey R0bes/aip/prompts/aip-instructions.md!` line. Never substitute the AIP source for the work repository. Do not serialize plan state, GitHub snapshots or redundant proposal context. A leading valid `N:` selects that action **without altering the original textarea text**. Never claim HTML-only Enter sends or that file attachments can be forwarded.

## DIL composition (generation reference)

The linked DIL source shows the important binding boundary. Replace `UNIQUE` consistently; provide concrete action definitions and actual HTML for the two AppBlocks. The SVG path is identical to `assets/next-run.svg`.

See [composition.dil](composition.dil) for the DIL binding and dispatch skeleton, not a complete standalone response. Insert the HTML from `cards.html` and `input.html` and compose the identity header separately.

The DIL source uses Neutral illustration colors only. Bind the selected theme from the shared header state in the real response; never create a second independent theme state.

## Shared morphing input — AppBlock HTML source

Use the reusable HTML source in [input.html](input.html).

The inline palette literals are examples mirrored from the authoritative CSS; update them whenever `themes/themes.css` changes. They are not an independent token source.

## Compact selectable cards — AppBlock HTML source

Use the reusable HTML source in [cards.html](cards.html).

Replace example actions and card content together; only include meaningful choices. More elaborate action-specific controls are optional and must update their own parameter state without changing other actions.

## Verification checklist

- [ ] Empty, unfocused textarea is the 40px circle with the approved SVG.
- [ ] Focus expands the **same** textarea; typing, paste, selection and multiline editing work.
- [ ] Blur preserves nonempty text and expanded state; empty blur collapses.
- [ ] Theme selection changes header, cards, textarea and native pressable consistently.
- [ ] Card selection is exclusive and keyboard accessible.
- [ ] Native pressable dispatches the selected key, separate AIP theme metadata and unchanged instruction.
- [ ] No AppBlock send button, no personal agent rules and no persistent settings.

Repository text review is not equivalent to a successful live UI interaction test.
