# CVS — Cryptographic Verification Sidecar

Licensed under the Apache License, Version 2.0.
See `LICENSE` and `LEGAL_NOTICE.md` for details.

---

This repository defines a **reference architecture for independent,
fail-open evidence systems**.

It specifies how complex digital systems can produce verifiable,
independently defensible evidence of what occurred — without
interrupting execution, exposing sensitive data, or concentrating
authority.

This is not a product.
This is not a platform.
This is not a service.

It is an architectural specification.

> **Pre-hardening phase in progress.** Language and normative framework
> are being tightened. See [`PRE_HARDENING_NOTICE.md`](./PRE_HARDENING_NOTICE.md).

---

## Canonical Specification

The canonical CVS specification is defined exclusively by the
documents in `/08_CANON/`:

- `/08_CANON/CVS_ARCHITECTURE_v{M}.{m}.md` — current canonical version
- `/08_CANON/CVS_IMPLEMENTATION_v{M}.{m}.md` — current canonical version

Cryptographic fingerprints of these files are recorded in:

- `/08_CANON/CANON_HASHES.md`

If any conflict exists between documents in this repository,
the files in `/08_CANON/` take precedence.

Version numbers are immutable. Canonical documents must not be
silently modified. Subsequent revisions must increment version numbers.

---

## What CVS Is

A CVS is an external witness that:

- observes system events out-of-band
- records cryptographic evidence
- preserves time ordering and detectability of gaps
- anchors proof to a neutral public settlement layer

The sidecar does not execute logic.
It does not enforce policy.
It does not decide outcomes.

It witnesses.

---

## What CVS Is Not

This repository does not define:

- a commercial offering
- a hosted service
- an SDK or API
- a certification or conformance badge
- an enforcement or governance system
- a truth or correctness engine
- an access control system
- a monitoring or logging tool

Commercial implementations may exist elsewhere.
They are explicitly out of scope here.

---

## Core Properties

A CVS-Conforming implementation satisfies these non-negotiable
constraints:

- **Fail-Open** — evidence systems must never block, delay, or
  interrupt execution

- **Witness-Only** — the sidecar may observe and record, but never
  act, decide, or enforce

- **Authority Limits** — no hidden, delegated, or implicit power
  is permitted

- **Selective Disclosure** — transparency must be precise, bounded,
  and minimal

- **Independent Verification** — verification must be possible
  without trusting the operator

These properties are defined in detail within the repository
and are normative.

---

## Architecture Overview

The architecture consists of four explicitly separated layers:

1. **Evidence Model**
   Minimal, immutable Evidence Objects chained cryptographically
   to preserve integrity, ordering, and detectable gaps.

2. **Disclosure Kernel**
   A proof minimisation mechanism for scoped evidence release
   without over-exposure. Not an access control system.

3. **Settlement Layer**
   A neutral public ledger used solely for anchoring cryptographic
   receipts proving existence at a point in time.

4. **Commercial Layer**
   A funding mechanism that pays for settlement without influencing
   evidence generation, disclosure, or verification.

Each layer is isolated to prevent authority bleed.

---

## Settlement and Ledgers

This architecture requires a settlement layer with:

- deterministic finality
- predictable and bounded cost
- public verifiability
- no execution-layer coupling

The XRP Ledger satisfies these requirements and is profiled in
this repository. An alternative ledger profile is included to
demonstrate ledger interchangeability.

The architecture is ledger-agnostic by design.

---

## Who This Is For

| Audience | Start here |
|---|---|
| Executives & General Readers | `public/EXECUTIVE_SUMMARY.md` |
| CFOs & Risk Committees | `public/CFO_BRIEF.md` |
| Regulators & Auditors | `public/REGULATOR_NOTE.md` |
| Technology Vendors | `public/VENDOR_SUPPLY_NOTE.md` |
| Public Service & Government | `public/PUBLIC_SERVICE_GOVERNMENT_NOTE.md` |
| Engineers & Architects | Start with `00_INTENT/`, read in order |

---

## Industry Applicability

This architecture applies wherever:

- outcomes are disputed after the fact
- internal logs are not trusted
- execution cannot be interrupted
- liability attaches retroactively

Illustrative industry mappings: broadcast and digital media,
financial markets, AI systems, supply chains, public sector systems.

Mappings are illustrative, not exhaustive.

---

## Normative Documents

The following documents are normative and apply to the architecture
as a whole:

- `CONFORMANCE.md` — minimum behavioral requirements for a
  CVS-Conforming implementation; includes operational states,
  binary test checklist, and non-conformant patterns

- `ANTI_DRIFT.md` — non-negotiable architectural boundaries;
  layer separation, fixed observation model, prohibited configurations

- `VERIFICATION_PROTOCOL.md` — canonical six-step verification
  protocol for auditors, regulators, and independent reviewers

- `INTEROPERABILITY.md` — how independent implementations verify,
  exchange, and validate evidence without shared control

---

## Guidance Documents

The following documents are informational only:

- `ADOPTION.md` — incremental path for organisations to introduce
  the architecture without disrupting existing systems

- `CRYPTOGRAPHY.md` — cryptographic minimum properties and
  implementation considerations; does not mandate specific algorithms

Normative documents use MUST / MUST NOT language.
Guidance documents are informational only.

---

## Legal and Regulatory Posture

This repository provides technical architecture, not legal advice.

It does not guarantee evidentiary admissibility in any jurisdiction.

Its purpose is to make evidence stronger, more independent, and more
defensible — not to replace legal judgment, regulatory authority,
or due process.

See `LEGAL_NOTICE.md` for limitation of responsibility,
Apache 2.0 attribution, and open commons declaration.

---

## Relationship to 512

CVS is compatible with, but independent of, the 512 constraint set.

512 defines discovered constraints governing execution-time legitimacy.
CVS defines one witness architecture that can operate alongside
systems satisfying 512's properties.

Neither governs the other.
CVS may operate without 512. Systems satisfying 512's properties
may use witness architectures other than CVS.

---

## Status

This repository is intentionally complete.

Future changes should be additive, restrained, and justified by
real-world failure modes.

Complexity is not a feature.

See `PRE_HARDENING_NOTICE.md` for current hardening phase status.

---

## Reference

- `PRIMITIVE_BOUNDARY.md` — what CVS defines and what it does not;
  derivative responsibility
- `UPSTREAM.md` — three-layer stack (Constraint Architecture / 512 /
  CVS) and upstream constraint definition responsibility
- `02_EVIDENCE_MODEL/GATE_OUTPUT_MATRIX.md` — gate completion states
  and witness classification matrix
- `LIVING_DOCUMENTS.md` — which documents are dynamic and subject
  to revision
- `PRE_HARDENING_NOTICE.md` — current hardening phase status

---

## Final Note

Trust is no longer established at runtime.

It is established after the fact, under scrutiny.

This architecture exists for that moment.
