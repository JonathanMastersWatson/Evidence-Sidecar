# Evidence Object

This document defines the canonical **Evidence Object** within the
Cryptographic Verification Sidecar (CVS) specification.

The canonical CVS specification is defined by:

- `CVS_ARCHITECTURE_v2.7.md`
- `CVS_IMPLEMENTATION_v2.2.md`

If conflict exists, the canonical specification governs.

The Evidence Object is the minimal, structured representation of what occurred,
when it occurred, and how it can be independently verified.

It contains no payload data and confers no authority.

---

## Purpose of the Evidence Object

The Evidence Object exists to:

- represent observed events in a verifiable form,
- preserve temporal ordering,
- enable detection of omission or tampering,
- support selective disclosure.

It does not exist to:

- store content,
- encode business logic,
- convey interpretation,
- assert correctness or legitimacy.

---

## Core Properties

Every CVS-Conforming Evidence Object MUST satisfy the following properties:

1. **Immutability**  
   Once finalized, the object MUST NOT be altered without detection.

2. **Minimality**  
   It contains only what is necessary to prove existence, order, and integrity.

3. **Independence**  
   It can be verified without access to the originating system.

4. **Composability**  
   It may be chained, aggregated, or batched with other objects.

5. **Non-Authoritative**  
   It records observable facts without asserting correctness or legality.

---

## Required Fields

Each Evidence Object MUST contain, at minimum, the following fields:

### 1. Evidence Identifier

A unique identifier derived from the object’s canonicalized content.

This identifier MUST:

- be deterministic,
- be collision-resistant,
- be reproducible by independent verifiers.

---

### 2. Observation Timestamp

A timestamp indicating when the event was observed by the sidecar.

It MUST:

- be sourced from a synchronized clock,
- be expressed in a standard format,
- be monotonic within a chain.

Clock source and precision SHOULD be disclosed.

---

### 3. Event Descriptor

A concise descriptor of the observed event.

This MAY include:

- event type,
- source system identifier,
- stream or channel identifier,
- protocol-level metadata.

Descriptors MUST NOT contain payload data.

---

### 4. Evidence Hash

A cryptographic hash representing the observed event or segment.

The hashing strategy MUST:

- be disclosed,
- be deterministic,
- permit independent recomputation.

Full payloads MUST NOT be embedded in the Evidence Object.

---

### 5. Chain Reference

A reference to the preceding Evidence Object in the sequence.

This creates a tamper-evident chain.

Missing references MUST result in detectable gaps.

---

### 6. Witness Attestation

A signature or attestation produced by the sidecar.

This attests only that:

- the event was observed,
- at the stated time,
- and recorded as described.

It does not attest to correctness, intent, or validity.

---

## Optional Fields

Optional fields MAY include:

- clock synchronization state,
- sidecar instance identifier,
- environment metadata,
- segmentation parameters,
- error indicators.

Optional fields MUST NOT alter canonical evidence semantics.

---

## Evidence Object Lifecycle

1. **Observation**  
   The sidecar observes an event or segment.

2. **Construction**  
   The Evidence Object is assembled from observed data.

3. **Chaining**  
   The object is linked to prior evidence.

4. **Attestation**  
   The sidecar signs or attests to the object.

5. **Persistence**  
   The object is stored locally or remotely.

6. **Aggregation**  
   Objects may be batched for settlement anchoring.

---

## Absence and Gaps

Evidence Objects MUST support explicit representation of absence.

If observation fails or is interrupted:

- a gap MUST be detectable,
- continuity MUST NOT be silently assumed,
- downstream verifiers MUST be able to identify missing segments.

Absence is itself evidence.

---

## Verification

An independent verifier MUST be able to:

- recompute hashes,
- validate signatures,
- confirm chain integrity,
- detect omissions.

Verification MUST NOT require privileged access to the originating system.

---

## Scope Limitation

The Evidence Object:

- does not prove correctness,
- does not establish intent,
- does not guarantee regulatory compliance,
- does not replace legal review.

It preserves integrity and detectability only.

---

## Summary

The Evidence Object is the atomic unit of verifiable integrity within CVS.

It is intentionally minimal, independently verifiable, and non-authoritative.

Everything else builds upon it.
