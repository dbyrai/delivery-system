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

Activation creates one `mattpocock-skills.md` in that documentation root. It
writes the bundled, adapted methods only after all source checks pass. The
helper refuses to replace an existing different entry, even if another
activation creates it concurrently. Repeating the same selection is idempotent.

## Use and remove

Give the agent a concrete assignment and name the method, for example:

> Apply the `diagnosing-bugs` method from `docs/mattpocock-skills.md` to this
> issue. Read and follow the applicable Delivery System rules first.

The entry is loaded by explicit request. Native slash commands, plugins, remote
scripts, and automatic updates are outside this add-on's activation path. The
entry does not change canonical instructions, agent roles, tracker settings, or
approval gates. Its methods apply within the authorized task and inherit project
rules for bootstrap, blockers, source authority, and verification. It works
without the add-on directory after activation. Agent compliance during use is
separate from the helper's local write boundary.

Use the [deactivation prompt](deactivation-prompt.md) to remove the entry.
To change the selection or adopt a newer reviewed version, preserve any local
edits and remove or archive the old entry before activating the new selection.
The bundled adaptations derive from MIT-licensed sources. [Upstream license](LICENSE.upstream)
