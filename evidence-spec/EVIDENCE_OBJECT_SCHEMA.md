# Canonical Evidence Object Schema

## Purpose

The Evidence Object is the canonical witness artifact emitted by CVS
beside an execution-boundary decision.

It records what was observed at the boundary, binds the proposal to
the decision, binds the decision to the active specification, and
provides deterministic cryptographic material for later verification.

The Evidence Object is immutable after creation.

This schema is a domain-specific profile of the CVS Evidence Object
defined in `CVS_ARCHITECTURE_v3.2.md §3`. It specialises the canonical
structure for 512 execution-boundary events. Two deliberate departures
from the canonical serialisation rules are declared in §Serialisation
Note below.

---

## Canonical JSON Shape

```json
{
  "schema_version": "cvs-ebi-1.0",
  "identity": {
    "evidence_object_id": "string",
    "proposal_id": "string",
    "decision_id": "string",
    "witness_id": "string",
    "runtime_id": "string"
  },
  "execution_evidence": {
    "decision": "ALLOW|DENY",
    "invariant_result": "string|null",
    "invariant_id": "string|null",
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
    "merkle_leaf_hash": "string",
    "witness_attestation": {
      "signature": "string",
      "algorithm": "string",
      "key_id": "string"
    }
  },
  "witness_metadata": {
    "witness_version": "string",
    "hash_algorithm": "string",
    "anchor_status": "NOT_ANCHORED|PENDING|ANCHORED|FAILED|DELAYED"
  },
  "gap_evidence": {
    "gap_detected": false,
    "gap_reason": null,
    "gap_start": null,
    "gap_end": null
  }
}
```

---

## Serialisation Note — Declared Profile Departures

The canonical CVS serialisation rules (`CVS_ARCHITECTURE_v3.2 §5.2`)
state that optional fields are omitted entirely rather than set to
null. This profile departs from that rule in two cases:

1. Nullable fields (`invariant_id`, `invariant_result`,
   `anchor_timestamp`, `previous_evidence_hash`, and all
   `gap_evidence` fields) are **present with explicit null values**
   rather than omitted. This preserves a stable, predictable schema
   surface across ALLOW and DENY cases, simplifying validator
   implementation.

2. `gap_evidence` is **embedded in every Evidence Object** as a block
   with `gap_detected: false` when no gap exists. The canonical
   `CVS_IMPLEMENTATION_v2.7 §2.3` models gaps as separate gap marker
   objects. This profile embeds gap state to keep the Evidence Object
   self-contained for 512 boundary events.

Both departures must be declared in the validation profile supplied
to any cross-organisation verifier.

---

## Field Requirements

All top-level objects are required.

All fields are required.

Nullable fields must be present with explicit `null` values when no
value exists. Omitting a required field invalidates the Evidence Object.

---

## Identity Fields

### `evidence_object_id`

Unique identifier for the Evidence Object.

Must be deterministic or collision-resistant.

Aligns with `evidence_object_id` as used in
`CVS_IMPLEMENTATION_v2.7 §2.2` Proof Bundle schema.

Recommended construction:
evidence_object_id = hash(runtime_id || witness_id || decision_id
|| monotonic_timestamp)

### `proposal_id`

Identifier of the proposal evaluated by the execution boundary.

### `decision_id`

Identifier of the boundary decision observed by CVS.

### `witness_id`

Identifier of the CVS witness instance emitting the evidence.

### `runtime_id`

Identifier of the local runtime environment where the witness
observed the boundary event.

---

## Execution Evidence Fields

### `decision`

The observed gate decision.

Valid values:
ALLOW
DENY

No other values are permitted. `GAP` is not a valid decision value.

### `invariant_result`

**On DENY (invariant failure):** the invariant identifier that failed
— e.g. `inv_2`.

**On DENY (evaluation error):** the string `evaluation_error`.

**On ALLOW:** `ALL_PASS`.

The witness records the value emitted by the boundary. It does not
reinterpret it.

### `invariant_id`

**On DENY (invariant failure):** the canonical invariant identifier
that failed — e.g. `inv_2`, corresponding to K2.

**On DENY (evaluation error):** `null`. No invariant was evaluated.

**On ALLOW:** `null`. No single invariant is identified; all passed.

### `proposal_hash`

Canonical hash of the proposal payload as known to the boundary at
decision time.

### `decision_hash`

Canonical hash of the decision payload emitted by the boundary.

### `specification_hash`

Canonical hash of the active specification used by the boundary at
decision time. Binds the decision to the ruleset in force when it
occurred.

For 512-conformant gates: `7B08C024B77A24830C15E7952D6E54BED383
AA960F4C74A71FF95CE51F4D80F5`

---

## Temporal Evidence Fields

### `monotonic_timestamp`

Runtime monotonic time captured by the witness. Used for ordering,
replay validation, and continuity checks.

### `witness_timestamp`

Wall-clock timestamp assigned by the witness runtime (ISO 8601 UTC).

### `anchor_timestamp`

Timestamp returned by the external anchor or settlement layer.
Nullable — anchoring is asynchronous. A missing anchor timestamp
does not invalidate the Evidence Object.

---

## Integrity Fields

### `evidence_hash`

Canonical hash of the Evidence Object with `integrity.evidence_hash`
temporarily set to `null` during hash construction. See
`CANONICALIZATION.md` for the full procedure.

### `previous_evidence_hash`

Hash of the previous Evidence Object in the witness chain. `null`
for the first object in a chain. A mismatch between this value and
the prior object's `evidence_hash` is a chain continuity break and
must be recorded as gap evidence.

### `merkle_leaf_hash`

Hash used as the Merkle leaf for batching and anchoring.

Default construction:
merkle_leaf_hash = hash(evidence_hash)

### `witness_attestation`

Cryptographic attestation that the event was observed at the stated
time and recorded as described. Required per
`CVS_ARCHITECTURE_v3.2 §3.5`.

**`signature`** — the detached signature value (hex-encoded).

**`algorithm`** — signing algorithm used. Valid values: `ECDSA-secp256k1`,
`ECDSA-secp256r1`, `RSA-2048`, `RSA-4096`, `EdDSA-Ed25519`.

**`key_id`** — identifier of the public key in the federation
directory used to verify this signature. The corresponding public
key must be pre-published at `_cvs.<domain>` or
`/.well-known/cvs-federation.json` before any events are signed.

The private key used to produce the signature must never leave the
HSM boundary. Signing operations execute inside the HSM.

The attestation does not attest to correctness or validity of the
observed decision — only that the event was observed and recorded
as described.

---

## Witness Metadata Fields

### `witness_version`

Version of the witness runtime that emitted the object.

### `hash_algorithm`

Hash algorithm used for deterministic hashing. Default: `SHA-256`.
`SHA-3-256` is acceptable. Proprietary hash functions are not
conformant.

### `anchor_status`

Anchoring state of the Evidence Object.

Valid values:
NOT_ANCHORED
PENDING
ANCHORED
FAILED
DELAYED

Anchoring state is witness metadata — not execution authority.

---

## Gap Evidence Fields

### `gap_detected`

Boolean. `false` in the normal (no-gap) case. `true` when the
witness has detected a continuity, availability, anchoring, or
emission gap.

The default state in the canonical JSON shape is `false` with all
other gap fields set to `null`.

### `gap_reason`

Bounded reason code. `null` when `gap_detected` is `false`.

Valid values when gap is detected:
WITNESS_UNAVAILABLE
ANCHOR_DELAYED
STORAGE_OUTAGE
HASH_MISMATCH
RUNTIME_RESTART
CHAIN_CONTINUITY_BREAK

### `gap_start`

Timestamp indicating when the witness-layer gap began. Nullable.

### `gap_end`

Timestamp indicating when the witness-layer gap ended. Nullable.
`null` while the gap is unresolved.

---

## ALLOW Case Summary

When `decision` is `ALLOW`:

```json
"execution_evidence": {
  "decision": "ALLOW",
  "invariant_result": "ALL_PASS",
  "invariant_id": null,
  ...
}
```

---

## DENY — Evaluation Error Case Summary

When the gate emits `DENY evaluation_error` (internal gate failure,
not invariant failure):

```json
"execution_evidence": {
  "decision": "DENY",
  "invariant_result": "evaluation_error",
  "invariant_id": null,
  ...
}
```

In production, this condition should trigger the gate's fail-open
handler rather than producing a denial. See
`512_IMPLEMENTATION_v3.3 §3.6`. The witness records whatever the
gate emitted.

---

## Invalid Evidence Conditions

An Evidence Object is invalid if:

- any required field is missing
- field ordering is non-canonical during hashing
- the decision value is not `ALLOW` or `DENY`
- `GAP` appears as a decision value
- `witness_attestation` is absent or uses a prohibited algorithm
- mutable post-creation fields are introduced
- probabilistic confidence values are added
- external state is fetched during object construction
- interpretation or policy mapping is embedded in the object
- the evidence hash cannot be reproduced

---

## Architectural Constraint

The witness records what the boundary emitted.

The witness does not decide whether the boundary was correct.
