# Release Notes for v1.0.2

## Summary

This patch clarifies existing task documentation and verification evidence.
Required paths, status values, template sections, bootstrap order, and approval
gates remain unchanged. The task overview heading and title column use English
without changing their purpose or structure.

## Changes

- Fixed: the Project Manager task example uses the same `Not Started` and
  `In Progress` capitalization as the task template.
- Clarified: how the task overview, individual task details, and file status
  relate, and how to keep them consistent.
- Clarified: executed checks need actual results and known limitations;
  planned commands alone are not evidence of successful verification.
- Changed: task overview labels consistently use `Task Order` and `Title`.
- Breaking changes: none. Existing task files do not need to be migrated or
  have their headings renamed.

## Updating Existing Projects

Affected files:

- `.github/agents/README.md`
- `.github/agents/project-manager.agent.md`
- `docs/tasks/template.md`
- `docs/tasks/README.md`
- `docs/quality/test-strategy.md`

Adopt these clarifications selectively. Preserve project-specific status
conventions, completed documents, and existing evidence. No required migration
or additional tool installation is introduced. After updating, check that task
order tables and detail sections agree and that verification results state
what was actually checked.

## Verification

- Reviewed the complete patch against `v1.0.1`.
- Checked task overview labels and status capitalization across role guidance,
  the task guide, and the template.
- Walked through new-project bootstrap and existing-project adoption as a
  documentation review; the existing bootstrap and open-question gates remain
  unchanged.
- Checked the diff for formatting errors and unintended changes.
- No client, device, or deployment tests were run; this is a documentation patch.

## Scope

These release notes apply only to maintaining the upstream repository. Context
optimization, optional diagnostic changes, new task ID conventions or fields,
archival rules, structure validators, and additional tool adapters are not part
of this patch. The agreed v2.0.0 scope remains separate.
