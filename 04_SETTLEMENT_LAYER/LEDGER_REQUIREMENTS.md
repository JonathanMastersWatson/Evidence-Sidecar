# Ledger Requirements

This document defines the technical and operational requirements
for any distributed ledger used as a public settlement and receipt layer
within the Cryptographic Verification Sidecar (CVS) specification.

The canonical CVS specification is defined by:

- `CVS_ARCHITECTURE_v2.7.md`
- `CVS_IMPLEMENTATION_v2.2.md`

If conflict exists, the canonical specification governs.

This document is normative.

The ledger exists solely to provide independent, verifiable anchoring
of evidence integrity.

It does not execute logic, store payloads, or confer authority.

---

## Purpose of the Settlement Layer

The settlement layer exists to:

- provide a public, neutral reference point,
- anchor evidence chains beyond local control,
- enable third-party verification,
- make tampering or retroactive alteration detectable.

It does not participate in execution or interpretation.

---

## Required Ledger Properties

Any ledger used for CVS settlement MUST satisfy the following properties.

---

### 1. Deterministic Finality

The ledger MUST provide deterministic finality.

This means:

- transactions, once confirmed, are final,
- confirmation semantics are clearly defined,
- historical reorganization is not expected under normal operation.

Probabilistic confirmation models are not sufficient for anchoring integrity guarantees.

---

### 2. Predictable Settlement Cost

Settlement cost MUST be:

- bounded,
- stable over time,
- reasonably predictable.

Evidence anchoring cannot rely on fee auctions,
congestion-driven price spikes,
or unbounded transaction costs.

---

### 3. Public Verifiability

The ledger MUST be:

- publicly accessible,
- independently verifiable,
- not dependent on a single operator for validation.

Verification MUST NOT require privileged access.

---

### 4. Bounded Confirmation Latency

The ledger MUST provide:

- bounded confirmation time,
- reliable receipt generation,
- timely availability of transaction identifiers.

Settlement latency affects freshness,
but MUST NOT block execution.

---

### 5. No Execution Dependency

The ledger MUST NOT:

- execute application logic,
- enforce policy,
- influence system behavior.

It functions strictly as a receipt layer.

---

### 6. No Payload Storage Requirement

The ledger MUST NOT require:

- storage of original payload data,
- storage of content bodies,
- storage of sensitive information.

Only compact cryptographic commitments MAY be recorded.

---

### 7. Resistance to Manipulation

The ledger SHOULD demonstrate resistance to:

- transaction censorship,
- ordering manipulation,
- front-running attacks,
- economic coercion affecting anchoring.

Anchoring reliability depends on structural predictability.

---

### 8. Governance Transparency

The ledger SHOULD provide:

- documented governance processes,
- predictable rule evolution,
- observable consensus rules.

Opaque discretionary control weakens anchoring neutrality.

---

## Settlement Frequency

Evidence chains MAY be settled:

- periodically,
- in batches,
- at defined intervals.

Settlement frequency MUST be:

- configurable,
- disclosed,
- independent of execution paths.

---

## Anchoring Semantics

Ledger anchoring MUST record:

- cryptographic commitments (e.g., Merkle roots),
- ledger-provided timestamps,
- transaction identifiers.

Anchoring proves existence at a point in time.
It does not validate correctness or meaning.

---

## Ledger Neutrality

CVS does not mandate any specific ledger.

Ledger selection is constrained by technical properties.

Any ledger meeting these requirements MAY be used.

---

## Scope Limitation

Ledger requirements:

- do not determine legal admissibility,
- do not define regulatory sufficiency,
- do not establish governance policy.

They define structural anchoring properties only.

---

## Summary

The settlement layer functions as a notary.

It provides timestamped receipts for cryptographic commitments.

If a ledger cannot behave predictably,
it cannot reliably anchor evidence.
