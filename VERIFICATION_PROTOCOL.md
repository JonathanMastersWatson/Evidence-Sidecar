# Verification Protocol

This document defines the canonical steps for third-party verification
of CVS evidence records.

It is written for verifiers — auditors, regulators, counterparties,
and independent reviewers — who need to confirm the integrity of
evidence produced by a CVS-Conforming implementation.

Verification requires no operator cooperation.
Verification requires no privileged access.
Verification requires no trust in the system being verified.

---

## What Verification Proves

Successful completion of this protocol proves:

1. The evidence record has not been tampered with since capture
2. The evidence was produced against a specific, identified constraint
   specification
3. The execution events occurred in the recorded order
4. Any gaps in the evidence record are detectable and located
5. Specific claims about execution can be confirmed without exposing
   the full record

Verification does not prove:

- That the constraint specification was correct or complete
- That the execution outcomes were desirable or lawful
- That the system behaved correctly in a moral or regulatory sense

Those determinations are upstream of verification and outside CVS scope.

---

## Prerequisites

Before beginning verification, obtain:

- The evidence record or the specific Evidence Objects to be verified
- The claimed constraint specification (to verify spec hash binding)
- The public ledger anchor reference (transaction ID or equivalent)
- The root hash of the Merkle batch containing the objects in scope

All of these MUST be obtainable without operator cooperation.
If any cannot be obtained independently, record this as a finding.

---

## Step 1 — Hash Chain Integrity

**Purpose:** Confirm the evidence record has not been tampered with.

**Method:**

1. Take the first Evidence Object in the chain
2. Compute its hash independently
3. Confirm the hash matches the recorded value
4. Take the next Evidence Object
5. Confirm its hash preimage includes the previous object's hash
6. Repeat for the full chain in scope

**Pass condition:** Every hash in the chain is independently reproducible
and each object correctly references its predecessor.

**Fail condition:** Any hash mismatch, any broken chain link, or any
object that does not reference its predecessor.

**What a gap looks like:** A missing sequence number or a chain link
that references a hash not present in the record. Gaps are findings,
not failures of the verification protocol. Record their location
and scope.

---

## Step 2 — Spec Hash Verification

**Purpose:** Confirm evidence was produced against the claimed
constraint specification.

**Method:**

1. Obtain the constraint specification claimed to be in force
2. Hash it independently using SHA-256
3. Compare the result to the spec hash embedded in each Evidence Object
   in scope

**Pass condition:** The independently computed hash matches the spec
hash in every Evidence Object examined.

**Fail condition:** Any mismatch between the independently computed
hash and the embedded spec hash.

**Note on divergence events:** If the chain contains a spec hash
binding event (indicating a constraint specification change), verify
both the pre-divergence and post-divergence spec hashes independently.
Evidence Objects on each side of the divergence event should match
their respective spec hashes.

---

## Step 3 — Ledger Anchor Confirmation

**Purpose:** Confirm the evidence existed before any dispute arose.

**Method:**

1. Obtain the ledger anchor reference from the evidence record
2. Look up the transaction on the public ledger using any public node
3. Extract the Merkle root from the transaction memo or payload
4. Confirm the Merkle root matches the root hash of the batch
   containing the Evidence Objects in scope

**Pass condition:** The Merkle root on the public ledger matches
the batch root hash. The ledger transaction timestamp predates
any claimed dispute or incident.

**Fail condition:** The Merkle root does not match, the transaction
does not exist, or the timestamp postdates the dispute.

**No operator cooperation required:** Public ledger transactions
are readable by any party using any public node or explorer.

---

## Step 4 — Merkle Inclusion Proof

**Purpose:** Confirm a specific Evidence Object is included in
the anchored batch without requiring the full batch.

**Method:**

1. Obtain the Merkle inclusion proof for the Evidence Object in scope
2. Compute the object's hash independently
3. Walk the Merkle path from the object hash to the root
4. Confirm the computed root matches the anchored Merkle root

**Pass condition:** The computed root matches the anchored root.

**Fail condition:** Any step in the Merkle path fails to produce
the expected parent hash.

**This step enables scoped verification:** A verifier can confirm
a single Evidence Object is part of an anchored batch without
receiving or processing the full batch.

---

## Step 5 — Proof Object Sufficiency

**Purpose:** Confirm each Evidence Object in scope is self-contained
and answers the four required questions.

**For each Evidence Object, confirm it contains:**

| Element | Question Answered | Present? |
|---|---|---|
| Intent hash | What was proposed? | ✓ / ✗ |
| Spec hash | What rules were active? | ✓ / ✗ |
| Decision record | What decision was made, per invariant? | ✓ / ✗ |
| Execution outcome | What occurred? | ✓ / ✗ |

**Pass condition:** All four elements present and independently
verifiable in every Evidence Object examined.

**Fail condition:** Any element missing, any element requiring
external context to interpret.

---

## Step 6 — Gap Assessment

**Purpose:** Confirm the completeness of the evidence record
over the period in scope.

**Method:**

1. Identify the expected sequence of execution events over
   the period in scope
2. Walk the evidence chain for the same period
3. Identify any missing sequence positions or broken chain links

**Pass condition:** The evidence chain is continuous over the
period in scope with no unaccounted gaps.

**Fail condition:** Gaps exist that are not accompanied by
an explicit gap declaration in the evidence chain.

**Note:** A gap accompanied by an explicit declaration is a
declared degraded mode event — this is conformant behavior.
A gap with no declaration is a coverage failure and is a material finding.

---

## Verification Summary Record

On completion, a verifier SHOULD produce a summary record containing:

| Field | Value |
|---|---|
| Verification date | |
| Evidence period in scope | |
| Objects examined | |
| Spec hash verified against | |
| Ledger anchor reference | |
| Hash chain result | Pass / Fail / Gaps found |
| Spec hash binding result | Pass / Fail |
| Ledger anchor result | Pass / Fail |
| Merkle inclusion result | Pass / Fail |
| Proof Object sufficiency result | Pass / Fail |
| Gap assessment result | Pass / Gaps declared / Gaps undeclared |
| Overall finding | Verified / Not verified / Partial |

This record is produced by the verifier.
It is not produced by the system being verified.

---

## Relationship to Other Documents

- `CONFORMANCE.md` — tests 6.1 and 6.2 govern independent verification
- `02_EVIDENCE_MODEL/SPEC_HASH_BINDING.md` — spec hash lifecycle
- `02_EVIDENCE_MODEL/HASH_CHAINING.md` — chain integrity requirements
- `02_EVIDENCE_MODEL/PROOF_OBJECT_INTEGRITY.md` — sufficiency requirements
- `04_SETTLEMENT_LAYER/LEDGER_REQUIREMENTS.md` — ledger anchor requirements

The canonical CVS specification (`CVS_ARCHITECTURE_v2.7.md`) governs
where any conflict exists.
