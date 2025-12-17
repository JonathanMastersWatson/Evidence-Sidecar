# Alternative Ledger Profile (Non-Exclusive)

At present, the XRP Ledger satisfies these requirements and is profiled in this repository.

An illustrative alternative ledger profile is included to demonstrate ledger interchangeability.

The architecture remains ledger-agnostic.

This document describes a **generic alternative settlement ledger profile** that satisfies the requirements defined in `LEDGER_REQUIREMENTS.md`.

It exists to demonstrate that the evidence sidecar architecture is **ledger-agnostic by design**, and that no single ledger is required or privileged.

This profile is illustrative, not prescriptive.

---

## Purpose

The purpose of this profile is to:

- reinforce vendor neutrality,
- reduce perception of ecosystem lock-in,
- and clarify that settlement is a replaceable component.

The architecture constrains *properties*, not platforms.

---

## Qualification Criteria

An alternative ledger qualifies for use as an evidence settlement layer if it satisfies **all** mandatory requirements defined in:

> `04_SETTLEMENT_LAYER/LEDGER_REQUIREMENTS.md`

These requirements are non-negotiable.

---

## Hypothetical Ledger Characteristics

A qualifying alternative ledger would exhibit the following properties:

### Deterministic Finality

- Transactions achieve finality within a bounded time window.
- Finality is irreversible once reached.
- No probabilistic reorganization is possible.

---

### Predictable and Bounded Cost

- Transaction fees are low and stable.
- Fees are not determined by auction mechanisms.
- Cost variability under load is bounded and observable.

---

### Public Verifiability

- Ledger state is publicly readable.
- Transaction inclusion can be independently verified.
- No permission is required to audit transactions.

---

### Minimal Execution Surface

- The ledger does not require smart contract execution.
- No application logic is embedded in settlement.
- Only cryptographic commitments are recorded.

---

### Payload Minimization

- Payload data is never stored on-ledger.
- Only compact commitments (e.g. hashes, Merkle roots) are permitted.
- Sensitive or proprietary data is excluded by design.

---

### Governance Predictability

- Ledger governance rules are transparent.
- No discretionary transaction censorship is permitted.
- No centralized actor can arbitrarily reverse transactions.

---

## Example Candidates (Non-Endorsing)

Examples of ledger designs that *could* satisfy these constraints include:

- deterministic BFT-based ledgers,
- permissionless append-only log systems with finality,
- or future public notary-style networks designed for receipts.

Mention of examples does not constitute endorsement.

---

## Interchangeability

Settlement ledgers are interchangeable within this architecture provided they satisfy all required properties.

Switching settlement layers must not require:

- changes to evidence objects,
- changes to disclosure semantics,
- or changes to witness authority boundaries.

Only settlement receipts differ.

---

## Non-Goals

This profile does not:

- rank alternative ledgers,
- evaluate ecosystems,
- or predict future adoption.

Ledger competition occurs outside this architecture.

---

## Summary

The settlement layer is a notary, not a platform.

Any ledger that behaves predictably, verifiably, and neutrally can fulfill this role.

No ledger is intrinsic to the architecture.
