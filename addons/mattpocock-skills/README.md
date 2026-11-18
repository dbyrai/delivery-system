# Matt Pocock Skills Add-on

Use selected methods from [mattpocock/skills](https://github.com/mattpocock/skills)
within a Delivery System project. The pinned catalog covers the skills listed in
the upstream README. Experimental files outside that catalog are excluded.

## Start in your agent

Copy the [integration prompt](integration-prompt.md) into an agent with access to
the target repository. It shows the catalog with a short description per skill
and asks for a selection. You can name the skills in your initial prompt.

The initial set contains `diagnosing-bugs`, `tdd`, `grill-me`, and
`to-questionnaire`. The helper adds the adapted `grilling` reference for
`grill-me` and `codebase-design` for `tdd`. Other entries remain discoverable
in the catalog, with their availability shown beside each name.

## Run directly

From the target project root, with Python 3.9 or newer:

```sh
python3 addons/mattpocock-skills/manage.py list
python3 addons/mattpocock-skills/manage.py activate diagnosing-bugs tdd grill-me to-questionnaire
```

Pass `--docs-root knowledge` to `activate` if `knowledge/` is your existing
documentation root. Listing works offline. On first activation the helper
fetches the selected sources from `raw.githubusercontent.com` and verifies
their Git blob IDs at the revision recorded in [the catalog](catalog.json).
If direct downloads are unavailable, the agent can fetch the exact file bytes
through a read-only GitHub connector into a temporary directory outside the
project and pass it as `--source-dir`. The same verification applies.

Activation creates `docs/project/integrations/mattpocock-skills.md` or the same
relative path under the project's existing documentation root. It creates the
integration directory as needed after verifying all sources. The helper checks
that the shared Delivery System instructions include the method routing and
refuses to replace an existing different entry. Repeating the same selection
is idempotent.

## Use and remove

Give the agent a concrete assignment, for example:

> Investigate why the import fails intermittently and establish a reproducible
> check before proposing a fix. Delivery diagnostics: on.

The [shared instructions](../../.github/copilot-instructions.md#optional-matt-pocock-methods)
select `diagnosing-bugs` for this assignment after normal role selection and
gate checks. The primary role uses the method. Diagnostics show the selected
method and the file the agent loaded. An explicit request can select an active
method or skip optional methods for the assignment. Unrelated tasks continue
through the regular workflow. The setup works without the add-on directory after
activation.

For projects that used the previous manual-only setup, activate the same
selection again with the updated shared instructions and helper. The previous
`<docs-root>/mattpocock-skills.md` stays available for review or archiving.
Automatic routing uses the entry under `project/integrations/`.

Use the [deactivation prompt](deactivation-prompt.md) to remove the entry.
To change the selection or adopt a newer reviewed version, preserve any local
edits and remove or archive the old entry before activating the new selection.
The bundled adaptations derive from MIT-licensed sources. [Upstream license](LICENSE.upstream)
