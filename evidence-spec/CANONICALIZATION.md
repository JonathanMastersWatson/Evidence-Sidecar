# Canonicalization and Hashing Rules

## Purpose

Canonicalization ensures that the same Evidence Object always produces
the same hash across runtimes, languages, platforms, and validators.

Evidence that cannot be hashed reproducibly is not CVS-EBI conformant.

This document defines the serialization rules for this profile. Where
these rules depart from the canonical CVS serialization specification
(`CVS_ARCHITECTURE_v3.2 §5.2`), the departure is declared explicitly.
Cross-organisation verifiers must be supplied a validation profile
declaring these departures before verification is attempted.

---

## Serialization Rules

Evidence Objects must be serialized using canonical JSON.

Required rules:

1. UTF-8 encoding only.
2. Lexicographic ordering of object keys at every level.
3. No insignificant whitespace.
4. No comments.
5. **Nullable fields are present with explicit `null` values** — they
   are not omitted. This is a declared departure from
   `CVS_ARCHITECTURE_v3.2 §5.2`, which specifies optional fields are
   omitted entirely. This profile retains explicit nulls to preserve
   a stable, predictable schema surface across all decision cases.
   Cross-organisation validators must be informed of this departure.
6. Strings must be normalized before serialization (NFC Unicode
   normalization).
7. Numbers, if ever introduced, must use canonical decimal
   representation.
8. Arrays, if ever introduced, must preserve declared order.

---

## Hash Input Rule

To calculate `evidence_hash`:

1. Construct the full Evidence Object.
2. Set `integrity.evidence_hash` to `null`.
3. Canonically serialize the object per the rules above.
4. Hash the serialized bytes using the declared `hash_algorithm`.
5. Insert the resulting digest into `integrity.evidence_hash`.

The `witness_attestation` block is included in the hash input.
The signature is computed over the `evidence_object_id`, not the
full Evidence Object. See `CVS_ARCHITECTURE_v3.2 §3.5` for the
full signing sequence.

---

## Hash Output Format

Hash values are represented as lowercase hexadecimal strings unless
a profile explicitly defines another encoding.

Required default format:
sha256:<lowercase_hex_digest>

---

## Proposal Hash

`proposal_hash` must be calculated from the exact proposal payload
evaluated by the boundary.

The witness must not normalize, enrich, or reinterpret the proposal
payload.

---

## Decision Hash

`decision_hash` must be calculated from the exact decision payload
emitted by the boundary.

The decision payload must include, at minimum:

- decision id
- proposal id
- decision value (`ALLOW` or `DENY`)
- invariant id (or `null` on ALLOW or evaluation_error)
- invariant result (`ALL_PASS`, `inv_<N>`, or `evaluation_error`)
- specification hash

---

## Specification Hash

`specification_hash` binds the observed decision to the specification
active at the boundary when the decision occurred.

The witness records the specification hash supplied by the boundary.

The witness does not calculate admissibility.

For 512-conformant gates the canonical specification hash is:
7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5

---

## Merkle Leaf Hash

Default construction:
merkle_leaf_hash = hash(evidence_hash)

A profile may include domain separation:
merkle_leaf_hash = hash("CVS-EBI-MERKLE-LEAF" || evidence_hash)

If domain separation is used, it must be declared in the validation
profile.

---

## Previous Evidence Hash

`previous_evidence_hash` is used for witness-chain continuity.

Rules:

- First evidence object in a chain must set this field to `null`.
- Subsequent evidence objects must reference the prior object's
  `evidence_hash`.
- A mismatch creates a witness-layer chain continuity break and must
  be recorded as gap evidence.
- A chain break must not influence gate admissibility.

---

## Witness Attestation

The `witness_attestation` block is part of the Evidence Object and
is therefore included in the `evidence_hash` input.

The `signature` value itself is computed over `evidence_object_id`
using the HSM-held private key. The private key never leaves the HSM
boundary.

The corresponding public key must be pre-published in the federation
directory (`_cvs.<domain>` or `/.well-known/cvs-federation.json`)
before any events are signed. Verification requires no operator
cooperation — the public key is available independently.

Valid signing algorithms: `ECDSA-secp256k1`, `ECDSA-secp256r1`,
`RSA-2048`, `RSA-4096`, `EdDSA-Ed25519`. Proprietary signing schemes
are not conformant per `CVS_ARCHITECTURE_v3.2 §5.2`.

---

## Forbidden Inputs

The following must not be included in canonical hash construction:

- local debug logs
- runtime stack traces
- mutable counters not present in the Evidence Object
- network lookups
- external policy mappings
- trust scores
- confidence scores
- model explanations
- natural-language interpretation layers

---

## Determinism Test

A conformant implementation must pass this test:
same Evidence Object

same canonicalization rules
same hash algorithm
= same evidence_hash


If two independent validators cannot reproduce the same hash, the
Evidence Object is non-conformant.

---

## Cross-Organisation Validation Profile Requirements

When supplying an Evidence Object for cross-organisation verification,
the following departures from `CVS_ARCHITECTURE_v3.2 §5.2` must be
declared in the accompanying validation profile:

1. Nullable fields are present as explicit `null` rather than omitted.
2. Gap evidence is embedded per Evidence Object rather than issued as
   separate gap marker objects.

Validators not informed of these departures will produce hash
mismatches on nullable fields and must not be treated as indicating
evidence tampering.
