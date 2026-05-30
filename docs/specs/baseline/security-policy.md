# Baseline Security And Policy Requirements

These requirements apply across the project unless a spec states otherwise.

## Secrets And Credentials

- SEC-BASE-001: Do not commit real secrets, tokens, private keys, passwords, or production credentials.
- SEC-BASE-002: Use example values in documentation and `.env.example` files.

## Data Handling

- SEC-BASE-003: Document any sensitive, personal, or regulated data handled by the project.
- SEC-BASE-004: Avoid storing production data locally unless there is an approved reason and handling procedure.

## Access Control

- SEC-BASE-005: Permission and role assumptions must be documented for protected functionality.

## External Services

- SEC-BASE-006: External integrations must document required credentials, data exchanged, and failure behavior.

## Open Questions

- TBD
