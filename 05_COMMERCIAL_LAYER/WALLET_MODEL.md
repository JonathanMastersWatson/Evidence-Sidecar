# Wallet Model

This document defines the wallet model used to fund evidence settlement without granting the commercial layer authority over evidence generation or disclosure.

The wallet exists to pay for settlement.  
It does not own evidence.

---

## Purpose

The wallet model exists to:

- fund ledger settlement operations,
- attribute settlement costs,
- and produce auditable financial records.

It does not participate in evidence generation, verification, or interpretation.

---

## Separation of Concerns

The wallet must be strictly separated from:

- the witness engine,
- the disclosure kernel,
- and the evidence model.

This separation ensures that economic incentives do not distort evidence integrity.

---

## Funding Directionality

Settlement funding flows in one direction only:

- from the party choosing to produce evidence,
- toward the public settlement layer.

No downstream party may influence evidence generation through payment.

---

## No Pay-to-Observe

The wallet must not enable:

- selective observation based on payment,
- differential evidence quality tiers,
- or outcome-based settlement incentives.

Evidence is produced uniformly.

---

## Pre-Funding Model

Settlement wallets may be pre-funded to ensure:

- uninterrupted settlement,
- predictable operating costs,
- and bounded financial exposure.

Pre-funding must not block evidence generation.

---

## Deferred Payment Handling

If settlement funds are temporarily unavailable:

- evidence generation must continue,
- settlement may be deferred,
- and the funding gap must be observable.

Financial failure must not cause evidence failure.

---

## Cost Attribution

The wallet must support attribution of settlement costs to:

- systems,
- streams,
- customers,
- or organizational units.

Attribution rules must be deterministic and auditable.

---

## Transparency of Charges

Settlement charges must be:

- visible,
- itemized,
- and verifiable.

Opaque pricing models undermine trust.

---

## No Asset Custody Claims

The wallet does not:

- custody assets for others,
- act as a financial intermediary,
- or provide investment services.

It is a funding mechanism only.

---

## Regulatory Posture

The wallet model is designed to:

- minimize regulatory surface area,
- avoid commingling of funds,
- and remain subordinate to existing financial controls.

Implementations must comply with applicable financial regulations.

---

## Summary

The wallet pays for witnessing.

It does not buy truth, influence evidence, or control disclosure.

Money flows around the system — never through it.
