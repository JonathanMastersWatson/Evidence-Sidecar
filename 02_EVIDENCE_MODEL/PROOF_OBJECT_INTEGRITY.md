# Proof Object Integrity

This document defines the integrity requirements for Evidence Objects
produced by a CVS-Conforming implementation.

It addresses two specific drift vectors:

1. **Schema hijacking** — a third party publishes a fixed CVS schema
   and claims it as canonical
2. **Semantic drift** — implementations vary field semantics while
   preserving surface structure, producing incompatible evidence

---

## What a Proof Object Is

A Proof Object is the atomic unit of CVS evidence.

It is the cryptographically bound record of a single execution event,
containing sufficient information to answer four questions without
reference to any external system:

1. What was proposed?
2. What rules were active?
3. What decision was made?
4. What occurred?

If a record cannot answer all four questions in isolation, it is not
a Proof Object. It is a log entry.

---

## Minimum Required Elements

Every Proof Object MUST contain the following elements.

### Element 1 — Intent Hash

A cryptographic commitment to the proposed action, captured before
constraint evaluation begins.

- MUST be produced before the commit boundary is crossed
- MUST be deterministic for identical proposals
- MUST NOT be modifiable after capture

### Element 2 — Spec Hash

A cryptographic commitment to the constraint set active at the moment
of evaluation.

- MUST reference the versioned constraint specification
- MUST be the same hash used by the enforcement layer
- MUST NOT be derived after the fact

This element is what binds the evidence to the declared rules.
Without it, a Proof Object cannot prove what constraints were applied.

### Element 3 — Decision Record

The outcome of constraint evaluation, recorded per invariant.

- MUST record the result for every constraint evaluated
- MUST NOT aggregate or summarise — per-invariant granularity is required
- MUST be binary per constraint: satisfied / not satisfied / gap

### Element 4 — Execution Outcome

The actual post-execution state, captured after the commit boundary
is crossed.

- MUST be captured after execution, not before
- MUST be cryptographically linked to the Intent Hash and Decision Record
- MUST NOT be reconstructed from logs

---

## Self-Containment Requirement

A Proof Object MUST be interpretable in isolation.

This means:

- No database lookup required
- No operator cooperation required
- No external schema reference required
- No runtime context required

A verifier with only the Proof Object and the public constraint
specification MUST be able to verify the record completely.

If external context is required, the implementation is not
producing Proof Objects. It is producing log references.

---

## Schema Position

CVS does not define a canonical Proof Object schema.

This is a deliberate architectural decision, not an omission.

Reasons:

- Domains have legitimately different data structures
- Fixing schema at the base layer creates a hijack surface
- What must be consistent is semantics, not structure

### What This Means in Practice

| Fixed by CVS | Implementation-defined |
|---|---|
| Four required elements | Field names |
| Semantic meaning of each element | Data types |
| Self-containment requirement | Serialisation format |
| Cryptographic binding method | Schema version |
| Per-invariant decision granularity | Domain-specific extensions |

### What No Third Party May Do

No third party may:

- publish a schema and describe it as the canonical CVS Proof Object format
- require other implementations to conform to their schema
- claim CVS conformance requires adoption of their schema

Any such claim is non-conformant and architecturally incorrect.

Interoperability is achieved through semantic consistency,
not structural uniformity.

---

## Cryptographic Binding Requirements

The four elements MUST be cryptographically bound to each other.

- The Intent Hash MUST be included in the Decision Record's hash preimage
- The Spec Hash MUST be included in the Decision Record's hash preimage
- The Execution Outcome MUST reference the Decision Record hash
- The complete Proof Object MUST produce a single verifiable root hash

Alteration of any element MUST produce a detectable hash mismatch.

---

## What a Proof Object Is Not

A Proof Object is not:

- a log entry
- an audit trail record
- a compliance report
- a monitoring event
- a debugging artifact

These are downstream interpretations of evidence.
They are produced from Proof Objects, not equivalent to them.

An implementation that produces only logs and describes them as
Proof Objects is not CVS-Conforming.

---

## Relationship to Other Documents

- `EVIDENCE_OBJECT.md` — defines the Evidence Object data model
- `HASH_CHAINING.md` — defines integrity chaining requirements
- `ANTI_DRIFT.md` — defines schema hijacking as a prohibited pattern
- `CONFORMANCE.md` — test 3.1 and 3.2 govern Proof Object conformance

The canonical CVS specification (`CVS_ARCHITECTURE_v2.7.md`) governs
where any conflict exists.
