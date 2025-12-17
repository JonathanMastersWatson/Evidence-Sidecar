# Conformance

This document defines the requirements for an implementation to be considered
**conformant** with the Evidence Sidecar Reference Architecture.

Conformance is behavioral, not declarative.

---

## Normative Language

The key words **MUST**, **MUST NOT**, **SHOULD**, and **MAY** in this document
are to be interpreted as described in RFC 2119.

Where conflict exists, **MUST** and **MUST NOT** take precedence.

---

## Conformance Levels

This architecture defines two conformance levels.

### 1. Core Conformance (Mandatory)

An implementation claiming conformance **MUST** satisfy all Core Conformance
requirements defined in this document.

Core conformance is binary.

Partial compliance is non-conformance.

---

### 2. Optional Extensions (Non-Normative)

Implementations **MAY** provide additional features or integrations provided that:

- they do not violate any Core Conformance requirements
- they do not alter evidence semantics
- they do not introduce hidden authority
- they are clearly identified as non-normative

Optional extensions do not affect conformance status.

---

## Mandatory Properties

A conformant implementation **MUST** exhibit all of the following properties.

---

### Fail-Open Behavior

- The system **MUST NOT** block, delay, or alter execution of the observed system.
- Failure of the sidecar **MUST NOT** affect system availability.
- Failure **MUST** be observable through detectable gaps.

Fail-open behavior is non-negotiable.

---

### Witness-Only Authority

- The sidecar **MUST NOT** execute application logic.
- The sidecar **MUST NOT** enforce policy or outcomes.
- The sidecar **MUST NOT** alter observed inputs or outputs.

The sidecar witnesses events only.

---

### Detectable Gaps

- Absence of observation **MUST** be detectable.
- Gaps **MUST NOT** be concealed, smoothed, or reconstructed.
- Resumption after failure **MUST** be explicit.

Silence is evidence.

---

### Hash Chaining

- Evidence Objects **MUST** be cryptographically chained.
- Alteration of historical evidence **MUST** be detectable.
- Chaining **MUST** preserve ordering within observable scope.

Hash chaining establishes integrity, not correctness.

---

### Independent Verification

- Verification **MUST** be possible without trusting the operator.
- Verification **MUST NOT** require privileged access.
- Evidence integrity **MUST** be independently reproducible.

Verification is external by design.

---

### Selective Disclosure

- Disclosure **MUST** be scope-bounded.
- Disclosure **MUST** follow minimal revelation principles.
- Over-disclosure **MUST** be preventable by design.

Disclosure is precise, not maximal.

---

## Prohibited Capabilities

A conformant implementation **MUST NOT** include the following capabilities.

---

### Inline Execution Dependency

- Evidence generation **MUST NOT** be inline with execution.
- Settlement **MUST NOT** be required for execution to proceed.

Execution never waits for evidence.

---

### Enforcement Logic

- The sidecar **MUST NOT** enforce rules, compliance, or policy.
- The sidecar **MUST NOT** block or modify outcomes.

Enforcement is outside scope.

---

### Pay-to-Verify

- Verification **MUST NOT** require payment.
- Receipts **MUST** be publicly verifiable.

Charging for verification undermines trust.

---

### Hidden Authority

- No undisclosed decision power **MAY** exist.
- No implicit trust delegation **MAY** be assumed.
- Authority boundaries **MUST** be explicit and minimal.

Hidden power is non-conformant.

---

## Evidence of Conformance

An implementation claiming conformance **MUST** be able to demonstrate:

- fail-open behavior under induced failure
- detectable evidence gaps
- independent verification by third parties
- scoped disclosure without payload exposure
- resistance to coercive over-disclosure

Demonstration outweighs documentation.

---

## Claims an Implementation Must Not Make

A conformant implementation **MUST NOT** claim that it:

- guarantees correctness
- guarantees truth
- prevents wrongdoing
- enforces compliance
- replaces legal or regulatory judgment

Such claims are non-conformant.

---

## Non-Conformance Examples

The following patterns constitute non-conformance:

- inline logging that blocks execution
- evidence systems that fail closed
- “always-on” full disclosure pipelines
- proprietary verification requirements
- settlement-dependent execution
- retroactive evidence reconstruction

These failures are architectural, not incidental.

---

## Relationship to Other Documents

This document is normative and must be read in conjunction with:

- `README.md`
- `01_PRINCIPLES/*`
- `02_EVIDENCE_MODEL/*`
- `03_SELECTIVE_DISCLOSURE/*`
- `07_FAILURE_MODES/*`

Where ambiguity exists, this document governs conformance.

---

## Summary

Conformance is earned by behavior under stress.

An implementation either conforms — or it does not.
