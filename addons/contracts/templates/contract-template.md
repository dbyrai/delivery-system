# Contract: {Name}

**Type**: {api | ui-component | auth-context | event | database | config | versioning}
**Scope**: {app-wide | module-internal}
**Provider**: {Module or Package that owns this contract}
**Consumer(s)**: {Module(s) or Package(s) that depend on this contract}
**Version**: {semver for app-wide, "N/A — Git history" for module-internal}
**Status**: {draft | review | final | deprecated}
**Last Updated**: {YYYY-MM-DD}

## Definition

{What this contract guarantees. What the provider commits to delivering. What consumers can rely on.}

## Schema / Interface

{Reference to the code artifact (interface, OpenAPI path, event payload schema) or an inline definition.}

```
{Inline schema example if applicable}
```

## Breaking Change Rules

{What constitutes a breaking change for this contract. What the provider must do before making a breaking change. Migration obligations for consumers.}

**For app-wide contracts:**
- Major version bump required for breaking changes
- Migration guide must be provided
- All consumer teams notified
- PO approval required

**For module-internal contracts:**
- Developer decides autonomously
- Update all consumers within the module
- No formal versioning required

## Examples

{Optional: example payloads, usage patterns, or integration code.}
