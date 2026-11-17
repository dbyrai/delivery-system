# Kiro Workflow Add-on

This optional package adapts Kiro steering and spec-driven work to the shared
Delivery System. It provides a deployable steering template and setup/removal
prompts. It requires no MCP connection, external ticket system, hooks, or service.
Keeping these files under `addons/` does not activate them. The existing
`AGENTS.md` may already supply shared instructions in Kiro independently of this
add-on.

## Origin and Scope

Adapted from [schroeder's PR #1](https://github.com/dbyrai/delivery-system/pull/1),
commit `bb9b63bfeb41bc588bfc9112966583cc49ae5be8`. The contribution's steering,
shared roles, and requirements/design/tasks approach are retained as an optional
package. General workflow rules remain in
[the shared instructions](../../.github/copilot-instructions.md); role profiles
remain in [the role index](../../.github/agents/README.md).

## Setup

1. Open the target repository in Kiro. Inspect its existing instructions,
   `.kiro/steering/` files, and specs before changing them. Preserve local rules.
2. Run the [integration prompt](integration-prompt.md). For a manual setup, copy
   [the template](templates/delivery-system.md) to
   `.kiro/steering/delivery-system.md` in the target repository, after checking
   that the destination does not already exist. Reconcile an existing file;
   do not overwrite it. Adjust paths if shared instructions are elsewhere.
3. Create or update a self-contained integration record in the established
   documentation root, for example `docs/project/integrations/kiro.md`. Record
   the Kiro surface/version, owner, installed steering path, source commit,
   spec mapping, authority, verification, and removal plan. Add a short pointer
   to it in the canonical shared instructions for work involving Kiro specs.
4. In a new Kiro conversation verify that the steering file is loaded and that
   Kiro can read the shared instructions and select the relevant role. Resolve
   conflicts with generated product/tech/structure steering rather than copying
   general rules into them.

The template uses `inclusion: always`. Custom Kiro agents require explicit
steering resources; reconcile the selected agent's existing configuration and
verify loading there separately. See the official
[steering documentation](https://kiro.dev/docs/steering/) for inclusion modes,
file references, custom-agent behavior, and surface differences. A shared role
profile does not create a runnable Kiro custom agent.

## Specs and Delivery Mapping

Use Kiro-native spec files only when choosing its spec workflow. They do not
replace completed project documentation or change the bootstrap sequence.
Before generation, read the established specification and task conventions,
linked blockers, and requirements. For a new project complete or explicitly
defer the existing bootstrap; for an adopted project retain completed work.

| Kiro working artifact | Authoritative Delivery System source |
| --- | --- |
| `.kiro/specs/<feature>/requirements.md` | Existing requirement/spec in the project's documentation root |
| `.kiro/specs/<feature>/design.md` | Relevant architecture, decisions, and approved design/spec |
| `.kiro/specs/<feature>/tasks.md` | Existing delivery task files, stable IDs, owners, dependencies, and acceptance evidence |

Record exact reciprocal paths and IDs in the project record and the affected
documents. Prefer links to copying content. When Kiro needs editable native
content, label it as a working view and reconcile proposed changes into the
authoritative files for review before execution. Stop dependent work on a
conflict; a generated spec cannot override security or architecture decisions.
Follow the shared question and approval gates. Execute according to recorded
dependencies; this add-on imposes no global sequential execution rule.

Kiro task numbering supplements existing delivery IDs. Keep task ordering,
owner, status, blockers, and evidence in the canonical delivery task format.
Mark a Kiro task complete only after its mapped delivery task meets acceptance
criteria and records verification. A checkbox alone is not acceptance evidence.
Do not add another authority or synchronization service implicitly.

## Verification

- Check installed paths, front matter, and links; ensure active instructions
  and records do not require removable `addons/` files.
- In Kiro, ask it to name the canonical shared instruction file and relevant
  role, then classify a small read-only task. Confirm it reads only relevant
  sources and respects diagnostics being off by default.
- Walk through a sample spec with an unresolved question: dependent task
  generation/implementation must remain blocked until resolution or explicit
  deferral is recorded. Use a disposable fixture, preserving actual project work.
- Verify a mapped task carries the existing ID and source references; check
  that its completion requires evidence in the authoritative delivery task.
- Repeat setup and confirm it updates/reuses the existing steering and record
  without duplicates. Report static checks and live Kiro checks separately.

Record actual outcomes and unrun checks. Files being present is a prepared setup;
claim verified activation only after observing instruction loading in Kiro.

## Removal

Use the [deactivation prompt](deactivation-prompt.md). Reconcile pending native
spec changes into the authoritative documents before removing required access
or steering. Preserve Kiro specs and evidence unless deletion is authorized.
Remove only the add-on-owned steering/routing, retaining unrelated Kiro settings
and the core shared workflow. A new conversation must confirm the resulting
state; `AGENTS.md` can continue supplying the shared workflow after deactivation.

The installed steering and durable record must remain usable after deleting
`addons/kiro/` or all optional packages. Delete the optional files and clean their
index links separately; this does not deactivate installed steering.
