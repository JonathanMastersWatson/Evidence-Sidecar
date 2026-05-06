# Witness Runtime

This folder defines the local CVS witness runtime interface.

The witness runtime receives boundary events, constructs canonical Evidence Objects, hashes them deterministically, and emits anchor-ready proof material.

The witness runtime is asynchronous and non-authoritative.

It must never block, modify, reinterpret, or influence execution.

## Files

- `WITNESS_INTERFACE.md` — runtime input/output contract
- `FAILURE_AND_GAPS.md` — fail-open witness behavior and gap semantics
