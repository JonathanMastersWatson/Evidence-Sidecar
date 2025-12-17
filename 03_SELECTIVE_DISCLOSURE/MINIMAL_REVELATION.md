# Minimal Revelation

This document defines the **Minimal Revelation Principle** governing all disclosures produced under this architecture.

Minimal revelation ensures that transparency does not become exposure.

---

## Purpose

The purpose of minimal revelation is to:

- satisfy legitimate inquiries,
- protect unrelated data and systems,
- preserve confidentiality and autonomy,
- and prevent disclosure from becoming a liability vector.

Revealing more than necessary is a defect.

---

## Principle

For any disclosure request, the system must reveal:

> **The smallest amount of evidence sufficient to answer the specific question posed.**

Nothing more.

---

## Field-Level Minimization

Disclosed Evidence Objects must include only:

- fields required for verification,
- fields required to establish ordering,
- fields required to demonstrate integrity.

Optional or contextual fields must be excluded unless explicitly required by scope.

---

## Temporal Minimization

Disclosures must be limited to:

- the shortest feasible time window,
- bounded strictly by the request,
- inclusive of gaps within that window.

Adjacent periods must not be included by default.

---

## Structural Minimization

Disclosure must include:

- only the relevant evidence path,
- only the necessary chain references,
- only the required attestations.

Parallel chains, unrelated segments, and external context must be excluded.

---

## No Derived Inference

The disclosure process must not:

- infer intent,
- infer correctness,
- infer causality beyond ordering,
- or provide analytical conclusions.

Only raw, verifiable structure is disclosed.

---

## No Payload Revelation

Minimal revelation explicitly prohibits disclosure of:

- original payload data,
- content bodies,
- personal information,
- proprietary system internals.

Proof is established cryptographically, not through content exposure.

---

## Redaction vs Omission

Where minimization requires removal of fields:

- omission is preferred to redaction,
- omitted fields must be noted as omitted,
- redaction must not alter canonical structure.

Hidden redaction is prohibited.

---

## Disclosure Sufficiency

The system must be able to demonstrate that:

- disclosed evidence is sufficient for verification,
- no additional undisclosed evidence is required to validate integrity,
- and completeness within scope is provable.

---

## Legal and Regulatory Alignment

Minimal revelation aligns with:

- proportionality principles,
- data minimization requirements,
- and reasonable disclosure standards.

Over-disclosure increases legal risk.

---

## Summary

Minimal revelation is not secrecy.

It is precision.

Transparency is strongest when it is bounded, intentional, and exact.
