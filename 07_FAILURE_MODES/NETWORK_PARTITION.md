# Network Partition

This document defines system behavior when network partitions occur between the sidecar, observed systems, storage, or settlement layers.

Network partitions are expected conditions in distributed systems, not exceptional failures.

---

## Purpose

The purpose of this document is to ensure that:

- network partitions do not halt execution,
- evidence generation remains honest under isolation,
- and post-event reconstruction remains possible.

Partitions reveal design truth.

---

## Definition of Network Partition

A network partition occurs when:

- communication between components is interrupted,
- latency exceeds operational bounds,
- or connectivity becomes asymmetric or intermittent.

Partitions may be partial, transient, or prolonged.

---

## Partition Tolerance Principle

During a partition:

- observed systems must continue operating,
- sidecars must continue observing locally,
- and no component may assume global state.

Availability is prioritized over consistency.

---

## Local Evidence Continuity

When isolated, a sidecar must:

- continue local evidence generation,
- maintain hash chain integrity,
- record observation time locally,
- and preserve ordering within its partition.

Global ordering is not assumed.

---

## Partition Detection

Partitions must be:

- detectable,
- recorded as part of evidence,
- and disclosed upon verification.

Silent partition healing is prohibited.

---

## Divergent Chains

During partitions, multiple evidence chains may diverge.

Upon reconnection:

- chains must not be merged retroactively,
- reconciliation must be explicit,
- and divergence must remain observable.

Convergence must not erase history.

---

## Settlement During Partition

If settlement connectivity is lost:

- settlement is deferred,
- evidence chains persist locally,
- and settlement resumes post-partition.

Settlement delay must be disclosed.

---

## Clock Drift and Isolation

Network partitions may affect time synchronization.

The sidecar must:

- disclose synchronization state,
- record drift where detectable,
- and avoid fabricating precision.

Uncertainty is part of evidence.

---

## Verification After Partition

An independent verifier must be able to:

- identify partition intervals,
- distinguish local vs global ordering,
- and assess impact on evidence completeness.

Partitions must not invalidate evidence — only contextualize it.

---

## Legal and Forensic Considerations

Partitions strengthen credibility when disclosed.

They demonstrate:
- lack of centralized manipulation,
- honesty in evidence limits,
- and realistic system behavior.

---

## Summary

Network partitions are not errors.

They are the moment distributed systems tell the truth.
