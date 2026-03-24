# Spec Hash Binding

This document defines the lifecycle of spec hash binding in a
CVS-Conforming implementation.

Spec hash binding is the mechanism that ties every Evidence Object
to the exact constraint specification that was active at the moment
of execution. Without it, a Proof Object cannot prove what rules
were applied — only that something was recorded.

---

## What the Spec Hash Is

The spec hash is a cryptographic commitment to the constraint
specification governing execution at a specific point in time.

It answers the question:
> "What rules were in force when this decision was made?"

It is not a version number. It is not a label.
It is a deterministic hash of the exact constraint content.
Any change to the constraint specification — including whitespace —
produces a different spec hash.

---

## Binding Lifecycle

### Stage 1 — Initialisation Binding

The spec hash MUST be computed and bound at system initialisation,
before any execution is observed.

- The constraint specification is hashed at startup
- The resulting hash is recorded as the active spec hash
- All Evidence Objects produced after this point include this hash

Binding at initialisation ensures that the spec hash reflects the
constraint set the system was started with — not a later state.

### Stage 2 — Per-Object Embedding

Every Evidence Object MUST embed the active spec hash in its
hash preimage.

- The spec hash is included before the Evidence Object hash is computed
- This makes the spec hash tamper-evident within every object
- A verifier can confirm the constraint version without trusting the operator

### Stage 3 — Divergence Handling

If the constraint specification changes after initialisation,
the implementation MUST handle divergence explicitly.

A CVS-Conforming implementation MUST choose one of the following
divergence responses:

**Option A — Halt and rebind**
Execution observation halts. The new specification is hashed.
A new binding is recorded. Observation resumes under the new spec hash.
All Evidence Objects after resumption carry the new hash.

**Option B — Log and continue**
The divergence is recorded as an explicit event in the evidence chain.
Execution observation continues under the original spec hash.
A new binding event is logged with the new spec hash.
Evidence Objects after the binding event carry the new hash.

**Option C — Halt and alert**
Execution observation halts. An alert is raised.
Observation does not resume until the divergence is explicitly resolved
by an authorised process.

### What Is Not Permitted

The following divergence responses are non-conformant:

- Silent rebinding without a logged divergence event
- Continuing to embed the old spec hash after a specification change
- Ignoring divergence and producing Evidence Objects with no spec hash
- Allowing runtime modification of the constraint specification
  without triggering a divergence response

Silent rebinding is the highest-risk failure mode. It produces
Evidence Objects that appear valid but reference a constraint
specification that was no longer active.

---

## Verification of Spec Hash Binding

A third-party verifier MUST be able to confirm spec hash binding
without operator cooperation by:

1. Obtaining the claimed constraint specification
2. Hashing it independently using the same algorithm
3. Comparing the result to the spec hash embedded in the Evidence Object
4. Confirming the hashes match

If they match, the Evidence Object was produced against that exact
constraint specification.

If they do not match, either:
- the constraint specification has changed since the object was produced
- the Evidence Object has been tampered with
- the implementation did not bind correctly

All three are material findings.

---

## Interoperability Note

Different implementations MAY choose different divergence responses
(Options A, B, or C above).

This is permitted. What is not permitted is undisclosed divergence handling.

An implementation MUST document which divergence response it uses.
A verifier examining an evidence chain MUST be able to determine
which response was in effect at any point in the chain.

This enables cross-implementation verification — a verifier working
with evidence from an unknown implementation can determine the
binding lifecycle from the evidence chain itself.

---

## Relationship to Other Documents

- `EVIDENCE_OBJECT.md` — defines the Evidence Object data model
- `HASH_CHAINING.md` — defines integrity chaining requirements
- `PROOF_OBJECT_INTEGRITY.md` — defines Element 2 (Spec Hash) requirements
- `CONFORMANCE.md` — test 3.1 and 3.2 govern Proof Object conformance

The canonical CVS specification (`CVS_ARCHITECTURE_v2.7.md`) governs
where any conflict exists.
