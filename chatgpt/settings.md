# ChatGPT settings interaction (draft)

A visually secondary ⚙ settings control may appear next to the AIP action selector and version label. It is a **meta action**, not a numbered workflow step.

When activated, start a new user-visible settings interaction. Show only settings that are meaningful and actually controllable in the current ChatGPT client.

## Proposed session preferences

- **Interface mode**: `development` (default) or `minimal`. Future domain profiles may be added.
- **Density**: `compact` (default) or `comfortable`.
- **Color accent**: `host-default` (default); offer additional choices only if supported by the host. Do not promise arbitrary CSS or theme control.
- **Version information**: display the version that was actually read; optionally show the exact commit/revision if known.
- **Repository refresh**: future capability, **not implemented**. A user-requested manual re-read may be performed if repository access exists; never imply automatic polling or persistent syncing.

Preferences are session-scoped unless the host provides explicit persistence. Do not assume that a later agent run remembers settings; include required settings in the dispatched self-contained instruction. Do not perform writes, repository sync, or change account settings as a side effect of merely opening settings.

## Example footer

`[0 Continue] [1 Verify]   [⚙ Settings]  AIP 0.3.0`

On a text-only client, show `settings` as a separate textual meta action.
