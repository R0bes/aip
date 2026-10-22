# AIP integration · 0.4.0

This file is the reusable entry point for adding AIP to **any** agent task.

1. Read `R0bes/aip/AGENTS.md` from the AIP source repository at the start of this run when accessible, and consult the relevant component contracts and generation references. Do not claim a refresh if access fails; say so.
2. Use AIP as a **presentation and interaction convention**, not as the target project, unless the user's task explicitly concerns AIP. The agent name/role, work repository and current task in the identity header must come from the **actual assignment**, not the AIP source.
3. Apply the selected AIP theme to the entire response, including other native UI components where supported. Follow the host's actual component and interaction capabilities.
4. For a subsequent Next Run, preserve the user's task intent and append exactly this reusable instruction line, rather than copying this file or AGENTS.md into the prompt:

`Obey R0bes/aip/prompts/aip-instructions.md!`

5. Keep handoffs stateless and concise; never invent project state, repository refs, successful UI interactions or verification. If the AIP source is unavailable, continue the task with an honest disclosure.

This document is a bootstrap reference; `AGENTS.md` remains the authoritative AIP specification.
