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

### 1.1 Commit Gate (Enforcement Layer)

- Executes at the commit boundary
- Enforces pre-committed constraints
- Produces binary output only: allow / deny / gap
- Contains no interpretation, discretion, or state accumulation

### 1.2 Witness Layer (CVS)

- Observes execution events out-of-band
- Produces immutable Evidence Objects
- Has no ability to influence execution
- Is independently verifiable

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

CVS emits exactly three event types:

1. **Pre-Validation** — intent declaration, before constraint evaluation
2. **Validation Result** — constraint evaluation outcome
3. **Post-Execution** — actual execution outcome

These events are:

- emitted at the commit boundary
- cryptographically linked
- correlated via shared identifiers

### 2.2 Prohibited Variants

The following are non-conformant:

- Custom capture planes that redefine observation points
- Vendor-defined observation surfaces
- Partial or selective event emission
- Systems that observe without binding to commit execution
- Systems that substitute logging for structured event emission

A system that does not emit all three event types for every execution
is not CVS-Conforming.

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

### 5.3 Warning

Systems that do not explicitly define constraints upstream will:

- drift into inconsistent enforcement
- produce unverifiable outcomes
- fail under adversarial scrutiny

This is an upstream failure, not a CVS failure. CVS will faithfully
record adherence to incorrect constraints. That is by design.

---

## 6. Anti-Drift Principle

Any implementation that:

- introduces interpretation at the commit boundary
- merges enforcement and witness authority
- reconstructs evidence post hoc
- modifies constraint semantics without versioned commitment
- defines its own observation surface
- implements disclosure as access control

has drifted from the architecture.

Such systems are not variants of CVS.
They are different systems and MUST NOT be described as CVS-Conforming.

---

## 7. Claims This Document Prohibits

The following claims are invalid for any CVS implementation:

- "CVS-compatible" without satisfying all conformance requirements
- "CVS-enabled" without independent witness separation
- "Proof-based compliance" without execution-bound evidence
- "512-compatible" without full invariant enforcement at the commit boundary
- Any claim implying CVS validates the correctness of upstream constraints

---

## Relationship to Conformance Document

This document and `CONFORMANCE.md` are complementary.

`CONFORMANCE.md` defines what a CVS-Conforming implementation must do.

This document defines what the architecture is — and what it is not.
Where both documents address the same property, both apply.
Neither supersedes the other.

The canonical CVS specification (`CVS_ARCHITECTURE_v2.7.md` and
`CVS_IMPLEMENTATION_v2.2.md`) governs where any conflict exists.
