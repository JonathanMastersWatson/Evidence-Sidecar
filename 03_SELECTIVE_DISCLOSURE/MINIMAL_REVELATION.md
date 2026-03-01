
# Minimal Revelation

This document defines the Minimal Revelation Principle within the
Cryptographic Verification Sidecar (CVS) specification.

The canonical CVS specification is defined by:

- `CVS_ARCHITECTURE_v2.7.md`
- `CVS_IMPLEMENTATION_v2.2.md`

If conflict exists, the canonical specification governs.

This document is normative.

Minimal revelation ensures that transparency does not become exposure.

---

## Purpose

The purpose of minimal revelation is to:

- satisfy scoped inquiries,
- protect unrelated data and systems,
- preserve confidentiality and autonomy,
- prevent disclosure from expanding beyond its defined boundary.

Revealing more than necessary weakens structural integrity.

---

## Principle

For any disclosure request, the system MUST reveal:

> The smallest set of evidence sufficient to answer the defined question.

No additional evidence SHOULD be included.

---

## Field-Level Minimization

Disclosed Evidence Objects MUST include only:

- fields required for independent verification,
- fields required to establish ordering,
- fields required to demonstrate integrity.

Optional or contextual fields MUST be excluded unless explicitly required
by the defined scope.

---

## Temporal Minimization

Disclosures MUST be limited to:

- the shortest feasible time window,
- strictly bounded by the request,
- inclusive of any gaps within that window.

Adjacent periods MUST NOT be included by default.

---

## Structural Minimization

Disclosure MUST include:

- only the relevant evidence path,
- only necessary chain references,
- only required attestations.

Parallel chains, unrelated segments, or external context
MUST NOT be included.

---

## No Derived Inference

The disclosure process MUST NOT:

- infer intent,
- assert correctness,
- construct narrative conclusions,
- imply causality beyond observable ordering.

Disclosure provides structure, not interpretation.

---

## No Payload Revelation

Minimal revelation requires that disclosures MUST NOT include:

- original payload data,
- content bodies,
- personal data,
- proprietary system internals.

Integrity is established cryptographically.

---

## Redaction vs Omission

Where minimization requires removal of fields:

- omission SHOULD be preferred to redaction,
- omitted fields SHOULD be structurally indicated,
- redaction MUST NOT alter canonical integrity.

Opaque redaction that alters structure is non-conformant.

---

## Disclosure Sufficiency

A CVS-Conforming implementation MUST be able to demonstrate that:

- disclosed evidence is sufficient for independent verification,
- no undisclosed evidence is required to validate integrity,
- completeness within scope is provable.

---

## Scope Limitation

Minimal revelation:

- does not determine legal sufficiency,
- does not evaluate proportionality,
- does not define authorization policy.

It governs structural disclosure boundaries only.

---

## Summary

Minimal revelation is precision.

Transparency is strongest when it is bounded, intentional, and exact.
