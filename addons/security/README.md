# Security Add-on

Use this optional guide to choose a software review, an infrastructure review, or
both for a Delivery System project. Start with the project's own security rules
and use the catalog to select upstream methods for the files in scope.

## Skill catalog

| Skill | Choose it when | Source |
| --- | --- | --- |
| `security-review` | Choose this for a pull or merge request that changes application code, authentication, authorization, or sensitive data handling. | [Sentry](https://github.com/getsentry/skills/blob/main/skills/security-review/SKILL.md) |
| `infra-security` | Choose this for a local review of Terraform, CloudFormation, Kubernetes, Helm, Docker, or Compose configuration. | [Superagent](https://github.com/superagent-ai/skills/blob/main/skills/infra-security/SKILL.md) |
| `code-security` | Choose this when designing or writing a change and you want secure coding or configuration guidance for your stack. | [Semgrep, beta](https://github.com/semgrep/skills/tree/main/skills/code-security) |
| `semgrep` | Choose this when you want a rule-based source scan or need to check a recurring code pattern across the repository. | [Semgrep](https://github.com/semgrep/skills/blob/main/skills/semgrep/SKILL.md) |
| `codeql` | Choose this for deeper data-flow analysis across functions when your project already has a supported CodeQL setup. | [Trail of Bits](https://github.com/trailofbits/skills/tree/main/plugins/static-analysis/skills/codeql) |
| `sarif-parsing` | Choose this when you already have SARIF reports and need to group or deduplicate findings. | [Trail of Bits](https://github.com/trailofbits/skills/tree/main/plugins/static-analysis/skills/sarif-parsing) |

## Recommended starting point

| Project or change | Start with | Add to existing CI if applicable |
| --- | --- | --- |
| Application code | `security-review` for the change | Semgrep for static source checks |
| Infrastructure or container configuration | `infra-security` for the changed files | Trivy for IaC misconfigurations and container image vulnerabilities |
| Application and infrastructure in one repository | Both review skills, scoped to their respective files | Semgrep and Trivy on the relevant stages or paths |

[Trivy](https://github.com/aquasecurity/trivy) is a standalone scanner that can
also check supported dependencies for known vulnerabilities and scan for secrets.
Reuse existing scanners that cover your project. Use the project's security
policy to decide which findings block a merge or release. This guide provides
selection and review instructions. Skill installation and CI setup are separate
steps, with availability depending on the client and project.

## Ask your agent for a recommendation

Copy this prompt into an agent with access to the project and this guide.

```text
Read the project instructions, security policy, and Security Add-on guide.
Use the requested change or project scope to identify relevant application code,
infrastructure files, and existing scanner configuration.

Show the skill catalog in my language, with one sentence per skill explaining
when to choose it. Recommend the smallest set for this scope and explain why.
Mention which existing scanners already cover the scope and suggest any useful
CI checks separately. If scope is unclear, give the guide's recommendation for
application-only, infrastructure-only, and mixed projects. Stop at the selection
unless I also ask for a review or setup.
```

For a review, report each confirmed finding with its severity, file and line,
impact, and suggested fix. List findings that still need verification and any
gaps in coverage. Keep secrets out of reports and use the project's existing
review and delivery workflow.
