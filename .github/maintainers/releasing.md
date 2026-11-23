# Maintaining and Releasing the Delivery System

## Scope

This document applies only to maintaining and publishing the original dbyrai Delivery System repository. It does not define requirements for projects created from or adopting this template. Those projects define their own delivery and release processes.

Keep upstream maintenance instructions here. Keep `delivery-system.md`, shared agent instructions, and the project templates under `docs/` generic. No CI/CD automation is introduced by this workflow.

## Branch Names

Use `codex/<type>/<short-description>` for changes prepared by Codex. Use lowercase English words separated by hyphens in the description. For human contributors, `<type>/<short-description>` is sufficient.

| Type | Purpose | Example |
| --- | --- | --- |
| `docs` | Documentation and maintainer guidance | `codex/docs/maintainer-release-workflow` |
| `feat` | New templates, roles, or delivery capabilities | `codex/feat/upgrade-guide` |
| `fix` | Corrections to existing behavior or instructions | `codex/fix/bootstrap-step-order` |
| `chore` | Repository maintenance | `codex/chore/repository-metadata` |

Describe the change in the branch name. Assign the release version from the complete reviewed scope; a branch does not need a version number.

## Change Workflow

1. Describe the problem, scope, and effect on existing users. Use an issue for substantial changes; a small correction can be described directly in its pull request.
2. Start a focused branch from the current `main`. Check the working tree first; preserve unrelated changes and keep them out of the commit and pull request.
3. Make the scoped change. Follow the applicable repository instructions and open-question gates for changes to the Delivery System.
4. Verify changed links, paths, examples, and consistency between affected instructions. For changes to the delivery process, walk through both a new-project bootstrap and adoption by an existing project.
5. Prepare a pull request targeting `main`. Describe the problem, resulting behavior, verification, compatibility, and any actions existing users must take.
6. Review and merge the approved change. Obtain explicit authorization before an agent commits or pushes; authorization already given for the current task remains valid.

## Version Policy

Use `vMAJOR.MINOR.PATCH` tags, following [Semantic Versioning](https://semver.org/) principles. When external validation is required before a stable publication, use an incrementing `vMAJOR.MINOR.PATCH-rc.N` tag and mark the GitHub release as a pre-release. Publish the stable version only after the release-candidate findings are resolved or explicitly accepted. For this template, the compatibility surface consists of documented bootstrap behavior, required gates, file paths, template structure, and shared agent instructions.

| Increment | When to use it | Example |
| --- | --- | --- |
| Patch | Compatible corrections, clarifications, or maintenance documentation with no change to the adopter workflow | `v1.0.0` to `v1.0.1` |
| Minor | New compatible capabilities, such as an optional template or role | `v1.0.0` to `v1.1.0` |
| Major | Changes requiring existing users to adapt, such as renamed required paths or new mandatory gates | `v1.0.0` to `v2.0.0` |

Judge compatibility by behavior, even when only Markdown changes. Adding this maintainer guide and its README link alone is a patch-level change. Determine the final version from all changes included in the release.

## Release Checklist

1. Confirm the complete release scope has been reviewed, verified, and merged into `main`.
2. Confirm the approved source commit is present in the upstream GitHub repository. Compare local and remote state before choosing the release commit; do not release uncommitted working-tree changes.
3. Select the version and prepare release notes using the outline below. Review the changes since the previous release tag rather than only the latest pull request.
4. Confirm who will create the tag, push it, and publish the GitHub release. An agent requires explicit authorization for these actions. Request only authorization not already provided in the current task.
5. Create an annotated tag on the exact approved commit. For a release candidate,
   use the approved `vX.Y.Z-rc.N` version and mark the corresponding GitHub release
   as a pre-release. Replace both placeholders below before running the command:

   ```sh
   git tag -a vX.Y.Z <approved-commit-sha> -m "Delivery System vX.Y.Z"
   ```

6. Inspect the tag and push only that release tag after authorization:

   ```sh
   git show --no-patch vX.Y.Z
   git push origin refs/tags/vX.Y.Z
   ```

7. On GitHub, open **Releases**, create a release draft, select the existing tag, and add the reviewed release notes. Verify the tag points to the approved commit, then publish after authorization. See [GitHub's release instructions](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository).
8. Verify the published tag, notes, and source download. If an existing CI/CD pipeline applies, use it and verify that it runs against the same approved commit.

A local tag is not a published GitHub release. Do not move or overwrite a published version tag; publish corrections under a new version.

## Release Notes Outline

Use GitHub release notes as the published change record. Include links to relevant pull requests and compare tags when a previous release exists.

```markdown
## Summary

[Version purpose and user-visible outcome.]

## Changes

- Added: [...]
- Changed: [...]
- Fixed: [...]
- Breaking changes: [Details or none.]

## Updating Existing Projects

- Affected files: [...]
- Required actions: [Exact steps or none.]
- Optional changes: [...]
- Verification after updating: [...]
```

For the initial `v1.0.0`, describe the included baseline and state that there is no previous numbered release. For later releases, explain which changes existing projects should adopt. Users should record the adopted Delivery System version in their project documentation and merge changes selectively, preserving their completed project documents and custom instructions.

## Removing Upstream Maintainer Documentation

Projects adopting the template can remove this directory using the command in the [root README](../../README.md#maintaining-this-repository), then remove that README section. Removing this directory does not remove the shared agent instructions or project templates.
