# Finality and Receipts

This document defines the meaning of settlement finality and the role of ledger receipts within the evidence sidecar architecture.

Finality provides proof of existence, not proof of correctness.

---

## Purpose

Settlement finality exists to:

- establish that evidence existed at a given point in time,
- anchor evidence beyond local control,
- and enable independent verification.

It does not validate behavior or outcomes.

---

## Definition of Finality

Finality is achieved when:

- a cryptographic commitment is accepted by the settlement ledger,
- the transaction is confirmed under deterministic rules,
- and the confirmation is publicly verifiable.

Once final, the receipt is immutable.

---

## What Finality Proves

Ledger finality proves that:

- a specific cryptographic commitment existed,
- no later than the settlement time,
- and was recorded publicly.

It proves nothing about:
- the meaning of the evidence,
- the correctness of events,
- or the legitimacy of outcomes.

---

## Receipts

A receipt consists of:

- the settlement transaction identifier,
- the ledger-provided timestamp,
- and the committed cryptographic value.

Receipts are compact, durable, and verifiable.

---

## Receipt Binding

Receipts must be bound to:

- specific evidence batches,
- defined hash chains,
- and disclosed batching rules.

This binding enables verification of inclusion.

---

## Independence from Execution

Receipt generation must be:

- asynchronous,
- decoupled from execution,
- and fail-open.

Settlement delays do not affect system behavior.

---

## Deferred and Retroactive Settlement

Evidence may be settled after observation.

Deferred settlement must:

- preserve original observation time,
- record settlement delay,
- and maintain chain integrity.

Retroactive settlement does not weaken evidence, provided delays are disclosed.

---

## Verification Workflow

An independent verifier must be able to:

1. retrieve the receipt from the ledger,
2. recompute the cryptographic commitment,
3. confirm inclusion and finality,
4. trace the commitment to disclosed evidence.

Verification must not require trust in the operator.

---

## Multiple Receipts

Evidence chains may be anchored:

- multiple times,
- at different intervals,
- or to multiple ledgers.

Multiple receipts strengthen resilience but do not alter semantics.

---

## Non-Goals

Finality does not:

- enforce compliance,
- assign blame,
- or certify correctness.

It records that something existed, not that it was right.

---

## Summary

Finality closes the window for silent alteration.

Receipts transform local evidence into public fact.

They witness existence — nothing more.
