# Evidence Specification

This folder defines the canonical Evidence Object emitted by the CVS witness layer.

The Evidence Object is immutable, deterministic, hash-stable, and language-agnostic.

It is not a log entry.
It is not telemetry.
It is not interpretation.

It is a cryptographic evidence object formed beside an execution-boundary decision.

## Files

- `EVIDENCE_OBJECT_SCHEMA.md` — canonical field model
- `CANONICALIZATION.md` — deterministic ordering, serialization, and hashing rules
