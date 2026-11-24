# Kiro Workflow Add-on

This optional package connects Kiro to the shared Delivery System without making
Kiro part of the core. It installs local steering only after explicit activation.
The template repository intentionally contains no root `.kiro/` directory.

No MCP connection, hook, service, or custom agent is installed. The canonical
workflow remains `.github/copilot-instructions.md`, and canonical roles and skills
remain under `.github/`. Removing this package does not change the core workflow.

## Contents

| Source | Activated as | Purpose |
| --- | --- | --- |
| [templates/delivery-system.md](templates/delivery-system.md) | `.kiro/steering/delivery-system.md` | Route Kiro to the canonical workflow |
| [record.md](record.md) | `<docs-root>/project/integrations/kiro.md` | Durable ownership, mapping, verification, and removal |
| [integration-prompt.md](integration-prompt.md) | Run manually | Reconcile and activate the add-on |
| [deactivation-prompt.md](deactivation-prompt.md) | Run manually | Remove owned steering safely |

## Activation

Use the [integration prompt](integration-prompt.md). It must preserve existing
steering, create a self-contained project record, and add one conditional pointer
to that record for Kiro-related work. Installed files and the record must work
after `addons/kiro/` is removed.

The steering template uses `inclusion: always`, so activation is a deliberate
project decision. Never install it merely because Kiro files are present in this
package. Custom Kiro agents may require separate steering resources; verify the
actual Kiro surface rather than assuming they inherit workspace steering.

## Native Specs

Kiro-native specs are optional working views. They never replace project source
documents or relax bootstrap and open-question gates.

| Kiro artifact | Authoritative source |
| --- | --- |
| `.kiro/specs/<feature>/requirements.md` | Existing project requirement or specification |
| `.kiro/specs/<feature>/design.md` | Approved design, architecture, and decisions |
| `.kiro/specs/<feature>/tasks.md` | Existing task files with stable IDs and evidence |

Record reciprocal paths in the durable Kiro record. Reconcile proposed changes
into authoritative documents before implementation. A generated checkbox is not
acceptance evidence.

## Verification

- Confirm no root `.kiro/` files existed before explicit activation.
- Check installed paths, front matter, links, and absence of `addons/` imports.
- In a fresh Kiro conversation, verify the steering and canonical instructions
  are actually loaded and the relevant role is selected.
- Exercise a mapped spec with a blocking question; dependent work must stop.
- Repeat activation and confirm no duplicate steering, records, or pointers.
- Run deactivation and confirm unrelated Kiro configuration is preserved.

Record static and live checks separately. Until live loading is observed, report
the add-on as prepared or Preview, not operationally verified.

## Deactivation

Use the [deactivation prompt](deactivation-prompt.md). Reconcile pending native
spec changes before removing steering. Preserve specs and evidence unless their
deletion is explicitly authorized.
