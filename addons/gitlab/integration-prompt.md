# GitLab Integration Prompt

Copy this prompt into your AI tool from the target project. Include known GitLab
host and project URLs in your message; resolve unknown decisions in dialogue.

```text
Adapt the optional GitLab add-on to this project.

Read applicable repository entry instructions and shared workflow first, then
addons/README.md, addons/gitlab/README.md, and addons/gitlab/instructions.md.
Load only project sources needed for this integration.

Inspect the working tree, existing documentation root, task IDs, decisions, issue
conventions, repository remotes, and CI/CD boundaries. Preserve existing content.
Resolve the exact GitLab host, target projects, and any group/board scope. Verify
the actual tool's read and write capabilities separately for selected resources,
using only authorized read-only inspection initially. Confirm instance/version
and feature availability. Never ask for, print, or store access tokens.

Resolve blocking decisions one at a time where needed: authoritative source per
field, issue/board/merge-request scope, stable task ID mapping, issue numbers versus
API IDs, status/label/account mapping, direction and trigger, ownership, conflict
handling, permissions, and authorized external writes. Reuse decisions and action
authorization already given. Record explicit deferrals and leave dependent work
inactive. Do not infer write authorization from this prompt.

Prepare a durable integration record in the existing documentation root and a
concrete preview of affected local and external fields. Locate existing mapped
issues before creating anything. Preserve other description sections, comments,
labels, and shared boards. Do not change pipelines, publish, merge, or install
webhooks or recurring jobs as part of this setup. Apply only resolved changes
within current authorization; request only missing authorization once the preview
is concrete. Check for unintended issue closing patterns before writing.

Read back changed issue data and selected board configuration. Report partial
failures and verify existing task markers before retrying uncertain creates. If
supported access is unavailable, provide manual steps and label live setup
unverified instead of claiming a connection.

Keep durable project rules independent of addons/: targets and identifiers, owner,
verified capabilities, field mappings and source decisions, credential-location
reference without secrets, action permissions, triggers, conflict/retry handling,
verification, and shutdown. Route future relevant work to that project record.
Explain separate removal of local add-on files and active integration connections;
preserve remote work, shared access, and existing CI/CD. Summarize changed files,
verified results, limitations, and remaining work. Do not commit or push unless
separately authorized.
```
