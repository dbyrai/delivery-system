# Active Workspace Layout

**Status**: Active
**Application repository**: `{relative-application-directory}`
**Project documentation root**: `{relative-application-directory}/{project-docs-directory}`
**Private documentation root**: `{private-docs-directory}`
**Application visibility**: {public | private}
**Durable decision record**: `{private-docs-directory}/project/integrations/workspace-layout.md`

Load this file before resolving project-document paths. The Delivery System and
application are separate Git repositories. Start AI tools from the private
workspace root so the canonical shared instructions are available.

## Routing Rules

- Treat workspace `docs/` as unfilled templates and baselines. Write product
  documents only under the configured project documentation root.
- Write confidential policies, security findings, unreleased vulnerabilities,
  internal repository reviews, and reports containing personal data only under
  the configured private documentation root. Never link private documents from
  the application repository.
- Run application and project-document Git commands with
  `git -C {relative-application-directory}`. Use workspace Git only for Delivery
  System files and private records.
- The application directory must be ignored by workspace Git. Do not treat an
  embedded repository as workspace content or stage it from the workspace root.
- Resolve active add-on records under the project or private documentation root
  named by their own routing pointer. Do not assume one root for every record.
- Preserve both repositories' authorization, review, commit, push, merge, and
  release rules. Permission in one repository grants no permission in the other.

If any configured path is missing, ambiguous, absolute, escapes the workspace,
or resolves through an unexpected symbolic link, stop dependent writes and ask
the owner to correct the durable record.
