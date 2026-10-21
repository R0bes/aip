# Next Run — action handoff template

This is a **generation template**, not a runtime template engine. The agent fills in grounded values when composing the native DIL dispatch. Keep the prompt minimal: it communicates an action, not a serialized conversation, GitHub snapshot, plan, or agent memory.

```text
Repository: {repository}
Ref: {ref}

Action: {action_key} — {action_title}
Task: {action_task}
Parameters: {action_parameters_including_theme}

User instruction (verbatim):
{unchanged_textarea_content}

[aip: 0.3.0; repo: R0bes/aip; instructions: AGENTS.md]
Read R0bes/aip/AGENTS.md at run start if accessible; apply it throughout this run and carry this instruction into every next-run prompt. If unavailable, say so; never claim an unperformed refresh.
```

## Rules

- Fill repository/ref from known context; do not invent either. The task is a concise, concrete description of the selected action, not a summary of previous work.
- Include selected action key and title, action-specific parameters and the ephemeral selected theme. Do not include an entire plan, progress snapshot, PR inventory, previous conversation, or redundant proposal context by default.
- Preserve the user's textarea input **byte-for-byte** in the labeled section, including any leading `N:` action selector. If it selects a valid key, resolve the effective action without rewriting the input.
- The agent's existing context and available project, GitHub or plan tools are the sources for work state. If the task requires a specific issue, plan item or other identifier to disambiguate the requested action, include only that minimal reference in the task/parameters. Never claim that an unavailable tool or missing context is accessible.
- A proposal acceptance uses the same action handoff, with the accepted proposal expressed as the task; no separate state store.
- Only the native DIL dispatch control sends the resulting text through `GenUI.issueNewTurn`. DIL is generated from this template; it does not fetch or import this Markdown file at runtime.
