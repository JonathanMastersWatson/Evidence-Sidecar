# Cryptography Considerations

This document describes cryptographic considerations for implementations of the Evidence Sidecar Reference Architecture.

It defines **minimum properties**, not fixed algorithms.

This document is non-normative.

---

## Purpose

Cryptography in this architecture exists to:

- ensure integrity,
- enable independent verification,
- and make tampering detectable.

It does not provide confidentiality, identity, or authorization.

---

## Design Philosophy

Cryptographic choices must prioritize:

- longevity over novelty,
- standardization over customization,
- and verifiability over performance tricks.

Custom cryptography is prohibited.

---

## Hash Functions

Hash functions used for Evidence Objects and chaining must:

- be collision-resistant,
- be widely standardized,
- have no known practical attacks,
- and be suitable for long-term verification.

Examples of acceptable classes include:
- SHA-2 family
- SHA-3 family

Specific algorithm choice must be disclosed.

---

## Digital Signatures and Attestation

Attestation mechanisms must:

- bind Evidence Objects to a witnessing entity,
- be independently verifiable,
- and support key rotation.

Acceptable classes include:
- standard asymmetric digital signatures
- hardware-backed signing where available

Signature schemes must be documented.

---

## Canonicalization

Before hashing or signing:

- Evidence Objects must be serialized canonically
- field ordering must be deterministic
- encoding ambiguity must be eliminated

Canonicalization rules are part of verifiability.

---

## Key Management

Key management must ensure that:

- keys are protected against unauthorized use,
- compromise is detectable,
- rotation events are observable,
- and historical evidence remains verifiable.

Key compromise does not invalidate past evidence, but must be disclosed.

---

## Algorithm Agility

Implementations must support:

- future algorithm replacement,
- coexistence of multiple algorithms,
- and verification of historical evidence created under older algorithms.

Hard-coding a single algorithm indefinitely is discouraged.

---

## What Cryptography Does Not Do

Cryptography in this architecture does not:

- prove correctness,
- establish intent,
- prevent bad behavior,
- or guarantee trustworthiness.

It proves integrity and existence only.

---

## Compliance and Regulation

Implementations must comply with:

- applicable cryptographic regulations,
- export controls,
- and jurisdictional requirements.

This architecture does not override local law.

---

## Summary

Cryptography here is structural, not magical.

Its job is to make lies expensive and tampering visible — nothing more.
