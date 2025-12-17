# Hash Chaining

This document defines the required method for chaining Evidence Objects into a tamper-evident sequence.

Hash chaining ensures that:
- evidence cannot be modified retroactively,
- omissions are detectable,
- and temporal order is preserved.

---

## Purpose

Hash chaining provides structural integrity.

It allows an independent verifier to determine whether:
- any Evidence Object has been altered,
- any object has been removed,
- or any sequence has been reordered.

This is achieved without storing payload data.

---

## Basic Chain Structure

Each Evidence Object must include a reference to its immediate predecessor.

The chain reference is typically implemented as:
- the cryptographic hash of the prior Evidence Object, or
- a digest derived from the prior object’s canonical representation.

This creates a linear, append-only sequence.

---

## Chain Continuity

Chain continuity must be enforced as follows:

- Each new Evidence Object must reference exactly one predecessor.
- The initial object in a sequence must be explicitly marked as a genesis event.
- Any missing reference constitutes a detectable gap.

Silent truncation is prohibited.

---

## Segmentation and Batching

For high-throughput systems, evidence may be segmented.

Segmentation rules:
- segments must be clearly defined (e.g., time-based or count-based),
- segmentation boundaries must be recorded,
- and segments must be chained in order.

Within a segment:
- individual events may be aggregated,
- a segment-level hash may represent the group.

This enables scalability without sacrificing integrity.

---

## Merkle Structures

Implementations may use Merkle trees to:

- batch multiple Evidence Objects,
- reduce settlement overhead,
- or support partial verification.

When Merkle structures are used:
- the construction method must be disclosed,
- root hashes must be preserved,
- and leaf membership must be provable.

Merkle roots may be anchored externally.

---

## Hash Function Requirements

Hash functions used for chaining must:

- be cryptographically secure,
- be collision-resistant,
- be widely standardized,
- and have known security properties.

The chosen hash function must be documented.

Custom or proprietary hash functions are prohibited.

---

## Canonicalization

Before hashing, Evidence Objects must be:

- serialized in a canonical form,
- free of ambiguous ordering,
- and stable across implementations.

Canonicalization rules must be explicit and deterministic.

---

## Detection of Tampering

Tampering is detected when:

- a hash fails to validate,
- a chain reference is missing,
- or a sequence is inconsistent.

Detection does not require trust in the sidecar operator.

---

## Gaps and Discontinuities

When evidence production is interrupted:

- the chain must reflect the interruption,
- gaps must not be silently filled,
- and continuity must not be inferred.

Explicit discontinuity markers may be used.

---

## Interaction with Settlement

Hash chains may be periodically anchored to an external settlement layer.

Anchoring:
- does not alter the chain,
- does not affect execution,
- and serves only as a public receipt.

Settlement frequency is implementation-specific.

---

## Summary

Hash chaining transforms individual observations into a coherent historical record.

Integrity emerges from structure, not authority.

A broken chain is visible by design.
