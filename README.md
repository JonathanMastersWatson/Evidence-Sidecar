# Evidence Sidecar Reference Architecture

This repository defines a **reference architecture for independent, fail-open evidence systems**.

It specifies how complex digital systems can produce verifiable, court-defensible
evidence of what occurred — **without interrupting execution, exposing sensitive
data, or concentrating authority**.

This is not a product.  
This is not a platform.  
This is not a service.

It is an architectural constraint set.

---

## What This Is

This repository defines an architectural pattern known as an **evidence sidecar**.

An evidence sidecar is an external witness that:

- observes system events out-of-band,
- records cryptographic evidence,
- preserves time ordering and detectability of gaps,
- and anchors proof to a neutral public settlement layer.

The sidecar does not execute logic.  
It does not enforce policy.  
It does not decide outcomes.

It witnesses.

---

## What This Is Not

This repository does **not** define:

- a commercial offering
- a hosted service
- an SDK or API
- a certification or compliance badge
- an enforcement or governance system
- a truth or correctness engine

Commercial implementations may exist elsewhere.  
They are explicitly out of scope here.

---

## Core Principles

All compliant implementations must satisfy these non-negotiable constraints:

- **Fail-Open**  
  Evidence systems must never block, delay, or interrupt execution.

- **Witness-Only**  
  The sidecar may observe and record, but never act, decide, or enforce.

- **Voluntary Participation**  
  Adoption is opt-in. Consequences are emergent, not mandated.

- **Authority Limits**  
  No hidden, delegated, or implicit power is permitted.

- **Selective Disclosure**  
  Transparency must be precise, bounded, and minimal.

These principles are defined in detail within the repository and are normative.

---

## Architecture Overview

At a high level, the architecture consists of four explicitly separated layers:

1. **Evidence Model**  
   Minimal, immutable Evidence Objects chained cryptographically to preserve
   integrity, ordering, and detectable gaps.

2. **Disclosure Kernel**  
   A constrained mechanism for scoped, proportional evidence release without
   over-exposure.

3. **Settlement Layer**  
   A neutral public ledger used solely for anchoring cryptographic receipts
   proving existence at a point in time.

4. **Commercial Layer**  
   A funding mechanism that pays for settlement without influencing evidence
   generation, disclosure, or verification.

Each layer is isolated to prevent authority bleed.

---

## Settlement and Ledgers

This architecture requires a settlement layer with:

- deterministic finality,
- predictable and bounded cost,
- public verifiability,
- and no execution-layer coupling.

At present, the XRP Ledger satisfies these requirements and is profiled in this
repository.

An illustrative alternative ledger profile is included to demonstrate ledger
interchangeability.

The architecture is ledger-agnostic by design.

---

## Who This Is For

Different audiences should start in different places:

- **Executives & General Readers**  
  → `public/EXECUTIVE_SUMMARY.md`

- **CFOs & Risk Committees**  
  → `public/CFO_BRIEF.md`

- **Regulators & Auditors**  
  → `public/REGULATOR_NOTE.md`

- **Technology Vendors**  
  → `public/VENDOR_SUPPLY_NOTE.md`

- **Public Service & Government**  
  → `public/PUBLIC_SERVICE_GOVERNMENT_NOTE.md`

Engineers and architects should read the repository in order, starting with
`00_INTENT`.

---

## Industry Applicability

This architecture applies wherever:

- outcomes are disputed after the fact,
- internal logs are not trusted,
- execution cannot be interrupted,
- and liability attaches retroactively.

Illustrative industry mappings include:

- broadcast and digital media
- financial markets
- AI systems
- supply chains
- public sector systems

Mappings are illustrative, not exhaustive.

---

## Normative and Guidance Documents

This repository includes several cross-cutting documents that apply to the
architecture as a whole.

These documents are not tied to a single layer and should be read alongside the
core specification.

### Normative

- `CONFORMANCE.md`  
  Defines the minimum behavioral requirements for an implementation to be
  considered conformant with this architecture.

- `INTEROPERABILITY.md`  
  Defines how independent implementations verify, exchange, and validate
  evidence without shared control or coordination.

### Non-Normative Guidance

- `ADOPTION.md`  
  Describes a low-risk, incremental path for organizations to adopt the
  architecture without disrupting existing systems.

- `CRYPTOGRAPHY.md`  
  Describes cryptographic minimum properties and implementation considerations.
  It does not mandate specific algorithms.

Normative documents use MUST / MUST NOT language.  
Guidance documents are informational only.

---

## Legal and Regulatory Posture

This repository provides **technical architecture**, not legal advice.

It does not guarantee evidentiary admissibility in any jurisdiction.

Its purpose is to make evidence **stronger, more independent, and more
defensible** — not to replace legal judgment, regulatory authority, or due
process.

---

## Adoption Philosophy

This architecture is designed to spread quietly.

No mandate is required.  
No authority is asserted.

Systems that adopt independent witnesses gain defensibility.  
Systems that do not remain operational — but increasingly indefensible.

---

## Relationship to 512

This work is **compatible with**, but **independent of**, the 512 constraint
kernel.

512 defines high-level invariants around voluntariness, transparency,
contestability, and authority limits.

This repository defines one possible realization of those constraints: the
production of independent, fail-open evidence.

Neither governs the other.

---

## Status

This repository is intentionally complete.

Future changes should be additive, restrained, and justified by real-world
failure modes.

Complexity is not a feature.

---

## Final Note

Trust is no longer established at runtime.

It is established **after the fact**, under scrutiny.

This architecture exists for that moment.
