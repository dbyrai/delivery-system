# Kiro Add-on: Review and Verification

## Scope and Decision

Prepared on 2026-11-17 for Dirk's review on `codex/feat/kiro-addon`, based on
`origin/main` at `582f1a8`. The user requested adapting PR #1 as an optional add-on.
Primary owner: Technical Lead. This is an upstream maintenance change, so no
adopter project templates under `docs/` are populated.

Source: [schroeder's PR #1](https://github.com/dbyrai/delivery-system/pull/1),
commit `bb9b63bfeb41bc588bfc9112966583cc49ae5be8`. Adapted manually instead of
merging the original branch: its shared-role index and instruction layout
predate the current canonical cross-tool workflow. The original PR remains open.

The steering and spec-workflow idea is packaged under `addons/kiro/`. No active
root `.kiro/` configuration is installed in this template repository. The package
contains a steering template, setup/deactivation prompts, and a spec-mapping
contract. Shared workflow rules and roles stay authoritative. Existing projects
can adopt selectively without changing their documentation roots or assigned IDs.

Alternatives considered: merging the original duplicated instruction body would
create a second rule source; installing root steering by default would make the
integration active for every adopter. Both conflict with the requested optional
package. Native spec working views require explicit reconciliation into canonical
delivery documents; no automatic synchronization is introduced.

## Review Focus

- Check that the adapted contribution preserves useful Kiro support while
  routing to current shared rules.
- Review setup, existing-file reconciliation, spec/task mapping, and removal.
- Verify new-project bootstrap and existing-project adoption still follow their
  existing gates. Check installed configuration survives removal of `addons/`.
- Confirm no hooks, MCP configuration, custom agents, or external writes are
  implicitly activated. Custom-agent steering loading is a separate live check.

## Verification

Official references checked on 2026-11-17:
[steering](https://kiro.dev/docs/steering/) and
[specs](https://kiro.dev/docs/specs/). The steering guide documents workspace
paths, `inclusion: always`, and explicit resources for custom agents. Task
dependencies govern execution rather than requiring universal sequential work.

Static verification passed: 8 Markdown files, 42 local link targets, balanced
code fences, steering front matter and canonical paths, and no active root
`.kiro/` configuration. A temporary-project copy verified template routes resolve
without `addons/`. `git diff --check` passed; scoped diffs were reviewed. These
checks do not execute the setup/deactivation prompts or prove repeatability.
New-project walkthrough: select package, retain bootstrap gates, install steering,
record authority/mapping, and verify in Kiro before claiming activation.
Existing-project walkthrough: reconcile existing steering/IDs/specs, add scoped
routing, preserve completed documentation, and reuse on repeated setup.
Removal walkthrough: reconcile native edits, retain evidence, remove owned
steering/routing, preserve shared files, and verify a fresh conversation.

Live Kiro execution, loading, repeated setup, blocker behavior, task acceptance,
and deactivation have **not been tested**. Dirk should run the live checklist in
the add-on README on a disposable project and record Kiro surface/version and
results before treating the add-on as live-verified. Static checks cannot prove
model adherence. No commit, push, merge, release, or review request is included
without the user's authorization.
