# Contracts Integration Prompt

Copy this prompt into an agent with access to the target Delivery System project.

```text
Set up the optional Contracts add-on for this Delivery System project.

Read the applicable project instructions and addons/contracts/README.md. Identify
the project root and the existing documentation root. Inspect the working tree so
you can preserve existing changes. Verify that the shared instructions contain the
Optional Process Add-ons section; if it is missing, report that the routing update
is required and stop.

Check for existing contract documentation, API specifications, or interface
conventions. Never overwrite an existing different file; report it and ask how to
merge. Show me the open decisions in addons/contracts/record.md (contract types in
use, who approves application-wide breaking changes, owner). Ask one focused
question at a time with a recommended answer and record explicit deferrals.

After my confirmation:
1. Write the completed record to <docs-root>/project/integrations/contracts.md.
2. Copy the templates to <docs-root>/contracts/README.md and
   <docs-root>/contracts/template.md.
3. Add a Contracts table (Contract, Type, Role, Status) to the spec template, a
   Required Contracts checklist to each task in the task template, and the two
   contract items from the README to the Definition of Done.
4. If the SCRUM record is active, add contract readiness to DoR Spec and DoR Task.
5. Adjust docs paths in copied files if the documentation root is not docs/.

Activated files must not reference addons/. Read back every written file, compare
the working tree with its initial state, and report paths, decisions, deferrals,
and checks actually run. Activation authorizes no contract creation for existing
code, commits, or pushes.
```
