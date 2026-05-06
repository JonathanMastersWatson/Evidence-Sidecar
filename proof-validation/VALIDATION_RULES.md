# Proof Validation Rules

## Purpose

Proof validation allows an independent party to verify that an Evidence Object is deterministic, hash-stable, linked to the proposal and decision, and consistent with its declared specification hash.

Validation does not decide whether execution should have occurred.

Validation proves what the witness recorded.

---

## Validator Inputs

A validator may receive:

- Evidence Object
- proposal payload or proposal hash
- decision payload or decision hash
- active specification or specification hash
- prior Evidence Object or previous evidence hash
- Merkle proof
- anchor receipt
- validation profile

---

## Required Validation Checks

A conformant validator must verify:

1. Required fields are present.
2. Decision value is only `ALLOW` or `DENY`.
3. Canonical serialization reproduces `evidence_hash`.
4. `proposal_hash` matches supplied proposal material, when provided.
5. `decision_hash` matches supplied decision material, when provided.
6. `specification_hash` matches supplied specification material, when provided.
7. `previous_evidence_hash` links to the prior Evidence Object, when provided.
8. `merkle_leaf_hash` is reproducible from `evidence_hash`.
9. Merkle inclusion proof is valid, when provided.
10. Anchor receipt commits to the Merkle root or evidence hash, when provided.
11. Gap evidence is explicit and not hidden.

---

## Evidence Hash Reproduction

To reproduce `evidence_hash`:

1. Parse the Evidence Object.
2. Confirm all required fields exist.
3. Copy the object.
4. Set `integrity.evidence_hash` to `null`.
5. Canonically serialize the copied object.
6. Hash the serialized bytes using `witness_metadata.hash_algorithm`.
7. Compare the result to the declared `integrity.evidence_hash`.

Mismatch means the Evidence Object is invalid or non-canonical.

---

## Chain Continuity Validation

If a prior Evidence Object is supplied:

```text
current.previous_evidence_hash must equal prior.evidence_hash
```

If not, validators must report a continuity break.

A continuity break does not imply the execution decision was invalid.

It means the witness chain has a visible evidence-layer gap.

---

## Merkle Inclusion Validation

To verify Merkle inclusion:

1. Reproduce `merkle_leaf_hash`.
2. Apply the supplied Merkle path.
3. Reconstruct the Merkle root.
4. Compare the reconstructed root to the anchored root or batch manifest root.

Mismatch means the Evidence Object is not included in the claimed batch.

---

## Specification Hash Validation

If the active specification is supplied, the validator must canonicalize and hash it using the declared specification profile.

The resulting digest must match `execution_evidence.specification_hash`.

This proves the decision was bound to a specific ruleset identity.

It does not prove the ruleset was wise, legal, ethical, or sufficient.

---

## Proposal-to-Decision Linkage

The validator should confirm:

```text
Evidence Object proposal_id == Decision payload proposal_id
Evidence Object proposal_hash == hash(Proposal payload)
Evidence Object decision_hash == hash(Decision payload)
```

This binds the observed decision to the proposal it evaluated.

---

## Decision-to-Evidence Linkage

The validator should confirm:

```text
Evidence Object decision_id == Decision payload decision_id
Evidence Object decision == Decision payload decision
Evidence Object invariant_id == Decision payload invariant_id
Evidence Object invariant_result == Decision payload invariant_result
Evidence Object specification_hash == Decision payload specification_hash
```

This binds the Evidence Object to the boundary decision.

---

## Replay Validation

Replay validation reconstructs the evidence path from supplied artifacts.

A replay validator must not fetch external state unless the validation profile explicitly allows retrieval of already-anchored public receipts.

Replay validation must identify:

- reproducible hashes
- broken hashes
- missing fields
- chain gaps
- anchoring gaps
- Merkle inclusion failures
- specification mismatches

---

## Invalid Conditions

Validation must fail if:

- required fields are missing
- `decision` contains any value other than `ALLOW` or `DENY`
- `GAP` appears as a decision
- `evidence_hash` cannot be reproduced
- `merkle_leaf_hash` cannot be reproduced
- supplied Merkle proof does not reconstruct the claimed root
- supplied anchor receipt does not bind to the claimed root or hash
- supplied proposal, decision, or specification material does not match declared hashes

---

## Validator Boundary

The validator verifies cryptographic consistency.

It does not perform governance interpretation.

It does not become a policy engine.

It does not replace 512.
