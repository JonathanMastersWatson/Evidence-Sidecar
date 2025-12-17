# Ledger Requirements

This document defines the technical and operational requirements for any distributed ledger used as a **public settlement and receipt layer** for evidence produced by a compliant sidecar.

The ledger exists solely to provide independent, verifiable anchoring of evidence integrity.

It does not execute logic, store payloads, or confer authority.

---

## Purpose of the Settlement Layer

The settlement layer exists to:

- provide a public, neutral point of reference,
- anchor evidence chains beyond local control,
- enable third-party verification,
- and make tampering or retroactive alteration detectable.

It does not participate in execution or interpretation.

---

## Required Ledger Properties

Any ledger used for settlement **must** satisfy all of the following properties.

Failure to satisfy any requirement disqualifies the ledger.

---

### 1. Deterministic Finality

The ledger must provide deterministic finality.

This means:

- transactions, once confirmed, are final,
- no probabilistic reorganization is possible,
- and confirmation semantics are clear and consistent.

Probabilistic finality is insufficient for legal and regulatory evidence.

---

### 2. Predictable Settlement Cost

Settlement cost must be:

- low,
- stable,
- and predictable over time.

Evidence systems cannot tolerate:

- fee auctions,
- congestion-driven price spikes,
- or adversarial transaction ordering.

Unbounded or volatile costs undermine reliability.

---

### 3. Public Verifiability

The ledger must be:

- publicly accessible,
- independently verifiable,
- and not controlled by a single operator.

Verification must not require permission.

---

### 4. Minimal Latency for Receipt

The ledger must support:

- near-immediate transaction acceptance,
- bounded confirmation time,
- and rapid receipt availability.

Settlement latency affects evidence freshness but must not block execution.

---

### 5. No Execution Dependency

The ledger must not:

- execute application logic,
- enforce policy,
- or affect system behavior.

It exists purely as a receipt layer.

---

### 6. No Payload Storage Requirement

The ledger must not require:

- storage of payload data,
- storage of content,
- or storage of sensitive information.

Only compact cryptographic commitments may be recorded.

---

### 7. Resistance to Manipulation

The ledger must resist:

- transaction censorship,
- reordering attacks,
- front-running,
- or economic manipulation.

Evidence anchoring must not be gamed.

---

### 8. Legal Clarity

The ledger must have:

- a clear legal posture,
- predictable jurisdictional interpretation,
- and no ambiguous governance controls.

Opaque or discretionary governance undermines evidentiary value.

---

## Settlement Frequency

Evidence chains may be settled:

- periodically,
- in batches,
- or on defined intervals.

Settlement frequency must be:

- configurable,
- disclosed,
- and independent of execution paths.

---

## Anchoring Semantics

Ledger anchoring must record:

- cryptographic commitments (e.g. Merkle roots),
- timestamps provided by the ledger,
- and transaction identifiers.

Anchoring does not validate correctness — only existence.

---

## Disallowed Ledger Characteristics

The following characteristics are incompatible with this architecture:

- probabilistic finality
- volatile fee markets
- opaque governance
- smart-contract dependency
- payload storage requirements
- execution-layer coupling

---

## Ledger Neutrality

This repository does not promote or endorse ideologies, assets, or ecosystems.

Ledger selection is constrained by technical properties alone.

Any ledger meeting these requirements may be used.

---

## Summary

The settlement layer is a notary, not a computer.

It provides receipts, not execution.

If a ledger cannot behave predictably, it cannot anchor evidence.
