# Witness Runtime Interface

## Purpose

The witness runtime receives execution-boundary events from 512 and emits deterministic CVS Evidence Objects.

It sits beside the gate.

It is not inside the gate.

---

## Runtime Responsibilities

The witness runtime must:

- receive boundary events from 512
- construct a canonical Evidence Object
- hash the Evidence Object deterministically
- preserve witness-chain continuity
- optionally batch Merkle leaves
- emit anchor-ready output
- record witness-layer gaps
- tolerate delayed anchoring
- tolerate temporary storage failure

---

## Runtime Non-Responsibilities

The witness runtime must not:

- modify decisions
- block execution
- request reevaluation
- reinterpret invariant meaning
- fetch external state during evidence construction
- convert execution to DENY
- add a third gate decision state
- participate in admissibility

---

## Boundary Event Input

The minimum boundary event received by the witness should include:

```json
{
  "proposal_id": "string",
  "decision_id": "string",
  "runtime_id": "string",
  "decision": "ALLOW|DENY",
  "invariant_result": "string",
  "invariant_id": "string",
  "proposal_hash": "string",
  "decision_hash": "string",
  "specification_hash": "string",
  "boundary_monotonic_timestamp": "string"
}
```

The witness may add witness-specific timing and metadata.

The witness may not add interpretation.

---

## Witness Output

The primary output is a canonical Evidence Object.

Secondary outputs may include:

- Merkle leaf hash
- Merkle batch candidate
- anchor-ready payload
- local durable queue entry
- validation manifest

Secondary outputs must not mutate the Evidence Object.

---

## Asynchronous Operation

The witness runtime must be decoupled from the commit path.

A conformant implementation may use:

- local queue
- shared memory event emission
- append-only local buffer
- file-backed spool
- durable message queue

The gate must not wait for witness completion.

The gate must not depend on witness success.

---

## Recommended Runtime Flow

```text
1. Boundary emits decision event.
2. Witness receives event asynchronously.
3. Witness constructs Evidence Object.
4. Witness calculates evidence_hash.
5. Witness calculates merkle_leaf_hash.
6. Witness writes Evidence Object to local durable store or queue.
7. Witness batches leaves when available.
8. Witness emits anchor-ready batch payload.
9. Anchor result updates external anchoring metadata profile without changing original evidence semantics.
```

---

## Anchoring Rule

Anchoring is downstream of evidence construction.

Delayed anchoring does not invalidate the Evidence Object.

Failed anchoring creates witness-layer gap evidence.

Anchoring failure does not affect execution admissibility.

---

## Chain Continuity Rule

The witness should preserve continuity by linking each Evidence Object to the previous Evidence Object through `previous_evidence_hash`.

If continuity cannot be preserved, the witness must emit gap evidence.

The chain break is evidence-layer degradation, not execution-layer authority.

---

## External State Rule

The witness must not fetch external state during Evidence Object construction.

External state creates non-determinism and breaks independent replay verification.
