# Attestation

This document defines the scope, limits, and meaning of attestations produced by a compliant evidence sidecar.

Attestation confirms observation and recording.  
It does not confer correctness, legitimacy, or intent.

---

## Purpose of Attestation

Attestation exists to:

- bind Evidence Objects to a specific witness,
- confirm that an observation occurred,
- and enable independent verification of integrity.

It does not exist to:
- validate outcomes,
- approve behavior,
- or assert truth.

---

## What Is Being Attested

An attestation by the sidecar asserts only that:

- a specific event or segment was observed,
- at a specific observation time,
- and recorded according to the disclosed process.

Nothing more.

---

## What Is Not Being Attested

The sidecar does not attest that:

- the observed event was correct,
- the event was legitimate,
- the system behaved properly,
- or the outcome was valid.

Interpretation is external.

---

## Attesting Entity

Each attestation must identify:

- the witnessing sidecar instance,
- its cryptographic identity,
- and its operational context.

Identity mechanisms must be verifiable and disclosed.

---

## Attestation Methods

Attestation may be implemented using:

- digital signatures,
- hardware-backed keys,
- or other cryptographic mechanisms.

The chosen method must:
- be secure,
- be documented,
- and permit independent verification.

Proprietary or undisclosed methods are prohibited.

---

## Key Management

Key management practices must ensure that:

- keys are protected from unauthorized use,
- compromise is detectable,
- and rotation events are observable.

Key compromise does not invalidate historical evidence, but must be disclosed.

---

## Attestation Scope

Attestations must be:

- scoped to individual Evidence Objects or batches,
- linked to the hash chain,
- and unambiguous in meaning.

Broad or vague attestations are disallowed.

---

## Revocation and Compromise

If a witnessing key is compromised:

- the compromise must be recorded,
- affected attestations must be flagged,
- and subsequent evidence must use new keys.

Historical evidence remains verifiable but may be weighed accordingly.

---

## Legal Interpretation

In legal contexts, attestations serve as:

- proof of observation,
- proof of process,
- and proof of integrity.

They do not serve as proof of correctness or intent.

This limitation is intentional and protective.

---

## Summary

Attestation binds evidence to a witness without granting authority.

It answers the question:

“Who observed this, and how was it recorded?”

It does not answer:

“Was this right?”
