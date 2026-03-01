# Attestation

This document defines the scope, limits, and meaning of attestations
within the Cryptographic Verification Sidecar (CVS) specification.

The canonical CVS specification is defined by:

- `CVS_ARCHITECTURE_v2.7.md`
- `CVS_IMPLEMENTATION_v2.2.md`

If conflict exists, the canonical specification governs.

This document is normative.

Attestation confirms observation and recording.
It does not confer correctness, legitimacy, or intent.

---

## Purpose of Attestation

Attestation exists to:

- bind Evidence Objects to a specific witness,
- confirm that an observation occurred,
- enable independent verification of integrity.

It does not:

- validate outcomes,
- approve behavior,
- assert correctness,
- enforce policy.

Interpretation remains external.

---

## What Is Being Attested

An attestation asserts only that:

- a specific event or segment was observed,
- at a specific observation time,
- and recorded according to the disclosed process.

Nothing beyond that scope is implied.

---

## What Is Not Being Attested

The sidecar does not attest that:

- the observed event was correct,
- the event was legitimate,
- the system behaved properly,
- the outcome was valid.

Attestation binds process, not meaning.

---

## Attesting Entity

Each attestation MUST identify:

- the witnessing sidecar instance,
- its cryptographic identity,
- its operational context (where applicable).

Identity mechanisms MUST be independently verifiable and documented.

---

## Attestation Methods

Attestation MAY be implemented using:

- digital signatures,
- hardware-backed keys,
- other standardized cryptographic mechanisms.

The chosen method MUST:

- be secure,
- be documented,
- permit independent verification.

Undocumented or opaque mechanisms are non-conformant.

---

## Key Management

Key management MUST ensure that:

- keys are protected from unauthorized use,
- compromise is detectable,
- rotation events are observable.

If compromise occurs:

- the event MUST be recorded,
- subsequent attestations MUST use new keys.

Historical evidence remains verifiable, though trust context may change.

---

## Attestation Scope

Attestations MUST be:

- scoped to individual Evidence Objects or defined batches,
- linked to the hash chain,
- unambiguous in meaning.

Overbroad or undefined attestations are non-conformant.

---

## Revocation and Compromise

If a witnessing key is compromised:

- the compromise MUST be represented in evidence,
- affected attestations MUST be identifiable,
- chain integrity MUST remain intact.

Attestation continuity must remain verifiable.

---

## Scope Limitation

Attestation:

- does not prove correctness,
- does not establish intent,
- does not guarantee regulatory sufficiency.

It proves observation and integrity only.

---

## Summary

Attestation binds evidence to a witness without granting authority.

It answers:

“Who observed this, and how was it recorded?”

It does not answer:

“Was this correct?”
