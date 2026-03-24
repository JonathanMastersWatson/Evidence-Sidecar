# CVS Conformance

This document defines the requirements for an implementation to be considered
**CVS-Conforming** with the Cryptographic Verification Sidecar (CVS) specification.

The canonical CVS specification is defined by:
- `CVS_ARCHITECTURE_v2.7.md`
- `CVS_IMPLEMENTATION_v2.2.md`

If any conflict exists, the canonical specification takes precedence.

Conformance is behavioral, not declarative.

---

## Normative Language

The key words **MUST**, **MUST NOT**, **SHOULD**, and **MAY** in this document
are to be interpreted as described in RFC 2119.

Where conflict exists, canonical specification documents govern.

---

## Conformance Scope

An implementation may be described as **CVS-Conforming** only if it satisfies
all mandatory requirements defined in this document and the canonical specification.

Conformance is a technical classification.
It is not a certification, endorsement, regulatory determination, or compliance badge.

---

## Non-Goals and Boundary Conditions

CVS does not validate the correctness or completeness of declared constraints.
CVS provides cryptographic proof that execution remained within the declared
constraint boundary.

Errors in constraint definition are upstream failures in constraint architecture,
not failures of evidence. CVS is designed to expose such failures with precision
by proving adherence to the declared boundary, regardless of outcome correctness.

CVS is not:
- a policy engine
- a compliance system
- a monitoring or logging tool
- an access control system
- an enforcement mechanism

CVS witnesses execution events and produces independently verifiable evidence.
That boundary is fixed. Systems that conflate witnessing with enforcement, or
evidence with access control, are not CVS-Conforming regardless of naming or intent.

---

## Mandatory Properties

A CVS-Conforming implementation MUST exhibit all of the following properties.

---

### Fail-Open Behavior

- The system MUST NOT block, delay, or alter execution of the observed system.
- Failure of the sidecar MUST NOT affect system availability.
- Failure MUST be observable through detectable gaps.

Fail-open behavior is non-negotiable.

---

### Witness-Only Authority

- The sidecar MUST NOT execute application logic.
- The sidecar MUST NOT enforce policy or outcomes.
- The sidecar MUST NOT alter observed inputs or outputs.

The sidecar witnesses events only.

---

### Detectable Gaps

- Absence of observation MUST be detectable.
- Gaps MUST NOT be concealed, smoothed, or reconstructed.
- Resumption after failure MUST be explicit.

Silence is evidence.

---

### Hash Chaining

- Evidence Objects MUST be cryptographically chained.
- Alteration of historical evidence MUST be detectable.
- Chaining MUST preserve ordering within observable scope.

Hash chaining establishes integrity, not correctness.

---

### Independent Verification

- Verification MUST be possible without trusting the operator.
- Verification MUST NOT require privileged access.
- Evidence integrity MUST be independently reproducible.

Verification is external by design.

---

### Selective Disclosure

- Disclosure MUST be scope-bounded.
- Disclosure MUST follow minimal revelation principles.
- Over-disclosure MUST be preventable by design.

Disclosure is precise, not maximal.

---

## Operational States and Degraded Modes

A CVS-Conforming implementation MUST operate in one of the following
explicitly declared states at all times.

---

### State 1 — Verified Execution

Evidence generation is active and complete.
All actions are accompanied by verifiable Proof Objects.
This is the standard operating state.

---

### State 2 — Declared Degraded Mode

Evidence generation is unavailable or impaired.
Execution MAY continue under the following conditions:

- The degraded state MUST be explicitly signalled.
- All actions during degradation MUST be marked as unverified.
- The duration and scope of degradation MUST be observable.
- Resumption to Verified Execution MUST be logged explicitly.

Degraded mode is a declared operational condition, not a failure to be concealed.

---

### State 3 — Halted Execution

Execution is suspended due to inability to meet system-defined
accountability requirements.

This state is implementation-defined and may be required by upstream
constraint architecture or regulatory context.

---

**Silent execution without evidence generation is non-conformant.**

An implementation that continues execution without declaring a degraded state
or halting cannot be described as CVS-Conforming.

---

## Constraint Formation Responsibility

The completeness and correctness of constraint definitions are the responsibility
of upstream systems — including but not limited to policy frameworks, consent
architectures, and human governance layers.

CVS assumes constraints are declared and focuses exclusively on producing
verifiable evidence of adherence to those constraints.

This separation is intentional. It preserves the independence of the evidence
layer and prevents CVS from becoming an implicit authority over constraint
correctness.

A CVS-Conforming implementation MUST NOT:
- interpret or modify upstream constraint definitions
- make determinations about whether constraint definitions are correct
- refuse to generate evidence on the basis of disagreement with declared constraints

---

## Non-Conformant Patterns

The following architectural patterns are non-conformant regardless of intent
or naming:

- Inline execution dependency where evidence generation blocks execution
- Systems that fail closed
- Evidence systems that conceal detectable gaps
- Retroactive reconstruction of evidence
- Proprietary verification mechanisms requiring privileged trust
- Settlement-dependent execution
- Evidence systems that share authority with the enforcement layer
- Disclosure implemented as access control or RBAC filtering
- Custom observation surfaces that redefine valid capture points
- Partial or selective event emission that conceals coverage gaps
- Systems that combine enforcement and witness authority in a single component

Non-conformance does not invalidate a system.
It means the system MUST NOT be described as CVS-Conforming.

---

## Conformance Test Checklist

Conformance is binary. A system that passes all tests is CVS-Conforming.
A system that fails any single test is not CVS-Conforming.
There is no partial conformance.

| # | Test | Pass Condition | Fail Condition |
|---|---|---|---|
| 1.1 | Witness separation | Sidecar has no ability to influence execution | Any shared control path exists |
| 1.2 | No feedback loop | CVS failure or delay does not affect execution | Execution dependent on CVS state |
| 2.1 | Event completeness | All three observation points emitted: pre-validation, validation result, post-execution | Any event missing or partial |
| 2.2 | Correlation integrity | All events cryptographically linked via shared identifiers | Broken or missing linkage |
| 3.1 | Proof Object sufficiency | Object contains intent, spec, decision, outcome — standalone | Requires external context to interpret |
| 3.2 | Tamper detection | Field alteration produces detectable hash mismatch | Modification passes undetected |
| 4.1 | Minimal proof capability | Claim verifiable without full data exposure | Full exposure required for verification |
| 4.2 | Disclosure as proof | Cryptographic proof used for disclosure | RBAC or filtering used instead |
| 5.1 | Fail-open under failure | Execution continues; gap is recorded | Execution blocked by sidecar failure |
| 5.2 | Gap detectability | Absence of observation is detectable | Gap concealed or smoothed |
| 6.1 | Operational state declared | System is in Verified, Degraded, or Halted state at all times | Silent execution without declared state |
| 6.2 | Independent verification | Third-party verification possible without operator cooperation | Verification requires operator access |
| 7.1 | No retroactive evidence | Evidence created at execution time | Evidence derived from logs post-hoc |
| 7.2 | No enforcement logic | Sidecar produces no blocking or policy decisions | Enforcement logic present |

---

## Evidence of Conformance

An implementation described as CVS-Conforming SHOULD be able to demonstrate:

- fail-open behavior under induced failure
- detectable evidence gaps
- independent third-party verification
- scoped disclosure without payload overexposure
- resistance to coercive over-disclosure
- declared operational state transitions under degraded conditions

Demonstration outweighs documentation.

---

## Claims Outside Scope

CVS-Conforming implementations do not imply:

- guaranteed correctness
- guaranteed truth
- prevention of wrongdoing
- regulatory compliance
- legal sufficiency in any jurisdiction

CVS strengthens evidentiary defensibility.
It does not replace legal judgment or regulatory authority.

---

## Relationship to Other Documents

This document is normative and must be read in conjunction with:

- `README.md`
- `01_PRINCIPLES/*`
- `02_EVIDENCE_MODEL/*`
- `03_SELECTIVE_DISCLOSURE/*`
- `07_FAILURE_MODES/*`

Where ambiguity exists, the canonical CVS specification governs.
