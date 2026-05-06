# CVS-EBI Conformance Checklist

An implementation is CVS-EBI conformant only if all required
conditions are met.

---

## Plane Separation

- [ ] CVS operates within the Capture Plane only —
      `CVS_ARCHITECTURE_v3.2 §2.2`
- [ ] The Capture Plane has no inbound connections from the
      Access or Interpretation Planes
- [ ] The Access Plane exposes read-only interfaces only — no
      write access to the Evidence Store
- [ ] Interpretation tools consume evidence via Access Plane
      APIs only — they do not inject or modify Evidence Objects

---

## Boundary Separation

- [ ] CVS does not participate in execution decisions
- [ ] CVS does not block execution
- [ ] CVS does not modify execution flow
- [ ] CVS does not reinterpret invariant meaning
- [ ] CVS remains separable from the gate

---

## Decision Semantics

- [ ] Gate output observed by CVS is binary: `ALLOW` or `DENY`
- [ ] `GAP` is never recorded as a decision value
- [ ] Gap evidence exists only in the witness layer — never as
      a gate output token
- [ ] `DENY evaluation_error` is treated as `DENY` —
      `invariant_id` is set to `null`,
      `invariant_result` is set to `"evaluation_error"`
- [ ] `ALLOW` decisions set `invariant_id` to `null` and
      `invariant_result` to `"ALL_PASS"`

---

## Evidence Object

- [ ] Evidence Object follows the canonical schema —
      `EVIDENCE_OBJECT_SCHEMA.md`
- [ ] All required fields are present
- [ ] Nullable fields are explicitly set to `null`
- [ ] `evidence_object_id` is used (not `evidence_id`)
- [ ] Evidence Object is immutable after creation
- [ ] No probabilistic trust scores are included
- [ ] No interpretation layer is embedded
- [ ] `witness_attestation` block is present with `signature`,
      `algorithm`, and `key_id`
- [ ] Signing algorithm is one of: `ECDSA-secp256k1`,
      `ECDSA-secp256r1`, `RSA-2048`, `RSA-4096`, `EdDSA-Ed25519`
- [ ] Private signing key never leaves the HSM boundary
- [ ] Attestation public key is pre-published in federation
      directory before any events are signed

---

## Hashing

- [ ] Canonical JSON serialization is used per `CANONICALIZATION.md`
- [ ] Field ordering is deterministic and lexicographic at every level
- [ ] `evidence_hash` is reproducible
- [ ] `proposal_hash` binds to the proposal
- [ ] `decision_hash` binds to the decision — includes invariant
      result and specification hash
- [ ] `specification_hash` binds to the active specification
- [ ] `merkle_leaf_hash` is reproducible from `evidence_hash`
- [ ] Null-vs-omit profile departure is declared to
      cross-organisation validators

---

## Runtime

- [ ] Witness runtime operates asynchronously — not on the
      commit path
- [ ] Witness runtime does not fetch external state during
      evidence construction
- [ ] Witness runtime tolerates delayed anchoring
- [ ] Witness runtime tolerates temporary storage failure
- [ ] Witness runtime records gaps explicitly — never silently
      discards evidence state
- [ ] Witness runtime preserves chain continuity when possible
- [ ] Local queue is used for gap evidence retry on storage
      restoration

---

## Validation

- [ ] Independent verification is supported
- [ ] Offline verification is supported
- [ ] Replay validation is supported
- [ ] Merkle inclusion verification is supported
- [ ] Chain continuity verification is supported
- [ ] Cross-organisation validation profile declares both profile
      departures from `CVS_ARCHITECTURE_v3.2 §5.2`

---

## Non-Conformance Triggers

An implementation is non-conformant if it:

- makes CVS part of the decision path
- allows CVS to block execution
- uses `GAP` as a gate output or decision field value
- records `ALLOW` with a non-null `invariant_id`
- records `DENY evaluation_error` with a non-null `invariant_id`
- omits `witness_attestation` from any Evidence Object
- uses a proprietary signing algorithm for `witness_attestation`
- mutates Evidence Objects after creation
- fetches external state during evidence construction
- adds probabilistic scoring to evidence semantics
- embeds policy interpretation in the evidence object
- cannot reproduce declared hashes independently
- omits nullable fields rather than setting them to explicit `null`
  without declaring the departure to cross-organisation validators
