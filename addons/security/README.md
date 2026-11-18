# Security Add-on

Use this optional add-on to activate a software review, an infrastructure review,
or both in a Delivery System project. Start with the project's security policy
and choose methods for the files in scope.

## Skill catalog

| Skill | Choose it when | Availability | Source |
| --- | --- | --- | --- |
| `security-review` | Choose this for a pull or merge request that changes application code, authentication, authorization, or sensitive data handling. | Activatable | [Sentry](https://github.com/getsentry/skills/blob/a582c51ee29d0f35e6ac321340796f77d43da733/skills/security-review/SKILL.md) |
| `infra-security` | Choose this for a local review of Terraform, CloudFormation, Kubernetes, Helm, Docker, or Compose configuration. | Activatable | [Superagent](https://github.com/superagent-ai/skills/blob/0da315b873ed141025fa601ed6e0ebe0c878d5af/skills/infra-security/SKILL.md) |
| `code-security` | Choose this when designing or writing a change and you want secure coding or configuration guidance for your stack. | Reference | [Semgrep, beta](https://github.com/semgrep/skills/tree/main/skills/code-security) |
| `semgrep` | Choose this when you want a rule-based source scan or need to check a recurring code pattern across the repository. | Reference | [Semgrep](https://github.com/semgrep/skills/blob/main/skills/semgrep/SKILL.md) |
| `codeql` | Choose this for deeper data-flow analysis across functions when your project already has a supported CodeQL setup. | Reference | [Trail of Bits](https://github.com/trailofbits/skills/tree/main/plugins/static-analysis/skills/codeql) |
| `sarif-parsing` | Choose this when you already have SARIF reports and need to group or deduplicate findings. | Reference | [Trail of Bits](https://github.com/trailofbits/skills/tree/main/plugins/static-analysis/skills/sarif-parsing) |

## Recommended starting point

| Project or change | Start with | Add to existing CI if applicable |
| --- | --- | --- |
| Application code | `security-review` for the change | Semgrep for static source checks |
| Infrastructure or container configuration | `infra-security` for the changed files | Trivy for IaC misconfigurations and container image vulnerabilities |
| Application and infrastructure in one repository | Both review skills, scoped to their respective files | Semgrep and Trivy on the relevant stages or paths |

[Trivy](https://github.com/aquasecurity/trivy) is a standalone scanner that can
also check supported dependencies for known vulnerabilities and scan for secrets.
Reuse existing scanners that cover your project. Use the project's security
policy to decide which findings block a merge or release. Configure any scanners
separately in the existing pipeline.

## Select and activate

From the project root, with Python 3.9 or newer and the [shared Security routing](../../.github/copilot-instructions.md#optional-security-methods):

```sh
python3 addons/security/manage.py list
python3 addons/security/manage.py activate security-review infra-security
```

Pass only the names you selected. Use `--docs-root knowledge` if `knowledge/` is
your existing documentation root. Activation verifies the SHA-256 of the Markdown
sources pinned in [catalog.json](catalog.json) and writes the project's reviewed
adaptations to `docs/project/integrations/security-skills.md`, or the equivalent
under the chosen documentation root. Activation with the same selection is
idempotent and preserves any existing different entry. If direct downloads are
unavailable, obtain the exact pinned files through a read-only GitHub connection,
save them under `<source-dir>/<owner>/<repo>/<revision>/<upstream-path>` and pass
`--source-dir <source-dir>` to apply the same verification locally.

To have an agent suggest a selection and activate it, copy this prompt into an
agent with access to the project and this guide.

```text
Read the project instructions, security policy, and Security Add-on guide.
Use the requested change or project scope to identify relevant application code,
infrastructure files, and existing scanner configuration.

Run `python3 addons/security/manage.py list`. Show the catalog in my language,
with one sentence per skill explaining when to choose it and whether it can be
activated. Recommend the smallest set for this scope and explain why. Mention
existing scanners separately. If scope is unclear, give the guide's defaults
for application-only, infrastructure-only, and mixed projects.

If I ask for activation and name the methods, activate them with the command in
the guide and the verified project documentation root. If I ask for activation
without naming methods, ask me to choose after showing the recommendation.
Read back the generated entry and report its path, selected methods and any
checks that could not run. If I only ask for a recommendation, show the catalog
and stop at the selection.
```

## Use and verify

Ask for a security review of application or infrastructure files and add
`Delivery diagnostics: on` to see the selected method and loaded entry. The
existing primary role applies it. The activation helper writes a documentation
entry.

For an independent read-only review, select the `security-reviewer` agent or
explicitly request it in your review prompt. The Delivery System ships one
[shared role profile](../../.github/agents/security-reviewer.agent.md) for GitHub
Copilot and thin project adapters for Codex and Claude Code. Assistants with
repository access can also follow the shared profile directly. A separate second
review requires client support for an independent reviewer.

For a review, report each confirmed finding with its severity, file and line,
impact, and suggested fix. List findings that still need verification and any
gaps in coverage. Keep secrets out of reports and use the project's existing
review and delivery workflow.

To deactivate or change a selection, archive the active entry outside the routing
path or remove it after reviewing any local edits. Activate the new selection
from the project root if needed. The active entry can be used after the optional
add-on files are removed.
