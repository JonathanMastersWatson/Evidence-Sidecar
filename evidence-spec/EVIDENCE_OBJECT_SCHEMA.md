# Canonical Evidence Object Schema

## Purpose

The Evidence Object is the canonical witness artifact emitted by CVS beside an execution-boundary decision.

It records what was observed at the boundary, binds the proposal to the decision, binds the decision to the active specification, and provides deterministic cryptographic material for later verification.

The Evidence Object is immutable after creation.

---

## Canonical JSON Shape

```json
{
  "schema_version": "cvs-ebi-1.0",
  "identity": {
    "evidence_id": "string",
    "proposal_id": "string",
    "decision_id": "string",
    "witness_id": "string",
    "runtime_id": "string"
  },
  "execution_evidence": {
    "decision": "ALLOW|DENY",
    "invariant_result": "string",
    "invariant_id": "string",
    "proposal_hash": "string",
    "decision_hash": "string",
    "specification_hash": "string"
  },
  "temporal_evidence": {
    "monotonic_timestamp": "string",
    "witness_timestamp": "string",
    "anchor_timestamp": "string|null"
  },
  "integrity": {
    "evidence_hash": "string",
    "previous_evidence_hash": "string|null",
    "merkle_leaf_hash": "string"
  },
  "witness_metadata": {
    "witness_version": "string",
    "hash_algorithm": "string",
    "anchor_status": "NOT_ANCHORED|PENDING|ANCHORED|FAILED|DELAYED"
  },
  "gap_evidence": {
    "gap_detected": true,
    "gap_reason": "string|null",
    "gap_start": "string|null",
    "gap_end": "string|null"
  }
}
```

---

## Field Requirements

All top-level objects are required.

All fields are required.

Nullable fields must be present with explicit `null` values when no value exists.

Omitting a required field invalidates the Evidence Object.

---

## Identity Fields

### `evidence_id`

Unique identifier for the Evidence Object.

Must be deterministic or collision-resistant.

Recommended construction:

```text
evidence_id = hash(runtime_id || witness_id || decision_id || monotonic_timestamp)
```

### `proposal_id`

Identifier of the proposal evaluated by the execution boundary.

### `decision_id`

Identifier of the boundary decision observed by CVS.

### `witness_id`

Identifier of the CVS witness instance emitting the evidence.

### `runtime_id`

Identifier of the local runtime environment where the witness observed the boundary event.

---

## Execution Evidence Fields

### `decision`

The observed gate decision.

Valid values:

```text
ALLOW
DENY
```

No other values are permitted.

`GAP` is not a valid decision value.

### `invariant_result`

Deterministic result emitted by the execution boundary for the evaluated invariant.

The witness records the value but does not reinterpret it.

### `invariant_id`

Identifier of the invariant evaluated at the execution boundary.

### `proposal_hash`

Canonical hash of the proposal payload as known to the boundary at decision time.

### `decision_hash`

Canonical hash of the decision payload emitted by the boundary.

### `specification_hash`

Canonical hash of the active specification used by the boundary at decision time.

This binds the decision to the ruleset in force when the decision occurred.

---

## Temporal Evidence Fields

### `monotonic_timestamp`

Runtime monotonic time captured by the witness.

This is used for ordering, replay validation, and continuity checks.

### `witness_timestamp`

Wall-clock timestamp assigned by the witness runtime.

### `anchor_timestamp`

Timestamp returned by an external anchor or settlement layer.

This field is nullable because anchoring is asynchronous.

A missing anchor timestamp does not invalidate the Evidence Object.

---

## Integrity Fields

### `evidence_hash`

Canonical hash of the Evidence Object with the `evidence_hash` field temporarily set to `null` during hash construction.

### `previous_evidence_hash`

Optional hash of the previous Evidence Object in the witness chain.

Must be present as `null` when no previous hash exists.

### `merkle_leaf_hash`

Hash used as the Merkle leaf for batching and anchoring.

Recommended construction:

```text
merkle_leaf_hash = hash(evidence_hash)
```

---

## Witness Metadata Fields

### `witness_version`

Version of the witness runtime that emitted the object.

### `hash_algorithm`

Hash algorithm used for deterministic hashing.

Recommended default:

```text
SHA-256
```

### `anchor_status`

Anchoring state of the Evidence Object.

Valid values:

```text
NOT_ANCHORED
PENDING
ANCHORED
FAILED
DELAYED
```

Anchoring state is witness metadata, not execution authority.

---

## Gap Evidence Fields

### `gap_detected`

Boolean indicating whether the witness detected a continuity, availability, anchoring, or emission gap.

### `gap_reason`

Human-readable but bounded reason code or reason string.

This field must not contain interpretation of execution admissibility.

Examples:

```text
WITNESS_UNAVAILABLE
ANCHOR_DELAYED
STORAGE_OUTAGE
HASH_MISMATCH
RUNTIME_RESTART
CHAIN_CONTINUITY_BREAK
```

### `gap_start`

Timestamp indicating when the witness-layer gap began.

Nullable.

### `gap_end`

Timestamp indicating when the witness-layer gap ended.

Nullable.

---

## Invalid Evidence Conditions

An Evidence Object is invalid if:

- any required field is missing
- field ordering is non-canonical during hashing
- the decision value is not `ALLOW` or `DENY`
- `GAP` appears as a decision
- mutable post-creation fields are introduced
- probabilistic confidence values are added
- external state is fetched during object construction
- interpretation or policy mapping is embedded in the object
- the evidence hash cannot be reproduced

---

## Architectural Constraint

The witness records what the boundary emitted.

The witness does not decide whether the boundary was correct.
