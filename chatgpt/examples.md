# Example report layout

Context: `R0bes/aip` · `main` · `AIP 0.3.x`

**Changes** — Updated ChatGPT layout documentation.

**Expect when testing** — Run proposals are horizontally arranged; per-card text input accepts pasted text; no global paste control.

**Local command** — `python scripts/validate.py` (from repository root; requires `jsonschema`).

**Agent handoff** — A separate copyable review prompt referencing repository, branch, and required checks.

**Copy report** — Explicit Markdown export containing context, changes, verification status, and next actions.

**Next runs** — Compact horizontal cards, with icons and title on the same row, small keyboard index in the corner, and action-local parameters. Keep an input mounted in each card for mouse-driven paste.
