# Kiro Setup Prompt

Copy this prompt into your project AI tool with repository access.

```text
Set up the optional Kiro workflow add-on for this project.

Read applicable repository instructions, addons/kiro/README.md, and its steering
template. Inspect the working tree, existing Kiro steering/specs, and the relevant
shared workflow and role guidance. Preserve completed project documentation,
local customizations, IDs, documentation roots, and unrelated changes. Report
missing sources; do not claim to have read them. This is a local workflow
integration, so do not apply the MCP adapter connection or ticket-creation gates.

Prepare and apply a focused local diff installing or reconciling the template at
.kiro/steering/delivery-system.md. Keep inclusion: always and route to the actual
canonical shared instruction file. Never duplicate its workflow or role rules.
Do not overwrite existing steering or create competing instruction files. Inspect
the chosen Kiro surface/version and custom-agent settings. Configure steering
resources only for a selected custom agent, preserving its existing resources.
Do not install Kiro, MCP servers, hooks, services, or external integrations.

Create/update a self-contained record under the established documentation root:
owner, Kiro surface/version, steering path, source version/commit, current spec
mapping, authoritative files, acceptance workflow, checks, and deactivation plan.
Follow applicable documentation language rules. Add a short conditional pointer
from the canonical shared instructions for Kiro spec work. Resolve actual paths;
ongoing rules must not require addons/ files after setup.

If native specs are requested, map requirements/design/tasks to authoritative
project specs, decisions, and delivery task files with reciprocal paths and stable
IDs. Do not generate unsolicited feature specs. Reconcile proposed native edits
into authoritative documents before execution; retain task owners, dependencies,
statuses, blockers, and evidence. Apply existing bootstrap/question gates without
rerunning completed bootstrap. Resolve blocking choices before dependent work.

Check paths, links, front matter, and setup repeatability. In an actual Kiro
conversation verify instruction loading, relevant role selection, scoped context,
question blocking, and mapped task completion with acceptance evidence. If Kiro
is unavailable, record static verification only and leave live checks pending.
Summarize changed files and remaining owner actions. Do not commit, push, publish,
or send review messages without separate authorization.
```
