# Cost and Batching

This document defines how evidence settlement costs are managed, bounded, and optimized through batching.

The goal is to ensure that evidence anchoring remains economically predictable and operationally sustainable at scale.

---

## Purpose

Evidence systems must be economically boring.

Costs must be:
- bounded,
- predictable,
- and decoupled from system throughput.

Batching is the primary mechanism by which this is achieved.

---

## Cost Characteristics

Settlement costs must satisfy the following conditions:

- costs are independent of event frequency,
- costs do not scale linearly with system throughput,
- costs are immune to congestion-based spikes,
- and costs are observable and auditable.

Unbounded costs undermine adoption.

---

## Evidence Batching

Evidence Objects may be aggregated into batches prior to settlement.

Batching involves:

- grouping multiple Evidence Objects,
- constructing a Merkle tree over the batch,
- and anchoring the Merkle root to the settlement layer.

Batch composition rules must be disclosed.

---

## Batching Dimensions

Batching may occur along one or more dimensions:

- time-based (e.g. per minute, per hour),
- count-based (e.g. every N objects),
- system-based (e.g. per stream or channel),
- or facility-based (e.g. per site).

The chosen strategy must be deterministic.

---

## Settlement Frequency

Settlement frequency must be:

- configurable,
- documented,
- and independent of execution paths.

Settlement must never be synchronous with system operation.

---

## Cost Attribution

Batch settlement enables cost attribution across:

- systems,
- channels,
- customers,
- or organizational units.

Attribution must be deterministic and auditable.

---

## Deferred Settlement

Temporary inability to settle (e.g. ledger unavailability) must not:

- block evidence generation,
- interrupt execution,
- or invalidate local evidence chains.

Deferred settlement must be recorded and observable.

---

## Cost Predictability

Predictable settlement cost enables:

- budgeting,
- insurance modeling,
- and risk pricing.

Volatile or adversarial fee mechanisms are incompatible with evidentiary systems.

---

## Transparency of Costs

Settlement costs must be:

- measurable,
- attributable,
- and reportable.

Hidden costs or opaque fee structures undermine trust.

---

## Non-Goals

Batching does not:

- reduce evidentiary integrity,
- alter hash chaining semantics,
- or obscure individual Evidence Objects.

Batching is an economic optimization only.

---

## Summary

Batching transforms evidence anchoring from a variable expense into a fixed operational cost.

Economic predictability is a prerequisite for trust infrastructure.
