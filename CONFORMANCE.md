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

## Non-Conformant Patterns

The following architectural patterns are considered non-conformant:

- Inline execution dependency where evidence generation blocks execution
- Systems that fail closed
- Evidence systems that conceal detectable gaps
- Retroactive reconstruction of evidence
- Proprietary verification mechanisms requiring privileged trust
- Settlement-dependent execution

Non-conformance does not invalidate a system.
It simply means the system should not be described as CVS-Conforming.

---

## Evidence of Conformance

An implementation described as CVS-Conforming SHOULD be able to demonstrate:

- fail-open behavior under induced failure
- detectable evidence gaps
- independent third-party verification
- scoped disclosure without payload overexposure
- resistance to coercive over-disclosure

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
