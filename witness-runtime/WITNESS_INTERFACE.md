# Witness Runtime Interface

## Purpose

The witness runtime receives execution-boundary events from 512 and
emits deterministic CVS Evidence Objects.

It sits beside the gate. It is not inside the gate.

The witness runtime operates within the **Capture Plane** of the CVS
three-plane architecture (`CVS_ARCHITECTURE_v3.2 §2.2`). The Capture
Plane observes execution, constructs Evidence Objects, chains them
cryptographically, and anchors commitments to a public settlement
ledger. It has no inbound connections from the Access or
Interpretation Planes. It never blocks execution.

---

## Runtime Responsibilities

The witness runtime must:

- receive boundary events from 512 asynchronously
- construct a canonical Evidence Object per `EVIDENCE_OBJECT_SCHEMA.md`
- hash the Evidence Object deterministically per `CANONICALIZATION.md`
- produce a `witness_attestation` signature via HSM — private key
  never leaves the HSM boundary
- preserve witness-chain continuity via `previous_evidence_hash`
- optionally batch Merkle leaves
- emit anchor-ready output
- record witness-layer gaps explicitly
- tolerate delayed anchoring
- tolerate temporary storage failure
- queue gap evidence locally for retry on storage restoration

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

The minimum boundary event received by the witness must include:

```json
{
  "proposal_id": "string",
  "decision_id": "string",
  "runtime_id": "string",
  "decision": "ALLOW|DENY",
  "invariant_result": "ALL_PASS|inv_|evaluation_error",
  "invariant_id": "string|null",
  "proposal_hash": "string",
  "decision_hash": "string",
  "specification_hash": "string",
  "boundary_monotonic_timestamp": "string"
}
```

**`invariant_result` values:**

- `ALL_PASS` — decision is ALLOW; all seven invariants passed
- `inv_<N>` — decision is DENY; invariant N failed (N = 1–7)
- `evaluation_error` — decision is DENY; gate failed internally

**`invariant_id` values:**

- `null` on ALLOW — no single invariant identified
- `inv_<N>` on DENY invariant failure
- `null` on DENY evaluation_error — no invariant was evaluated

The witness records the values emitted by the boundary. It does not
reinterpret them.

---

## Witness Output

The primary output is a canonical Evidence Object per
`EVIDENCE_OBJECT_SCHEMA.md`.

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

Boundary emits decision event.
Witness receives event asynchronously.
Witness constructs Evidence Object.
Witness sets evidence_hash to null.
Witness canonically serializes Evidence Object.
Witness calculates evidence_hash.
Witness signs evidence_object_id via HSM → witness_attestation.
Witness calculates merkle_leaf_hash.
Witness writes Evidence Object to local durable store or queue.
Witness batches leaves when available.
Witness emits anchor-ready batch payload.
Anchor result updates anchor_status in witness metadata — does
not modify original evidence semantics.


---

## Anchoring Rule

Anchoring is downstream of evidence construction.

Delayed anchoring does not invalidate the Evidence Object.

Failed anchoring creates witness-layer gap evidence.

Anchoring failure does not affect execution admissibility.

---

## Chain Continuity Rule

The witness preserves continuity by linking each Evidence Object to
the previous one via `previous_evidence_hash`.

If continuity cannot be preserved, the witness must emit gap evidence.

The chain break is evidence-layer degradation — not execution-layer
authority.

---

## External State Rule

The witness must not fetch external state during Evidence Object
construction.

External state creates non-determinism and breaks independent replay
verification.

---

## Normative References

| Document | Relevance |
|---|---|
| `CVS_ARCHITECTURE_v3.2 §2.2` | Three-plane architecture — Capture Plane definition |
| `CVS_ARCHITECTURE_v3.2 §3.5` | Full signing sequence and HSM custody requirement |
| `CVS_ARCHITECTURE_v3.2 §5.2` | Canonical serialization rules |
| `CVS_IMPLEMENTATION_v2.7 §1.1` | Capture Plane normative behaviours |
| `EVIDENCE_OBJECT_SCHEMA.md` | Canonical Evidence Object schema |
| `CANONICALIZATION.md` | Hashing and serialization rules |
| `FAILURE_AND_GAPS.md` | Gap semantics and prohibited gap behaviour |
| `512_IMPLEMENTATION_v3.3 §3.6` | Gate fail-open handler — gate-layer failure |
