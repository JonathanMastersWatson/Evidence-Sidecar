# CVS_IMPLEMENTATION_v2.7.md
### A Reference Architecture for Evidence Access, Interpretation Interfaces, and Enterprise System Integration

**Jonathan M. Watson**
**May 2026 — Version 2.7**
**github.com/JonathanMastersWatson/Evidence-Sidecar**

*This document is a technical reference architecture, not a deployable product.*
*Its authority derives from constraints, not control.*

---

## §-1. Legal Notice, License, and Limitation of Liability

### §-1.1 Informational Nature

This document is a technical specification and reference implementation guide for the Cryptographic Verification Sidecar (CVS). It is provided for informational, architectural, and implementation reference purposes only.

CVS records cryptographic evidence of observation. It does not certify correctness, compliance, safety, security, legality, underwriting outcomes, dispute resolution success, or fitness for any purpose. No outcome is guaranteed.

Nothing in this document constitutes legal, regulatory, financial, insurance, audit, cybersecurity, or professional advice. Implementers must obtain independent advice appropriate to their jurisdiction and industry.

### §-1.2 No Warranty

To the extent permitted under applicable law, this document and any associated materials are provided "AS IS" and "AS AVAILABLE", without warranties or conditions of any kind, express or implied, including (without limitation) warranties of merchantability, fitness for a particular purpose, non-infringement, regulatory compliance, insurance eligibility, performance, or outcome.

### §-1.3 No Reliance; No Certification; No Endorsement

This document is not a certification, audit report, compliance determination, underwriting instrument, or guarantee of coverage. No regulator, insurer, court, standards body, or institution is represented as having approved, validated, certified, or endorsed CVS or any implementation by virtue of this publication.

Any statement of conformance, compliance, underwriting impact, audit sufficiency, or legal adequacy is the sole responsibility of the implementing party and must be independently demonstrated.

### §-1.4 Limitation of Liability

To the extent permitted under applicable law, the authors, contributors, and publishers shall not be liable for any direct, indirect, incidental, consequential, special, exemplary, or punitive damages, or for any loss of profits, revenue, data, business opportunity, goodwill, or reputational harm arising from use, misuse, inability to use, or reliance upon this document or any implementation derived from it, even if advised of the possibility of such damages.

Where any limitation is held unenforceable, liability is intended to be limited to the minimum extent permitted by law.

### §-1.5 Licensing Posture: 512 Constraint Set vs CVS Specification

**512 (constraint set):** 512 is treated in this work as a discovered constraint category — a set of invariants that a Commit Gate may satisfy. No licence is asserted by the authors over the constraint set itself as an abstract constraint category.

**CVS (specification + reference architecture):** CVS is an invented witness architecture and is released under the Apache License, Version 2.0.

This distinction is about licensing posture and does not create or imply any operational dependency: CVS may witness systems with or without a 512-conformant Commit Gate; and 512-conformant Commit Gates may be witnessed by CVS or by other evidence systems.

### §-1.6 License

This document is licensed under the Apache License, Version 2.0 (the "License"). You may not use this work except in compliance with the License. Unless required by applicable law or agreed to in writing, material distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

The full licence text is included in the repository as `LICENSE` and applies to this document and associated specification materials within the CVS repository unless explicitly stated otherwise.

---


## 0. Normative Relationships

### 0.1 Canonical Document Hierarchy

`CVS_IMPLEMENTATION_v1.4.md` sits within a four-document canonical set. The hierarchy is:

| Document | Audience | Authority |
|---|---|---|
| `512_ARCHITECTURE_v3.4.md` | CTO / Board | Why a witness layer is necessary; the discovered constraint that CVS serves |
| `CVS_ARCHITECTURE_v{M}.{m}.md` | CTO / Board | What CVS is; the full CTO-level model |
| `CVS_IMPLEMENTATION_v{M}.{m}.md` | Engineer | How to build CVS; all Access and Interpretation Plane behaviour |
| `512_IMPLEMENTATION_v{M}.{m}.md` | Engineer | How to build a Commit Gate satisfying 512's invariants |

### 0.2 Normative Dependency: `512_ARCHITECTURE_v3.4.md`

`512_ARCHITECTURE_v3.4.md` is authoritative for the discovered necessity of the **Commit Gate** category (`512_ARCHITECTURE_v3.4 §1`), the seven Lockean invariants that define 512's constraint set (`512_ARCHITECTURE_v3.4 §3`), why a witness layer is operationally necessary alongside any Commit Gate (`512_ARCHITECTURE_v3.4 §5`), and the open licensing model for 512 and CVS (`512_ARCHITECTURE_v3.4 §11`).

`CVS_IMPLEMENTATION` does not redefine these elements. When this document describes CVS witnessing a Commit Gate, the constraint set being witnessed is defined in `512_ARCHITECTURE_v3.4 §3`, not here.

### 0.3 Normative Dependency: `CVS_ARCHITECTURE_v{M}.{m}.md`

`CVS_ARCHITECTURE_v{M}.{m}.md` is authoritative for the following elements, which are referenced but not redefined in this document:

- Evidence Object structure and semantics (`CVS_ARCHITECTURE §2`)
- Witness-only constraint — no execution, no enforcement, no decisioning (`CVS_ARCHITECTURE §3`)
- Fail-open behaviour — zero execution dependency; failure creates detectable gaps (`CVS_ARCHITECTURE §3`)
- Detectable gaps — discontinuities are explicit, never smoothed or reconstructed (`CVS_ARCHITECTURE §4`)
- Independent verification — third parties verify with public receipts and disclosed evidence (`CVS_ARCHITECTURE §5`)
- Selective disclosure via Disclosure Kernel — minimal revelation; refusal is valid (`CVS_ARCHITECTURE §6`)
- Merkle batching and anchoring model (`CVS_ARCHITECTURE §7`)
- Settlement Layer constraints — notary-only; no execution; no governance (`CVS_ARCHITECTURE §8`)
- Ledger-agnostic stance — XRPL used only as example profile (`CVS_ARCHITECTURE §8`)
- Conformance behaviours — mandatory behaviours and disqualifying characteristics (`CVS_ARCHITECTURE §9`)

All `CVS_ARCHITECTURE` invariants remain in force. `CVS_IMPLEMENTATION` extends without modifying.

### 0.4 Paper Series Context

This document is the implementation specification in the CVS architecture series:

| Document | Scope |
|---|---|
| `CVS_ARCHITECTURE_v{M}.{m}.md` | Witness-only capture, Evidence Objects, hash chaining, settlement layer |
| `CVS_IMPLEMENTATION_v{M}.{m}.md` (this document) | Access Plane, Interpretation Plane, enterprise integration, deployment topologies |
| CVS Interoperability Specification | Cross-organisation verification, canonical serialisation, federation directory, portability requirements |

`CVS_ARCHITECTURE` and `CVS_IMPLEMENTATION` define the architecture within an organisation. The Interoperability Specification defines what happens at organisational boundaries.

### 0.5 Non-Redefinition Constraint

No element defined in `512_ARCHITECTURE_v3.4.md` or `CVS_ARCHITECTURE_v{M}.{m}.md` is redefined here. If a conflict appears to exist between this document and a normatively superior document, the normatively superior document governs. Discrepancies must be reported as implementation errata.

### 0.6 Deployment Responsibility

Operators assume full responsibility for all deployment decisions and their consequences. This includes but is not limited to:

- Evidence storage configuration, retention policy, and physical or cloud security
- Key custody, HSM provisioning, and attestation key lifecycle management
- Anchoring configuration — ledger selection, batch window, retry policy, and wallet provisioning
- Jurisdictional compliance analysis and applicable legal advice
- Representations made to regulators, insurers, courts, or counterparties on the basis of evidence produced by the deployment
- Coverage completeness and the accuracy of the Declared Observation Surface
- Integration completeness — what is not declared observed is not observed

The author does not operate, audit, certify, or endorse any deployment. No configuration shown in this document constitutes a recommendation for any specific jurisdiction, regulatory context, or operational requirement. Operators must conduct independent legal, regulatory, and technical analysis before representing CVS evidence in any formal proceeding.


### 0.7 Primitive Boundary

CVS defines evidence formation at the execution boundary.

It does not define system architecture, orchestration, deployment models, or implementation patterns.

Any system built using CVS as a primitive is a derivative implementation. Responsibility for design, deployment, and operation of that derivative remains entirely with the implementing party.

### 0.8 Companion Reference Documents

**`VCP_AND_CVS.md`** acknowledges VeritasChain Protocol (VCP) as an independently developed parallel architecture and documents the architectural properties that distinguish CVS from VCP: XRPL consensus-based external time anchoring, three-plane structural separation, administrative independence requirement, and the Disclosure Kernel. Priority is established by CVS genesis commit `32cbd9b`, December 17, 2025 — 27 days before VCP v1.0.

**`CANONICAL_COMMITMENT.md`** is the permanent priority record for 512 and CVS. It records genesis commit dates, the XRPL anchor transaction, the canonical kernel hash, and sealed archive hashes across three independent proof layers. This is the dated reference for any dispute, standards body submission, or ecosystem conversation referencing CVS's prior art status.

---

## Abstract

`CVS_ARCHITECTURE_v{M}.{m}.md` defined the Cryptographic Verification Sidecar as a minimal, fail-open, witness-only evidence primitive. That architecture operates as a parallel observation plane — never blocking execution, never storing content, never interpreting meaning. It established what CVS is and what constraints govern its behaviour.

**CVS does not block execution under any circumstance.** Failure of the sidecar creates a detectable gap in the evidence chain; it does not halt the observed system. This is an architectural property, not a configuration choice — there is no mode of CVS operation in which sidecar availability is a precondition for execution continuity.

This document defines the layers that sit on top of CVS: how evidence is accessed, how systems integrate with the evidence surface, and how the architecture may be deployed across heterogeneous infrastructure. The Access Plane provides read-only interfaces to the evidence chain. The Interpretation Plane enables external tools to consume evidence without altering it. System integration patterns address both human-speed operational workflows and machine-speed agentic execution.

**The implementation patterns described herein are illustrative and non-exhaustive.** They represent one valid approach to realising the CVS architecture. Operators are expected to adapt, extend, and re-evaluate every configuration decision for their specific deployment context. No configuration described here is prescribed as the only valid approach. No outcome described is guaranteed. No regulatory sufficiency is implied.

The core principle remains unchanged: evidence generation is disjoint from evidence access, and evidence access is disjoint from evidence interpretation. These planes never collapse. The separation is structural, not administrative.

---

## 1. Architectural Positioning

CVS architecture operates across three strictly separated planes.

### 1.1 The Three Planes Are Structurally Isolated

**Capture Plane (`CVS_ARCHITECTURE_v{M}.{m}.md` Domain)**

The Capture Plane observes execution, constructs Evidence Objects, chains them cryptographically, and anchors commitments to a public settlement ledger.

Normative behaviours (defined in `CVS_ARCHITECTURE §3`):

- **MUST** observe events without blocking execution
- **MUST** construct Evidence Objects with canonical serialisation
- **MUST** chain Evidence Objects via hash references
- **MUST** mark gaps explicitly when observation is interrupted
- **MUST** anchor cryptographic commitments to an operator-selected public ledger
- **MUST NOT** execute application logic, enforce policy, or alter observed data

**Access Plane (this document's domain)**

The Access Plane provides read-only interfaces to the evidence chain through three services:

- **Evidence Store:** Append-only, immutable storage (WORM semantics)
- **Proof Service:** Chain verification and Merkle inclusion proof generation
- **Replay Service:** Time-ordered evidence retrieval with filtering

Normative behaviours:

- **MUST** provide read-only access to Evidence Objects
- **MUST** preserve evidence immutability (no updates, no deletes)
- **MUST** expose gaps explicitly in replay results
- **MAY** create mutable indexes/caches that do not alter evidence integrity
- **MUST NOT** modify Evidence Objects, suppress gaps, or block Capture Plane operations

**Interpretation Plane (External Tools)**

The Interpretation Plane consists of dashboards, analytics engines, compliance tools, forensic platforms, and auditor workstations that consume evidence through the Access Plane.

Normative behaviours:

- **MUST** consume evidence via read-only Access Plane APIs
- **MUST** store interpretation artifacts separately from evidence
- **MUST NOT** modify Evidence Objects, inject new Evidence Objects, or claim authority over evidence correctness

### 1.2 Plane Separation Guarantees

No interpretation tool can modify captured evidence — the Access Plane exposes read-only APIs exclusively. No dashboard can block execution — the Capture Plane is disjoint from all operational paths. Interpretation artifacts are stored outside the evidence chain and referenced via cryptographic pointers only. Independent verification remains possible because verifiers bypass all interpretation tooling.

CVS records evidence only. It does not assert correctness, enforce policy, or determine outcomes. The evidence chain is a record of what was observed; all determination of significance, sufficiency, or legal effect is external to the architecture and remains with the humans and institutions that act on the evidence.

### 1.3 Architectural Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    INTERPRETATION PLANE                          │
│   (External Tools: Dashboards, Analytics, Conformance)          │
│   ┌──────────┐  ┌────────────┐  ┌─────────────┐               │
│   │Dashboard │  │ Analytics  │  │ Conformance │               │
│   │Vendor A  │  │ Engine B   │  │  Tool C     │               │
│   └────┬─────┘  └──────┬─────┘  └──────┬──────┘               │
│        └────────────────┼────────────────┘                      │
│                         │ READ-ONLY APIs                        │
└─────────────────────────┼─────────────────────────────────────┘
                          │
┌─────────────────────────┼─────────────────────────────────────┐
│                    ACCESS PLANE                                  │
│   ┌───────────────┐  ┌──────────────┐  ┌─────────────────┐   │
│   │Evidence Store │  │Proof Service │  │ Replay Service  │   │
│   │  (WORM/S3)    │  │(Merkle Ver.) │  │ (Time-Ordered)  │   │
│   └───────────────┘  └──────────────┘  └─────────────────┘   │
│         NO WRITE ACCESS TO CAPTURE PLANE                        │
└─────────────────────────┬─────────────────────────────────────┘
                          │ Append-Only Feed
┌─────────────────────────┼─────────────────────────────────────┐
│           CAPTURE PLANE (CVS_ARCHITECTURE domain)               │
│   ┌────────────┐   ┌──────────────┐   ┌────────────────┐     │
│   │CVS Sidecar │──→│Hash Chaining │──→│Settlement Layer│     │
│   │(Witness)   │   │(Merkle Tree) │   │(Ledger Anchor) │     │
│   └────────────┘   └──────────────┘   └────────────────┘     │
│      OBSERVES EXECUTION | NEVER BLOCKS | NEVER INTERPRETS      │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. The Access Plane Exposes a Read-Only Evidence Surface

### 2.1 Evidence Store

The Evidence Store implements Write-Once-Read-Many (WORM) semantics.

**WORM Requirements**

- **MUST** append objects but never modify or delete them
- **MUST** enforce object immutability through object locking or versioning constraints
- **MUST** disable deletion at the storage layer
- **MUST** ensure backup processes preserve immutability
- **MUST** ensure restored evidence is cryptographically identical to original

**Storage Topology Options**

- On-Premises: MinIO, Ceph with object lock
- Cloud: S3 Object Lock, Azure Immutable Blob Storage, GCP Bucket Lock
- Hybrid: Replicate across boundaries with settlement anchors proving identity

These options are illustrative. Operators select storage infrastructure appropriate to their data sovereignty, cost, and regulatory requirements.

**Scalability Model**

Evidence Objects are small (typically 1–5 KB each).

| Events/sec | Objects/day | Daily Storage (uncompressed) | Daily Storage (compressed 70%) |
|---|---|---|---|
| 100 | 8.6M | 17 GB | 5.1 GB |
| 1,000 | 86M | 172 GB | 51.6 GB |
| 10,000 | 860M | 1.72 TB | 516 GB |

Storage costs (AWS S3 Standard): $0.023/GB/month *(illustrative — see §-1.9)*
Archive costs (Glacier Deep Archive): $0.00099/GB/month *(illustrative — see §-1.9)*

### 2.2 Proof Service

The Proof Service generates cryptographic proofs that specific Evidence Objects were included in specific settlement batches.

**Design Requirements**

- **MUST** operate statelessly
- **MUST** operate purely on stored evidence and published settlement receipts
- **MUST** perform independent ledger verification — it does not trust operator-provided receipts
- **MUST** generate proofs deterministically

**Proof Bundle JSON Schema**

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": [
    "proof_version", "evidence_object_id", "observation_timestamp",
    "event_descriptor", "evidence_hash",
    "merkle_inclusion_proof", "settlement_anchor"
  ],
  "properties": {
    "proof_version":         { "type": "string", "pattern": "^[0-9]+\\.[0-9]+$" },
    "evidence_object_id":    { "type": "string" },
    "observation_timestamp": { "type": "string", "format": "date-time" },
    "evidence_hash":         { "type": "string", "pattern": "^(sha256|sha3-256):[a-f0-9]{64}$" },
    "merkle_inclusion_proof": {
      "required": ["batch_id", "merkle_root", "sibling_hashes"],
      "properties": {
        "batch_id":       { "type": "string" },
        "merkle_root":    { "type": "string" },
        "sibling_hashes": { "type": "array", "items": { "type": "string" } }
      }
    },
    "settlement_anchor": {
      "required": ["ledger", "transaction_id", "ledger_timestamp", "anchored_root"],
      "properties": {
        "ledger":           { "type": "string", "enum": ["xrpl", "ethereum", "stellar", "other"] },
        "transaction_id":   { "type": "string" },
        "ledger_timestamp": { "type": "string", "format": "date-time" },
        "anchored_root":    { "type": "string" }
      }
    }
  }
}
```

### 2.3 Replay Service

The Replay Service provides time-ordered, filterable access to Evidence Objects.

**Design Requirements**

- **MUST** provide deterministic time-ordered retrieval (repeatable results)
- **MUST** include explicit gap markers — discontinuities are never smoothed
- **MUST** support pagination with stable cursors

**Deterministic Ordering Rules**

- **MUST** sort primarily by `observation_timestamp` ascending
- **MUST** sort secondarily by `evidence_object_id` as a stable tiebreaker
- **MUST** maintain monotonic timestamps within a single chain

**Gap Reporting Format**

```json
{
  "gap_start":              "2027-03-15T14:16:01.456Z",
  "gap_end":                "2027-03-15T14:28:15.789Z",
  "chain_id":               "chain_payment-engine-03",
  "gap_duration_seconds":   734,
  "resumption_evidence_id": "eo_3c4d5e6f"
}
```

> **Detectable Gaps — Causal Note:** Gaps may reflect infrastructure failure, network partition, sidecar unavailability, or undeclared execution surfaces. The CVS does not infer cause. It records absence. Causal interpretation remains external to the architecture.

---

## 3. Interpretation Interface Contract

### 3.1 What Interpretation Tools May Consume

Interpretation tools:

- **MAY** query the Replay Service for time-ordered Evidence Objects
- **MAY** request Proof Service Merkle inclusion proofs
- **MAY** correlate evidence across systems using correlation IDs
- **MAY** generate reports and findings
- **MAY** cache query results for performance

### 3.2 Conforming Interpretation Tool Behaviour

A tool operating within the Interpretation Plane qualifies as conforming only if it:

- does not modify Evidence Objects
- does not alter hash chains
- does not suppress or smooth gaps
- does not inject new Evidence Objects into chains
- does not block Capture Plane operations

### 3.3 Formal API Contracts

**Base URL**

```
https://evidence.example.com/api/v1
```

**GET /replay**

Query Parameters:

- `start` (ISO 8601, required): Start of time window
- `end` (ISO 8601, required): End of time window
- `source_system_id` (string, optional)
- `event_type` (string, optional)
- `correlation_id` (string, optional)
- `limit` (integer, optional, default 1000, max 10000)

Response (200 OK):

```json
{
  "query":            { "..." },
  "evidence_objects": [ "..." ],
  "gaps":             [ "..." ],
  "total_count":      42,
  "index_lag_ms":     127,
  "has_more":         false
}
```

**GET /proof**

Query Parameters: `evidence_id` (string, required)

Response: Proof Bundle (see schema in §2.2)

**GET /anchor**

Query Parameters: `transaction_id` (string, required)

Response (200 OK):

```json
{
  "ledger":                 "xrpl",
  "transaction_id":         "E7F4A9B2...",
  "ledger_timestamp":       "2027-03-15T14:32:23.000Z",
  "anchored_root":          "sha256:7d4b9a2f...",
  "verification_status":    "confirmed",
  "ledger_query_timestamp": "2027-03-15T16:45:12.000Z"
}
```

---

## 4. System Integration Architecture

### 4.1 Adapter Layer

Adapters connect CVS to event streams. Each adapter is purpose-built for a specific integration point. The adapters described below are examples; operators may implement other adapter types consistent with the witness-only constraint.

**Kafka Adapter**

- Capture Point: Kafka topics
- Integration Method: Standard Kafka consumer
- Latency: <10ms observation delay
- **MUST NOT** acknowledge messages; passive observer only

**Change Data Capture (CDC) Adapter**

- Capture Point: Database replication streams (Postgres, MySQL, Oracle)
- Latency: <100ms observation delay
- **MUST NOT** write to database; observe after-commit only

**OpenTelemetry (OTEL) Adapter**

- Capture Point: Distributed traces and spans
- Latency: <5ms observation delay
- **MUST** operate as one additional OTEL exporter; never block traces

**API Gateway Mirror Adapter**

- Capture Point: HTTP request/response traffic
- Latency: 0ms added (async mirror)
- Operates on mirrored traffic only

**SmartNIC Capture Adapter**

- Capture Point: Network interface hardware
- Latency: <1μs observation delay
- Dedicated hardware; zero CPU impact

#### 4.1.6 Observation Scope Clarification

CVS observes declared integration points. It does not discover undeclared execution surfaces, infer hidden transmission paths, or enumerate operational topology automatically. Coverage completeness depends on explicit integration.

### 4.2 Canonical Descriptor Mapping

Event descriptors provide consistent schema across heterogeneous systems.

**Canonical Descriptor Schema**

```json
{
  "descriptor_version": "1.0",
  "source_system_id":   "payment-engine-03",
  "event_type":         "payment_executed",
  "observed_timestamp": "2027-03-15T14:32:18.447Z",
  "origin_timestamp":   "2027-03-15T14:32:18.441Z",
  "stream_id":          "kafka_topic_payments",
  "correlation_ids": {
    "transaction_id": "txn_9f4a8c2b",
    "trace_id":       "trace_a7b8c9d0"
  },
  "payload_hash": "sha256:a3f7c2e1...",
  "metadata":     {}
}
```

**Canonicalisation Rules**

- **MUST** format timestamps as ISO 8601 with timezone (UTC preferred)
- **MUST** use lowercase, snake_case keys for correlation IDs
- **MUST** use a controlled vocabulary for event types
- **MUST** hash using SHA-256 or SHA-3-256 only
- **MUST** maintain stable field ordering for serialisation

### 4.3 Coverage Integrity and Boundary Declaration

#### 4.3.1 Purpose

The Capture Plane records what it observes. It does not guarantee that all operational transmission surfaces are instrumented. An implementation **MAY** partially instrument with CVS. A deployment that represents partial observation as complete evidentiary coverage is not a conforming deployment.

#### 4.3.2 Declared Observation Surface

An implementation claiming full evidentiary coverage **MUST** publish a Declared Observation Surface (DOS) manifest. The DOS **MUST**:

- Enumerate all declared transmission points and commit boundaries
- Assign each transmission point a unique `surface_id`
- Declare expected event classes per surface
- Declare expected emission cadence or silence threshold
- Declare adapter type per surface
- Be serialised deterministically
- Be hashed using SHA-256 or SHA-3-256
- Be versioned

**Example DOS (informative):**

```json
{
  "dos_version": "1.0",
  "surfaces": [
    {
      "surface_id":                "kafka_topic_payments",
      "adapter":                   "kafka_passive_consumer",
      "expected_event_types":      ["payment_executed"],
      "silence_threshold_seconds": 60
    },
    {
      "surface_id":                "api_gateway_orders",
      "adapter":                   "http_mirror",
      "expected_event_types":      ["order_submitted"],
      "silence_threshold_seconds": 30
    }
  ]
}
```

The DOS hash **MUST** be anchored via the Settlement Layer. The DOS **MAY** change over time, but each change **MUST** produce a new DOS hash, be versioned, be anchored publicly, and preserve prior DOS records for historical verification.

#### 4.3.3 Coverage Attestation

An implementation claiming boundary completeness **MUST** periodically emit a Coverage Attestation Evidence Object including: DOS hash, total declared surfaces, surfaces observed during interval, surfaces silent beyond declared threshold, coverage percentage, and attestation timestamp.

```json
{
  "event_type":        "coverage_attestation",
  "dos_hash":          "sha256:abcd1234...",
  "declared_surfaces": 142,
  "observed_surfaces": 142,
  "silent_surfaces":   [],
  "coverage_percent":  100.0
}
```

#### 4.3.4 Silence and Negative Space Detection

If a declared surface fails to emit events within its declared silence threshold, a `coverage_gap_detected` Evidence Object **MUST** be generated. The silent `surface_id` **MUST** be included. Silence duration **MUST** be recorded.

Silence **MUST NOT** be ignored. Silence **MUST NOT** be reconstructed. Silence is evidentiary.

#### 4.3.5 Representations Incompatible with Coverage Conformance

A deployment making any of the following representations is not conforming with respect to coverage declarations:

- claiming "complete coverage" without an anchored DOS
- representing partial instrumentation as boundary-complete
- excluding transmission points from the DOS while implying their inclusion
- removing surfaces from the DOS without versioning and anchoring the change
- excluding coverage gaps from replay queries

#### 4.3.6 Coverage Declaration Is a Liability Boundary

Absence of a DOS constitutes an undefined observation boundary. An undefined boundary means evidentiary posture is partial. Where evidentiary posture is partial, completeness cannot be established. The CVS produces a record of what it observed. The DOS produces a record of what it declared it would observe. Both are required before evidentiary completeness can be characterised.

---

## 5. Human-Speed Integration Profile (Profile H)

Profile H addresses systems where human judgment or operational oversight is expected. The examples below are illustrative.

### 5.1 Factory Manufacturing Example

**Event Types**

- `batch_started`
- `equipment_state_change`
- `environmental_reading`
- `quality_checkpoint_passed`
- `deviation_recorded`
- `batch_completed`

**Evidence Volume (Single Batch)**

- Equipment state changes: 50 events → 100 KB
- Environmental readings: 144 events → 216 KB
- Quality checkpoints: 8 events → 16 KB
- Total per batch: ~340 KB

**Evidence Disclosure Package**

1. Query Replay Service for `batch_id=X`
2. Retrieve all Evidence Objects for batch
3. Generate Proof Bundles for critical checkpoints
4. Package: Evidence Objects + Merkle proofs + settlement anchors
5. Disclose to relevant parties
6. Independent verification via public ledger

**Illustrative Premium Impact:** 10–15% reduction ($20K–30K/year savings) — see §-1.9 disclaimer

**Regulatory Relevance:** Product liability evidence chains may be relevant to requirements under the EU Product Liability Directive (updated 2024, effective December 2026 transposition deadline), which extends liability to AI-enabled and software-updated products. Automated equipment with CVS evidence chains provides reconstruction capability of the type the Directive's defect attribution requirements contemplate. Whether any specific deployment satisfies applicable legal obligations is a determination for legal counsel, not this document.

### 5.2 Broadcast Media Example

**Event Types**

- `story_assigned`
- `content_approved`
- `graphics_rendered`
- `playout_scheduled`
- `segment_aired`

**Evidence Volume (Single Hour)**

~75 events → ~110 KB/hour

**Evidence Disclosure Package**

Produces a structured, independently verifiable record of the sequence from editorial approval through broadcast, including each step in the human oversight chain for AI-generated or AI-assisted content. Whether this record satisfies any specific legal or regulatory obligation is a determination for the operator's legal counsel.

**Illustrative Premium Impact:** 10–20% reduction ($10K–20K/year savings) — see §-1.9 disclaimer

**Regulatory Relevance:** UK Online Safety Act (2023, enforcement active 2025) requires broadcasters to demonstrate governance of AI-assisted content. Evidence chains showing approval sequences are relevant to the "reasonable steps" analysis. EU AI Act Article 26 (Regulation EU 2024/1689) requires deployers of high-risk AI systems to maintain logs — CVS provides the kind of independent log infrastructure this requirement contemplates. Whether any specific deployment satisfies these obligations requires independent legal analysis.

---

## 6. Machine-Speed Agentic Integration Profile (Profile M)

Profile M addresses autonomous systems operating at sub-10μs decision latency. The examples below are illustrative.

### 6.1 Financial Transaction Automation Example

**Event Types**

- `market_data_received`
- `model_inference_computed`
- `risk_check_evaluated`
- `order_submitted`
- `execution_confirmed`

**Latency Characteristics**

| Stage | Execution Latency | CVS Observation Latency |
|---|---|---|
| Market data ingestion | 10–50 μs | <1 μs (SmartNIC) |
| Model inference | 100–500 μs | <5 μs (OTEL) |
| Risk check | 10–50 μs | <10 μs (API mirror) |
| Order submission | 50–200 μs | <10 μs (Kafka) |
| **Total** | **170–800 μs** | **0 μs added (parallel)** |

**Evidence Volume (Single Trading Day)**

- Assumptions: 1,000 orders/sec, 10,000 inferences/sec
- Total: ~535M events/day → ~440 GB/day uncompressed
- Compressed (70%): ~132 GB/day

**Settlement Batching**

- Batch every 1 second (86,400 batches/day)
- Each batch: ~6,200 Evidence Objects
- Settlement cost at 1-second intervals using XRPL as example ledger: ~$65/month *(illustrative — see §-1.9)*

**Dispute Resolution**

Traditional forensic reconstruction requires 2–4 weeks. CVS-enabled resolution may complete in 2–4 hours, potentially saving $50K–100K in outside counsel per incident. *(illustrative — see §-1.9)*

**Illustrative Premium Impact:** 10–20% reduction ($200K–400K/year savings for large trading firm) — see §-1.9 disclaimer

**Regulatory Relevance:** MiFID II Article 25 requires investment firms to maintain records of all services, activities, and transactions. EMIR requires trade repositories to maintain records for 10 years. CVS provides independently verifiable, tamper-evident record infrastructure of the type both regulations contemplate. Under DORA (Regulation EU 2022/2554, effective January 2025), financial entities must maintain ICT-related incident logs and demonstrate operational resilience — CVS evidence chains are relevant to both requirements. Whether any specific deployment satisfies these regulatory obligations requires independent legal analysis.

#### 6.1.1 Declared Observation Surface

The CVS observes only declared integration points. It does not autonomously discover execution paths, hidden services, shadow infrastructure, or undeclared transmission channels. It subscribes exclusively to the event streams explicitly configured during deployment. Completeness of evidence is therefore bounded by declared coverage.

The set of subscribed systems, streams, and interfaces constitutes the Declared Observation Surface (DOS). The DOS **MUST** be documented, versioned, and, where required, independently attestable.

If execution occurs outside the declared surface, the CVS records silence — not failure. Silence is observable. Silence is not proof of absence. It is proof of non-observation within the declared boundary. Claims of complete coverage are non-conformant unless the coverage boundary is explicitly defined and documented.

### 6.2 Commit Gate Witnessing (512)

Machine-speed systems that are built to satisfy 512's properties operate a **Commit Gate** at the execution boundary. 512 is a discovered constraint — a property set that physics imposes at execution boundaries operating at civilisational scale. CVS witnesses the evaluation outcomes that a 512-conformant Commit Gate emits, capturing per-invariant results in a structured, independently verifiable form. It does not witness "512" as a deployed artifact; it witnesses constraint evaluation events emitted by systems whose specifications conform to 512's properties, as defined in `512_ARCHITECTURE_v3.4 §3`.

When a 512-conformant Commit Gate evaluates execution requests, CVS captures three Evidence Objects representing the validation sequence.

**Pre-Validation Evidence Object**

```json
{
  "evidence_id":           "sha256:7f4a8c2b3d9e1f5a...",
  "observation_timestamp": "2027-03-15T14:32:18.447Z",
  "event_descriptor": {
    "source_system_id": "ai_agent_orchestrator_03",
    "event_type":       "execution_validation_request",
    "correlation_ids": {
      "execution_id": "exec_9f4a8c2b",
      "agent_id":     "agent_7f3a9b"
    }
  }
}
```

**Validation Evidence Object (512-conformant Commit Gate)**

```json
{
  "evidence_id":           "sha256:8g5b9d3c4e0f2a7k...",
  "observation_timestamp": "2027-03-15T14:32:18.492Z",
  "event_descriptor": {
    "source_system_id": "commit_gate_instance_02",
    "event_type":       "512_constraint_evaluation"
  },
  "validation_result": {
    "overall_result": "DENY",
    "constraint_evaluation": {
      "invariant_1_noncoercion":        "PASS",
      "invariant_2_consent":            "PASS",
      "invariant_3_property_integrity": "PASS",
      "invariant_4_reversibility":      "PASS",
      "invariant_5_visibility":         "PASS",
      "invariant_6_attribution":        "PASS",
      "invariant_7_bounded_authority":  "FAIL"
    },
    "violated_constraint_detail": "capability_grant_exceeded"
  }
}
```

#### 6.2.1 Validation System Independence

CVS records validation outcomes. It does not influence validation logic, modify validation rules, override validation decisions, or enforce constraints. Validation systems remain independent enforcement components. CVS remains witness-only.

**Regulatory Relevance:** EU AI Act Article 9 (Regulation EU 2024/1689) requires high-risk AI systems to have risk management systems including logging of operations. Article 12 requires automatically generated logs to be kept for at least 6 months. The CVS validation evidence chain — capturing per-constraint outcomes for every execution request — provides tamper-evident, independently verifiable records that self-declared internal logs cannot match, and is relevant to both requirements. Whether a specific deployment satisfies Articles 9 and 12 is a determination for legal counsel.

---

## 7. Multi-Vendor Interoperability

CVS architecture enables multi-vendor deployments where different organisations operate independent CVS instances yet produce mutually verifiable evidence. Full interoperability specification is defined in the CVS Interoperability Specification. This section summarises requirements.

### 7.1 Evidence Object Portability Requirements

Evidence Objects **MUST** be portable across implementations. An Evidence Object produced by Vendor A's CVS **MUST** be verifiable by Vendor B's tooling without requiring Vendor A's software.

**Portability Properties**

- **MUST** use canonical serialisation: deterministic, stable field ordering
- **MUST** maintain hash stability: same content produces the same hash across all implementations
- **MUST** use standard signature algorithms only: ECDSA, RSA, EdDSA

**Canonical Serialisation Rules**

- **MUST** use lowercase snake_case field names
- **MUST** format timestamps as ISO 8601 with timezone (UTC)
- **MUST** hex-encode binary data (hashes, signatures)
- **MUST** omit optional fields entirely — not set to null
- **MUST** order fields alphabetically by key name

**Hash Stability Rules**

- **MUST** compute hashes deterministically and reproducibly
- **MUST** use SHA-256 by default; SHA-3-256 is acceptable
- **MUST NOT** use proprietary hash functions — use of a proprietary hash function is not conforming

### 7.2 Open-Source Verification Requirement

Every conformant CVS implementation **MUST** provide open-source verification tooling that allows any party to independently verify a Proof Bundle without access to operator infrastructure, vendor-specific software, or credentials of any kind.

The verification tool:

- **MUST** accept a Proof Bundle as its sole required input
- **MUST** verify that the Evidence Object hash matches the canonical serialisation of the event descriptor
- **MUST** verify Merkle inclusion proof validity against the batch root
- **MUST** query the settlement ledger directly to confirm the anchored root matches the Proof Bundle's `settlement_anchor.anchored_root`
- **MUST** verify timestamp consistency between the Evidence Object, batch window, and ledger anchor
- **MUST** be published under an open-source licence with no field-of-use restrictions
A verification tool qualifies as conforming under this requirement only if it:

- executes without requiring payment, registration, or operator-issued credentials
- completes all verification steps without depending on proprietary libraries, vendor APIs, or operator-hosted endpoints
- returns a non-passing result whenever any of the hash, Merkle, or anchor checks have not all succeeded — a tool that returns "valid" on partial pass is not conforming

**Example Verification Execution**

```bash
$ cvs-verify proof_bundle.json
✓ Evidence hash matches descriptor
✓ Merkle inclusion proof valid
✓ Settlement anchor confirmed on ledger (XRPL tx: E7F4A9B2...)
✓ Timestamp consistency verified
✓ Proof is valid
Verification completed in 487ms
```

### 7.3 Federation Directory Model

In multi-vendor deployments, a federation directory maps system IDs to CVS endpoints.

**DNS-Based Federation**

```
_cvs.example.com. TXT "cvs=https://evidence.example.com/api/v1;
  pubkey=0x04a7b8c9..."
```

**HTTPS-Based Federation**

Federation descriptor at: `https://example.com/.well-known/cvs-federation.json`

```json
{
  "organization":    "Example Corporation",
  "cvs_endpoint":    "https://evidence.example.com/api/v1",
  "api_version":     "1.0",
  "verification_keys": [
    {
      "key_id":     "key_2027_01",
      "algorithm":  "ecdsa-secp256k1",
      "public_key": "04a7b8c9d0e1f2a3b4c5..."
    }
  ],
  "settlement_ledger": "xrpl"
}
```

**Cross-Organisation Evidence Workflow — Supply Chain Example**

1. Shipper (Org A) records custody transfer
2. Receiver (Org B) queries Org A's CVS via DNS discovery
3. Receiver records receipt with same correlation ID
4. Dispute arises: both parties disclose evidence independently
5. Settlement anchors prove timing — liability determined via evidence, not trust

> **Ledger Neutrality:** Reference to the XRP Ledger is descriptive, not prescriptive. Mention of XRPL does not imply endorsement, partnership, dependency, or affiliation. The architecture remains ledger-agnostic. Any ledger satisfying mandatory settlement properties may be substituted without altering evidentiary semantics.

---

## 8. Performance Envelope and Scaling

### 8.1 Events/Sec Tiers

**Tier 1: Human-Speed (1–100 events/sec)**

Use cases include manufacturing, healthcare, and editorial workflows. Infrastructure: single CVS sidecar, 60-second batching, monthly storage <100 GB, anchor cost <$10/month.

**Tier 2: Mixed-Speed (100–10,000 events/sec)**

Use cases include e-commerce and API-driven services. Infrastructure: multiple sidecars, 30-second batching, monthly storage 500 GB–5 TB, anchor cost $50–200/month.

**Tier 3: Machine-Speed (10,000–1,000,000 events/sec)**

Use cases include financial trading and network telemetry. Infrastructure: dozens of sidecars, SmartNIC offload, 1–10 second batching, monthly storage 10–100 TB, anchor cost $200–500/month.

All tier descriptions and cost figures are illustrative — see §-1.9.

### 8.2 Storage Growth Per Day

| Events/sec | Objects/day | Daily Uncompressed | Daily Compressed (70%) |
|---|---|---|---|
| 100 | 8.6M | 17 GB | 5.1 GB |
| 1,000 | 86M | 172 GB | 51.6 GB |
| 10,000 | 860M | 1.72 TB | 516 GB |
| 100,000 | 8.6B | 17.2 TB | 5.16 TB |

### 8.3 Anchor Frequency Options

| Frequency | Anchors/Month | Monthly Cost (XRPL — example ledger) |
|---|---|---|
| Every 60 seconds | 43,200 | $1.08 |
| Every 30 seconds | 86,400 | $2.16 |
| Every 10 seconds | 259,200 | $6.48 |
| Every 1 second | 2,592,000 | $64.80 |

> **Ledger Selection Note:** Cost figures in this table use XRPL as one example settlement ledger. Operators select the ledger appropriate to their deployment. Equivalent or different costs apply on other ledgers. Anchoring to any specific ledger is not required — ledger selection is entirely the operator's decision. All figures are illustrative — see §-1.9.

Human-speed workflows use 60-second batching. Mixed-speed deployments use 30-second batching. Machine-speed deployments may use 1–5 second batching where logging requirements mandate frequent public timestamping.

### 8.4 CPU/Memory Baselines

| Tier | Events/sec | vCPU | RAM | Storage (local) |
|---|---|---|---|---|
| Tier 1 | 1–100 | 2 | 4 GB | 100 GB SSD |
| Tier 2 (low) | 100–1,000 | 4 | 8 GB | 500 GB SSD |
| Tier 2 (high) | 1,000–10,000 | 8 | 16 GB | 1 TB NVMe |
| Tier 3 | 10,000–100,000 | 16 | 32 GB | 2 TB NVMe |
| Tier 3 (extreme) | 100,000–1M | 32 | 64 GB | 5 TB NVMe + SmartNIC |

### 8.5 Cost Scaling Model — Tier 2 Deployment (1,000 events/sec)

*(illustrative — see §-1.9)*

| Component | Monthly Cost | Annual Cost |
|---|---|---|
| CVS Sidecar (EC2 m6i.xlarge) | $140 | $1,680 |
| Access Plane (EC2 m6i.large) | $70 | $840 |
| Evidence Store (S3 Standard) | $34.50 | $414 |
| Settlement Anchoring | $2.16 | $26 |
| Network Egress | $45 | $540 |
| Observability | $20 | $240 |
| **Total First-Year Average** | **$313.16** | **$3,740** |

Doubling throughput increases costs by ~80% — sub-linear due to batching efficiency.

---

## 9. Security and Isolation Model

### 9.1 Plane Isolation Requires Network Segmentation

The three planes — Capture, Access, Interpretation — are isolated through network segmentation, IAM policies, and API design.

**Isolation Topology**

```
┌────────────────────────────────────────────┐
│ INTERPRETATION PLANE (External/DMZ)        │
│ SG: allow outbound to Access Plane only    │
└──────────────┬─────────────────────────────┘
               │ READ-ONLY HTTPS
┌──────────────▼─────────────────────────────┐
│ ACCESS PLANE (Internal DMZ)                │
│ SG: allow inbound from Interpretation only │
│     allow outbound to Evidence Store only  │
└──────────────┬─────────────────────────────┘
               │ READ-ONLY (S3 API)
┌──────────────▼─────────────────────────────┐
│ EVIDENCE STORE (Storage VLAN)              │
│ SG: allow write from Capture only          │
│     allow read from Access only            │
└──────────────▲─────────────────────────────┘
               │ APPEND-ONLY
┌──────────────┴─────────────────────────────┐
│ CAPTURE PLANE (Production VLAN)            │
│ SG: allow outbound to Store & Ledger only  │
│     NO inbound connections                 │
└────────────────────────────────────────────┘
```

### 9.2 IAM Boundary Separation

**Capture Plane Service Role**

Permissions: Evidence Store write-only (append objects); Settlement Wallet read-only (query balance, submit transactions); HSM sign Evidence Objects.

Prohibited: read from Evidence Store; modify settlement wallet balance; assume Access or Interpretation roles.

**Access Plane Service Role**

Permissions: Evidence Store read-only (list, get objects); Settlement Ledger query-only (public RPC).

Prohibited: write to Evidence Store; access settlement wallet or HSM; assume Capture Plane role.

### 9.3 HSM Key Custody

Attestation keys — used to sign Evidence Objects — are stored in Hardware Security Modules (HSMs). Private keys never leave the HSM.

**HSM Requirements**

- **MUST** use FIPS 140-2 Level 2 or higher (Level 3 recommended)
- **MUST** maintain a dedicated HSM partition for CVS attestation keys
- **MUST** generate keys inside the HSM
- **MUST** perform signing operations inside the HSM

Available options include AWS CloudHSM (FIPS 140-2 Level 3), Azure Dedicated HSM (FIPS 140-2 Level 3), and Thales Luna HSM (on-premises, FIPS 140-2 Level 3). Operators select HSM infrastructure appropriate to their security posture and budget.

### 9.4 Key Rotation Model

**Rotation Process**

1. Generate new key pair in HSM
2. Publish new public key to key registry
3. Update sidecars to sign with new key (rolling deployment)
4. Archive old public key — retain for verification
5. Old key remains in registry indefinitely

Evidence Objects include a `key_id` field. Historical evidence remains verifiable indefinitely by querying the key registry for retired keys.

**Rotation Frequency**

- **SHOULD** rotate annually for standard deployments
- **SHOULD** rotate quarterly for high-security environments
- **SHOULD** rotate immediately upon suspected compromise

### 9.5 Compromise Protocol

**Sidecar Compromise (Capture Plane)**

An attacker who compromises a sidecar can observe evidence being generated and potentially delay evidence, creating gaps. The attacker cannot alter existing evidence (WORM storage), cannot sign false evidence (private key in HSM), and cannot backdate evidence (settlement anchors prove timing).

Response: isolate the compromised sidecar; analyse evidence chain for gaps; rotate attestation keys; disclose compromise if evidence integrity is questioned.

**Settlement Wallet Compromise**

An attacker who compromises the settlement wallet can drain the balance — a denial of service against anchoring. The attacker cannot alter historical anchors (immutable ledger).

Response: rotate settlement wallet keys; re-anchor recent batches from backup; historical anchors remain valid.

### 9.6 Insider Threat Mitigation

**Separation of Duties**

- **MUST** ensure no single individual has both write access to the Evidence Store and control over the settlement wallet
- **MUST** ensure no single individual has both HSM admin access and production evidence access

Sensitive operations — key rotation, sidecar deployment changes, settlement wallet provisioning — **SHOULD** require dual authorisation from two independently credentialled individuals.

**Continuous Observation**

Anomaly detection **MUST** cover: bulk evidence downloads (>10,000 objects in <1 hour); access outside normal business hours; repeated disclosure requests (>5 per day); failed authentication attempts (>3 per hour).

#### 9.6.1 Structural Authority Separation Is Not Procedural

No single role or system component shall possess simultaneous authority to suppress evidence, prevent settlement anchoring, modify stored Evidence Objects, or control attestation keys. Authority separation is structural, not procedural.

**Regulatory Relevance:** DORA Article 9 (Regulation EU 2022/2554) requires ICT systems to have security controls preventing unauthorised access and modifications. NIS2 Directive (EU 2022/2555, effective October 2024) requires multi-layer security measures for essential and important entities. The structural authority separation model is relevant to both frameworks' access control requirements. Whether it satisfies specific obligations is a determination for the deploying organisation's legal counsel.

### 9.7 Disclosure Logging

Every evidence disclosure request is logged as evidence.

**Disclosure Log Schema**

```json
{
  "disclosure_id":          "disc_20270315_001",
  "requester_identity":     "legal@example.com",
  "query_parameters":       { "..." },
  "evidence_ids_disclosed": ["eo_4a7f9c3e", "eo_5c8g0d4f"],
  "outcome":                "success | rejected | partial",
  "timestamp":              "2027-03-16T10:22:00Z"
}
```

Disclosure logs are themselves evidence: hashed, chained, and anchored.

### 9.8 Gap Taxonomy

The CVS defines four gap types. Each represents a distinct failure of evidentiary continuity — not of execution continuity. CVS never blocks execution. It records the nature and boundary of each discontinuity.

All gap types **MUST** be surfaced explicitly. A conforming implementation surfaces each gap type as a structured Evidence Object in the chain. Concealment, smoothing, interpolation, or exclusion from replay queries is not conforming. Gap records are first-class Evidence Objects: hashed, chained, and anchored.

---

#### Evidence Gap

An Evidence Gap records a discontinuity in the observation chain caused by sidecar unavailability.

**Trigger condition:** The CVS sidecar crashes, restarts, is deliberately disabled, or loses connectivity to the Evidence Store for any duration. The gap begins at the timestamp of the last successfully written Evidence Object and ends at the timestamp of the first successfully written Evidence Object after recovery.

**Detection mechanism:** On recovery, the sidecar determines the last known good `evidence_id` and `observation_timestamp` from its crash-recovery log or from the Evidence Store directly. A `gap_record` Evidence Object is constructed and written as the first post-recovery object before normal observation resumes. The gap record's `previous_evidence_hash` is the hash of the last known good Evidence Object. The first normal Evidence Object after recovery sets its `previous_evidence_hash` to the hash of the gap record, maintaining chain continuity.

**Disclosure behaviour:** Evidence Gaps appear as explicit gap markers in all Replay Service responses that span the gap window. The gap marker **MUST** include: `gap_start`, `gap_end`, `gap_duration_seconds`, `chain_id`, `cause_code`, and `resumption_evidence_id`. The Replay Service **MUST NOT** return a continuous sequence that omits the gap. Any party querying the chain **MUST** receive the gap record as part of the ordered sequence.

---

#### Settlement Gap

A Settlement Gap records a period during which Evidence Objects were captured but could not be anchored to the settlement ledger.

**Trigger condition:** The settlement ledger is unreachable for longer than the configured queue flush threshold (default: 30 minutes, 360 retry attempts at 5-second intervals). Evidence Objects continue to be observed and written to the Evidence Store during this period. Anchoring is queued locally. A `settlement_gap_detected` Evidence Object is emitted when the threshold is breached.

**Detection mechanism:** The sidecar monitors ledger reachability continuously. Failed anchor submissions increment a retry counter. When the threshold is breached, the sidecar emits `settlement_gap_detected` into the evidence chain. On reconnection, the local queue is flushed in chronological order. Queued batches **MUST NOT** be merged — each batch retains its original window and Merkle root. The Proof Service detects Settlement Gaps by comparing the sequence of settlement anchors against the evidence chain timeline; anchors that are missing or delayed are surfaced as settlement discontinuities in proof responses.

**Disclosure behaviour:** The Proof Service **MUST** report the settlement gap when generating proofs for Evidence Objects captured during the gap window. Proof Bundles for these objects carry a `settlement_status` of `pending` until anchoring completes. A `pending` status is not a verification failure — it is a precisely scoped temporal claim about public anchor availability. Settlement Gaps **MUST NOT** be concealed from Proof Service responses.

---

#### Coverage Gap

A Coverage Gap records silence on a declared observation surface that exceeds the surface's declared silence threshold.

**Trigger condition:** A surface declared in the Declared Observation Surface (DOS) manifest fails to emit any events within its configured `silence_threshold_seconds`. The gap begins at the last observed event on that surface and ends when the surface resumes emission or the surface is removed from the DOS.

**Detection mechanism:** The sidecar monitors emission cadence per declared `surface_id`. When the silence threshold is breached, a `coverage_gap_detected` Evidence Object **MUST** be generated. The object **MUST** include: the silent `surface_id`, silence start timestamp, silence duration at time of detection, and the `dos_hash` of the DOS version that declared the surface. Silence **MUST NOT** be inferred as normal — it is evidentiary. The CVS does not distinguish between silence caused by infrastructure failure and silence caused by undeclared execution on an unmonitored path. Both produce the same `coverage_gap_detected` record.

**Disclosure behaviour:** Coverage Gaps appear in Replay Service responses for the affected chain and surface. The `coverage_gap_detected` Evidence Object is retrievable by `surface_id` filter. Coverage Attestation Evidence Objects **MUST** report silent surfaces explicitly; a surface that exceeded its silence threshold during an attestation interval **MUST** appear in the `silent_surfaces` field with duration. Coverage Gaps **MUST NOT** be excluded from attestation reports or replay responses.

---

#### Validation Gap

A Validation Gap records silence on the constraint evaluation event stream of a Commit Gate, indicating that the gate is not producing per-invariant evaluation records.

**Trigger condition:** A Commit Gate operating within a declared observation surface fails to emit `constraint_evaluation` events within the surface's declared silence threshold. This indicates that either the Commit Gate is unavailable, has been bypassed, or is not producing observable output.

**Detection mechanism:** The Commit Gate's event stream is treated as a declared surface in the DOS. Silence detection follows the Coverage Gap mechanism: when the `silence_threshold_seconds` for the Commit Gate's `surface_id` is breached, a `coverage_gap_detected` Evidence Object is emitted with the Commit Gate's `surface_id`. The Validation Gap is distinguished from a Coverage Gap by the `event_type` context of the silent surface — specifically, the absence of `512_constraint_evaluation` events. The sidecar does not interpret why the Commit Gate is silent. It records that it is.

**Disclosure behaviour:** Validation Gaps surface through the same Replay Service mechanism as Coverage Gaps. The gap record is queryable by the Commit Gate's `surface_id`. Validation Gaps **MUST NOT** be treated as routine operational events. Their presence indicates that machine-speed constraint enforcement was either inactive or unobservable for the gap duration. This is evidentiary with respect to any execution that occurred during the window.

---

**Gap Type Summary**

| Gap Type | Trigger | Detection Object | Chain Continuity |
|---|---|---|---|
| Evidence Gap | Sidecar unavailable | `gap_record` | Maintained via gap record chaining |
| Settlement Gap | Ledger unreachable > threshold | `settlement_gap_detected` | Maintained; anchoring deferred |
| Coverage Gap | Surface silent > threshold | `coverage_gap_detected` | Maintained; surface silence recorded |
| Validation Gap | Commit Gate silent > threshold | `coverage_gap_detected` (gate surface) | Maintained; constraint silence recorded |

All gap records **MUST** remain in the chain permanently. Gap records **MUST NOT** be deleted, modified, or excluded from replay results.

### 9.9 Failure Classification Matrix

The CVS distinguishes execution continuity from evidentiary continuity.

| Failure Type | Execution Impact | Evidence Impact | Observability | Gap Type Produced |
|---|---|---|---|---|
| Sidecar crash | None | Gap in chain | Explicit discontinuity | Evidence Gap |
| Ledger unavailability | None | Deferred anchor | Delayed settlement receipt | Settlement Gap |
| Coverage omission | None | Silence outside declared surface | Non-observed execution | Coverage Gap |
| Commit Gate silence | None | Constraint evaluation unobservable | Silent surface on gate stream | Validation Gap |
| Disclosure refusal | None | Scoped denial | Logged refusal event | No gap — logged as refusal |
| Clock desynchronisation | None | Timestamp drift | Detectable inconsistency | No gap — anomaly flagged |

The CVS never blocks execution. It records deviation from declared evidence continuity. Every failure type that produces a gap does so explicitly — the gap is itself evidence.

---

## 10. Operational Ownership Model

### 10.1 Role Matrix

| Role | Responsibilities | Authority | Cannot |
|---|---|---|---|
| Platform Engineering | Deploy/maintain sidecars; operate Access Plane; monitor health; scale | Modify sidecar config; deploy adapters; tune performance | Modify evidence; access wallet; approve disclosure |
| Security | Manage attestation keys; oversee HSM; compromise response; audit logs | Rotate keys; disable compromised sidecars; investigate | Generate evidence; interpret evidence |
| Legal | Define disclosure policies; approve requests; engage in disputes | Approve/reject disclosure; define scope constraints | Access evidence directly; modify evidence |
| Risk | Monitor gaps; assess operational risk; coordinate with insurers | Escalate gaps; recommend deployment priorities | Modify evidence; approve disclosures |
| Finance | Provision settlement wallet; monitor costs; budget infrastructure | Fund wallet; approve budgets | Access evidence; approve disclosures |
| Data Engineering | Optimise storage; manage backups; tune indexing | Modify storage config (within WORM constraints) | Modify evidence content; suppress gaps |

### 10.2 Escalation Paths

**Evidence Gap Detected**

1. Platform Engineering investigates sidecar health
2. If infrastructure failure: Platform Engineering remediates
3. If intentional disablement: escalate to Risk and Legal
4. Risk assesses operational impact
5. Legal evaluates disclosure obligations

**Disclosure Request Received**

1. Legal reviews request scope
2. Legal determines validity (valid | overbroad | privileged)
3. If valid: Legal approves with scope constraints
4. Security validates requester identity
5. Platform Engineering generates disclosure
6. Legal delivers package

**Compromise Suspected**

1. Security leads incident response
2. Platform Engineering assists with forensics
3. Legal assesses obligations (breach notification)
4. Risk coordinates with insurers
5. Finance assesses financial impact

### 10.3 Claims Incompatible with CVS-Conforming Status

A deployment making any of the following claims is not accurately described as a CVS-conforming implementation:

- that it guarantees correctness
- that it guarantees truth
- that it prevents wrongdoing
- that it enforces compliance
- that it replaces legal or regulatory judgment
- that it provides complete system coverage where no Declared Observation Surface is explicitly documented
- that it guarantees insurance premium reduction
- that it guarantees regulatory approval or audit success
- that it provides automatic fraud prevention
- that it provides autonomous compliance enforcement

The CVS architecture provides cryptographic evidence of observation. It does not certify behaviour, outcomes, or legal sufficiency.

---

## 11. Deployment Topologies

The topologies described in this section are illustrative. Operators are responsible for selecting and validating infrastructure appropriate to their security posture, data sovereignty requirements, and operational constraints.

### 11.1 On-Premises Model

On-premises deployments are typical for regulated industries — healthcare, defence, financial services — where data sovereignty and air-gap requirements exist.

**Architecture Diagram**

```
┌─────────────────────────────────────────────┐
│           On-Premises Network                │
│                                             │
│  ┌──────────┐      ┌────────────────┐      │
│  │Observed  │─obs─→│ CVS Sidecar(s) │      │
│  │Systems   │      │ (Capture VLAN) │      │
│  └──────────┘      └────────┬───────┘      │
│                             │              │
│                   ┌─────────▼────────┐     │
│                   │ Evidence Store   │     │
│                   │ (WORM/MinIO)     │     │
│                   └─────────┬────────┘     │
│                             │              │
│                   ┌─────────▼────────┐     │
│                   │ Access Plane     │     │
│                   │ (DMZ VLAN)       │     │
│                   └─────────┬────────┘     │
└─────────────────────────────┼──────────────┘
                              │
               ┌──────────────▼──────────────┐
               │ Interpretation Tools        │
               └─────────────────────────────┘
```

**Network Isolation Rules**

- **MUST** place production systems in a dedicated VLAN with no direct Evidence Store access
- **MUST** place CVS sidecars in Capture VLAN with outbound-only connectivity
- **MUST** place Evidence Store in Storage VLAN accessible only to sidecars (write) and Access Plane (read)
- **MUST** place Access Plane in DMZ VLAN exposing read-only APIs

**Infrastructure Components**

| Component | Technology | Specification |
|---|---|---|
| CVS Sidecar | Docker/Kubernetes | 4 vCPU, 16 GB RAM, 500 GB SSD |
| Evidence Store | MinIO (S3-compatible) | 10 TB, object lock enabled |
| Access Plane | Docker/Kubernetes | 2 vCPU, 8 GB RAM |
| HSM | Thales Luna/Entrust | FIPS 140-2 Level 3 |

### 11.2 Hybrid Cloud Model

Hybrid deployments are typical for organisations transitioning to cloud or operating across multiple trust boundaries. CVS sidecars run on-premises; Evidence Objects replicate to cloud storage via encrypted tunnel; settlement anchoring occurs from on-premises for low latency; the Access Plane and Interpretation tools run in cloud. Evidence replicates to operator-selected regions with encryption in transit (TLS 1.3) and at rest (AES-256). Evidence replication is append-only.

### 11.3 Fully Cloud-Native Model

Cloud-native deployments are typical for SaaS providers, digital-native enterprises, and organisations without on-premises infrastructure.

**Security Groups**

- Production VPC: Sidecars in separate SG with outbound-only rules
- Evidence Storage VPC: S3 with Object Lock, VPC endpoint restricts access
- Access Plane VPC: ALB with HTTPS-only, rate limiting (WAF), DDoS protection

**Infrastructure Components and Cost** *(illustrative — see §-1.9; XRPL used as example settlement ledger)*

| Component | Technology | Monthly Cost |
|---|---|---|
| CVS Sidecars | ECS Fargate (4 tasks) | $560 |
| Evidence Store | S3 Standard | $34.50 |
| Evidence Archive | S3 Glacier | $1.50 |
| Access Plane | ECS Fargate (2 tasks) | $140 |
| ALB | Application Load Balancer | $25 |
| CloudHSM | AWS CloudHSM | $1,388 |
| Data Transfer | Egress | $45 |
| Settlement | Example ledger (30s batches) | $2.16 |
| **Total** | | **$2,196.16** |

### 11.4 Deployment Topology Selection Guide

| Requirement | On-Premises | Hybrid | Cloud-Native |
|---|---|---|---|
| Data sovereignty (strict) | ✓ Best | ✓ OK | ✗ May not comply |
| Air-gap requirement | ✓ Best | ✗ Not possible | ✗ Not possible |
| Rapid scaling | ✗ Slow | ~ Moderate | ✓ Best |
| Low capital expenditure | ✗ High capex | ~ Moderate | ✓ Low capex |
| Existing on-prem infra | ✓ Leverage | ✓ Leverage | ✗ New investment |
| Geographic distribution | ✗ Expensive | ~ Moderate | ✓ Easy |
| Disaster recovery | ~ Manual | ✓ Cloud backup | ✓ Built-in |

---

## 12. API Specification

### 12.1 Authentication and Rate Limiting

All APIs require authentication. Machine-to-machine clients use API keys (Bearer token); user-facing tools use OAuth 2.0 (authorisation code flow). Rate limiting defaults to 1,000 requests/hour per API key, is configurable per API key, and exposes headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`.

```
Authorization: Bearer <api_key>
Base URL: https://evidence.example.com/api/v1
```

### 12.2 Complete API Reference

**GET /replay** — Retrieve time-ordered Evidence Objects with filtering

| Parameter | Type | Required | Description |
|---|---|---|---|
| start | ISO 8601 | Yes | Start of time window (inclusive) |
| end | ISO 8601 | Yes | End of time window (inclusive) |
| source_system_id | string | No | Filter by source system |
| event_type | string | No | Filter by event type |
| correlation_id | string | No | Filter by correlation ID |
| limit | integer | No | Max results (default 1000, max 10000) |
| offset | integer | No | Pagination offset (default 0) |

**GET /proof** — Generate Merkle inclusion proof for specific Evidence Object

Query Parameters: `evidence_id` (string, required)
Response: Complete Proof Bundle (see §2.2 schema)

**GET /batch** — Retrieve metadata for settlement batch

Query Parameters: `batch_id` (string, required)

```json
{
  "batch_id":    "batch_2027-03-15_1432",
  "time_window": {
    "start": "2027-03-15T14:32:00.000Z",
    "end":   "2027-03-15T14:33:00.000Z"
  },
  "object_count":     "1247",
  "merkle_root":      "sha256:7d4b9a2f...",
  "settlement_anchor": {
    "ledger":           "xrpl",
    "transaction_id":   "E7F4A9B2...",
    "ledger_timestamp": "2027-03-15T14:32:23.000Z"
  }
}
```

**GET /anchor** — Retrieve and verify settlement anchor from public ledger

Query Parameters: `transaction_id` (string, required)

```json
{
  "ledger":                  "xrpl",
  "transaction_id":          "E7F4A9B2...",
  "ledger_timestamp":        "2027-03-15T14:32:23.000Z",
  "anchored_root":           "sha256:7d4b9a2f...",
  "verification_status":     "confirmed",
  "ledger_query_timestamp":  "2027-03-15T16:45:12.000Z"
}
```

Verification Status Values: `confirmed` (transaction exists, root matches); `pending` (submitted but not finalised); `not_found` (transaction ID not found).

---

## 13. Budget and Infrastructure Modelling

> **§-1.9 Disclaimer applies to this entire section.** All figures are illustrative. No financial outcome is guaranteed. Operators must conduct their own infrastructure analysis for their specific deployment requirements.

### 13.1 Infrastructure Cost Model — Tier 2 (1,000 events/sec)

| Component | Specification | Monthly Cost | Annual Cost |
|---|---|---|---|
| CVS Sidecar | EC2 m6i.xlarge (4 vCPU, 16GB) | $140 | $1,680 |
| Access Plane | EC2 m6i.large (2 vCPU, 8GB) | $70 | $840 |
| Evidence Store (first 90d) | S3 Standard, 1.5TB/month new | $34.50 | $414 |
| Evidence Archive (>90d) | S3 Glacier, cumulative growth | +$1.50/mo | +$18/yr |
| Settlement Anchoring (example ledger) | 86,400 anchors/month (30s) | $2.16 | $26 |
| Data Transfer Out | 500GB/month | $45 | $540 |
| Monitoring | CloudWatch Metrics + Logs | $20 | $240 |
| **Total Month 1** | | **$313.16** | — |
| **Total Steady-State** | | **~$340** | **~$4,080** |

### 13.2 Engineering Effort Estimate

**Initial Deployment (First 90 Days)**

| Role | Hours | Rate | Cost |
|---|---|---|---|
| Platform Engineering | 220 | $150/hr | $33,000 |
| Security | 120 | $175/hr | $21,000 |
| Legal | 100 | $400/hr | $40,000 |
| Data Engineering | 90 | $150/hr | $13,500 |
| **Total** | | | **$107,500** |

**Ongoing Maintenance (Annual)**

| Role | Hours | Rate | Cost |
|---|---|---|---|
| Platform Engineering | 180 | $150/hr | $27,000 |
| Security | 80 | $175/hr | $14,000 |
| **Total** | | | **$41,000** |

### 13.3 Illustrative Insurance Premium Impact

**Manufacturing Example** *(illustrative — see §-1.9)*

Baseline premium: $200,000/year. CVS evidence infrastructure directionally supports a 10–15% reduction. Illustrative annual savings: $20,000–30,000/year.

**Financial Services Example** *(illustrative — see §-1.9)*

Baseline E&O + Cyber Liability: $2,000,000/year. Regulatory penalties: $500,000/year average. Directional impact: 10–20% reduction plus penalty avoidance potential. Illustrative annual savings: $450,000–900,000/year total.

### 13.4 First-Year Cost Analysis *(illustrative — see §-1.9)*

| Item | Cost |
|---|---|
| Infrastructure (Year 1) | $3,778 |
| Engineering (initial deployment) | $107,500 |
| Engineering (maintenance, 9 months) | $30,750 |
| **Total First-Year Investment** | **$142,028** |

| Benefit Category | Conservative | Optimistic |
|---|---|---|
| Insurance premium reduction | $20,000 | $30,000 |
| Audit cost reduction | $130,000 | $217,000 |
| Penalty avoidance | $0 | $125,000 |
| **Total First-Year Benefit** | **$150,000** | **$372,000** |

Conservative net: +$7,972 (6%)
Optimistic net: +$229,972 (162%)
Payback Period: Conservative 11 months | Optimistic 5 months

### 13.5 5-Year Total Cost of Ownership *(illustrative)*

- 5-Year Total Cost: $322,828
- 5-Year Net Benefit (Conservative): +$427,172 (132% total ROI)
- 5-Year Net Benefit (Optimistic): +$2,179,172 (675% total ROI)

---

## 14. Regulatory and Legislative Alignment

CVS architecture is designed to be regulatory-agnostic. The architecture does not prescribe or guarantee compliance outcomes. This section identifies regulatory frameworks whose record-keeping, logging, and evidentiary requirements are structurally consistent with what CVS produces. Whether any specific deployment satisfies any specific obligation is a legal determination requiring independent analysis by qualified counsel in the applicable jurisdiction.

Organisations must obtain independent legal advice on obligations in their specific jurisdictions before representing CVS evidence in any formal proceeding.

### 14.1 European Union AI Act (Regulation EU 2024/1689)

The EU AI Act entered into force August 2024. Obligations phase in through 2027.

**Article 9 — Risk Management System.** High-risk AI systems must maintain risk management documentation including records of system operation. CVS provides independent evidence infrastructure relevant to this record-keeping requirement: Evidence Objects capture what the system did, at what time, with what outcome, independently of the system operator's control.

**Article 12 — Record-Keeping.** High-risk AI systems must automatically generate logs allowing for post-market monitoring. Logs must be retained for at least 6 months for systems listed in Annex III. CVS provides WORM storage with configurable retention and hash-chained integrity that self-attests against tampering, supporting this requirement.

**Article 26 — Obligations of Deployers.** Deployers must monitor system operation and report serious incidents. CVS produces an independently verifiable event record relevant to this monitoring requirement. Incident reports that include CVS evidence chains contain independently verifiable, tamper-evident records, structurally distinguishable from reports relying solely on operator-controlled internal logs.

**Article 72 — Fundamental Rights Impact Assessment.** Public authorities deploying high-risk AI must conduct impact assessments. CVS provides the operational record infrastructure that can support retrospective verification of whether systems operated within declared parameters.

**Timeline:** Prohibited practices rules from February 2025. GPAI model obligations from August 2025. High-risk AI system obligations from August 2026.

### 14.2 Digital Operational Resilience Act (DORA — Regulation EU 2022/2554)

DORA is directly applicable to financial entities in the EU from January 2025.

**Article 8 — ICT Risk Management.** Financial entities must identify, classify, and document ICT assets and risks. CVS evidence chains provide operational records cryptographically verifiable against a public anchor, relevant to ICT risk management documentation requirements.

**Article 9 — Protection and Prevention.** Financial entities must have policies to detect anomalous ICT activity. CVS gap detection — silence on declared surfaces triggers `coverage_gap_detected` — produces a structured, independently verifiable record of evidentiary discontinuity, structurally consistent with anomaly detection documentation requirements.

**Article 10 — Detection.** Financial entities must implement mechanisms to promptly detect anomalous activities including ICT-related incidents. CVS evidence chains support time-deterministic incident reconstruction.

**Article 17 — ICT-Related Incident Classification.** Financial entities must classify incidents and report major incidents to competent authorities. CVS-backed incident reports contain independently verifiable records that are structurally distinguishable from self-declared internal logs, relevant to the classification and reporting process.

**Scope:** Credit institutions, payment institutions, investment firms, insurance undertakings, and ICT third-party service providers providing services to these entities.

### 14.3 Network and Information Security Directive 2 (NIS2 — Directive EU 2022/2555)

NIS2 was transposed into national law across EU member states by October 2024.

**Article 21 — Cybersecurity Risk Management Measures.** Essential and important entities must implement measures including logging and monitoring capabilities. CVS provides logging infrastructure that is architecturally independent from the systems being logged — a critical distinction when insider threats can compromise co-located logging systems — and is relevant to this requirement.

**Article 23 — Reporting Obligations.** Entities must notify significant incidents to national authorities. CVS evidence chains provide independently verifiable records relevant to the notification process, structurally distinguishable from internal logs maintained under operator control.

**Categories covered:** Energy, transport, banking, financial market infrastructure, health, drinking water, wastewater, digital infrastructure, ICT service management, public administration, space.

### 14.4 SEC Cybersecurity Disclosure Rules (US — Effective December 2023)

**Item 1.05 Form 8-K.** Public companies must disclose material cybersecurity incidents within 4 business days of determining materiality. CVS evidence chains provide independently verifiable records relevant to materiality determination and the factual basis of disclosure.

**Item 106 Regulation S-K.** Public companies must describe their cybersecurity risk management processes, governance, and material risks in annual reports (Form 10-K). CVS deployment provides independently verifiable evidence infrastructure structurally consistent with this disclosure requirement.

### 14.5 NIST AI Risk Management Framework (AI RMF 1.0 — 2023)

NIST AI RMF is voluntary but increasingly referenced by US regulators as the baseline for AI governance.

**GOVERN 1.2.** Policies, processes, procedures, and practices across the organisation related to AI risk must be in place, transparent, and implemented effectively. CVS evidence chains produce independently verifiable observation records: what governance policies existed at execution time, that constraint evaluation occurred against those policies, and what the per-invariant outcomes were.

**MEASURE 2.5.** The AI system to be deployed must be demonstrated to be valid and reliable through sound statistical and domain-informed model evaluation metrics. CVS inference event records — capturing model identifier, version hash, input hash, output hash, timestamp — provide operational validation records relevant to this function.

**MANAGE 2.4.** Residual risks or system performance falling below acceptable thresholds must be managed, documented, and monitored. CVS gap detection and failure classification matrix are directly relevant to residual risk monitoring requirements.

### 14.6 OSFI Operational Resilience Guideline (Canada — B-10 — Effective November 2024)

**Principle 5 — Incident Response.** Federally regulated financial institutions must maintain documented, tested incident response capabilities. CVS evidence chains support faster incident reconstruction, a capability relevant to B-10 compliance.

**Third-Party Risk.** B-10 requires robust management of technology and cyber risks introduced by third-party arrangements. CVS cross-organisation evidence workflows — where both parties produce independently verifiable records for the same event sequence — provide evidentiary infrastructure relevant to third-party risk management.

### 14.7 APRA Prudential Standard CPS 230 (Australia — Effective July 2025)

**Section 41 — Severe but Plausible Scenarios.** Entities must identify and assess severe but plausible operational disruption scenarios. CVS gap taxonomy (Validation Gap, Evidence Gap, Settlement Gap, Coverage Gap) provides a structured framework for scenario analysis relevant to CPS 230's requirements.

**Section 58 — Business Continuity Planning.** Service disruptions must be detected, communicated, and resolved within defined tolerance levels. CVS fail-open behaviour and explicit gap detection support evidence gap detection within seconds of occurrence.

### 14.8 UK DPDI Act and ICO AI Auditing Framework

**Accountability.** Organisations must demonstrate that automated decisions comply with data protection principles. CVS evidence chains — capturing AI agent decisions with input/output hashes, model version identifiers, and validation outcomes — provide infrastructure relevant to this accountability requirement.

**Subject Access Requests (SARs).** Individuals have the right to information about automated decisions affecting them. CVS selective disclosure, via the Disclosure Kernel, enables scoped disclosure of evidence relevant to a specific individual's request without exposing unrelated operational data.

### 14.9 GDPR Evidence Handling (EU 2016/679)

**Article 5(2) — Accountability.** Controllers must demonstrate compliance. CVS produces cryptographically verifiable records of observation. These records are structurally distinguishable from self-declared compliance assertions in that their integrity is independently verifiable against a public settlement anchor rather than relying on operator attestation alone.

**Article 30 — Records of Processing Activities.** Controllers must maintain records of processing. CVS Evidence Objects are structurally consistent with processing records for automated systems and are independently verifiable against the settlement layer.

**Data Minimisation Constraint.** CVS payload-hash-not-payload design is consistent with GDPR data minimisation requirements. Evidence Objects record that a specific payload was processed without storing the payload itself.

**Right of Erasure Interaction.** Evidence Objects contain payload hashes, not personal data. Erasure obligations under Article 17 apply to the original data, not to evidence that the data was processed. Organisations should obtain independent legal advice on the interaction between retention obligations (Article 5(1)(e)) and erasure rights in their specific deployment context.

---

## 15. Jurisdictional Deployment Considerations

### 15.1 Data Residency

Evidence Objects contain payload hashes, not payload content. In most jurisdictions, hash values of personal data are not themselves personal data — the hash does not reconstruct the original. However, legal analysis varies by jurisdiction and context. Organisations should confirm the classification of Evidence Objects with their legal counsel before cross-border replication. The guidance below is general orientation only and is not legal advice.

EU: Evidence Objects are likely not personal data under GDPR (no reconstruction possible from hash). US: No federal classification; state-specific analysis may be required in California (CCPA) and other states. Canada: PIPEDA and provincial privacy laws; likely not personal information for the same reasons. UK: Post-Brexit GDPR-aligned; similar analysis to EU.

### 15.2 Financial Services Regulatory Perimeters

**EU (MiFID II / EMIR / DORA):** Trade records must be retained for 5 years. Evidence Objects support retention requirements with immutability stronger than mutable internal systems. DORA ICT incident records must be retained for 5 years.

**US (SEC Rule 17a-4 / FINRA 4511):** Broker-dealers must maintain records in WORM format with third-party download capability. S3 Object Lock with compliance mode is consistent with Rule 17a-4 WORM requirements. CVS evidence chains add tamper-evident chaining and public settlement anchoring to this foundation.

**Canada (OSFI):** Record retention requirements under B-10 align with the WORM storage model. Independent verification via public ledger produces records structurally consistent with retention requirements.

**Australia (APRA CPS 234 / CPS 230):** Security control documentation must be retained and independently verifiable. CVS structural authority separation supports the independence requirement.

### 15.3 Healthcare Deployment Considerations

**EU MDR (Medical Device Regulation 2017/745):** Software integral to a medical device may be regulated. Sidecar software operating in observe-only mode, with no pathway to influence clinical decisions, is unlikely to meet the definition of medical device software — but organisations must conduct their own classification analysis.

**US HIPAA:** CVS Evidence Objects contain payload hashes, not Protected Health Information (PHI). Where event descriptors include information that could identify patients, PHI handling obligations apply to those descriptors. Organisations should configure event descriptors to minimise PHI exposure surface.

**Canada PHIPA (Ontario) / Health Information Act (Alberta):** Similar PHI handling analysis applies. Hash-not-payload design minimises but does not eliminate health information handling obligations where event descriptors identify individuals.

---

## 16. Conformance Requirements

### 16.1 Mandatory Behaviors (MUST)

**Access Plane Requirements**

1. **Read-Only Interface** — The Access Plane **MUST** expose read-only APIs exclusively. No write, update, or delete operations are exposed to external consumers. IAM policies enforce read-only permissions. *Verification: Attempt to write via API returns HTTP 403 or 405.*

2. **Gap Reporting** — Replay queries **MUST** return explicit gap markers when evidence chains are discontinuous. Gap metadata **MUST** include: start timestamp, end timestamp, duration, resumption indicator. Gaps are never smoothed, interpolated, or concealed. *Verification: Introduce intentional sidecar failure; confirm gap appears in replay.*

3. **Independent Verification** — Proof bundles **MUST** be self-contained and independently verifiable. The open-source verification tool **MUST** be the sole mechanism required for verification. The tool **MUST** perform all checks — hash match, Merkle inclusion, settlement anchor confirmation, and timestamp consistency — without operator involvement. No vendor credentials, proprietary software, operator-hosted endpoints, or payment of any kind **MUST** be required. *Verification: A third party with no operator relationship executes the open-source tool against a Proof Bundle and receives a passing result.*

4. **Deterministic Replay Ordering** — Primary sort: `observation_timestamp` ascending. Secondary sort: `evidence_object_id` (stable tiebreaker). *Verification: Identical query executed twice returns identical results.*

5. **Settlement Anchor Validation** — The Proof Service **MUST** query the settlement ledger directly (not via operator proxy). Anchor verification uses public ledger RPC endpoints.

6. **Evidence Store Immutability** — Evidence Objects **MUST** be stored with WORM semantics. Object modification and deletion **MUST** be disabled at the storage layer.

**Interpretation Plane Requirements**

7. **Separate Artifact Storage** — Interpretation artifacts **MUST** be stored separately from the Evidence Store. Interpretation outputs are never written to the Evidence Store.

8. **Attestation Logging** — All disclosure requests **MUST** be logged as evidence. Disclosure logs are hashed, chained, and anchored.

### 16.2 Behaviours Disqualifying Conformance

A deployment exhibiting any of the following behaviours is not conforming.

**Access Plane**

A deployment is not conforming in its Access Plane if it:

- modifies Evidence Objects
- smooths, interpolates, or conceals gaps
- requires vendor-specific verification tools for independent verification
- requires payment to the operator in order to verify evidence
- allows settlement anchoring to block execution

**Interpretation Plane**

A tool is not conforming in its Interpretation Plane behaviour if it:

- injects new Evidence Objects
- claims authority over evidence correctness
- reconstructs missing evidence

### 16.3 Claims Incompatible with CVS-Conforming Status

A deployment making any of the following claims is not accurately described as a CVS-conforming implementation:

- that CVS guarantees insurance payout
- that CVS ensures regulatory compliance
- that CVS eliminates liability
- that CVS guarantees correctness
- that CVS replaces audits
- that the deployment is regulatorily sufficient for any jurisdiction
- that the deployment has been certified, approved, or validated by any regulator, standards body, or authority

CVS records evidence only. All determination of sufficiency, significance, and legal effect is external to the architecture.

### 16.4 Conformance Verification Checklist

| Test | Expected Result | Pass/Fail |
|---|---|---|
| Attempt HTTP POST to /replay | Returns 405 Method Not Allowed | [ ] |
| Attempt to modify Evidence Object via API | Returns 403 Forbidden | [ ] |
| Attempt to overwrite Evidence Object | Operation fails (WORM enforced) | [ ] |
| Restore from backup | Restored evidence matches original hash | [ ] |
| Execute same query twice | Results identical (same order) | [ ] |
| Execute query from different API keys | Results identical | [ ] |
| Query ledger directly | Anchored root matches proof bundle | [ ] |
| Check interpretation artifact location | Not stored in Evidence Store | [ ] |
| Attempt to write artifact to Evidence Store | Operation fails (permission denied) | [ ] |
| Execute disclosure request | Disclosure log entry created | [ ] |
| Check disclosure log contents | Includes requester, query, timestamp | [ ] |
| DOS published and anchored | DOS hash retrievable from Settlement Layer | [ ] |
| Coverage Attestation emitted | Attestation appears at defined interval | [ ] |
| **Evidence Gap — Detection** | | |
| Stop sidecar for 5 minutes, restart | `gap_record` Evidence Object written on recovery | [ ] |
| Evidence Gap — gap_record fields | Includes `gap_start`, `gap_end`, `cause_code`, `resumption_evidence_id` | [ ] |
| Evidence Gap — chain continuity | `gap_record.previous_evidence_hash` = last pre-gap object hash | [ ] |
| Evidence Gap — replay visibility | Gap marker appears in Replay Service response spanning window | [ ] |
| Evidence Gap — no interpolation | Replay returns gap marker, not fabricated continuity | [ ] |
| **Settlement Gap — Detection** | | |
| Block ledger access for 35 minutes | `settlement_gap_detected` Evidence Object emitted | [ ] |
| Settlement Gap — Proof Service reporting | Proof Bundle for queued object carries `settlement_status: pending` | [ ] |
| Settlement Gap — queue flush | On reconnection, queued batches flushed in chronological order | [ ] |
| Settlement Gap — batch integrity | Flushed batches retain original window timestamps and Merkle roots | [ ] |
| Settlement Gap — replay visibility | Replay response for gap window includes settlement gap indicator | [ ] |
| **Coverage Gap — Detection** | | |
| Silence declared surface beyond threshold | `coverage_gap_detected` Evidence Object emitted | [ ] |
| Coverage Gap — required fields | Includes `surface_id`, silence start timestamp, silence duration, `dos_hash` | [ ] |
| Coverage Gap — Coverage Attestation | Silent surface appears in `silent_surfaces` field of attestation | [ ] |
| Coverage Gap — replay visibility | `coverage_gap_detected` retrievable via `surface_id` filter | [ ] |
| **Validation Gap — Detection** | | |
| Silence Commit Gate surface beyond threshold | `coverage_gap_detected` emitted for gate `surface_id` | [ ] |
| Validation Gap — surface declared in DOS | Commit Gate event stream present as declared surface | [ ] |
| Validation Gap — replay visibility | Gap queryable by Commit Gate `surface_id` | [ ] |
| **Verification Tooling** | | |
| Open-source tool available | Tool published under open licence, no registration required | [ ] |
| Open-source tool — hash check | Tool verifies Evidence Object hash against canonical serialisation | [ ] |
| Open-source tool — Merkle check | Tool verifies Merkle inclusion proof against batch root | [ ] |
| Open-source tool — anchor check | Tool queries settlement ledger directly; confirms anchored root | [ ] |
| Open-source tool — timestamp check | Tool verifies timestamp consistency across Evidence Object, batch, anchor | [ ] |
| Open-source tool — no operator dependency | Tool completes all checks with no operator-hosted endpoint | [ ] |
| Open-source tool — no payment | Tool executes without payment, credential, or registration | [ ] |
| Open-source tool — failure behaviour | Tool returns non-zero exit code when any check fails; does not return "valid" on partial pass | [ ] |

**Conformance is binary.** A single failure on any mandatory behaviour test is non-conformance. There is no partial conformance tier. A partially conformant implementation is a non-conformant implementation. When a test fails: document the failure with precise reproduction steps; remediate the implementation; retest from the beginning of the checklist. Conformance is established by completing the full checklist from the beginning following any remediation — completing only the previously failing test does not establish conformance, as remediation of one failure may introduce regressions elsewhere. The conformance definition includes no exception category.

| Result | Condition |
|---|---|
| Conformant | All mandatory behaviour tests pass |
| Non-Conformant | One or more mandatory behaviour tests fail |

---

## 17. Attack Vectors

**Evidence Fabrication** — An attacker attempts to inject a false Evidence Object into a chain, creating a record of an event that did not occur.
*Mechanism:* The attacker crafts an Evidence Object with a plausible hash and submits it directly to the Evidence Store, bypassing the sidecar.
*Defense:* The Evidence Store enforces write access exclusively from the Capture Plane IAM role. Evidence Objects must be signed by the attestation key held in the HSM. An unsigned or incorrectly signed object fails verification.
*Residual risk:* If an attacker compromises the Capture Plane IAM role and the HSM simultaneously, fabrication becomes possible. This requires defeating two independent security boundaries.

**Evidence Backdating** — An attacker attempts to insert an Evidence Object with a falsified timestamp earlier than its actual creation time, altering the apparent sequence of events.
*Mechanism:* The attacker manipulates the sidecar host clock or constructs an Evidence Object with a past timestamp before submission.
*Defense:* Settlement anchors carry an independent ledger-confirmed timestamp. An Evidence Object with a timestamp earlier than the settlement anchor of the batch it appears in is flagged as a timestamp anomaly by the Proof Service. Clock manipulation on the sidecar host is detectable via NTP drift monitoring.
*Residual risk:* Timestamp anomalies are flagged but not discarded. An attacker who can manipulate both the host clock and the settlement timing faces an extremely narrow window. Intra-batch ordering is the primary remaining exposure.

**Gap Suppression** — An attacker or operator attempts to conceal a discontinuity in the evidence chain, presenting a continuous record where gaps exist.
*Mechanism:* The operator modifies the Replay Service response to exclude gap markers, or deletes gap records from the Evidence Store.
*Defense:* Evidence Objects are stored with WORM semantics — deletion is disabled at the storage layer. Settlement anchors prove what objects existed at each batch window. A missing Evidence Object between two anchored batches is detectable by any independent verifier comparing chain sequence against batch contents.
*Residual risk:* A gap at the very tail of the chain — after the last anchor — is not yet publicly provable until the next anchor is committed. This window equals the configured batch interval (default 30 seconds).

**Evidence Store Compromise** — An attacker gains write access to the Evidence Store and modifies stored Evidence Objects.
*Mechanism:* The attacker exploits misconfigured IAM policies or a storage-layer vulnerability to overwrite or replace existing objects.
*Defense:* S3 Object Lock (compliance mode) or equivalent WORM storage prevents modification even by the account owner. IAM policies restrict the Evidence Store to append-only from the Capture Plane role and read-only from the Access Plane role. Network segmentation prevents direct access from outside the Storage VLAN.
*Residual risk:* A storage administrator with both IAM and WORM override capability — typically requiring AWS root account or equivalent — could defeat this defense. Dual authorisation requirements for account-level operations are an operational control that cannot be architecturally enforced.

**Settlement Wallet Compromise** — An attacker drains the settlement wallet, preventing new anchors from being submitted.
*Mechanism:* The attacker compromises the settlement wallet's signing key and transfers funds out.
*Defense:* The settlement wallet holds only a minimal balance (~$100–500). Draining it creates a denial-of-service against future anchoring but does not alter historical anchors, which are already recorded on an immutable public ledger.
*Residual risk:* A wallet drain creates a settlement gap for the period until the wallet is replenished and anchoring resumes. Evidence observation continues during this period; evidence is queued locally.

**Proprietary Lock-In** — A vendor implements CVS in a way that makes independent verification depend on the vendor's proprietary software, defeating the open verification guarantee.
*Mechanism:* The vendor uses non-standard hash functions, proprietary serialisation formats, or encrypts Proof Bundles such that only the vendor's tooling can decode them.
*Defense:* A CVS-conforming implementation uses only standard hash functions, canonical serialisation with defined rules, and provides open-source verification tooling. A conformant implementation is independently verifiable with public-domain tools. A deployment requiring payment for verification does not meet the conformance definition.
*Residual risk:* A vendor may claim conformance while not providing open-source tooling. Independent verification of the conformance claim itself requires running the checklist, which includes testing open-source tool availability.

**Cross-Tenant Evidence Access** — In a multi-tenant deployment, a requester attempts to access evidence from a tenant they are not authorised for.
*Mechanism:* The attacker uses an API key authorised for Tenant A to query evidence associated with Tenant B, exploiting misconfigured access control or query parameter injection.
*Defense:* The Disclosure Kernel validates `tenant_id` binding before any evidence is retrieved. A request for evidence outside the requester's authorised tenant returns HTTP 404 — not 403 — to avoid revealing the existence of other tenants. WORM storage prefixes are tenant-scoped at the IAM level, not the application level.
*Residual risk:* Misconfigured `tenant_id` assignment during onboarding could result in evidence being written to or readable from the wrong prefix. This is a deployment error, not an architectural vulnerability. Deployment verification procedures must include tenant isolation testing.

---

## Conclusion

`CVS_IMPLEMENTATION_v1.4.md` describes implementation patterns for evidence access, interpretation interfaces, enterprise system integration, and the regulatory landscape in which evidence operates. The patterns described are illustrative and non-exhaustive. The architecture preserves the core witness-only, fail-open, externally verified constraint model established in `CVS_ARCHITECTURE_v{M}.{m}.md`.

CVS does not block execution. It records evidence only. All determination of the significance, sufficiency, and legal effect of that evidence rests with the organisations, regulators, insurers, and courts that act on it.

The Access Plane delivers a read-only evidence surface through Evidence Store (WORM), Proof Service (Merkle verification), and Replay Service (time-ordered retrieval). The Interpretation Plane remains external — tools consume evidence without altering it. System integration requires zero code changes — adapters tap into existing observability infrastructure. Multi-vendor interoperability is mechanical — portable Evidence Objects, open-source verification. Security is defence-in-depth — plane isolation, IAM boundaries, HSM key custody. Deployment topologies are operator-selected — on-premises, hybrid, or fully cloud-native. Regulatory alignment is mapped as relevance, not sufficiency — operators obtain independent legal analysis for their specific jurisdictions and obligations. Conformance is verifiable and binary — mandatory behaviours, disqualifying behaviours, and a pass/fail checklist with no partial tier. Coverage is explicit — DOS manifests declare observation boundaries; silence is evidentiary. Deployment responsibility is operator-held — the author provides architecture; operators provide analysis, decisions, and accountability.

The architecture's authority derives from constraints, not control. Evidence generation is disjoint from evidence access. Evidence access is disjoint from evidence interpretation. These planes never collapse. The separation is structural, not administrative.

---

*The next phase is deployment. Operators own that phase entirely.*

---

## Document Control

| Field | Value |
|---|---|
| Document | `CVS_IMPLEMENTATION_v2.7.md` |
| Version | 2.7 |
| Publication Date | May 2026 |
| Authors | Jonathan M. Watson |
| Repository | github.com/JonathanMastersWatson/Evidence-Sidecar |
| Normative Dependencies | `512_ARCHITECTURE_v3.4.md`; `CVS_ARCHITECTURE_v3.2.md` |
| License | Apache 2.0 |
| Contact | evidence-admin@512.systems |

### Changelog — v2.7

**May 2026 — competitive landscape and priority record cross-references.**

**Additions:**
- §0.8 Companion Reference Documents: new subsection — `VCP_AND_CVS.md` (parallel development acknowledgment) and `CANONICAL_COMMITMENT.md` (permanent priority and dated proof record).
- Document Control: Status updated to Active.

**Modifications:**
- §0.1, §0.2, §0.5: Cross-references updated from `512_ARCHITECTURE_v3.2.md` to `512_ARCHITECTURE_v3.4.md`.
- §0.3: CVS_ARCHITECTURE normative dependency updated to reference `CVS_ARCHITECTURE_v3.2.md`.
- Document Control table: version corrected from v2.4 to v2.6 (prior entry omitted table update); now advanced to v2.7. Publication date updated March 2026 → May 2026.

**Removals:** Nothing removed.

---

### Changelog — v2.6

**Hardening pass — April 2026 repository alignment and cross-reference update.**

**Modifications:**
- §0.1, §0.2, §0.5: Cross-references updated from `512_ARCHITECTURE_v3.0.md` to `512_ARCHITECTURE_v3.4.md` following architecture version bump.
- §3.1 Observation Point 2 (Validation Result): fail-open observation path alignment confirmed — validation_result is absent on fail-open events; gap_record replaces it. Per-constraint unevaluated state distinguished from overall evidence chain gap.
- §7 Conformance Requirements: GATE_OUTPUT_MATRIX.md cross-reference added — the five-scenario gate output and witness classification matrix defining the relationship between gate completion states and CVS classifications.
- §7.1 Mandatory Behaviours / §7.2 Prohibited Behaviours: alignment confirmed with GATE_OUTPUT_MATRIX.md critical semantic rules — unevaluated is never pass; gap record is not a gate output; gap record and unevaluated are distinct; ALLOW requires all seven constraints evaluated and passed.

**Additions:**
- Document Control: Status field added — Pre-Seal Hardening.

**Removals:** Nothing removed.

---

### Changelog — v2.5

**Pre-hardening pass. Primitive boundary declaration. Cross-reference update.**

**Additions:**
- Document header: pre-hardening phase notice callout linking to repository `PRE_HARDENING_NOTICE.md`
- §0.7 Primitive Boundary: CVS defines evidence formation at the execution boundary; does not define system architecture, orchestration, deployment models, or implementation patterns; derivative responsibility rests entirely with the implementing party

**Modifications:**
- §0.2 and §0.5: Cross-references updated from `512_ARCHITECTURE_v2.0.md` to `512_ARCHITECTURE_v3.4.md` following architecture major version bump
- §0.1 canonical document hierarchy table: `512_ARCHITECTURE_v2.0.md` updated to `512_ARCHITECTURE_v3.4.md`
- Version 2.4 → 2.5; date March 2026 → April 2026

**Removals:** Nothing removed.

---

### Changelog — v2.4

**ANTI_DRIFT §13 language alignment pass.**

**Modifications:**
- §3.1 diagram: "Compliance" label in Interpretation Plane ASCII diagram → "Conformance" — ANTI_DRIFT §13: compliance → conformance
- §3.1 diagram: "Compliance Tool C" box label → "Conformance Tool C" — ANTI_DRIFT §13: compliance → conformance
- §8.3, §11.3 cost tables: "Monitoring" row → "Observability" — ANTI_DRIFT §13: monitoring → observation
- §9.5: "**Continuous Monitoring**" heading → "**Continuous Observation**" — ANTI_DRIFT §13: monitoring → observation
- §4.3.1: "An implementation MAY deploy CVS partially" → "An implementation MAY partially instrument with CVS" — ANTI_DRIFT §13: deploy CVS → instrument with CVS

**Additions:** Nothing added.
**Removals:** Nothing removed.

---

### Changelog — v2.3

**Document identity fix. Legal section consolidation.**

**Modifications:**
- H1: Corrected from `CVS_IMPLEMENTATION_v1.4.md` to `CVS_IMPLEMENTATION_v2.3.md` — eliminates document identity mismatch present since v2.0
- §-1 through §-X: Consolidated nine-subsection §-1 block (§-1.1 through §-1.9) plus four-subsection §-X block (§-X.1 through §-X.4) into a single six-subsection §-1 block (§-1.1 Informational Nature; §-1.2 No Warranty; §-1.3 No Reliance; No Certification; No Endorsement; §-1.4 Limitation of Liability; §-1.5 Licensing Posture: 512 Constraint Set vs CVS Specification; §-1.6 License). All protections preserved; duplication removed. Net reduction: approximately 6,100 characters.
- §-1.5: Replaces prior ownership/licensing table and body paragraphs with plain-prose licensing posture statement distinguishing 512 (no licence asserted over constraint set) from CVS (Apache 2.0); operational independence of CVS and 512 explicitly stated
- Document Control: filename updated to `CVS_IMPLEMENTATION_v2.3.md`

**Additions:** Nothing added.
**Removals:** §-1.6 Public Ledger References (merged into §-1.3 no-endorsement coverage); §-1.7 License (content consolidated into §-1.6); §-1.8 Jurisdictional Scope (protection preserved in §-1.4); §-1.9 Financial Projections Disclaimer (protection preserved in §-1.1 and §-1.2); §-X.1 through §-X.4 (protections consolidated into §-1.3).

---

### Changelog — v2.2

**Conformance and tone hardening for Apache compatibility.**

**Modifications:**
- §0.3: "mandatory and prohibited capabilities" replaced with "mandatory behaviours and disqualifying characteristics" — removes enforcement-residue term "prohibited"
- §4.3.6: "invalidates completeness claims" replaced with "completeness cannot be established" — removes legal invalidation framing; "The CVS proves" / "The DOS proves" replaced with "The CVS produces a record of" / "The DOS produces a record of" — removes proof-assertion framing; full paragraph rewritten in definitional terms
- §7.1: "this violates conformance" replaced with "use of a proprietary hash function is not conforming" — converts enforcement verb "violates" to definitional non-conformance statement
- §9.8 opening: "No gap type MUST NOT be concealed, smoothed, interpolated, or excluded from replay queries" — grammatical double negative producing ambiguous coercive construction — replaced with "A conforming implementation surfaces each gap type as a structured Evidence Object in the chain. Concealment, smoothing, interpolation, or exclusion from replay queries is not conforming."
- §16.4: "Partial retesting is not accepted" replaced with "Conformance is established by completing the full checklist from the beginning following any remediation — completing only the previously failing test does not establish conformance"; "Documented exceptions are not a conformance category" replaced with "The conformance definition includes no exception category" — converts enforcement-authority phrasing to definitional statements

**Additions:** Nothing added.
**Removals:** Nothing removed.

---

### Changelog — v2.1

**Apache 2.0 alignment pass.**

**Modifications:**
- §-1.5: Heading renamed from "Ownership and Licensing — Open Commons Declaration" to "Ownership and Licensing"; opener rewritten from authorial-intent framing to Apache licence statement; table column renamed from "Authors' Licensing Intent" to "Licensing"; 512 row rewritten from "The authors assert no proprietary claim…and do not intend to do so" to "No licence asserted by authors over the constraint set itself"; CVS base row rewritten from "authors do not assert or intend to assert proprietary control" to Apache 2.0 Section 3 contributor grant statement; body paragraph rewritten from "The authors do not assert proprietary control…and do not intend to do so" and Linux/SMTP/TCP/IP analogy to neutral statement of Apache 2.0 derivative rights
- §-1.7: Explanatory paragraphs rewritten; "not be encumbered by patent assertions" adversarial framing removed; "The project does not assert that patents over derivative implementations are impossible" negative-assertion framing removed; replaced with neutral description of Apache 2.0 rights scope and derivative commercialisation
- §0.2: "open commons model governing both 512 and CVS" replaced with "open licensing model for 512 and CVS" — removes "commons" and "governing" framing; cross-reference to `512_ARCHITECTURE_v3.4 §11` preserved
- Changelog v2.0 entries: CC BY 4.0 references replaced with "prior licence framework" — removes all references to prior licence framework from document body

**Additions:** Nothing added.
**Removals:** Nothing removed.

---

*This document is versioned. Changes require a version bump and changelog entry.*
*Current version: 2.6 | Last updated: April 2026*

**Additions:**
- §-X: No Reliance and No Endorsement — four subsections (§-X.1 through §-X.4) positioned after §-1.9 and before §0. Scope: no-reliance clause distinguishing this document from certification, regulatory sufficiency, audit guarantee, coverage guarantee, and operational fitness representation; no-endorsement clause covering implementations, derivative systems, organisations, ledgers, and commercial deployments, with institutional certification statement framed as factual knowledge claim rather than legal prohibition; independent verification scope clarification distinguishing cryptographic/structural verifiability from legal or institutional validation; builder responsibility clause enumerating eight responsibility areas and expressing authorial non-liability intent without absolute disclaimer language.

**Modifications (legal tone hardening):**
- §-1.1: "published as open infrastructure commons" replaced with "intentionally released as open infrastructure"
- §-1.2: "To the maximum extent permitted" changed to "To the extent permitted"; "All implementation risk rests solely with the deploying organisation" replaced with "The deploying organisation bears primary responsibility for assessing implementation risk and fitness for its intended use"
- §-1.4: "solely responsible" replaced with "responsible"
- §-1.5: Table column renamed from "Ownable?" to "Authors' Licensing Intent"; absolute impossibility language removed; CVS base row rewritten to reference Apache 2.0 release and authorial non-assertion of proprietary control; prior licence attribution statement replaced with Apache 2.0 contributor patent and copyright licence statement; Linux/SMTP/TCP/IP analogy removed
- §-1.7: Licence changed from prior licence framework to Apache License, Version 2.0; patent grant language added explaining Section 3 contributor patent grant; explanatory paragraphs rewritten to remove adversarial framing
- §-1.8: "To the fullest extent" changed to "To the extent"; absolute liability disclaimers reframed as authorial intent statements; zero-consideration absolute liability cap replaced with proportionate context statement; severability clause reframed as intent
- Document Control: license field updated to "Apache 2.0"

**Modifications (conformance language cleanup):**
- §3.2: Renamed from "What Interpretation Tools Must Not Modify" to "Conforming Interpretation Tool Behaviour"; MUST NOT list replaced with definitional qualification criteria
- §4.3.1: "MUST NOT represent partial observation as complete evidentiary coverage" replaced with "A deployment that represents partial observation as complete evidentiary coverage is not a conforming deployment"
- §4.3.5: Renamed from "Prohibited Representations" to "Representations Incompatible with Coverage Conformance"; MUST NOT list replaced with definitional non-conformance criteria
- §7.2: Three MUST NOT bullets replaced with conformance-definition block introduced by "A verification tool qualifies as conforming under this requirement only if it:"
- §10.3: Renamed from "Claims an Implementation Must Not Make" to "Claims Incompatible with CVS-Conforming Status"; MUST NOT claim list replaced with definitional non-conformance framing
- §16.2: Renamed from "Prohibited Behaviors (MUST NOT)" to "Behaviours Disqualifying Conformance"; MUST NOT lists replaced with disqualification framing
- §16.3: Renamed from "Claims the Implementation Must Not Make" to "Claims Incompatible with CVS-Conforming Status"; MUST NOT claim list replaced with definitional non-conformance framing
- §17 Proprietary Lock-In, Defense: "prohibit proprietary hash functions" and "Pay-to-verify is explicitly prohibited" replaced with definitional conformance framing
- Conclusion: "prohibited capabilities" replaced with "disqualifying behaviours"

**Modifications (regulatory implication review):**
- §5.2: "demonstrates the human oversight chain" replaced with "produces a structured, independently verifiable record of the sequence"
- §6.2: "with the granularity required for audit" replaced with "in a structured, independently verifiable form"
- §14 introduction: rewritten to "identifies regulatory frameworks whose record-keeping, logging, and evidentiary requirements are structurally consistent with what CVS produces"
- §14.1 Article 26: comparative credibility claim replaced with structural distinguishability description
- §14.2 Article 9: "functions as an anomaly detection layer" replaced with structurally consistent evidentiary record description
- §14.2 Article 17: "stronger evidentiary foundation" comparative claim replaced with structural distinguishability description
- §14.3 Article 23: "stronger than internal logs alone" comparative claim replaced with structural distinguishability description
- §14.4 Item 1.05: accuracy and factual-basis assurance replaced with "provide independently verifiable records relevant to materiality determination"
- §14.4 Item 106: "concrete, demonstrable risk management infrastructure" replaced with "independently verifiable evidence infrastructure structurally consistent with this disclosure requirement"
- §14.5 GOVERN 1.2: "producing verifiable outcomes" replaced with description of per-invariant observation record
- §14.9 Article 5(2): "demonstration infrastructure…as distinct from self-declared compliance assertions" replaced with structural distinguishability description
- §14.9 Article 30: "serve as processing records" replaced with "are structurally consistent with processing records"
- §15.2 OSFI: "provides capability exceeding baseline requirements" replaced with "produces records structurally consistent with retention requirements"

**Removals:** Nothing removed.

---

*This document is versioned. Changes require a version bump and changelog entry.*
*Current version: 2.0 | Last updated: March 2026*
