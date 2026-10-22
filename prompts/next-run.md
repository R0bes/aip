# Next Run — stateless task handoff · 0.4.0

Generation reference, not a runtime template engine. The **work repository** and AIP source are separate concepts. Omit optional project/ref fields if unknown; never substitute `R0bes/aip` for the work project.

```text
Project: {optional_work_repository}
Ref: {optional_work_ref}

Action: {action_key} — {action_title}
Task: {action_task}
Parameters: {task_parameters_only}

User instruction (verbatim):
{unchanged_textarea_content}

Obey R0bes/aip/prompts/aip-instructions.md!
```

The generated handoff may omit `Project`, `Ref` and `Parameters` when not applicable. The current theme is **presentation metadata**, not a task parameter: when a nondefault theme is selected, add `AIP theme: {theme}` before the final Obey line. If no theme was explicitly selected, Pastel is the fallback.

## Rules

- Keep the selected action key, title and concise concrete task; include only task-specific parameters and essential identifiers. Do not serialize the conversation, plan, GitHub snapshot or AIP rules.
- Preserve the user's textarea input **byte-for-byte**, including a leading valid `N:` selector; resolve the effective action key without rewriting the text.
- Source task state from actual context and available project tools. Do not claim that unavailable state or tools are accessible.
- Only a native DIL control dispatches through `GenUI.issueNewTurn`; HTML/AppBlock does not send a turn. The AIP source must be read by the receiving agent when accessible, not dynamically imported by DIL.
