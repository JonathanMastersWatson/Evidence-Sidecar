# Finality and Receipts

This document defines the meaning of settlement finality
and the role of ledger receipts within the
Cryptographic Verification Sidecar (CVS) specification.

The canonical CVS specification is defined by:

- `CVS_ARCHITECTURE_v2.7.md`
- `CVS_IMPLEMENTATION_v2.2.md`

If conflict exists, the canonical specification governs.

This document is normative.

Finality provides proof of existence,
not proof of correctness.

---

## Purpose

Settlement finality exists to:

- establish that a cryptographic commitment existed at a given time,
- anchor evidence beyond local control,
- enable independent verification.

It does not validate behavior or outcomes.

---

## Definition of Finality

Finality is achieved when:

- a cryptographic commitment is accepted by the settlement ledger,
- the transaction is confirmed under deterministic consensus rules,
- the confirmation is publicly verifiable.

Once confirmed under the ledger’s finality model,
the receipt is treated as immutable.

---

## What Finality Proves

Ledger finality proves that:

- a specific cryptographic commitment existed,
- no later than the settlement timestamp,
- and was recorded publicly.

It does not prove:

- semantic meaning of the evidence,
- correctness of events,
- legitimacy of outcomes,
- intent or compliance.

---

## Receipts

A receipt consists of:

- the settlement transaction identifier,
- the ledger-provided timestamp,
- the committed cryptographic value.

Receipts MUST be sufficient for independent retrieval and verification.

---

## Receipt Binding

Receipts MUST be bound to:

- specific evidence batches or commitments,
- defined hash chains,
- disclosed batching rules.

This binding enables inclusion verification.

---

## Independence from Execution

Receipt generation MUST be:

- asynchronous,
- decoupled from execution,
- fail-open.

Settlement delay MUST NOT alter execution behavior.

---

## Deferred Settlement

Evidence MAY be settled after observation.

Deferred settlement MUST:

- preserve original observation time,
- record settlement delay,
- maintain chain integrity.

Delay affects freshness, not structural validity.

---

## Verification Workflow

An independent verifier MUST be able to:

1. retrieve the receipt from the ledger,
2. recompute the cryptographic commitment,
3. confirm inclusion and finality,
4. trace the commitment to disclosed evidence.

Verification MUST NOT require privileged access to the operator.

---

## Multiple Receipts

Evidence chains MAY be anchored:

- multiple times,
- at different intervals,
- to multiple ledgers.

Additional receipts increase resilience but do not alter semantics.

---

## Scope Limitation

Finality:

- does not enforce compliance,
- does not assign responsibility,
- does not certify correctness.

It establishes existence at a point in time.

---

## Summary

Finality constrains retroactive alteration.

Receipts transform local commitments into publicly verifiable records.

They witness existence — and nothing beyond that boundary.
