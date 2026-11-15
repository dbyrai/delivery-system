# GitHub Projects Integration Prompt

Copy the prompt below into your AI tool from the target project. Supply known
repository and Project URLs in your message; leave unknown decisions for dialogue.

```text
Adapt the optional GitHub Projects add-on to this project.

Read the applicable repository entry instructions and shared workflow first.
Then read addons/README.md, addons/github-projects/README.md, and
addons/github-projects/instructions.md. Load only task-relevant project sources.

Inspect the current working tree, existing documentation root, task IDs, source
of truth, issue conventions, and existing integrations without changing them.
Identify the exact GitHub host, repository, Project owner and URL. Inspect the
available tool's actual issue and Project capabilities separately, using only
authorized read-only access. Never request or print tokens. Do not infer Project
write support from repository access.

Resolve one focused decision at a time where necessary: authoritative source per
field, issue/Project/PR scope, task ID mapping, status and account mapping,
synchronization direction and trigger, owner, permissions, conflict handling,
and which external writes are authorized. Reuse decisions and permissions already
given in this session. Record explicit deferrals; do not perform dependent work.

Prepare the project-specific integration record in the existing documentation
root and a concrete preview of affected local and external content. Preserve
existing task IDs, issue text outside managed sections, workflows, and project
gates. Search for existing mapped issues and Project items before creating any.
Apply only resolved operations within current authorization; request only missing
authorization after the concrete preview is ready. Do not merge, release, or
install recurring synchronization as part of this setup.

Verify changed repository issues and Project fields by reading them back. Report
partial failures and avoid duplicate creates on retries. If no supported access
exists, supply manual instructions and label live setup unverified.

Make the durable project record self-contained: targets and IDs, owner, capability
checks, mappings and source decisions, credential configuration reference without
secrets, allowed actions, triggers, conflict/retry rules, verification, and shutdown
steps. Route relevant future project work to that record, not to addons/ files.
Explain that deleting the add-on files does not disable the integration, and how
to disable active connections separately while preserving remote work and shared
access. Summarize changed files, verified behavior, limits, and outstanding work.
Do not commit or push unless separately authorized.
```
