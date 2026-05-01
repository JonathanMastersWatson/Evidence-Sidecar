# Spec Integrity and Anti-Drift

This document defines the non-negotiable architectural boundaries of the
Cryptographic Verification Sidecar (CVS).

Its function is to:

- prevent architectural drift
- prevent semantic reinterpretation
- prevent partial or misleading claims of conformance
- preserve independent verifiability

Any implementation that violates the constraints defined here is not
CVS-Conforming, regardless of naming, documentation, or intent.

---

## 1. Layer Separation

The architecture consists of three strictly independent layers.
These layers MUST NOT share authority, control paths, or decision logic.

The authoritative three-layer definition — covering what each layer
owns, produces, and must not claim — is maintained in the 512
repository at `LAYER_REFERENCE.md`. The summary below is scoped to
CVS-specific constraints.

### 1.1 Commit Gate (Enforcement Layer)

- Executes at the commit boundary
- Holds **exclusive commit authority** — the gate's authorisation
  signal is the structural prerequisite for the **non-bypassable
  commit path** to open
- Enforces pre-committed constraints deterministically
- Produces binary output only: ALLOW or DENY
- Contains no interpretation, discretion, or state accumulation
- When evaluation cannot complete: produces no output; execution
  proceeds under fail-open (Invariant 6); the witness layer records
  the ungoverned period as an evidence chain gap

### 1.2 Witness Layer (CVS)

- Observes execution events out-of-band
- Produces immutable Evidence Objects
- Has no ability to influence execution
- Is independently verifiable
- Records ALLOW or DENY results from the gate, and classifies
  ungoverned periods as evidence chain gaps

### 1.3 Interpretation Layer (External)

- Maps Evidence Objects to human or regulatory frameworks
- Performs no enforcement
- Produces no primary evidence
- Operates downstream of both enforcement and witness layers

### 1.4 Prohibited Configurations

The following configurations are explicitly non-conformant:

- A system that enforces constraints and controls its own evidence record
- A system that modifies Evidence Objects after capture
- A system that derives evidence from logs or reconstructed data
- A system that performs interpretation at the commit boundary
- A system that combines enforcement and witness authority in a single component

Any such system is not a CVS implementation.

---

## 2. Observation Model

There is no configurable observation surface.

### 2.1 Valid Observation Points

CVS emits exactly three event types per evaluated execution:

1. **Pre-Validation** — intent declaration, before constraint evaluation
2. **Validation Result** — constraint evaluation outcome (ALLOW or DENY)
3. **Post-Execution** — actual execution outcome

On fail-open events — where the gate cannot complete evaluation:

- Pre-Validation is emitted
- Validation Result is absent — the gate produced no output
- A gap record replaces Validation Result in the evidence chain
- Post-Execution is emitted

These events are:

- emitted at the commit boundary
- cryptographically linked
- correlated via shared identifiers

See `02_EVIDENCE_MODEL/GATE_OUTPUT_MATRIX.md` for the complete
matrix of gate completion states and corresponding witness
classification.

### 2.2 Prohibited Variants

The following are non-conformant:

- Custom capture planes that redefine observation points
- Vendor-defined observation surfaces
- Partial or selective event emission
- Systems that observe without binding to commit execution
- Systems that substitute logging for structured event emission

A system that does not emit all three event types for every evaluated
execution, or that does not emit a gap record for every fail-open
event, is not CVS-Conforming.

---

## 3. Proof Object Integrity

A Proof Object is defined by invariant sufficiency, not by structure.

### 3.1 Minimum Required Elements

Every Proof Object MUST answer:

1. What was proposed — intent hash
2. What rules were active — spec hash
3. What decision was made — per-invariant evaluation results
4. What occurred — execution outcome

### 3.2 Schema Position

- No canonical universal schema is defined by CVS
- Structure MAY vary by domain and implementation
- Field semantics MUST remain consistent with the four required elements
- A Proof Object MUST be self-contained — interpretable without external context

### 3.3 Non-Conformant Implementations

- Systems that standardise structure without preserving required semantics
- Systems that omit any of the four required elements
- Systems that require external context to interpret a Proof Object
- Systems that publish a fixed CVS schema and claim it as canonical

The last point is critical: no third party may publish a canonical CVS
Proof Object schema. Structure is implementation-defined. Semantics are not.

---

## 4. Disclosure Kernel

The Disclosure Kernel is a proof minimisation mechanism.
It is not an access control system.

### 4.1 Valid Behavior

The Disclosure Kernel enables:

- selective disclosure of fields
- Merkle inclusion proofs
- verification of constraint adherence without full data exposure
- scoped queries

### 4.2 Prohibited Interpretations

The following implementations are non-conformant:

- Disclosure implemented as RBAC or IAM
- Filtering access to data instead of proving claims
- Requiring full system exposure for verification
- Treating disclosure scope as a permissions boundary

Disclosure proves claims. It does not gate access.
Any implementation that conflates these two functions is not CVS-Conforming.

---

## 5. Upstream Constraint Definition

Constraint definition exists outside CVS.

### 5.1 Scope

The upstream constraint layer defines:

- consent logic
- authority models
- thresholds and limits
- domain-specific constraint encoding

### 5.2 CVS Position

- CVS does not define constraint values
- CVS does not validate constraint correctness
- CVS does not interpret constraint intent
- CVS proves adherence to whatever constraints are declared

### 5.3 Upstream Reference

The formation of constraint boundaries is addressed by the
Constraint Architecture discipline, maintained separately at:

https://github.com/JonathanMastersWatson/Constraint-Architecture

Errors in constraint definition are upstream failures, not CVS failures.
CVS will faithfully record adherence to incorrectly defined constraints.
That is by design.

### 5.4 Warning

Systems that do not explicitly define constraints upstream will:

- drift into inconsistent enforcement
- produce unverifiable outcomes
- fail under adversarial scrutiny

---

## 6. No Interpretation at Capture

The CVS capture layer MUST NOT perform interpretation.

Specifically, the capture layer MUST NOT:

- interpret constraint results
- classify outcomes beyond the recorded fields
- map events to regulatory frameworks at capture time
- derive conclusions from evidence
- annotate Evidence Objects with meaning

CVS records what happened. It does not record what it means.

Any system that performs interpretation at capture time is not
CVS-Conforming. Interpretation is the function of the external
Interpretation Layer (§1.3). It occurs downstream, never at capture.

This boundary is non-negotiable. Once interpretation enters the
capture layer, independence is compromised and evidence becomes
an argument rather than a record.

---

## 7. Evidence Formation Constraint

Evidence Objects MUST be formed at execution time.

They MUST NOT be:

- assembled from logs after execution
- reconstructed from system state
- derived from post-hoc analysis
- synthesised from partial records

An Evidence Object that is not formed at execution time is not
a Proof Object. It is a log entry. The distinction is material.

CVS does not improve logs. It replaces the need for them as evidence.

Any system that reconstructs evidence after execution and describes
the output as a Proof Object or Evidence Object is not CVS-Conforming.

---

## 8. Witness Isolation from Constraint Definition

The CVS witness layer MUST NOT participate in constraint definition.

Specifically, CVS MUST NOT:

- define constraints
- store constraint logic
- participate in constraint evaluation
- influence constraint configuration
- validate that constraints are correctly formed

Constraints are external inputs to the system being witnessed.
CVS observes outcomes against declared constraints only.

A witness layer that participates in constraint definition is no
longer independent. Its evidence is no longer independently verifiable.
Such a system is not CVS-Conforming.

---

## 9. No Control Loop from Witness

CVS MUST NOT feed signals back into the execution path.

Specifically, CVS MUST NOT:

- trigger execution decisions
- emit signals that influence system behaviour
- act as a monitoring or alerting system
- feed outputs into control or arbitration systems
- pause, block, or modify execution based on observed state

CVS is a passive observer. Passivity is not a limitation — it is
the architectural property that makes evidence independent.

The moment CVS becomes active, independence is gone and evidence
is compromised. Such a system is not CVS-Conforming.

---

## 10. Evidence Sufficiency Requirement

Each Evidence Object MUST be independently sufficient.

A single Evidence Object MUST enable a verifier to confirm:

- what was proposed (intent)
- what constraints were in force (governing specification)
- what evaluation result was produced (per-invariant)
- what execution outcome occurred

Verification MUST NOT require:

- access to execution systems
- access to internal logs
- trust in the operator
- external context of any kind

If external context is required to interpret an Evidence Object,
it is not an Evidence Object. It is a log reference.

This is what makes CVS evidence court-defensible and
third-party verifiable. Self-containment is not optional.

---

## 11. Multi-Party Verification

CVS MUST support independent verification by multiple parties.

### 11.1 Requirements

- Any third party MUST be able to verify evidence independently
- Verification MUST NOT require privileged system access
- Verification MUST NOT require operator cooperation
- Different parties MAY verify different scoped claims from the
  same underlying evidence record

### 11.2 Multi-Agency Pattern

Multiple regulatory bodies or counterparties may each verify
claims about the same execution record without sharing full
records with each other.

Each party receives a scoped Merkle proof for their specific claim.
No party receives the full record by default.
No party can determine what other parties verified.

This is not an access control model. It is a proof model.

### 11.3 Prohibited Configurations

- Verification gated behind authentication or permissions
- Evidence records requiring operator approval to access
- Verification requiring trust in the system being verified

---

## 12. What CVS Is Not

CVS is not:

- a logging system
- a monitoring platform
- a conformance tool
- an access control system
- a policy engine
- an analytics pipeline
- a control system
- an alerting system
- a truth engine
- a correctness validator

CVS is a witness layer for execution-bound evidence.

It records what happened at the commit boundary, proves that record
has not been tampered with, and enables independent verification
of specific claims without full data exposure.

That is its complete function. Nothing more is claimed.

---

## 13. Language Reference

The following language substitutions apply throughout all
CVS-Conforming documentation and implementations:

| Avoid | Use instead |
|---|---|
| monitoring | observation |
| logging | evidence capture |
| tracking | immutable record |
| analytics | — (remove from core) |
| compliance | conformance |
| compliant | CVS-Conforming |
| adopt | implement against |
| deploy CVS | instrument with CVS |

Language is where drift starts. Precise language prevents it.

---

## 14. Anti-Drift Principle

Any implementation that:

- introduces interpretation at the commit boundary
- merges enforcement and witness authority
- reconstructs evidence post hoc
- modifies constraint semantics without versioned commitment
- defines its own observation surface
- implements disclosure as access control
- feeds signals back into execution
- participates in constraint definition

has drifted from the architecture.

Such systems are not variants of CVS.
They are different systems and MUST NOT be described as CVS-Conforming.

---

## 15. Claims This Document Prohibits

The following claims are invalid for any CVS implementation:

- "CVS-compatible" without satisfying all conformance requirements
- "CVS-enabled" without independent witness separation
- "Proof-based conformance" without execution-bound evidence
- "512-compatible" without full invariant enforcement at the commit boundary
- Any claim implying CVS validates the correctness of upstream constraints
- Any claim implying CVS improves or replaces logs through reconstruction

---

## Relationship to Other Documents

This document and `CONFORMANCE.md` are complementary.

`CONFORMANCE.md` defines what a CVS-Conforming implementation must do.

This document defines what the architecture is — and what it is not.
Where both documents address the same property, both apply.
Neither supersedes the other.

- `CONFORMANCE.md` — behavioral requirements and conformance checklist
- `02_EVIDENCE_MODEL/GATE_OUTPUT_MATRIX.md` — gate completion states
  and witness classification matrix
- `PRIMITIVE_BOUNDARY.md` — CVS primitive scope and derivative
  responsibility
- `UPSTREAM.md` — three-layer stack and upstream constraint definition
- `512-main/LAYER_REFERENCE.md` — authoritative three-layer semantic
  firewall (Kernel / Commit Boundary / Witness Layer)

The canonical CVS specification in `/08_CANON/` governs where any
conflict exists.
