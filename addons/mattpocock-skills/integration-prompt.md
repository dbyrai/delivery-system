# Matt Pocock Skills Integration Prompt

Copy this prompt into an agent with access to the target Delivery System project.
Optional selection example: `diagnosing-bugs, tdd, grill-me`.

```text
Set up the optional Matt Pocock skills add-on for this Delivery System project.

Read the applicable project instructions and addons/mattpocock-skills/README.md.
Identify the project root and the existing documentation root from the repository.
Inspect the working tree so you can preserve existing changes.

From the project root run:
python3 addons/mattpocock-skills/manage.py list

Present the full printed catalog in my language, with each skill's name, short
explanation, availability and any referenced methods. Explain that activation
adds one project-local Markdown entry. If I did not name skills, ask once which
available methods I want. Wait for selection before writing. If I only ask to
see the catalog, finish after presenting it. If a selected name is unavailable,
explain its status and ask me to resolve the selection before activation.

Run the add-on helper with the confirmed names as individual arguments:
python3 addons/mattpocock-skills/manage.py activate NAME [NAME ...] --docs-root PATH
Replace PATH with the verified existing documentation root relative to the
project. Use only names in the catalog. The helper verifies the pinned sources
and brings in the corresponding adapted methods and their references. If direct
downloads are unavailable, use a read-only GitHub connector if available.
Fetch the exact files named in catalog.json for the selected methods and their
dependencies at the catalog's full revision. Preserve their bytes and relative
paths in a temporary directory outside the project. Run the same helper with
--source-dir pointing to that directory and clean up those temporary downloads.
If the helper cannot run or verify the sources, report the blocker. Keep the
pinned revision and the existing project state. Do not invoke the upstream
setup, marketplace, installers, scripts, or another path that bypasses this check.

Read back the generated entry and verify the selected methods and references.
Check the working tree against its initial state. The entry is the only planned
change. Preserve canonical instructions, specs, tasks, roles, bootstrap and
approval gates. Activation itself authorizes no application work, tracker writes,
automation, delegation, Git writes, or release actions. If you find a conflict,
report it and stop using the conflicting step. Preserve unrelated local edits.

Report the path, revision, methods and what was actually verified. Use a method
only on explicit request with a concrete assignment. Read the applicable project
instructions before using the selected method from the local entry.
```
