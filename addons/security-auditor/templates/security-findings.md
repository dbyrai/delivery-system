# Security Findings Log

Central log maintained by the Security Auditor role. Never delete entries; record the resolution in the status.

## Audit Format

```markdown
## Security Audit: {YYYY-MM-DD}

**Scope**: {task, milestone, or files reviewed}
**Files Reviewed**: {list or reference}

| # | Category | Severity | File | Line(s) | Description | Status | Handed To |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | {Vulnerability / Code Quality / Performance} | {Critical / High / Medium / Low} | `{path}` | {lines} | {what is wrong and why it matters} | {Open / Done YYYY-MM-DD / Superseded by #NN / Obsolete: reason} | {role} |

**Summary**: {n} findings; Critical {n}, High {n}, Medium {n}, Low {n}; handed off {n}
```

- Number findings continuously across audits so later audits can reference them.
- Mark `Done` only after verifying the fix; include the date and reference.
- Never record secret values.

---

## Findings

_No findings recorded yet._
