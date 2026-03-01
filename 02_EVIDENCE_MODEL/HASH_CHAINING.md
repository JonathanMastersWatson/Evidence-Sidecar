
# Hash Chaining

This document defines the required method for chaining Evidence Objects
within the Cryptographic Verification Sidecar (CVS) specification.

The canonical CVS specification is defined by:

- `CVS_ARCHITECTURE_v2.7.md`
- `CVS_IMPLEMENTATION_v2.2.md`

If conflict exists, the canonical specification governs.

This document is normative.

Hash chaining ensures that:

- evidence cannot be modified retroactively,
- omissions are detectable,
- temporal order is preserved.

---

## Purpose

Hash chaining provides structural integrity.

It allows an independent verifier to determine whether:

- any Evidence Object has been altered,
- any object has been removed,
- any sequence has been reordered.

This is achieved without storing payload data.

---

## Basic Chain Structure

Each Evidence Object MUST include a reference to its immediate predecessor.

The chain reference MUST be:

- the cryptographic hash of the prior Evidence Object, or
- a digest derived from the prior object’s canonical representation.

This creates a linear, append-only sequence.

---

## Chain Continuity

Chain continuity MUST satisfy the following:

- Each new Evidence Object MUST reference exactly one predecessor.
- The initial object in a sequence MUST be explicitly marked as a genesis event.
- Any missing reference MUST constitute a detectable gap.

Silent truncation is non-conformant.

---

## Segmentation and Batching

For high-throughput systems, evidence MAY be segmented.

Segmentation rules:

- segments MUST be clearly defined (e.g., time-based or count-based),
- segmentation boundaries MUST be recorded,
- segments MUST be chained in order.

Within a segment:

- individual events MAY be aggregated,
- a segment-level hash MAY represent the group.

This enables scalability without sacrificing integrity.

---

## Merkle Structures

Implementations MAY use Merkle trees to:

- batch multiple Evidence Objects,
- reduce settlement overhead,
- support partial verification.

When Merkle structures are used:

- the construction method MUST be documented,
- root hashes MUST be preserved,
- leaf membership MUST be independently provable.

Merkle roots MAY be anchored externally.

---

## Hash Function Requirements

Hash functions used for chaining MUST:

- be cryptographically secure,
- be collision-resistant,
- be widely standardized,
- have documented security properties.

The chosen hash function MUST be disclosed.

Proprietary or undocumented hash mechanisms are non-conformant.

---

## Canonicalization

Before hashing, Evidence Objects MUST be:

- serialized in a canonical form,
- free of ambiguous ordering,
- stable across implementations.

Canonicalization rules MUST be explicit and deterministic.

---

## Detection of Tampering

Tampering is detected when:

- a hash fails to validate,
- a chain reference is missing,
- a sequence is inconsistent.

Detection MUST NOT require trust in the operator.

---

## Gaps and Discontinuities

When evidence production is interrupted:

- the chain MUST reflect the interruption,
- gaps MUST NOT be silently filled,
- continuity MUST NOT be inferred.

Explicit discontinuity markers MAY be used.

---

## Interaction with Settlement

Hash chains MAY be periodically anchored to an external settlement layer.

Anchoring:

- does not alter the chain,
- does not affect execution,
- serves only as a public timestamped receipt.

Settlement frequency is implementation-specific.

---

## Scope Limitation

Hash chaining:

- does not prove correctness,
- does not establish intent,
- does not guarantee regulatory sufficiency.

It preserves integrity and detectability only.

---

## Summary

Hash chaining transforms individual observations into a coherent,
tamper-evident historical record.

Integrity emerges from structure, not authority.

A broken chain is visible by design.
