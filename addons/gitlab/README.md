# GitLab Add-on

Adapt the Delivery System to selected GitLab projects, issues, boards, and merge
request references. This optional add-on supplies instructions and an AI prompt;
it does not install a connector, pipeline, or synchronization service.

## Prerequisites and Use

1. Read the [shared add-on lifecycle](../README.md).
2. Identify the GitLab host and exact project or group scope.
3. Identify an authorized tool or manual access path. Confirm supported features
   for the target instance, version, permissions, and subscription; never paste
   access tokens into chat or documentation.
4. Read the [integration instructions](instructions.md), then copy the
   [integration prompt](integration-prompt.md) into your AI tool.

GitLab issues belong to projects. Issue boards offer views of issues at project
or group scope, and issue references connect delivery work with merge requests.
See [Issues](https://docs.gitlab.com/user/project/issues/),
[Issue boards](https://docs.gitlab.com/user/project/issue_board/), and
[Crosslinking issues](https://docs.gitlab.com/user/project/issues/crosslinking_issues/).

## Scope

Choose issue mapping, board or label conventions, milestones, and merge request
references as needed. Keep stable Delivery task IDs alongside GitLab identifiers.
Existing GitLab CI/CD and deployment processes remain authoritative; connecting
the task workflow does not authorize changing pipelines or releasing software.

## Removal

Delete unused add-on files and remove their links from the add-on index and other
instructions. After setup, keep durable project rules and mappings independently
of this directory. Deleting these files does not disable external connections or
remove GitLab issues, boards, merge requests, or pipelines.

For active removal, inspect the project's integration record. Stop only the
integration-specific jobs, webhooks, or tool connection within existing
permissions, remove its agent routing, and revoke dedicated access if authorized.
Keep shared credentials and the project's CI/CD process intact. Preserve remote
work and history, and record where task status and other mirrored fields will be
maintained after shutdown.
