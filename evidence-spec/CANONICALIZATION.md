# Canonicalization and Hashing Rules

## Purpose

Canonicalization ensures that the same Evidence Object always produces the same hash across runtimes, languages, platforms, and validators.

Evidence that cannot be hashed reproducibly is not CVS-EBI conformant.

---

## Serialization Rules

Evidence Objects must be serialized using canonical JSON.

Required rules:

1. UTF-8 encoding only.
2. Lexicographic ordering of object keys.
3. No insignificant whitespace.
4. No comments.
5. Explicit `null` values for nullable fields.
6. Strings must be normalized before serialization.
7. Numbers, if ever introduced, must use canonical decimal representation.
8. Arrays, if ever introduced, must preserve declared order.

---

## Hash Input Rule

To calculate `evidence_hash`:

1. Construct the full Evidence Object.
2. Set `integrity.evidence_hash` to `null`.
3. Canonically serialize the object.
4. Hash the serialized bytes using the declared `hash_algorithm`.
5. Insert the resulting digest into `integrity.evidence_hash`.

---

## Hash Output Format

Hash values should be represented as lowercase hexadecimal strings unless a profile explicitly defines another encoding.

Recommended default:

```text
sha256:<lowercase_hex_digest>
```

---

## Proposal Hash

`proposal_hash` must be calculated from the exact proposal payload evaluated by the boundary.

The witness must not normalize, enrich, or reinterpret the proposal payload.

---

## Decision Hash

`decision_hash` must be calculated from the exact decision payload emitted by the boundary.

The decision payload must include, at minimum:

- decision id
- proposal id
- decision value
- invariant id
- invariant result
- specification hash

---

## Specification Hash

`specification_hash` binds the observed decision to the specification active at the boundary when the decision occurred.

The witness records the specification hash supplied by the boundary.

The witness does not calculate admissibility.

---

## Merkle Leaf Hash

The default Merkle leaf construction is:

```text
merkle_leaf_hash = hash(evidence_hash)
```

A profile may include domain separation:

```text
merkle_leaf_hash = hash("CVS-EBI-MERKLE-LEAF" || evidence_hash)
```

If domain separation is used, it must be declared in the validation profile.

---

## Previous Evidence Hash

`previous_evidence_hash` is used for witness-chain continuity.

Rules:

- First evidence object in a chain must set this field to `null`.
- Subsequent evidence objects should reference the prior object's `evidence_hash`.
- A mismatch creates witness-layer gap evidence.
- A chain break must not influence gate admissibility.

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

```text
same Evidence Object + same canonicalization rules + same hash algorithm = same evidence_hash
```

If two independent validators cannot reproduce the same hash, the Evidence Object is non-conformant.
