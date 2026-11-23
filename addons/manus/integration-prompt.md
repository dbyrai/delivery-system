# Manus and GitHub Integration Prompt

Use in the target project with repository access. This prompt prepares setup;
application implementation requires a subsequent concrete assignment.

```text
Set up the optional Manus add-on for direct work in this GitHub project.

Read applicable project instructions and these files under addons/manus/:
README.md, howto.md, instructions.md, and templates/manus-project-instructions.md.
Inspect the working tree, documentation root, existing integrations, and roles.
Preserve code, documentation, IDs, and local customizations.

Choose level 1 (existing project) or level 2 (new project) from the actual state.
Clarify ambiguity before dependent work. Preserve completed Delivery System
adoption and bootstrap. First-time adoption requires repository review followed
by handbook bootstrap. For new projects, mark step 0 not applicable and follow
steps 1–12. Do not implement the application during this setup step.

Verify GitHub repository, branch, actual access, and mode: branch/PR connector
or web-app sync. Record automatic write behavior. A prompt cannot disable main
sync. Missing authority or conflict with project rules blocks dependent edits.
Do not independently connect accounts, export repositories, or activate sync.

Create/update a durable Manus integration record under the existing documentation
root: owner, entry level, source revision, actual paths, mode, authority, bootstrap
status, plan, checkpoints, verification, and removal. Copy required ongoing
operating rules there and explicitly identify unknowns. Adapt the project instruction
template and record how it is provided in Manus or at the start of every task.
Do not assume automatic AGENTS.md loading or invent Manus configuration paths.
Installed rules must remain usable without addons/ files.

Add a short conditional pointer from canonical shared instructions to the actual
record. Do not duplicate role/workflow guidance. Check local links, repeatable
setup without duplicates, and source availability. Before code changes, verify
that Manus identifies repository, branch, read instructions, role, and blockers.
Keep unavailable live checks pending.

Do not configure an external Manus API, API keys, services, automation, or ticket
synchronization. Report changed files, existing authority, and remaining steps.
Do not commit, push, merge, or release without authorization covering those actions.
```
