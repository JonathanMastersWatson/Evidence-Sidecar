# CVS-EBI Conformance Checklist

An implementation is CVS-EBI conformant only if all required conditions are met.

---

## Boundary Separation

- [ ] CVS does not participate in execution decisions.
- [ ] CVS does not block execution.
- [ ] CVS does not modify execution flow.
- [ ] CVS does not reinterpret invariant meaning.
- [ ] CVS remains separable from the gate.

---

## Decision Semantics

- [ ] Gate output is binary: `ALLOW` or `DENY`.
- [ ] `GAP` is never used as a gate output token.
- [ ] Gap evidence exists only in the witness layer.

---

## Evidence Object

- [ ] Evidence Object follows the canonical schema.
- [ ] Required fields are always present.
- [ ] Nullable fields are explicitly set to `null`.
- [ ] Evidence Object is immutable after creation.
- [ ] No probabilistic trust scores are included.
- [ ] No interpretation layer is embedded.

---

## Hashing

- [ ] Canonical JSON serialization is used.
- [ ] Field ordering is deterministic.
- [ ] `evidence_hash` is reproducible.
- [ ] `proposal_hash` binds to the proposal.
- [ ] `decision_hash` binds to the decision.
- [ ] `specification_hash` binds to the active specification.
- [ ] `merkle_leaf_hash` is reproducible.

---

## Runtime

- [ ] Witness runtime operates asynchronously.
- [ ] Witness runtime does not fetch external state during evidence construction.
- [ ] Witness runtime tolerates delayed anchoring.
- [ ] Witness runtime tolerates temporary storage failure.
- [ ] Witness runtime records gaps explicitly.
- [ ] Witness runtime preserves chain continuity when possible.

---

## Validation

- [ ] Independent verification is supported.
- [ ] Offline verification is supported.
- [ ] Replay validation is supported.
- [ ] Merkle inclusion verification is supported.
- [ ] Chain continuity verification is supported.

---

## Non-Conformance Triggers

An implementation is non-conformant if it:

- makes CVS part of the decision path
- allows CVS to block execution
- uses `GAP` as a gate output
- mutates Evidence Objects after creation
- fetches external state during evidence construction
- adds probabilistic scoring to evidence semantics
- embeds policy interpretation in the evidence object
- cannot reproduce declared hashes independently
