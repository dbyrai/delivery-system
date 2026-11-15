# v2.1.0 Release Notes — Draft

Publication is pending maintainer review and authorization. These notes describe
the prepared source, not an already published release.

## Summary

The Delivery System gains optional integration add-ons for Jira, Confluence,
GitHub Projects, and GitLab. Each provides setup instructions and a copyable AI
prompt for adapting the connection to an adopting project.

## Changes

- Added: `addons/README.md` with selection, a shared setup lifecycle, durable
  project records, and separate removal of instructions versus active connections.
- Added: four add-ons, each with a README, integration instructions, setup and deactivation prompts.
- Added: deactivation prompts require a remote/local knowledge inventory and a
  user decision about migration or external retention before dependent shutdown.
- Added: a selective adoption guide for existing v2.0.0 projects.
- Changed: root README and delivery handbook include optional discovery links.
- Breaking changes: none. No mandatory bootstrap steps, role-adapter changes,
  connectors, credentials, or synchronization services are introduced.

Each add-on covers actual tool capability discovery, source authority, stable
mapping, scoped authorization, conflict/retry handling, verification, and teardown.
Required ongoing rules are transferred into the project before optional add-on
files are removed. Product references link to official documentation; actual
client and hosting capabilities must be checked during each project's setup.

## Updating Existing Projects

- Required actions: none for projects retaining their v2.0 workflow.
- Optional changes: copy `addons/README.md`, selected add-on directories, and
  `howto/upgrades/v2.0-to-v2.1.md`; remove index entries for omitted add-ons.
  Merge discovery links only where useful. Follow the
  [adoption guide](../../howto/upgrades/v2.0-to-v2.1.md).
- Preserve existing documentation roots, completed content, task IDs, integration
  rules, diagnostic defaults, and security/approval boundaries. Do not replace
  project documents with this template.
- Verification after adoption: check links and mappings, resolve target-specific
  decisions, verify actual access, and confirm durable records survive removal
  of optional instructions. External writes require their applicable authorization.

## Verification and Limits

Local Markdown links, anchors, fences, whitespace, unchanged core files, and
selective adoption/removal scenarios were checked. Independent QA reviewed the
instructions and prompts. See the [verification record](v2.1.0-verification.md).
No authenticated connector, external write, rendered remote page, or live model
compliance was tested. The release supplies guidance rather than a working
integration service; target-specific validation remains part of project setup.
