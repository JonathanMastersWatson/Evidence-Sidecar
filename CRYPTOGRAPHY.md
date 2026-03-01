# CVS Cryptography Considerations

This document describes cryptographic considerations for implementations of the
Cryptographic Verification Sidecar (CVS) specification.

The canonical CVS specification is defined by:

- `CVS_ARCHITECTURE_v2.7.md`
- `CVS_IMPLEMENTATION_v2.2.md`

If conflict exists, the canonical specification governs.

This document defines minimum properties, not fixed algorithms.
It is normative where RFC-2119 language appears.

---

## Purpose

Cryptography in CVS exists to:

- ensure integrity,
- enable independent verification,
- and make tampering detectable.

It does not provide confidentiality, identity, authorization, or correctness guarantees.

---

## Design Philosophy

Cryptographic choices should prioritize:

- longevity over novelty,
- standardization over customization,
- and verifiability over performance shortcuts.

Cryptographic mechanisms must be publicly reviewable and independently verifiable.

---

## Hash Functions

Hash functions used for Evidence Objects and chaining MUST:

- be collision-resistant,
- be widely standardized,
- have no known practical attacks,
- and be suitable for long-term verification.

Examples of acceptable classes include:

- SHA-2 family
- SHA-3 family

Specific algorithm choice MUST be disclosed.

---

## Digital Signatures and Attestation

Attestation mechanisms MUST:

- bind Evidence Objects to a witnessing entity,
- be independently verifiable,
- support key rotation,
- preserve long-term auditability.

Acceptable classes include:

- standard asymmetric digital signatures
- hardware-backed signing where available

Signature schemes MUST be documented.

---

## Canonicalization

Before hashing or signing:

- Evidence Objects MUST be serialized canonically,
- field ordering MUST be deterministic,
- encoding ambiguity MUST be eliminated.

Canonicalization is part of verifiability.

---

## Key Management

Key management MUST ensure:

- keys are protected against unauthorized use,
- compromise is detectable,
- rotation events are observable,
- historical evidence remains verifiable.

Key compromise does not invalidate prior evidence,
but rotation events MUST be transparent.

---

## Algorithm Agility

Implementations MUST support:

- future algorithm replacement,
- coexistence of multiple algorithms,
- verification of historical evidence created under prior algorithms.

Hard-coding a single algorithm indefinitely is discouraged.

---

## Scope Limitation

Cryptography in CVS does not:

- prove correctness,
- establish intent,
- prevent misconduct,
- guarantee regulatory compliance,
- or replace legal review.

It proves integrity and existence only.

---

## Regulatory Considerations

Implementations are responsible for compliance with applicable cryptographic
regulations and export controls.

This architecture does not override jurisdictional law.

---

## Summary

Cryptography in CVS is structural.

Its function is to make tampering visible and independently detectable — nothing more.
