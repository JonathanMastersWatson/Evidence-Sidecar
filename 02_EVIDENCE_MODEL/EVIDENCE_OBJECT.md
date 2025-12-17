# Evidence Object

This document defines the canonical **Evidence Object** produced by a compliant evidence sidecar.

The Evidence Object is the minimal, structured representation of what occurred, when it occurred, and how it can be independently verified.

It contains no payload data and confers no authority.

---

## Purpose of the Evidence Object

The Evidence Object exists to:

- represent observed events in a verifiable form,
- preserve temporal ordering,
- enable detection of omission or tampering,
- and support selective disclosure.

It does not exist to:
- store content,
- encode business logic,
- or convey interpretation.

---

## Core Properties

Every Evidence Object **must** satisfy the following properties:

1. **Immutability**  
   Once finalized, the object cannot be altered without detection.

2. **Minimality**  
   It contains only what is necessary to prove existence, order, and integrity.

3. **Independence**  
   It can be verified without access to the originating system.

4. **Composability**  
   It may be chained, aggregated, or batched with other objects.

5. **Non-Authoritative**  
   It records facts without asserting correctness or legitimacy.

---

## Required Fields

Each Evidence Object must contain, at minimum, the following fields:

### 1. Evidence Identifier

A unique identifier derived from the object’s content, typically via cryptographic hashing.

This identifier must:
- be deterministic,
- be collision-resistant,
- and be reproducible by independent verifiers.

---

### 2. Observation Timestamp

A timestamp indicating when the event was observed by the sidecar.

Requirements:
- sourced from a synchronized clock,
- expressed in a standard format,
- monotonic within a chain.

Clock source and precision must be disclosed.

---

### 3. Event Descriptor

A concise descriptor of the observed event.

This may include:
- event type,
- source system identifier,
- stream or channel identifier,
- or protocol-level metadata.

Descriptors must not contain payload data.

---

### 4. Evidence Hash

A cryptographic hash representing the observed event or segment.

The hashing strategy:
- must be disclosed,
- must be deterministic,
- and must permit independent recomputation.

Full payloads must not be included.

---

### 5. Chain Reference

A reference to the preceding Evidence Object in the sequence.

This creates a tamper-evident chain.

Missing references indicate observable gaps.

---

### 6. Witness Attestation

A signature or attestation produced by the sidecar.

This attests only that:
- the event was observed,
- at the stated time,
- and recorded as described.

It does not attest to correctness or validity.

---

## Optional Fields

Optional fields may include:

- clock synchronization state,
- sidecar instance identifier,
- environment metadata,
- segmentation parameters,
- or error indicators.

Optional fields must not affect core verifiability.

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
   Objects may be batched for settlement.

---

## Absence and Gaps

Evidence Objects must support explicit representation of absence.

If observation fails or is interrupted:
- a gap must be detectable,
- continuity must not be silently assumed,
- and downstream verifiers must be able to identify missing segments.

Absence is itself evidence.

---

## Verification

An independent verifier must be able to:

- recompute hashes,
- validate signatures,
- confirm chain integrity,
- and detect omissions.

Verification must not require trust in the sidecar operator.

---

## Non-Goals

The Evidence Object must not:

- store original payloads,
- encode interpretation,
- enforce policy,
- or embed identity systems.

Such concerns belong outside this architecture.

---

## Summary

The Evidence Object is the atomic unit of trust in this system.

It is intentionally small, verifiable, and powerless.

Everything else builds upon it.
