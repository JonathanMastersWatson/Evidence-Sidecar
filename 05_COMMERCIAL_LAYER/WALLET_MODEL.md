# Wallet Model

This document defines the wallet model used to fund settlement
within the Cryptographic Verification Sidecar (CVS) specification.

The canonical CVS specification is defined by:

- `CVS_ARCHITECTURE_v2.7.md`
- `CVS_IMPLEMENTATION_v2.2.md`

If conflict exists, the canonical specification governs.

The wallet funds settlement anchoring.
It does not own, modify, or influence evidence.

---

## Purpose

The wallet model exists to:

- fund ledger settlement operations,
- attribute settlement costs,
- produce auditable financial records.

It does not participate in:

- evidence generation,
- verification,
- disclosure decisions,
- interpretation.

---

## Separation of Concerns

The wallet MUST remain structurally separated from:

- the witness engine,
- the Disclosure Kernel,
- the Evidence Model.

Economic mechanisms MUST NOT alter evidence integrity.

---

## Funding Directionality

Settlement funding flows:

- from the party choosing to anchor evidence,
- toward the public settlement layer.

Payment MUST NOT grant influence over:

- evidence generation,
- observation scope,
- disclosure semantics.

---

## Uniform Evidence Production

The wallet model MUST NOT enable:

- selective observation based on payment,
- tiered evidence integrity,
- outcome-based settlement incentives.

Evidence production remains structurally uniform.

---

## Pre-Funding

Settlement wallets MAY be pre-funded to ensure:

- uninterrupted anchoring,
- predictable operating cost,
- bounded financial exposure.

Pre-funding MUST NOT condition evidence generation.

---

## Deferred Funding

If settlement funds are temporarily unavailable:

- evidence generation MUST continue,
- settlement MAY be deferred,
- funding delay MUST be observable.

Financial state MUST NOT determine evidentiary state.

---

## Cost Attribution

The wallet SHOULD support deterministic attribution of settlement cost to:

- systems,
- streams,
- customers,
- organizational units.

Attribution rules MUST be auditable.

---

## Transparency of Charges

Settlement charges SHOULD be:

- visible,
- itemized,
- verifiable.

Opaque charging mechanisms reduce accountability.

---

## No Custodial Role

The wallet:

- does not custody assets for third parties,
- does not act as a financial intermediary,
- does not provide investment services.

It exists solely to fund anchoring operations.

---

## Regulatory Scope

Implementations using a wallet model:

- remain subject to applicable financial regulations,
- must comply with relevant jurisdictional requirements.

The CVS specification does not alter regulatory obligations.

---

## Scope Limitation

The wallet model:

- does not define revenue strategy,
- does not mandate pricing models,
- does not guarantee economic performance.

It defines structural funding boundaries only.

---

## Summary

The wallet funds settlement.

Funding must remain independent from evidence integrity.

Economic flow surrounds the architecture —
it does not control it.
