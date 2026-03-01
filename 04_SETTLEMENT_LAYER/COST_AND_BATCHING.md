# Cost and Batching

This document defines how evidence settlement costs are managed,
bounded, and optimized through batching within the
Cryptographic Verification Sidecar (CVS) specification.

The canonical CVS specification is defined by:

- `CVS_ARCHITECTURE_v2.7.md`
- `CVS_IMPLEMENTATION_v2.2.md`

If conflict exists, the canonical specification governs.

This document is normative.

The objective is to ensure that evidence anchoring remains
economically predictable and operationally sustainable at scale.

---

## Purpose

Evidence anchoring must be economically stable.

Settlement costs SHOULD be:

- bounded,
- predictable,
- decoupled from execution throughput.

Batching is the primary mechanism for achieving this separation.

---

## Cost Characteristics

Settlement cost structures SHOULD exhibit the following properties:

- cost is not directly proportional to individual event frequency,
- cost scaling remains controlled under high throughput,
- cost volatility is limited,
- cost is observable and auditable.

Unbounded or unpredictable cost structures weaken operational viability.

---

## Evidence Batching

Evidence Objects MAY be aggregated into batches prior to settlement.

Batching involves:

- grouping multiple Evidence Objects,
- constructing a Merkle tree over the batch,
- anchoring the Merkle root to the settlement layer.

Batch composition rules MUST be documented.

---

## Batching Dimensions

Batching MAY occur along one or more dimensions:

- time-based (e.g., per interval),
- count-based (e.g., every N objects),
- system-based (e.g., per stream or channel),
- facility-based (e.g., per site).

The chosen batching strategy MUST be deterministic.

---

## Settlement Frequency

Settlement frequency MUST be:

- configurable,
- documented,
- independent of execution paths.

Settlement MUST NOT be synchronous with system execution.

---

## Cost Attribution

Batch settlement MAY enable cost attribution across:

- systems,
- channels,
- customers,
- organizational units.

Attribution mechanisms SHOULD be deterministic and auditable.

---

## Deferred Settlement

Temporary inability to settle (e.g., ledger unavailability) MUST NOT:

- block evidence generation,
- interrupt execution,
- invalidate local evidence chains.

Deferred settlement MUST be observable.

---

## Cost Predictability

Predictable settlement cost supports:

- budgeting,
- risk modeling,
- long-term operational planning.

Excessive volatility in anchoring cost may require batching adjustment
or alternative ledger selection.

---

## Transparency of Costs

Settlement costs SHOULD be:

- measurable,
- attributable,
- reportable.

Opaque fee structures reduce anchoring transparency.

---

## Non-Goals

Batching does not:

- alter evidentiary integrity,
- modify hash chaining semantics,
- obscure individual Evidence Objects.

Batching is an economic optimization only.

---

## Scope Limitation

Cost and batching rules:

- do not determine ledger selection,
- do not define pricing policy,
- do not guarantee economic outcomes.

They define structural decoupling between execution and anchoring cost.
