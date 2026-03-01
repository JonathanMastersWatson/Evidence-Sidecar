# Time Ordering

This document defines the requirements for time representation and ordering
within the Cryptographic Verification Sidecar (CVS) specification.

The canonical CVS specification is defined by:

- `CVS_ARCHITECTURE_v2.7.md`
- `CVS_IMPLEMENTATION_v2.2.md`

If conflict exists, the canonical specification governs.

This document is normative.

Correct time ordering is essential for reconstructing sequences,
detecting manipulation, and preserving chain integrity.

---

## Purpose

Time ordering ensures that:

- events can be placed in a coherent sequence,
- ordering contradictions can be detected,
- reordering attempts are observable.

Absolute precision is less important than consistency and disclosure.

---

## Observation Time vs Event Time

CVS records **observation time**, not event intent.

- Observation time is when the sidecar observes the event.
- Event time may be declared by the originating system.

These timestamps MUST NOT be conflated.

If event time is recorded:

- it MUST be clearly labeled as declared,
- it MUST be treated as untrusted input.

Observation time governs ordering.

---

## Timestamp Requirements

Every Evidence Object MUST include:

- a timestamp with defined resolution,
- expressed in a standard, unambiguous format,
- derived from a disclosed clock source.

Timestamps MUST be monotonic within a chain.

---

## Clock Sources

The sidecar MUST disclose its clock source.

This MAY include:

- hardware time sources,
- network time protocols,
- platform-provided clocks.

Clock accuracy, drift, and synchronization state SHOULD be observable.

Perfect time is not required.  
Transparent time is required.

---

## Ordering Guarantees

The sidecar MUST guarantee:

- strict ordering of Evidence Objects within its own chain,
- consistency between ordering and chain references,
- detection of reordering attempts.

Global ordering across independent sidecars is not assumed.

---

## Concurrent Events

When multiple events occur concurrently:

- ordering MAY be arbitrary but MUST be deterministic,
- tie-breaking rules MUST be documented,
- concurrency MUST NOT be hidden.

The sidecar MUST NOT fabricate causal relationships.

---

## Clock Drift and Desynchronization

Clock drift or loss of synchronization MUST be:

- detectable,
- represented in evidence,
- observable during verification.

Silently rewriting timestamps is non-conformant.

---

## Time Gaps

When observation is interrupted:

- time gaps MUST be observable,
- missing intervals MUST NOT be interpolated,
- continuity MUST NOT be inferred.

Absence is part of the record.

---

## Scope Limitation

Time ordering:

- does not prove causation,
- does not establish intent,
- does not guarantee external synchronization accuracy.

It preserves internal sequence integrity only.

---

## Summary

Time ordering is not about precision.

It is about consistency, transparency, and detectability.

A disclosed uncertainty is stronger than fabricated certainty.
