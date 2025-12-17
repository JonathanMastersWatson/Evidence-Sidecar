# Time Ordering

This document defines the requirements for time representation and ordering within the evidence sidecar architecture.

Correct time ordering is essential for reconstructing events, resolving disputes, and detecting manipulation.

---

## Purpose

Time ordering ensures that:

- events can be placed in a coherent sequence,
- causality can be inferred,
- and contradictions can be identified.

Absolute precision is less important than **consistency and disclosure**.

---

## Observation Time vs Event Time

The sidecar records **observation time**, not event intent.

- Observation time is when the sidecar observes the event.
- Event time may be declared by the originating system.

These two timestamps must not be conflated.

When event time is recorded:
- it must be clearly labeled as declared,
- and treated as untrusted input.

---

## Timestamp Requirements

Every Evidence Object must include:

- a timestamp with defined resolution,
- expressed in a standard, unambiguous format,
- derived from a disclosed clock source.

The timestamp must be monotonic within a chain.

---

## Clock Sources

The sidecar must disclose its clock source, which may include:

- hardware time sources,
- network time protocols,
- or platform-provided clocks.

Clock accuracy, drift, and synchronization state must be observable.

Perfect time is not required.  
Honest time is required.

---

## Ordering Guarantees

The sidecar must guarantee:

- strict ordering of Evidence Objects within its own chain,
- consistency between ordering and chain references,
- and detection of reordering attempts.

Global ordering across multiple sidecars is not assumed.

---

## Concurrent Events

When multiple events occur concurrently:

- ordering may be arbitrary but deterministic,
- tie-breaking rules must be documented,
- and concurrency must not be hidden.

The sidecar must not fabricate causal relationships.

---

## Clock Drift and Desynchronization

Clock drift or loss of synchronization must be:

- detectable,
- recorded in evidence,
- and disclosed upon verification.

Silently corrected timestamps are prohibited.

---

## Time Gaps

When observation is interrupted:

- time gaps must be observable,
- missing intervals must not be interpolated,
- and continuity must not be implied.

Absence is part of the record.

---

## Legal and Forensic Considerations

In legal contexts, time ordering:

- supports reconstruction of sequences,
- reveals inconsistencies,
- and exposes manipulation.

Disclosed uncertainty is preferable to false precision.

---

## Summary

Time ordering is not about perfection.

It is about consistency, transparency, and detectability.

A timeline that admits uncertainty is stronger than one that hides it.
