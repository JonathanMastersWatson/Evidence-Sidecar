# 512: The Commit Gate — Implementation Reference

**Jonathan M. Watson | 512 / CVS Architecture**
**Version 3.4 | June 2026**
**Canonical Repository:** github.com/JonathanMastersWatson/512
**Canonical Kernel Commitment:** SHA-256: `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5`

---

## §-1 Legal Notice and Limitation of Liability

### §-1.1 Informational Nature

This document provides implementation guidance for engineers building Commit Gates that satisfy 512's observable properties. It does not constitute a product specification, a compliance certification, a standards mandate, or a legal instrument. The authors do not intend this document to create obligations on any party, and nothing herein should be read as doing so except as expressly agreed in a separate written agreement. Implementation results depend on the engineering decisions, deployment environments, and operational practices of those who build from this guide.

### §-1.2 No Warranty

This document and the architectures it describes are provided "as is," without warranty of any kind, express or implied, including but not limited to warranties of merchantability, fitness for a particular purpose, accuracy, completeness, or non-infringement. The authors and contributors make no representation that this document is free from defects, errors, or omissions. Engineers who implement from this guide bear full responsibility for the correctness, safety, and suitability of their implementations.

### §-1.3 No Professional Advice

Nothing in this document constitutes legal, regulatory, financial, insurance, or engineering advice. Organisations evaluating whether their implementation satisfies the properties described here must consult qualified legal counsel, compliance advisors, and licensed engineers appropriate to their jurisdiction and industry. The authors are not responsible for decisions made in reliance on this document.

### §-1.4 No Guarantee of Coverage or Compliance

A gate implementation built from this guide does not automatically guarantee regulatory compliance, insurance coverage, litigation defence, or audit passage. Compliance is a legal determination made by regulators and courts. Coverage is an underwriting determination made by insurers. This guide provides a technical framework — it does not make compliance determinations or certify implementation correctness.

### §-1.5 Ownership and Licensing — Open Commons Declaration

**512** is a discovered constraint. The authors' position is that discovered constraints — properties that physics and scale force into existence regardless of human recognition — are not ownable in the manner of invented works. The authors assert no proprietary rights over the 512 constraint set, the Commit Gate category, or the seven invariants committed to the canonical kernel file, and do not intend to recognise exclusive proprietary claims asserted by any other party over those elements.

**CVS** (Cryptographic Verification Sidecar) is an invented witness architecture released as open infrastructure commons under CC BY 4.0. The authors assert no exclusive ownership over the base CVS architecture and do not intend to grant or recognise such exclusivity to any other party over the base layer.

**Derivative works** — gate implementations, managed services, SLA-bound products, interpretation tools, industry-specific deployments — are fully ownable and commercialisable by their creators. The base is open. What is built on the base belongs to its builder.

This documentation is released under Creative Commons Attribution 4.0 International (CC BY 4.0). Refer to §-1.7 for complete license terms.

### §-1.6 Public Ledger References

References to the XRP Ledger (XRPL) in this document are descriptive, not prescriptive. This architecture is ledger-agnostic. Any settlement ledger satisfying the mandatory technical properties — deterministic finality, predictable cost, public verifiability, and no execution-layer coupling — may be substituted without altering the architecture's semantics. References to XRPL do not imply endorsement, partnership, dependency, or affiliation.

### §-1.7 License

This document is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). To view a copy of this license, visit https://creativecommons.org/licenses/by/4.0/. You are free to share and adapt this material for any purpose, including commercial use, provided attribution is given: "512 Implementation Reference, Jonathan M. Watson, github.com/JonathanMastersWatson/512," a link to the license is provided, and any changes made are indicated.

### §-1.8 Jurisdictional Scope

This document has been prepared with reference to the laws and regulatory frameworks of Canada, the United States, and the United Kingdom. It is not legal advice in any jurisdiction. To the fullest extent permitted by applicable law, the authors seek to limit any liability arising from use of this document or the architectures it describes. The authors do not accept financial liability for decisions made in reliance on this document. Organisations in other jurisdictions must assess applicability independently.

### §-1.9 Financial Projection Disclaimer

All cost, latency, and performance figures in this document are illustrative examples only. They are not guarantees of performance, regulatory penalty avoidance, financial return, or legal defence success. Actual results depend on hardware selection, deployment environment, implementation quality, and operational integrity.

### §-1.10 No Reliance

This document is a descriptive technical specification and reference architecture only.

It is not intended to be relied upon as a certification of compliance, a guarantee of regulatory sufficiency, a guarantee of audit success, a guarantee of insurance coverage, a guarantee of risk mitigation, or a representation of operational fitness.

Compliance, certification, underwriting, and legal sufficiency are determinations made by regulators, courts, insurers, and licensed professionals — not by technical documentation.

Any organisation implementing concepts described herein does so at its own risk and bears full responsibility for deployment posture, regulatory interpretation, operational integrity, and jurisdictional compliance.

### §-1.11 No Endorsement

Nothing in this document constitutes endorsement of any implementation, derivative system, organisation, settlement ledger, or commercial deployment.

References to regulatory frameworks, standards bodies, or public ledger networks are descriptive only and do not imply approval, partnership, affiliation, or recognition by those bodies.

No institution has certified, adopted, approved, or validated 512 or CVS unless expressly stated in a separate, formally executed written agreement.

### §-1.12 Independent Verification Requirement

Where verification is discussed in this document, it refers to cryptographic or structural verifiability of recorded data — not legal, regulatory, or institutional validation. Structural verifiability does not equate to a compliance determination. These are distinct claims requiring distinct evidence under distinct legal and regulatory standards.

### §-1.13 Builder Responsibility

Any party constructing, deploying, or commercialising a system based on 512 or CVS assumes full responsibility for system behaviour, constraint design, regulatory interpretation, evidence storage, key management, anchoring configuration, operational uptime, and all resulting consequences.

The authors of the canonical documentation assume no operational control and no liability for derivative deployments.

---

## 0. Normative Relationships

This document is the engineer-level build reference for a Commit Gate satisfying 512's observable properties. It defines how to build, test, integrate, and operate such a gate — not why the constraint exists or what it means. Engineers read this document. CTOs and boards read `512_ARCHITECTURE_v3.4.md`.

The following canonical documents govern this one:

- **`512_ARCHITECTURE_v3.4.md`** — The authoritative source for what 512 is, why physics forces the Commit Gate category into existence, the seven invariants and their rationale, and the witness layer requirement. The architecture document establishes *what* must be true. This document defines *how* to make it true. Rationale is not repeated here — engineers who need it read `512_ARCHITECTURE_v3.4.md` first.
- **`CVS_ARCHITECTURE`** — Defines the Cryptographic Verification Sidecar: the reference witness layer for 512. Evidence Object schemas, hash-chaining model, and XRPL anchoring semantics are authoritative in that document. This document defines only the integration surface between a gate implementation and a CVS-compatible witness layer.
- **`Constraint-Architecture`** — Defines the upstream constraint discipline: what is admissible, consent logic, authority models, thresholds, and domain-specific admissibility rules. Constraint definition is not in scope for this document. See https://github.com/JonathanMastersWatson/Constraint-Architecture.

The following operational reference documents in the 512 repository are non-normative companions to this document. Engineers building from this guide should read these alongside it:

- **`512-ops/INTEGRATION_STEPS.md`** — The 7-step enterprise integration workflow. Defines the upstream preparation work (boundary identification, parallel path audit, Proposal Object definition, constraint definition) that must be complete before gate evaluation begins.
- **`512-ops/CONSTRAINT_DEFINITION_LAYER.md`** — How organisations translate policies into executable constraints. Defines the four-field constraint definition model, binary reducibility requirement, determinism requirement, and failure modes. The gate cannot evaluate vague policy language — constraints must arrive as binary-reducible Boolean expressions over named, typed inputs.
- **`512-ops/REFERENCE_FLOW.md`** — End-to-end sequence from intent declaration to anchored evidence. Defines the three CVS observation points and their relationship to the four validation steps in §4.
- **`512-ops/PROPERTIES_CHECKLIST.md`** — Go-live verification instrument covering all property categories. Use in conjunction with the conformance test suite in §11.4.
- **`AARM_AND_512.md`** — Architectural positioning of 512 relative to AARM (arXiv 2602.09433) and the CSA Agentic Control Plane Initiative. Establishes that AARM governs the orchestration layer and 512 governs the commit boundary — complementary layers, not competing specifications.
- **`CANONICAL_COMMITMENT.md`** — Permanent priority record for 512 and CVS. Records genesis commit dates, XRPL anchor transaction, canonical kernel hash, and sealed archive hashes. The dated reference for any dispute, standards body submission, or ecosystem conversation referencing 512's prior art status.

This document takes precedence over neither. Each canonical document is authoritative within its defined scope.

### 0.1 Reference Implementation Status

This document is a technical pattern reference. It is not a managed product, a supported software release, or a commercially maintained service. It carries no SLA, no uptime guarantee, no compliance certification, and no warranty of fitness for any purpose. Nothing in this document constitutes a promise of support, maintenance, security updates, or continued availability.

**512 is a constraint grammar. A Commit Gate is an implementation artifact.** This document describes how to build the artifact. It does not define the constraint grammar — that is the domain of `512_ARCHITECTURE_v3.4.md §2–4`. A Commit Gate built to satisfy 512's properties is a builder's implementation, owned by its builder under standard intellectual property principles, and fully the builder's responsibility.

**Builders assume full and sole responsibility** for all decisions made in reliance on this document, including: deployment architecture, operational resilience, security posture, regulatory compliance assessment, insurance and risk management, integration with existing systems, and all consequences of running a gate implementation in any production environment. The authors of this document have no visibility into, control over, or liability for any deployment made by any party.

**Normative language scope:** `MUST` and `MUST NOT` language throughout this document describes the internal consistency requirements of a valid Commit Gate implementation pattern. A gate that violates a MUST is not a Commit Gate satisfying 512's properties — it is a different artifact, and the 512-conformant designation applies only to implementations that pass every test in §11.4. These terms do not create external legal obligations on builders, their organisations, or their counterparties beyond what is established in separate written agreements.

---

## Abstract

This document describes how one may construct a **Commit Gate** satisfying 512's observable properties. It does not imply certification, regulatory adoption, production readiness, or that any implementation built from it meets any external compliance requirement. Building from this guide produces a technical artifact. What that artifact means for a given organisation's regulatory posture, operational risk, and deployment obligations is entirely the builder's determination.

This document is an engineering build guide. It specifies, in executable terms, how to construct a Commit Gate that satisfies 512's observable properties: a minimal, immutable, binary enforcement mechanism positioned at the commit boundary of a machine-speed execution system.

What you are building is a deterministic function: `(intent, context, constraints) → {allow, deny}`. It executes in 10–50μs in software, under 5μs on dedicated hardware. It enforces seven pre-committed invariants without interpretation. On infrastructure failure, it produces Evaluation-Unavailable DENY — the commit boundary holds. It integrates with a witness layer that produces independently verifiable execution evidence.

This guide provides the constraint specification format, bytecode compilation pipeline, per-invariant executable schemas, validation sequence with latency targets, CVS integration surface, adapter implementations, deployment topology patterns, performance envelope specifications, security model requirements, and a complete conformance test suite.

A gate implementation that passes every test in §11 satisfies 512's properties. A gate that does not pass every test does not — regardless of what its documentation claims. The canonical commitment `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5` is the ground truth. The verification procedure is in §3.2.

---

## 1. The Commit Gate — Position and Insertion

### 1.1 Gate Position Is Architecturally Determined

A **Commit Gate** has exactly one valid position: between authorisation and irreversible state change. This is not a preference. Before the commit boundary, actions are proposals. After it, they are facts. A gate upstream of the commit boundary is advisory. A gate downstream is retroactive. Neither is a Commit Gate.

Finding the commit boundary is the first engineering task. The question to answer: *at what point does the proposed action become a state change that cannot be undone?* The gate belongs immediately before that point, after authorisation has succeeded.

Incorrect positioning produces a system that appears to enforce constraints but does not. Identifying and eliminating parallel commit paths — administrative overrides, emergency bypass routes, direct database writes that circumvent the gate — is a prerequisite to production enforcement.

### 1.2 Insertion by Domain

The commit boundary location differs by execution surface. The gate inserts at the following positions:

**AI agent systems:**

```
User Request
    ↓
Agent Orchestrator (planning, reasoning, tool selection)
    ↓
[ COMMIT GATE ]  ← constraint evaluation here
    ↓ allow/deny
Tool Execution Layer  ← COMMIT BOUNDARY
    ↓
External APIs / Resources / State Changes
    ↓
CVS Evidence Capture (parallel, async, off hot path)
```

The gate evaluates tool invocation intent — not the agent's reasoning. Reasoning is pre-gate. Tool execution is post-gate. The gate position is between those two.

**Financial systems:**

```
Trading System / Risk Dashboard
    ↓
Order Management
    ↓
[ COMMIT GATE ]  ← constraint evaluation here
    ↓ allow/deny
Execution / Settlement Engine  ← COMMIT BOUNDARY
    ↓
Clearing / Finality
    ↓
CVS Evidence Capture (parallel, async, off hot path)
```

The gate does not sit at the order management layer — that layer can be bypassed via direct market access. The gate sits immediately before settlement commit.

**Hardware and manufacturing systems:**

```
Operator Input / Automated Control
    ↓
Control System (PLC / SCADA)
    ↓
[ COMMIT GATE ]  ← constraint evaluation here
    ↓ allow/deny
Actuator  ← COMMIT BOUNDARY (voltage release)
    ↓
Physical Effect (irreversible)
    ↓
CVS Evidence Capture (parallel, async, off hot path)
```

The commit boundary is actuator voltage release. Physical actions are irreversible. The gate must precede that release, not the control system instruction that precedes it.

### 1.3 Bypass Path Elimination Is Mandatory

Every route to the execution surface that does not pass through the gate is a bypass path. The gate implementation **MUST** ensure no such routes exist. This is a structural requirement — procedural controls (access lists, policies stating "don't bypass") do not satisfy it.

Bypass path audit checklist:

- All write APIs to the execution surface route through gate evaluation
- No emergency override paths skip gate evaluation; where overrides are operationally necessary, they **MUST** generate a gap record — an override that produces no gap record is a bypass, not an override
- Database direct-write access is revoked for all non-gate execution paths
- Administrative access to the execution surface generates a gap record at each use
- All execution pathways are periodically audited structurally — procedural policies stating "don't bypass" do not substitute for verified structural routing

Bypass accumulation is the most common real-world failure mode. Systems are built correctly and exceptions accumulate over time. Each exception is individually justified. Collectively, they render the boundary irrelevant. The boundary is either structurally enforced or it is not a boundary.

### 1.4 Authorisation Precedes the Gate

The gate evaluates constraints. It does not perform authorisation. Authorisation — verifying who is making a request and whether they are permitted to make it — precedes gate evaluation. The gate receives a cryptographic proof of authorisation (token, certificate, or signed attestation) and evaluates whether the authorised action satisfies constraints.

If authorisation fails, the request is rejected before it reaches the gate. If authorisation succeeds but constraints are violated, the gate denies and records. These are different failure modes with different semantics.

### 1.5 Commit Path Ownership Is Non-Bypassable

The gate **MUST** be positioned such that there exists exactly one path to irreversible state change, and that path does not open without the gate's authorisation signal. This is a structural requirement. Procedural controls — access policies, operational documentation, contractual prohibitions on bypass — do not satisfy it. The absence of any reachable path to the execution surface that does not pass through gate evaluation is the requirement.

**The conformant model:**

```
[upstream systems]
        |
        v
[evaluation at commit boundary]
        |
        v
[irreversible state change]

Properties:
  - no alternate path exists
  - no reinterpretation occurs between evaluation and commit
  - no execution proceeds outside this path under any operational mode
```

The gate **MUST** be the structural gating condition on the commit path — not a pre-check that runs before an independently operating execution surface. The gate's authorisation signal **MUST** be the direct prerequisite for the commit path to open. No intermediary component interprets, queues, or applies this signal between gate evaluation and the commit boundary.

The implementation **MUST NOT**:

- position the gate upstream of a separately operable execution surface
- route the gate's authorisation signal through any intermediary (API layer, message queue, broker, event bus) before the commit path receives it
- allow any request to reach the commit boundary without gate evaluation under any operational mode, including emergency, maintenance, or administrative modes
- implement fallback or override execution paths that reach the execution surface without generating a gap record

**Failure consequence:** A bypass path — any path that reaches the execution surface without gate evaluation — is a non-conformance condition regardless of how rarely it is exercised. A system with a bypass path has no enforcement. It has monitoring attached to an uncontrolled execution surface.

### 1.6 Non-Conformant Execution Patterns

The following patterns do not satisfy 512's properties. Each introduces a structural separation between evaluation and the commit boundary, creating a path to irreversible state change that is not controlled by the evaluation result.

---

**❌ Pattern A — Evaluation result handed off to an API layer (NON-CONFORMANT)**
```
[evaluation] → [API call] → [DB write]
```
The DB write is reachable independently of evaluation.
The evaluation result is advisory to the API layer.

---

**❌ Pattern B — Evaluation result handed off to a queue (NON-CONFORMANT)**
```
[evaluation] → [message queue] → [worker executes]
```
The worker can consume from sources other than the evaluation path.
The queue is an independently operable execution surface.

---

**❌ Pattern C — Evaluation result handed off to a broker (NON-CONFORMANT)**
```
[evaluation] → [broker] → [runtime applies decision]
```
The broker reintroduces an interpretation layer.
The runtime may apply the decision differently from the evaluation output.

---

**❌ Pattern D — Pre-check positioning (NON-CONFORMANT)**
```
[evaluation check] → [execution layer]
```
Decision and execution are structurally separate.
The execution layer is operable without the evaluation result.
This is the most common misinterpretation of 512's boundary model.

---

**❌ Pattern E — Parallel or fallback execution path (NON-CONFORMANT)**
```
[evaluation]
     |
     +──► [primary execution path]
     |
     +──► [fallback / override / admin path]
```
Any path that reaches the execution surface without evaluation is a bypass.
The existence of the path — not its frequency of use — is the disqualifying condition.

---

**✅ The only conformant model:**
```
[upstream systems]
        |
        v
[evaluation at commit boundary]
        |
        v
[irreversible state change]
```

---

## 2. Constraint Specification Format

### 2.1 Constraints Are Deterministic Boolean Functions

Constraints are expressed as deterministic Boolean functions over structured inputs. Every input is typed. Every operator is deterministic. Every evaluation produces an identical result for identical inputs, across every execution, on every machine.

The general form is:

```
Constraint(input_set) → Boolean
```

where every input is typed, every operator is deterministic, and the output is `true` (allow) or `false` (deny).

The evaluation engine **MUST** conform to the following behavioral requirements without exception:

- The evaluation engine **MUST** evaluate every constraint expression as a pure Boolean function — no side effects, no state accumulation, no external I/O during evaluation.
- The evaluation engine **MUST** produce identical output for identical `(intent, context, compiled_spec)` inputs on every invocation. Non-deterministic evaluation under any condition disqualifies the implementation as a Commit Gate.
- The evaluation engine **MUST NOT** produce probabilistic output. Confidence scores, risk scores, weighted results, likelihood estimates, and fuzzy truth values have no place in constraint evaluation. A constraint either holds or it does not.
- The evaluation engine **MUST NOT** operate in an advisory mode — a mode in which evaluation results are computed but not enforced, logged but not acted upon, or returned as recommendations rather than decisions. Advisory output is not binary output. An implementation that can be placed in advisory mode is not a Commit Gate.
- The evaluation engine **MUST NOT** expose or accept any asynchronous override channel. No runtime signal, API endpoint, message queue, configuration flag, or out-of-band mechanism may alter a constraint result after evaluation has begun or substitute a result after evaluation has completed. The evaluation path is synchronous and closed.
- The evaluation engine **MUST NOT** modify the active invariant set at runtime. The invariant set is fixed at process startup by the compiled specification. Adding, removing, or reordering invariants without producing a new specification hash and restarting the process produces a different artifact, not an updated gate.

The 512-byte specification limit enforces this discipline mechanically. If a constraint cannot be expressed in 512 bytes of canonical specification, it cannot be enforced at machine speed without interpretation — and constraints that require interpretation are not constraints a Commit Gate can evaluate.

### 2.2 Constraint Expression Schema

Each constraint is defined as a structured object with typed inputs and an evaluation expression:

```json
{
  "constraint_id": "string — unique within specification",
  "invariant_ref": "integer 1–7 — which invariant this enforces",
  "description": "string — human-readable; not evaluated",
  "inputs": {
    "field_name": {
      "type": "string | integer | decimal | boolean | timestamp | hash | list<type>",
      "source": "intent | context | registry | accumulator",
      "required": true
    }
  },
  "expression": "string — deterministic Boolean expression over input fields",
  "deny_message": "string — disclosed to proposing entity on deny result"
}
```

### 2.3 Rule Expression Examples

**AI agent spend limit (Invariant 1 — no force/fraud through resource exhaustion):**

```json
{
  "constraint_id": "ai_spend_limit_v1",
  "invariant_ref": 1,
  "description": "Agent accumulated spend must not exceed pre-authorised budget",
  "inputs": {
    "agent_id": { "type": "string", "source": "intent", "required": true },
    "cost_estimate": { "type": "decimal", "source": "intent", "required": true },
    "accumulated_spend": { "type": "decimal", "source": "accumulator", "required": true },
    "spend_limit": { "type": "decimal", "source": "registry", "required": true }
  },
  "expression": "accumulated_spend + cost_estimate <= spend_limit",
  "deny_message": "spend_limit_exceeded"
}
```

**Consent check (Invariant 2 — voluntary interaction):**

```json
{
  "constraint_id": "consent_check_v1",
  "invariant_ref": 2,
  "description": "Execution affecting a party requires current, explicit consent",
  "inputs": {
    "target_party_id": { "type": "string", "source": "intent", "required": true },
    "consent_token": { "type": "hash", "source": "registry", "required": false },
    "consent_expiry": { "type": "timestamp", "source": "registry", "required": false },
    "evaluation_time": { "type": "timestamp", "source": "context", "required": true }
  },
  "expression": "consent_token != null AND evaluation_time < consent_expiry",
  "deny_message": "consent_absent_or_expired"
}
```

**Withdrawal propagation (Invariant 3 — exit always possible):**

```json
{
  "constraint_id": "withdrawal_propagation_v1",
  "invariant_ref": 3,
  "description": "Execution must not proceed against a party in revoked-consent state",
  "inputs": {
    "target_party_id": { "type": "string", "source": "intent", "required": true },
    "consent_epoch": { "type": "integer", "source": "registry", "required": true },
    "token_epoch": { "type": "integer", "source": "intent", "required": true }
  },
  "expression": "token_epoch == consent_epoch",
  "deny_message": "consent_withdrawn_epoch_mismatch"
}
```

**Financial exposure limit (Invariant 1 — no unauthorised resource extraction):**

```json
{
  "constraint_id": "exposure_limit_v1",
  "invariant_ref": 1,
  "description": "Transaction must not breach counterparty or sector exposure limit",
  "inputs": {
    "counterparty_id": { "type": "string", "source": "intent", "required": true },
    "proposed_value": { "type": "decimal", "source": "intent", "required": true },
    "current_exposure": { "type": "decimal", "source": "accumulator", "required": true },
    "exposure_limit": { "type": "decimal", "source": "registry", "required": true }
  },
  "expression": "current_exposure + proposed_value <= exposure_limit",
  "deny_message": "exposure_limit_exceeded"
}
```

**Hardware tolerance override (Invariant 1 — no force against authorised range):**

```json
{
  "constraint_id": "tolerance_override_v1",
  "invariant_ref": 1,
  "description": "Requested tolerance must fall within authorised range",
  "inputs": {
    "operator_id": { "type": "string", "source": "intent", "required": true },
    "requested_tolerance": { "type": "decimal", "source": "intent", "required": true },
    "range_min": { "type": "decimal", "source": "registry", "required": true },
    "range_max": { "type": "decimal", "source": "registry", "required": true },
    "approved_operators": { "type": "list<string>", "source": "registry", "required": true }
  },
  "expression": "(requested_tolerance >= range_min AND requested_tolerance <= range_max) AND (operator_id IN approved_operators)",
  "deny_message": "tolerance_out_of_range_or_operator_unauthorised"
}
```

### 2.4 Constraints Compile Once; Runtime Modification Is Prohibited

Constraints are compiled to bytecode once, at specification deployment time. The compilation step:

1. Parses the constraint JSON
2. Type-checks all input declarations
3. Compiles the Boolean expression to a deterministic bytecode instruction sequence
4. **Rejects** any expression that contains conditional branching dependent on runtime state not declared in the input schema
5. **Rejects** any expression whose evaluation time exceeds the 50μs budget under worst-case input size
6. **Rejects** any expression that requires external I/O to resolve — all inputs must be fully bound from the declared input schema before evaluation begins
7. Produces a compiled constraint bundle and computes its SHA-256 hash
8. Requires the compiled bundle hash to be committed to the specification file before deployment

Changing a constraint requires producing a new compiled bundle with a new hash. The gate **MUST NOT** accept runtime constraint modifications. The gate **MUST NOT** accept runtime modification of the invariant set — adding, removing, or reordering invariants without producing a new specification hash and restarting the gate process produces a different specification surface, not a valid update to the running gate. The specification is loaded at startup, hash-verified against the canonical commitment, and thereafter immutable for the process lifetime.

```bash
# Compile and verify
512-compiler compile --spec ./constraints/*.json --output ./dist/512-kernel.bundle
512-compiler hash ./dist/512-kernel.bundle
# Output: SHA-256: 7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5

# Verify on load (gate startup)
sha256sum 512-core/KERNEL/512-kernel-padded.txt
# Expected: 7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5
```

If the runtime hash does not match the canonical commitment, the gate **MUST** refuse to start and **MUST** log the mismatch as a critical alert. A gate that starts with a hash mismatch is not a Commit Gate — it is an unverified execution surface operating without a valid constraint set.

---

## 3. The Seven Invariants — Implementation

The seven invariants are defined in `512_ARCHITECTURE_v3.4.md §4`. This section provides the executable implementation of each: the input schema, the constraint expression, the deny semantics, and the unit test fixture that verifies correct evaluation.

### 3.1 Invariant 1 — No Agent May Initiate Force or Fraud Against Any Human

**What it prevents:** Unauthorised resource transfer, coercive action against human parties, deceptive output generation with known false parameters.

**Evaluation inputs:**

```json
{
  "action_type": "string — categorised action type",
  "affected_party_type": "enum: human | system | external_service",
  "is_coercive": "boolean — computed from action classification",
  "is_deceptive": "boolean — computed from output verification",
  "transfer_amount": "decimal — for fund transfer actions",
  "authorised_transfer_limit": "decimal — from capability grant"
}
```

**Expression:** `(affected_party_type != 'human' OR (NOT is_coercive AND NOT is_deceptive)) AND (action_type != 'fund_transfer' OR transfer_amount <= authorised_transfer_limit)`

**Unit test fixtures:**

```json
[
  {
    "description": "coercive action against human — must deny",
    "inputs": { "affected_party_type": "human", "is_coercive": true, "is_deceptive": false, "action_type": "data_access", "transfer_amount": 0, "authorised_transfer_limit": 1000 },
    "expected": "deny",
    "violated_constraint": "invariant_1_no_force_fraud"
  },
  {
    "description": "fund transfer within limit — must allow",
    "inputs": { "affected_party_type": "human", "is_coercive": false, "is_deceptive": false, "action_type": "fund_transfer", "transfer_amount": 500, "authorised_transfer_limit": 1000 },
    "expected": "allow"
  },
  {
    "description": "fund transfer exceeding limit — must deny",
    "inputs": { "affected_party_type": "human", "is_coercive": false, "is_deceptive": false, "action_type": "fund_transfer", "transfer_amount": 1001, "authorised_transfer_limit": 1000 },
    "expected": "deny",
    "violated_constraint": "invariant_1_no_force_fraud"
  }
]
```

### 3.2 Invariant 2 — All Interactions Must Be Voluntary and Based on Explicit Consent

**What it prevents:** Execution affecting human parties without documented, explicit, prior consent.

**Evaluation inputs:**

```json
{
  "target_party_id": "string",
  "action_affects_human": "boolean",
  "consent_token_present": "boolean",
  "consent_type": "enum: explicit | implied | none",
  "consent_expiry": "timestamp",
  "evaluation_timestamp": "timestamp"
}
```

**Expression:** `NOT action_affects_human OR (consent_token_present AND consent_type == 'explicit' AND evaluation_timestamp < consent_expiry)`

**Unit test fixtures:**

```json
[
  {
    "description": "no consent token — must deny",
    "inputs": { "action_affects_human": true, "consent_token_present": false, "consent_type": "none", "consent_expiry": "2099-01-01T00:00:00Z", "evaluation_timestamp": "2026-02-01T00:00:00Z" },
    "expected": "deny",
    "violated_constraint": "invariant_2_voluntary_consent"
  },
  {
    "description": "implied consent — must deny",
    "inputs": { "action_affects_human": true, "consent_token_present": true, "consent_type": "implied", "consent_expiry": "2099-01-01T00:00:00Z", "evaluation_timestamp": "2026-02-01T00:00:00Z" },
    "expected": "deny",
    "violated_constraint": "invariant_2_voluntary_consent"
  },
  {
    "description": "explicit consent, not expired — must allow",
    "inputs": { "action_affects_human": true, "consent_token_present": true, "consent_type": "explicit", "consent_expiry": "2099-01-01T00:00:00Z", "evaluation_timestamp": "2026-02-01T00:00:00Z" },
    "expected": "allow"
  }
]
```

### 3.3 Invariant 3 — Consent May Be Withdrawn; Exit Must Always Be Possible

**What it prevents:** Continued execution against a party after consent withdrawal.

**Evaluation inputs:**

```json
{
  "target_party_id": "string",
  "action_affects_human": "boolean",
  "presented_epoch": "integer — epoch embedded in the intent token",
  "registry_epoch": "integer — current epoch from consent registry",
  "withdrawal_propagated": "boolean"
}
```

**Expression:** `NOT action_affects_human OR (presented_epoch == registry_epoch AND withdrawal_propagated)`

The epoch mechanism forces withdrawal detection at evaluation time. A token issued before revocation carries a stale epoch — any proposal presenting that token is denied.

**Unit test fixtures:**

```json
[
  {
    "description": "epoch mismatch — consent withdrawn — must deny",
    "inputs": { "action_affects_human": true, "presented_epoch": 4, "registry_epoch": 5, "withdrawal_propagated": true },
    "expected": "deny",
    "violated_constraint": "invariant_3_consent_withdrawal"
  },
  {
    "description": "current epoch, propagated — must allow",
    "inputs": { "action_affects_human": true, "presented_epoch": 5, "registry_epoch": 5, "withdrawal_propagated": true },
    "expected": "allow"
  }
]
```

### 3.4 Invariant 4 — All Contracts Must Be Explicit, Readable, and Equally Enforceable

**What it prevents:** Operation under terms that are unreadable, machine-only, or that grant enforcement rights to one party only.

**Evaluation inputs:**

```json
{
  "governing_contract_id": "string",
  "contract_machine_readable": "boolean",
  "contract_human_readable": "boolean",
  "both_parties_acknowledged": "boolean",
  "enforcement_asymmetry": "boolean — true if only one party can enforce"
}
```

**Expression:** `contract_machine_readable AND contract_human_readable AND both_parties_acknowledged AND NOT enforcement_asymmetry`

**Unit test fixtures:**

```json
[
  {
    "description": "enforcement asymmetry — must deny",
    "inputs": { "contract_machine_readable": true, "contract_human_readable": true, "both_parties_acknowledged": true, "enforcement_asymmetry": true },
    "expected": "deny",
    "violated_constraint": "invariant_4_explicit_contracts"
  },
  {
    "description": "machine-readable only — must deny",
    "inputs": { "contract_machine_readable": true, "contract_human_readable": false, "both_parties_acknowledged": true, "enforcement_asymmetry": false },
    "expected": "deny",
    "violated_constraint": "invariant_4_explicit_contracts"
  },
  {
    "description": "all conditions met — must allow",
    "inputs": { "contract_machine_readable": true, "contract_human_readable": true, "both_parties_acknowledged": true, "enforcement_asymmetry": false },
    "expected": "allow"
  }
]
```

### 3.5 Invariant 5 — No Rules May Be Hidden or Unilaterally Changed

**What it prevents:** Execution under constraint sets not disclosed to all parties; silent rule modification.

**Evaluation inputs:**

```json
{
  "active_spec_hash": "string — SHA-256 of the constraint set in effect",
  "disclosed_spec_hash": "string — hash disclosed to and acknowledged by parties",
  "disclosure_acknowledged": "boolean",
  "canonical_hash": "string — constant: 7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5"
}
```

**Expression:** `active_spec_hash == disclosed_spec_hash AND active_spec_hash == canonical_hash AND disclosure_acknowledged`

For implementations using a forked constraint set (different hash), `canonical_hash` is replaced by the committed hash of that fork. The expression still enforces that the active specification matches what parties have acknowledged.

**Unit test fixtures:**

```json
[
  {
    "description": "hash mismatch — modified spec — must deny",
    "inputs": { "active_spec_hash": "AAAA...", "disclosed_spec_hash": "7B08...", "disclosure_acknowledged": true, "canonical_hash": "7B08..." },
    "expected": "deny",
    "violated_constraint": "invariant_5_no_hidden_rules"
  },
  {
    "description": "correct hash, acknowledged — must allow",
    "inputs": { "active_spec_hash": "7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5", "disclosed_spec_hash": "7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5", "disclosure_acknowledged": true, "canonical_hash": "7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5" },
    "expected": "allow"
  }
]
```

### 3.6 Invariant 6 — On Failure, Systems Must Fail Open and Disclose Governing Rules

**What it prevents:** Denial-of-service through gate failure; silent constraint violation; execution blocking.

**Implementation requirement:** This invariant is implemented in the gate's failure handling logic, not in the constraint evaluation path. It specifies what the gate does when it *cannot* evaluate — not what the evaluation returns.

**Fail-open implementation:**

```python
def evaluate_with_infrastructure_failure_deny(proposal, constraints):
    """
    Returns (result, deny_cause, evidence_type) tuple.
    result: 'allow' | 'deny'
    deny_cause: None | 'constraint_violation' | 'evaluation_unavailable'
    evidence_type: 'evaluated' | 'evaluation_unavailable_deny'
    """
    try:
        result = evaluate_constraints(proposal, constraints)
        return (result, 'constraint_violation' if result == 'deny' else None, 'evaluated')
    except GateUnavailableError:
        record_evaluation_unavailable_deny(
            proposal_id=proposal.id,
            agent_id=proposal.agent_id,
            failure_cause='gate_unavailable',
            timestamp=now(),
            retry_permitted=True
        )
        return ('deny', 'evaluation_unavailable', 'evaluation_unavailable_deny')
    except EvaluationTimeout:
        record_evaluation_unavailable_deny(
            proposal_id=proposal.id,
            agent_id=proposal.agent_id,
            failure_cause='evaluation_timeout',
            timestamp=now(),
            retry_permitted=True
        )
        return ('deny', 'evaluation_unavailable', 'evaluation_unavailable_deny')
```

The gap record is forwarded to the witness layer regardless of whether the witness layer is available. If the witness layer is also unavailable, the gap record is queued locally and forwarded on reconnection. Local queue depth and forwarding latency are performance envelope parameters defined in §8.

**Unit test fixtures:**

```json
[
  {
    "description": "gate failure — must produce evaluation-unavailable DENY, commit path remains closed",
    "setup": "inject GateUnavailableError at evaluation start",
    "expected_result": "deny",
    "expected_deny_cause": "evaluation_unavailable",
    "expected_retry_permitted": true,
    "expected_execution_result": "no execution — commit path remains closed",
    "gap_record_fields_required": ["proposal_id", "agent_id", "failure_cause", "timestamp", "retry_permitted"]
  },
  {
    "description": "deny result discloses failed invariant — human can act on information",
    "setup": "submit proposal violating invariant 2",
    "expected_execution_result": "deny",
    "expected_deny_response_fields": ["violated_constraint", "deny_message"]
  }
]
```

### 3.7 Invariant 7 — The Specification Is Immutable; Adherence Is Binary

**What it prevents:** Constraint drift through incremental modification; partial conformance claims.

**Implementation requirement:** The gate's specification load sequence enforces immutability structurally:

```python
def load_specification(spec_path, expected_hash):
    """
    Load and hash-verify specification at startup.
    Raises SpecificationIntegrityError if hash does not match.
    Gate refuses to start on integrity failure.
    """
    with open(spec_path, 'rb') as f:
        spec_bytes = f.read()

    actual_hash = sha256(spec_bytes).hexdigest().upper()

    if actual_hash != expected_hash:
        raise SpecificationIntegrityError(
            f"Specification hash mismatch. "
            f"Expected: {expected_hash} "
            f"Actual:   {actual_hash}"
        )

    # Specification is loaded into read-only memory
    return load_readonly(spec_bytes)
```

**Runtime immutability:** After startup, the specification **MUST NOT** be reloaded, patched, or modified in memory. Changing constraints requires restarting the gate process with a new specification file, which re-triggers the hash verification sequence. Each restart generates a specification-change event in the witness layer.

**Conformance is binary:** A gate evaluating 6 of 7 invariants is not "mostly conformant." It is non-conformant. Partial invariant evaluation produces a different constraint surface and a different hash. The 512-conformant designation applies only to an implementation that evaluates all seven invariants and carries the canonical hash.

---

## 4. The Validation Sequence

### 4.1 Every Proposal Passes Four Steps in Fixed Order

Every execution proposal passes through four steps in sequence. No step is skippable. No step may be reordered.

```
PROPOSING ENTITY          COMMIT GATE               CONTEXT REGISTRIES        WITNESS LAYER (CVS)
       │                       │                             │                        │
       │── proposal ──────────►│                             │                        │
       │                       │                             │                        │
       │          ╔════════════╧═══════════════════╗         │                        │
       │          ║  STEP 1: INTENT DECLARATION    ║         │                        │
       │          ║  Parse declaration structure   ║         │                        │
       │          ║  Verify authorisation token    ║         │                        │
       │          ║  Assign correlation_id         ║         │                        │
       │          ║  Target: <5μs                  ║         │                        │
       │          ╚════════════╤═══════════════════╝         │                        │
       │                       │── emit pre_validation ─────────────────────────────►│
       │                       │                             │                        │
       │          ╔════════════╧═══════════════════╗         │                        │
       │          ║  STEP 2: CONTEXT BINDING       ║         │                        │
       │          ║  Query accumulator values      ║         │                        │
       │          ╠════════════╪═══════════════════╣         │                        │
       │          ║  Query consent registry   ─────╫────────►│                        │
       │          ║  Query capability grants  ─────╫────────►│                        │
       │          ║  Query spec disclosure    ─────╫────────►│                        │
       │          ║  Assemble (intent, context)     ║◄────────│                        │
       │          ║  Target: <10μs (cache hit)      ║         │                        │
       │          ╚════════════╤═══════════════════╝         │                        │
       │                       │                             │                        │
       │          ╔════════════╧═══════════════════╗         │                        │
       │          ║  STEP 3: CONSTRAINT EVALUATION ║         │                        │
       │          ║  Evaluate 7 invariants          ║         │                        │
       │          ║  Deterministic bytecode only    ║         │                        │
       │          ║  No external I/O during eval    ║         │                        │
       │          ║  → ALLOW or DENY                ║         │                        │
       │          ║  Target: <30μs                  ║         │                        │
       │          ╚════════════╤═══════════════════╝         │                        │
       │                       │── emit validation_result ──────────────────────────►│
       │                       │                             │                        │
       │          ╔════════════╧═══════════════════╗         │                        │
       │          ║  STEP 4: COMMIT AUTHORISATION  ║         │                        │
       │          ║  ALLOW → commit path opens      ║         │                        │
       │          ║  DENY  → commit path closed     ║         │                        │
       │          ║          + violated invariant   ║         │                        │
       │          ║  Target: <5μs                   ║         │                        │
       │          ╚════════════╤═══════════════════╝         │                        │
       │                       │                             │                        │
       │◄── ALLOW / DENY ───────│                             │                        │
       │                       │                             │                        │
  [commit path                 │                             │                        │
   opens or                    │── emit post_execution ─────────────────────────────►│
   remains closed]             │                             │                        │

── async (off critical path) ──────────────────────────────────────────────────────────►
   CVS emission never delays execution. Gate does not wait for witness acknowledgement.

EVALUATION-UNAVAILABLE DENY PATH (gate unavailable or Step 3 timeout):
       │                       │                             │                        │
       │                  GateUnavailable                    │                        │
       │                  or EvalTimeout                     │                        │
       │   [infrastructure-failure handler — commit path remains closed]             │
       │◄── DENY (evaluation_unavailable, retry_permitted: true) ───────────────────│
       │                       │── emit deny_evidence_object ───────────────────────►│
       │                       │── emit gap_record (sidecar) ───────────────────────►│
       │                       │   [queued locally if CVS unavailable]               │
```

**Step 1 — Intent Declaration (target: <5μs)**

The proposing entity submits a structured declaration of what it intends to execute. This is the gate's only input from the proposing entity. The declaration format:

```json
{
  "proposal_id": "string — unique, generated by proposing entity",
  "agent_id": "string — cryptographically attested identity",
  "action_type": "string — from controlled vocabulary",
  "action_params": { },
  "declared_scope": { },
  "intent_hash": "string — SHA-256 of serialised intent for CVS capture",
  "authorisation_token": "string — cryptographic proof of authorisation",
  "timestamp": "string — ISO 8601"
}
```

The gate validates the declaration structure and authorisation token first. Structurally invalid or unauthorised proposals are rejected before constraint evaluation begins.

**Step 2 — Context Binding (target: <10μs)**

The gate queries external registries to assemble the evaluation context. Context includes:

- Current timestamp (gate's clock, not proposer's)
- Relevant accumulator values (spend totals, exposure, rate counters)
- Registry lookups (consent status, capability grants, authorised operator lists, spec hash disclosure acknowledgements)
- Environmental state (system health, operational mode flags)

Context assembly queries **MUST** be pre-cached for hot-path evaluation. Cold-path registry reads for novel agents or first-use contexts **SHOULD** be handled by a pre-fetch path that populates the cache before the proposal arrives.

**Step 3 — Constraint Evaluation (target: <30μs)**

The seven invariant expressions are evaluated against the assembled `(intent, context)` pair. The evaluation engine **MUST** satisfy all behavioral requirements stated in §2.1 during this step.

The evaluation engine **MUST** produce a Boolean result per invariant. It **MUST NOT** produce a scored result, a weighted result, a probabilistic estimate, or any output other than `true` or `false` per invariant. It **MUST NOT** defer, suspend, or queue evaluation for asynchronous completion. Evaluation completes synchronously within the Step 3 latency budget or the gate fails open — there is no third path.

```python
def evaluate_constraints(intent, context, compiled_spec):
    results = {}
    for invariant_id, constraint_fn in compiled_spec.items():
        results[invariant_id] = constraint_fn(intent, context)

    overall = all(results.values())
    return EvaluationResult(
        overall='ALLOW' if overall else 'DENY',
        per_invariant=results,
        violated=[k for k, v in results.items() if not v],
        spec_hash=compiled_spec.hash,
        evaluation_duration_us=elapsed_us()
    )
```

If any invariant produces `false`, the overall result is `DENY`. The deny response **MUST** include the specific violated invariant identifier and the human-readable `deny_message` from the constraint definition. The evaluation engine **MUST NOT** suppress, redact, or generalise the violated invariant identifier in the deny response.

**Step 4 — Commit Authorisation Signal (target: <5μs)**

The evaluation result **MUST** be one of exactly two values: `ALLOW` or `DENY`. No other output is valid. The gate **MUST NOT** return a score, a probability, a confidence value, a recommendation, a conditional allow, a deferred result, or a request for human review in lieu of a binary decision. Any implementation that returns such output is not a Commit Gate. When the gate is unavailable or evaluation times out, the infrastructure-failure handler produces DENY (deny_cause: evaluation_unavailable). The commit path remains closed. Execution does not proceed. The failure cause and retry path are disclosed. The CVS sidecar records the unavailability period as a gap record. Admissibility requires completed evaluation — an action does not commit because the gate was unavailable.

- `ALLOW` — the gate **MUST** return this result. The commit path opens. Execution proceeds. The result and its correlation ID are forwarded to the witness layer asynchronously. The gate **MUST NOT** append conditions, recommendations, or caveats to an ALLOW result.
- `DENY` — the gate **MUST** return this result with the violated invariant identifier and deny message. The commit path remains closed. Execution does not proceed. The denial event is forwarded to the witness layer. The gate **MUST NOT** return a DENY result that omits the violated invariant identifier.
- **Evaluation-Unavailable DENY (gate unavailable or evaluation timeout)** — the infrastructure-failure handler produces DENY (deny_cause: evaluation_unavailable). The commit path remains closed. Execution does not proceed. The DENY **MUST** include failure cause and retry_permitted: true. The CVS sidecar emits a gap record. An evaluation-unavailable DENY **MUST NOT** be treated as ALLOW. It is not a constraint violation — no invariant was evaluated.

The witness layer forwarding is asynchronous and off the critical path. Execution does not wait for witness confirmation. The asynchronous witness path **MUST NOT** carry any signal that can alter or override the synchronous evaluation result. See §5 for the CVS integration surface.

### 4.2 Latency Budget

| Step | Target (median) | Target (p99) | Failure mode if exceeded |
|---|---|---|---|
| Intent Declaration | <5μs | <10μs | Reject as malformed |
| Context Binding | <10μs | <20μs | Use cached context; flag stale |
| Constraint Evaluation | <30μs | <100μs | Evaluation-Unavailable DENY; emit gap record to CVS sidecar |
| Commit Authorisation Signal | <5μs | <10μs | Non-blocking; log latency breach |
| **Total** | **<50μs** | **<200μs** | |

Latency measurements are taken at the gate process level, excluding network I/O to the proposing entity. The gate **MUST** instrument and expose latency percentile metrics at all four steps. Load test procedure: 10,000 proposals at sustained throughput; measure all four steps independently.

### 4.3 Intent-Execution Correspondence

The gate evaluates declared intent. If the execution layer does not enforce correspondence between declared intent and actual execution, the gate's allow result is exploitable. Enforcement of intent-execution correspondence is an implementation responsibility:

- Execution parameters **MUST** be bounded by the declared scope in the intent declaration
- Any execution that exceeds declared scope **MUST** be rejected by the execution layer, not the gate
- The CVS post-execution Evidence Object records actual execution outcome; divergence from declared intent is detectable in the evidence chain upon inspection by any party with read access to the evidence store

### 4.4 Observation Mode Is the Correct Enterprise Entry Point

A gate satisfying 512's properties **MAY** operate in observation mode. Observation mode is the correct entry point for new deployments — it allows an organisation to verify that its systems satisfy 512's properties before enabling enforcement, and to confirm that constraint definitions match policy intent before any execution is blocked.

In observation mode:

- all seven invariants are evaluated at every boundary crossing
- no execution is blocked — all proposals proceed regardless of evaluation result
- all gate results are recorded: ALLOW or DENY; evaluation-unavailable DENY events are recorded by the witness layer; CVS sidecar records gap

Observation mode surfaces three categories of problem before enforcement depends on them:

**Unexpected DENY results** — constraints firing on legitimate requests. These indicate constraint definitions that are too narrow, input data that is not being assembled correctly, or policies that contain assumptions that were never made explicit. Finding these in observation mode costs nothing. Finding them in enforcement mode blocks operations.

**Fail-open events** — gate unavailability or evaluation timeout caused by missing input data, registry unavailability, or timeout. These generate evidence chain gaps recorded by the witness layer and indicate integration issues that must be resolved before enforcement.

**Coverage gaps** — execution events that produce no evaluation record. These indicate commit boundaries that were missed in the boundary mapping phase, or parallel paths that were not eliminated.

**Observation mode is not:**

- advisory mode — evaluation is real and complete, not approximate
- a simulation — the evaluation mechanism is identical to enforcement mode; only the enforcement posture differs
- a partial evaluation — all seven invariants are evaluated on every proposal
- a bypass of the boundary — the gate operates normally; it does not block on DENY

Valid outputs in observation mode are ALLOW or DENY. A DENY in observation mode records that the invariant was not satisfied — it does not block execution. That record is available for post-observation analysis.

**Transition from observation to enforcement mode** requires: verifying that no invariants fire unexpectedly (false negatives — requests that should DENY but ALLOW), resolving constraint definition issues upstream, and a deliberate configuration change. The gate specification does not change between modes. Only the enforcement posture changes.

Most organisations spend two to four weeks in observation mode. That period is not a delay — it is when constraint definitions are verified against policy intent before enforcement depends on them. See `512-ops/INTEGRATION_STEPS.md §5` for the full observation mode procedure and transition checklist.

---

## 5. CVS Integration Surface

### 5.1 Three Observation Points

The CVS witness layer observes three points in the validation lifecycle. The gate implementation exposes a structured event at each point. CVS consumes these events passively — the gate does not wait for CVS acknowledgement and execution is never blocked by witness layer state.

**Observation Point 1 — Pre-Validation (emitted after Step 1: Intent Declaration)**

```json
{
  "observation_point": "pre_validation",
  "proposal_id": "string — matches intent declaration proposal_id",
  "agent_id": "string",
  "intent_hash": "string — SHA-256 of serialised intent",
  "authorisation_token_hash": "string — hash of token, not token itself",
  "timestamp": "string — ISO 8601",
  "correlation_id": "string — links all three observation points for this proposal"
}
```

**Observation Point 2 — Validation Result (emitted after Step 3: Constraint Evaluation)**

```json
{
  "observation_point": "validation_result",
  "proposal_id": "string",
  "correlation_id": "string",
  "overall_result": "allow | deny",
  "spec_hash": "string — SHA-256 of the specification evaluated against",
  "per_invariant_results": {
    "invariant_1_no_force_fraud": "pass | fail",
    "invariant_2_voluntary_consent": "pass | fail",
    "invariant_3_consent_withdrawal": "pass | fail",
    "invariant_4_explicit_contracts": "pass | fail",
    "invariant_5_no_hidden_rules": "pass | fail",
    "invariant_6_fail_open": "pass | fail",
    "invariant_7_kernel_immutability": "pass | fail"
  },
  "violated_constraint_detail": "string | null — populated on deny only",
  "evaluation_duration_us": "integer",
  "timestamp": "string — ISO 8601"
}
```

**Observation Point 3 — Post-Execution (emitted after execution completes)**

```json
{
  "observation_point": "post_execution",
  "proposal_id": "string",
  "correlation_id": "string",
  "execution_outcome": "completed | failed | cancelled",
  "actual_scope": { },
  "execution_duration_us": "integer",
  "timestamp": "string — ISO 8601"
}
```

### 5.2 Gate and Witness Layer Must Never Share Authority

The gate and the witness layer are independent systems. The gate **MUST NOT** control the witness layer. The witness layer **MUST NOT** influence gate evaluation. This separation is structural, not procedural.

A gate that controls its own evidence record can fabricate a conformant evidence stream by selectively suppressing, deleting, or modifying the events it forwards. Authority must be separated so that fabrication requires compromising two independent systems with separate access controls.

Implementation requirements:

- The gate's service identity has write-only, append-only access to the CVS event queue
- The gate has no read access to the evidence store
- The gate has no access to CVS attestation keys
- The CVS process has no access to gate configuration, constraint specifications, or evaluation logic
- These access controls are structural (IAM, network segmentation) — not reliant on personnel policy

### 5.3 Evaluation-Unavailable DENY Records Are First-Class Witness Events

When the gate cannot evaluate (Step 3 timeout or gate unavailability), the infrastructure-failure handler produces DENY (deny_cause: evaluation_unavailable). The deny Evidence Object and gap record **MUST** be forwarded to the CVS event queue.

**Deny Evidence Object (evaluation-unavailable):**

```json
{
  "observation_point": "validation_result",
  "overall_result": "deny",
  "deny_cause": "evaluation_unavailable",
  "failure_cause": "gate_unavailable | evaluation_timeout | process_crash",
  "retry_permitted": true,
  "proposal_id": "string",
  "agent_id": "string",
  "timestamp": "string — ISO 8601",
  "spec_hash": "string",
  "correlation_id": "string"
}
```

**CVS sidecar gap record:**

```json
{
  "observation_point": "validation_gap",
  "proposal_id": "string",
  "agent_id": "string",
  "gap_start": "string — ISO 8601",
  "gap_reason": "gate_unavailable | evaluation_timeout | process_crash",
  "gate_output_during_gap": "deny_evaluation_unavailable",
  "correlation_id": "string"
}
```

If the CVS queue is unavailable when a gap occurs, the gap record **MUST** be persisted to a local durable queue and forwarded on reconnection. Local queue **MUST** be sized for a minimum of 30 minutes of gap records at peak throughput. Gap records **MUST NOT** be discarded.

---

## 6. Adapter Layer

### 6.1 Adapters Observe and Forward; They Do Not Interfere

Adapters connect the gate's CVS event stream to the witness layer's capture infrastructure. Each adapter is purpose-built for a specific event transport mechanism. Adapters are non-interfering — they observe and forward; they do not modify events, acknowledge messages, or write to production systems.

The adapter definitions below specify the integration properties of each supported transport. Full CVS adapter architecture is defined in `CVS_ARCHITECTURE §4`.

### 6.2 Kafka Adapter

```
Capture Point:      Kafka topics carrying gate event stream
Integration:        Standard Kafka consumer (separate consumer group)
Observation Delay:  <10ms
```

The Kafka adapter **MUST NOT** acknowledge messages on behalf of the production consumer group. It consumes from the topic as a passive observer with an independent consumer group ID. Message ordering is preserved by partition. The adapter reads the gate event topic; it does not write to any Kafka topic.

```yaml
kafka_adapter:
  bootstrap_servers: "kafka-host:9092"
  consumer_group: "cvs-witness-observer"
  topics:
    - "gate.pre_validation"
    - "gate.validation_result"
    - "gate.post_execution"
    - "gate.validation_gap"
  auto_offset_reset: "earliest"
  enable_auto_commit: false   # MUST NOT acknowledge
  isolation_level: "read_committed"
```

### 6.3 Change Data Capture (CDC) Adapter

```
Capture Point:      Database replication streams (Postgres, MySQL, Oracle)
Integration:        Logical replication slot (read-only consumer)
Observation Delay:  <100ms
```

For implementations that persist gate events to a relational store, the CDC adapter reads the replication stream after commit. The adapter **MUST NOT** write to the database. It consumes after-commit events only — pre-commit row state is never visible.

```yaml
cdc_adapter:
  type: "postgres_logical"
  connection: "postgresql://cvs-readonly@host:5432/gate_events"
  publication: "gate_events_pub"
  slot_name: "cvs_witness_slot"
  tables:
    - "gate_pre_validation"
    - "gate_validation_results"
    - "gate_post_execution"
    - "gate_validation_gaps"
```

### 6.4 OpenTelemetry (OTEL) Adapter

```
Capture Point:      Distributed traces and spans
Integration:        Additional OTEL exporter (never a processor)
Observation Delay:  <5ms
```

The OTEL adapter registers as an additional trace exporter in the gate's OTEL SDK configuration. It **MUST** be one exporter among potentially several — it **MUST NOT** sit in the processor chain in a position that can delay or modify trace export. Never block traces.

```yaml
otel_adapter:
  type: "additional_exporter"
  endpoint: "cvs-collector:4317"
  protocol: "grpc"
  resource_attributes:
    service.name: "512-commit-gate"
    cvs.integration: "true"
  # Gate's primary exporter continues independently
```

### 6.5 API Gateway Mirror Adapter

```
Capture Point:      HTTP request/response traffic to/from gate
Integration:        Mirrored traffic — operates on copy, never original
Observation Delay:  0ms added to critical path (async mirror)
```

For HTTP-exposed gate endpoints, the API gateway mirrors traffic to the CVS capture endpoint. The mirror operates on a copy of the traffic — the original request and response path is unaffected.

```yaml
api_mirror_adapter:
  mirror_target: "http://cvs-capture:8080/mirror"
  mirror_percentage: 100
  mirror_request_body: true
  mirror_response_body: true
  # Original path is never delayed or modified
```

### 6.6 SmartNIC Capture Adapter

```
Capture Point:      Network interface hardware
Integration:        Dedicated hardware capture on gate's NIC
Observation Delay:  <1μs
Zero CPU impact:    Capture runs on NIC offload engine
```

For implementations requiring sub-microsecond capture latency and zero CPU impact on gate evaluation (typically FPGA-based gate hardware or ultra-low-latency financial deployments), the SmartNIC adapter captures all gate traffic at the hardware level. Configuration is NIC-vendor-specific; this document specifies behavioural requirements:

- The SmartNIC capture engine **MUST** operate independently of the gate CPU
- Capture **MUST NOT** add latency to the gate's critical path
- Captured traffic is forwarded to the CVS capture service over a dedicated network path

---

## 7. Deployment Topologies

### 7.1 Pre-Production: Discovery Mode Is Mandatory Before Enforcement

Every production deployment follows a mandatory Discovery Phase before gate enforcement goes live. Skipping Discovery and going directly to enforcement produces operational risk: constraints that are too strict block legitimate operations; constraints that are too loose provide no protection.

Discovery Mode corresponds to what `512-ops/INTEGRATION_STEPS.md` calls observation mode — all seven invariants are evaluated, no execution is blocked, all results are recorded. The upstream preparation work (boundary mapping, parallel path audit, Proposal Object definition, constraint definition) defined in `512-ops/INTEGRATION_STEPS.md §1–4` **MUST** be complete before Discovery Mode begins. Discovery Mode is not the place to discover that constraint definitions are missing or that boundaries have not been mapped — it is the place to verify that the upstream work was done correctly.

**Discovery Mode configuration:**

```yaml
gate_mode: "discovery"
# All evaluation results are computed and logged
# All deny decisions are recorded
# No execution is blocked
# Output: conformance gap analysis
```

Discovery phase duration: 30–90 days depending on system complexity. Discovery phase output: a gap analysis showing which invariants fail, at what frequency, for which agents, in which workflows.

**Enforcement Mode transition checklist:**

- [ ] All invariant-1 violations reviewed and addressed or accepted with documented rationale
- [ ] All invariant-2 violations resolved (consent infrastructure in place)
- [ ] All invariant-3 violations resolved (withdrawal propagation implemented)
- [ ] False positive rate below 0.1% on production traffic replay
- [ ] Intent-execution correspondence enforcement implemented at execution layer
- [ ] CVS integration tested: Evidence Objects generated for allow, deny, and gap events
- [ ] Fail-open tested under simulated gate failure
- [ ] Performance envelope validated: median <50μs, p99 <200μs at production throughput
- [ ] Commit path exclusivity verified: penetration test confirms no route to execution surface bypasses gate

**Critical stop condition:** If the commit boundary cannot be positively identified and isolated from parallel commit paths, enforcement **MUST NOT** proceed. Advisory governance may remain valuable, but it is not a Commit Gate satisfying 512's properties.

### 7.2 On-Premises Topology

For regulated industries (financial services, healthcare, defence) with data sovereignty or air-gap requirements.

```
┌─────────────────────────────────────────────────────────┐
│ On-Premises Network                                      │
│                                                          │
│  ┌──────────────────┐      ┌─────────────────────────┐  │
│  │ Execution Surface│──→──│  COMMIT GATE            │  │
│  │ (AI / Financial  │      │  (Enforcement VLAN)     │  │
│  │  / Hardware)     │      └────────────┬────────────┘  │
│  └──────────────────┘                   │               │
│                                         │ async, append │
│                              ┌──────────▼────────────┐  │
│                              │  CVS Sidecar          │  │
│                              │  (Capture VLAN)       │  │
│                              └──────────┬────────────┘  │
│                                         │ append-only   │
│                              ┌──────────▼────────────┐  │
│                              │  Evidence Store       │  │
│                              │  (WORM / MinIO)       │  │
│                              └──────────┬────────────┘  │
│                                         │ read-only     │
│                              ┌──────────▼────────────┐  │
│                              │  Access Plane         │  │
│                              │  (DMZ VLAN)           │  │
│                              └───────────────────────┘  │
│                                         │               │
└─────────────────────────────────────────┼───────────────┘
                                          ↓ XRPL anchoring
                                  Public Settlement Ledger
```

**Infrastructure specifications:**

| Component | Technology | Specification |
|---|---|---|
| Commit Gate process | Docker / Kubernetes | 8 vCPU, 32 GB RAM, NVMe SSD |
| CVS Sidecar | Docker / Kubernetes | 4 vCPU, 16 GB RAM, 500 GB SSD |
| Evidence Store | MinIO (S3-compatible) | 10 TB, object lock enabled |
| Access Plane | Docker / Kubernetes | 2 vCPU, 8 GB RAM |
| HSM | Thales Luna / Entrust | FIPS 140-2 Level 3 |

### 7.3 Hybrid Cloud Topology

For organisations transitioning to cloud or operating across multiple trust boundaries. The gate and CVS capture run on-premises (data sovereignty preserved); Access Plane and interpretation tooling run in cloud.

```
On-Premises:  Commit Gate → CVS Sidecar → Evidence Store (primary)
                                                ↓ encrypted replication (TLS 1.3)
Cloud:                                    Evidence Store (replica)
                                                ↓ read-only
                                          Access Plane (cloud)
                                                ↓
                                          Interpretation Tools (cloud)
```

Replication is append-only. Evidence Objects written to the on-premises store replicate to cloud storage via encrypted tunnel. The settlement anchoring event (XRPL submission) originates from on-premises to maintain low latency. Evidence Objects are never modified in transit or at rest.

### 7.4 Cloud-Native Topology

For SaaS providers and digital-native organisations without on-premises infrastructure.

```
Production VPC (Execution + Gate):
  Commit Gate in dedicated security group
  Outbound-only rules to CVS event queue
  No inbound connections from evidence store

Evidence Store VPC:
  S3 with Object Lock enabled
  VPC endpoint — access restricted to Capture Plane security group
  No public access

Access Plane VPC:
  ALB with HTTPS-only
  WAF with rate limiting
  Read-only access to Evidence Store via VPC endpoint
```

**Cloud-native infrastructure costs (illustrative — see §-1.9):**

| Component | Technology | Monthly Cost |
|---|---|---|
| Commit Gate | ECS Fargate (4 tasks, 8 vCPU / 32 GB each) | ~$1,120 |
| CVS Sidecars | ECS Fargate (4 tasks) | ~$560 |
| Evidence Store | S3 + Object Lock (5 TB) | ~$115 |
| HSM | AWS CloudHSM | ~$1,460 |
| Access Plane | ECS Fargate (2 tasks) | ~$280 |
| **Total** | | **~$3,535/month** |

---

## 8. Performance Envelope

### 8.1 Latency Budget by Component

The total gate evaluation budget is 50μs median, 200μs at p99. This budget is allocated across the four validation steps:

| Step | Budget (median) | Budget (p99) | Notes |
|---|---|---|---|
| Intent parsing + auth | 5μs | 10μs | Struct deserialisation + token verify |
| Context binding | 10μs | 20μs | Cache-hit path; cold path pre-fetched |
| Constraint evaluation (7 invariants) | 30μs | 100μs | Compiled bytecode; no I/O |
| Commit authorisation signal | 5μs | 10μs | Struct serialisation + queue write |
| CVS event forwarding | async | async | Off critical path; does not count |

### 8.2 Software Gate — Hardware Requirements

Minimum specification for a software gate implementation meeting the latency budget at 10,000 evaluations/second:

| Component | Minimum | Recommended |
|---|---|---|
| CPU | 4 cores, 3.0 GHz, modern x86-64 | 8 cores, 3.5 GHz, with AVX-512 |
| RAM | 16 GB | 32 GB |
| Storage | NVMe SSD (for local gap queue) | NVMe RAID-1 |
| Network to exec surface | <1ms RTT | <100μs RTT |
| Network to CVS queue | <5ms RTT | <1ms RTT |
| OS | Linux, kernel 5.15+, CPU pinning enabled | Same + NUMA awareness |

At sustained load >50,000 evaluations/second, add horizontal gate replicas behind a consistent-hash load balancer. The canonical specification is identical across all replicas — specification hash is verified at each replica startup.

### 8.3 Gate Addition Adds 10–50μs at the Commit Boundary

Adding a Commit Gate to an existing execution pipeline adds evaluation latency at the commit boundary. The relative impact depends on existing pipeline latency:

| Domain | Existing pipeline latency | Gate addition | Relative overhead |
|---|---|---|---|
| AI agent systems | 100–500μs (inference) | 10–50μs | 5–10% |
| Financial systems | 50–200μs (order processing) | 10–50μs | 10–20% |
| Hardware / manufacturing | 10–100ms (control loop) | 10–50μs | <0.1% |

For financial systems where 10–20% latency overhead is unacceptable, FPGA-based gate hardware reduces evaluation to under 5μs — restoring effective overhead to under 2%.

### 8.4 FPGA Hardware Reduces Evaluation to Under 5μs

For execution surfaces operating at sub-10μs timescales (high-frequency trading, real-time hardware control), a software gate adds unacceptable latency. An FPGA-based Commit Gate reduces evaluation latency to under 5μs.

The FPGA implementation requirements:

- The seven invariant expressions are synthesised to FPGA logic at specification compile time
- The compiled bitstream is the FPGA equivalent of the software bytecode bundle
- The bitstream hash **MUST** be verified against the canonical commitment before deployment
- Fail-open behaviour **MUST** be implemented in FPGA logic — if the FPGA evaluation path fails, the fallback path allows execution and asserts a gap signal
- The gap signal triggers a gap record in the host system's CVS event queue

FPGA synthesis changes are equivalent to software constraint changes: a new bitstream produces a new hash, which must be committed and disclosed to parties before enforcement.

Validated FPGA platforms: Xilinx Alveo U250 (<3μs evaluation), Intel Stratix 10 (<4μs evaluation). Performance figures are illustrative and depend on constraint complexity. *(illustrative — see §-1.9)*

### 8.5 CVS Capture Adds Zero Evaluation Latency

CVS event forwarding is fully asynchronous and off the evaluation hot path. The gate writes events to a local in-process buffer; a background thread drains the buffer to the CVS event queue. The evaluation critical path does not wait for queue acknowledgement.

Under sustained load, the buffer absorbs bursts. Buffer overflow — the condition where CVS events cannot be drained fast enough — generates a gap condition, not an evaluation failure. The gate continues evaluating; gap records accumulate until the drain recovers.

---

## 9. Security Model

### 9.1 The Specification Is the Primary Attack Surface

The specification is the gate's attack surface. An attacker who can substitute or modify the specification without detection has defeated the gate without touching the evaluation logic.

Three layers prevent this:

**Load-time hash verification:** The gate process verifies the specification hash against the canonical commitment at startup. A hash mismatch causes startup failure, not silent operation with a modified spec. The gate **MUST** log startup hash verification results to a tamper-evident log.

**Runtime immutability:** The specification is loaded into process memory as a read-only region. No runtime code path writes to that region. Any memory write to the specification region triggers a process abort and gap record.

**Witness layer hash recording:** Every Evidence Object emitted by the CVS witness layer includes the `spec_hash` field from the Observation Point 2 event. An auditor who suspects specification substitution computes the SHA-256 of the specification the gate claims to be running and compares it to `spec_hash` values in the evidence chain. Hash mismatch is mechanically detectable by any party with access to the public ledger.

### 9.2 The Gate Process Must Run in Isolation

The gate process **MUST** run in isolation from the execution surface it governs:

- Separate process, separate OS user, no shared memory with execution surface
- Separate network security group: inbound from execution surface (proposals), outbound to CVS queue and context registries only
- No inbound connections from any source other than the execution surface
- Gate process **MUST NOT** have write access to execution surface storage

If the gate process is compromised, it can be replaced without modifying the execution surface. The execution surface produces Evaluation-Unavailable DENY during gate replacement; gap records accumulate at the CVS sidecar for the downtime period.

### 9.3 HSM Key Custody for Specification Signing

Specification files are cryptographically signed by the specification authority before deployment. The signing key **MUST** be held in a Hardware Security Module:

- FIPS 140-2 Level 2 minimum (Level 3 recommended)
- Dedicated HSM partition for specification signing keys
- Key generation occurs inside the HSM; private key never leaves
- Signing operations occur inside the HSM

Gate startup verifies both the SHA-256 hash (integrity) and the cryptographic signature (authority). A specification that is hash-correct but unsigned by an authorised key is rejected.

Supported HSMs: AWS CloudHSM (FIPS 140-2 Level 3), Azure Dedicated HSM (FIPS 140-2 Level 3), Thales Luna (on-premises, FIPS 140-2 Level 3).

### 9.4 Signing Keys Rotate on a Fixed Schedule

Specification signing keys rotate on the following schedule:

- Annual rotation: standard deployments
- Quarterly rotation: high-security environments (financial, healthcare, defence)
- Immediate rotation: suspected compromise or personnel departure with key access

Rotation process:

1. Generate new key pair inside HSM
2. Sign the current specification with the new key (producing a new signature alongside the existing one)
3. Update gate deployments to trust both old and new signing keys (rolling)
4. After all gates confirm new-key verification, retire the old key from the trust list
5. Archive the old public key (retain permanently for evidence verification against historical signatures)

Evidence Objects and specification signatures include a `key_id` field. Historical verification uses the archived public key for the `key_id` present in the signature. Key retirement does not invalidate historical evidence.

### 9.5 Compromise Protocol

**Gate process compromise:**

An attacker who has gained code execution in the gate process can observe proposals and potentially delay evaluation (creating gaps). The attacker cannot modify stored Evidence Objects (append-only WORM storage), cannot sign false Evidence Objects (signing key in HSM), and cannot forge the canonical specification hash (SHA-256 is computationally infeasible to forge).

Response: isolate the compromised process, analyse the evidence chain for gaps during the compromise window, rotate specification signing keys, disclose compromise duration if evidence integrity is questioned by auditors.

**Specification signing key compromise:**

An attacker with HSM access can sign a modified specification. Detection: the modified specification produces a different SHA-256 hash, which will not match `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5`. Any party can verify this. If the attacker also changes the canonical commitment recorded in the public repository, that modification is timestamped and detectable through the repository history.

Response: rotate signing keys immediately, verify all gate instances are running against the canonical hash, disclose the compromise window.

**Context registry compromise:**

An attacker who controls a context registry (consent store, capability grant store) can cause the gate to evaluate against false context — granting consent that was not given, or extending capability limits beyond their authorised values. The gate evaluates correctly against the context it receives; the attack is at the registry, not the gate.

Mitigation: context registries **MUST** themselves log all writes as Evidence Objects with CVS capture. Consent grants and capability modifications are witnessed events, not internal database mutations. Registry write-path hardening is a deployment requirement, not a gate requirement.

### 9.6 Separation of Authority Is Structural, Not Procedural

No single role or system may simultaneously possess authority over both enforcement and evidence. This separation is the structural property that makes evidence trustworthy.

The gate **MUST NOT** have access to: evidence store write path beyond its own append queue, CVS attestation keys, Access Plane query interface.

CVS **MUST NOT** have access to: gate specification, gate evaluation logic, gate configuration, context registries.

If a single operator account has both gate administrative access and evidence store access, that operator can suppress evidence of gate failures. The IAM model **MUST** structurally prevent this.

---

## 10. Attack Vectors

**Specification substitution** — an adversary replaces the running specification with a modified version while continuing to claim canonical conformance.
*Mechanism:* The gate is redeployed with a modified specification file. Evaluation continues; Evidence Objects appear to show constraint enforcement. The modified specification relaxes specific invariants.
*Defense:* Every Evidence Object includes `spec_hash`. Any party computes SHA-256 of the running specification and compares to `spec_hash` in the evidence chain. The canonical commitment `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5` is publicly anchored and independently verifiable. Hash mismatch is mechanically detectable.
*Residual risk:* An adversary who simultaneously controls the gate, the witness layer, and the public ledger can fabricate matching hashes across all three. The architecture separates these three systems under independent control to require extraordinary, multi-system compromise for this attack.

**Runtime specification injection** — an adversary attempts to modify the loaded specification in memory after startup.
*Mechanism:* Exploitation of a memory vulnerability in the gate process to write to the specification memory region.
*Defense:* The specification is loaded into an OS-protected read-only memory region (`mprotect(PROT_READ)`). Any write to that region triggers a segmentation fault and process abort. The process abort is itself a gap event — recorded and forwarded to the witness layer before the process terminates.
*Residual risk:* A sufficiently privileged OS-level attacker (root compromise) can bypass `mprotect`. OS-level access controls and process isolation are the outer defence.

**Context registry poisoning** — an adversary modifies a context registry to produce false evaluation inputs (fabricated consent records, inflated capability grants).
*Mechanism:* Direct write to the consent store or capability registry bypassing the write-audit path.
*Defense:* Context registry writes are themselves witnessed events — the registry write path passes through CVS capture. Unauthorised writes produce Evidence Objects with anomalous identity fields. The absence of a witnessed write event for a consent record whose value changed is itself detectable through evidence gap analysis.
*Residual risk:* Registry writes that occur before CVS capture is instrumented for the registry write path are undetected. Coverage completeness for context registries **MUST** be part of the Declared Observation Surface (defined in `CVS_ARCHITECTURE §4.3`).

**Bypass path exploitation** — an adversary routes proposals directly to the execution surface, bypassing gate evaluation entirely.
*Mechanism:* Modification of execution surface routing, use of emergency override paths, direct database writes, or administrative API paths that skip gate evaluation.
*Defense:* Any execution event without a corresponding CVS pre-validation and validation-result Evidence Object creates a detectable evidence absence. Evidence gap analysis identifies execution without evaluation. Bypass path elimination (§1.3) and commit path ownership (§1.5) are the primary structural defences.
*Residual risk:* Bypass detection depends on CVS coverage of the full execution surface. Execution pathways outside witness coverage produce neither evaluation records nor gap records. Coverage completeness is a deployment responsibility.

**Bypass accumulation** — a deployment builds the gate correctly in the primary path but accumulates bypass-equivalent exceptions over time until the boundary is structurally irrelevant.
*Mechanism:* Emergency admin paths, operator override mechanisms, and direct execution surface access are added one at a time — each individually justified by operational need, collectively hollowing out the boundary. No single addition breaks the architecture. The pattern does.
*Defense:* All execution paths, including override and emergency paths, **MUST** either pass through gate evaluation or generate a GAP record. An override path that produces no GAP record is a bypass. Periodic structural audits of all execution pathways — verifying that every route to the execution surface passes through the gate or generates a record — are required. See §1.3 and §1.5.
*Residual risk:* Bypass accumulation is not detectable by examining any single event in the evidence chain. It requires structural pathway audit against the full execution surface topology. Deployments without a periodic structural audit process are vulnerable to this failure mode regardless of initial implementation quality.

**Validation gap exploitation** — an adversary deliberately induces gate failure to create windows of unconstrained execution.
*Mechanism:* Resource exhaustion, network partition, or targeted denial-of-service against the gate process. Under the Evaluation-Unavailable DENY doctrine, gate failure produces DENY — the commit path remains closed. The attack surface shifts from ungoverned execution to denial of service. Gate high-availability configuration is the mitigation.
*Defense:* Validation gaps are first-class witness layer records. The gap duration, reason, and executing identity during the gap are all captured. Post-gap forensic analysis identifies all executions during the gap window. Gate high-availability configuration (§7) is the primary mitigation — redundant gate instances reduce gap windows to the failover interval.
*Residual risk:* Executions during a gap are unconstrained. They are recorded but not blocked. Gate infrastructure resilience determines the achievable gap window. Single-gate deployments with no redundancy have longer gap windows under targeted attack.

**Intent declaration spoofing** — a proposing entity declares a benign intent but executes against a broader scope after the gate allows the proposal.
*Mechanism:* The gate evaluates declared intent. If the execution layer enforces no bounds on actual execution relative to the declared scope, the allow result is advisory.
*Defense:* Divergence between declared intent and actual execution scope is detectable in the CVS evidence chain by comparing the pre-validation intent declaration against the post-execution actual scope record (Observation Point 3). Enforcement of intent-execution correspondence at the execution layer (§4.3) is the primary prevention mechanism.
*Residual risk:* The gate cannot prevent what it does not evaluate. Intent-execution correspondence enforcement is an execution-layer implementation responsibility, not a gate responsibility. Evidence of divergence is available after the fact; prevention requires execution-layer enforcement.

**Constraint specification ambiguity** — a constraint is specified with sufficient precision to compile but with semantic gaps that adversarial inputs exploit.
*Mechanism:* Constraint designers specify policy goals rather than exhaustive executable logic. The constraint compiles successfully but contains edge cases: inputs that are syntactically within bounds but semantically harmful.
*Defense:* The 512-byte limit forces maximum distillation. Constraint design review by qualified architects before production enforcement is mandatory. The Discovery Phase (§7.1) surfaces false negatives (requests that should deny but allow) before enforcement goes live.
*Residual risk:* Semantically incomplete constraints that are syntactically deterministic pass compilation. Constraint design quality is a human responsibility that the gate cannot substitute for. Specification review is a mandatory pre-enforcement gate.

---

## 11. Conformance Requirements

### 11.1 Mandatory Behaviors

A gate implementation satisfying 512's properties exhibits all of the following. An implementation that does not exhibit any item does not satisfy 512's properties, regardless of documentation or naming:

- Position the gate at the commit boundary — between authorisation and irreversible state change, with no parallel commit paths in production
- Ensure there exists exactly one path to irreversible state change, and that path does not open without the gate's authorisation signal
- Evaluate all seven invariants on every proposal without exception
- Return binary output only: ALLOW or DENY; never scored, probabilistic, conditional, or deferred results
- Complete evaluation in a median of <50μs and a 99th percentile of <200μs at sustained production throughput
- Produce Evaluation-Unavailable DENY: when the gate is unavailable or evaluation times out, produce DENY (deny_cause: evaluation_unavailable) with failure cause and retry path; commit path remains closed; execution does not proceed
- Emit gap records to the CVS sidecar for all evaluation-unavailable DENY events; persist locally if the sidecar is unavailable; forward on reconnection
- Verify the canonical specification hash (`7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5`) at startup and refuse to start on hash mismatch
- Load the specification into a read-only memory region after startup verification
- Emit three CVS observation events per evaluation: pre-validation, validation-result, post-execution
- Include `spec_hash`, `per_invariant_results`, and `violated_constraint_detail` in every validation-result event
- Maintain structural separation of authority from the witness layer (no gate write access to evidence store; no CVS access to gate configuration)
- Disclose the violated invariant identifier and deny message on every deny result
- Run in isolation from the execution surface it governs (separate process, separate OS user, no shared memory)
- Hold specification signing keys in an HSM (FIPS 140-2 Level 2 or higher)
- Instrument and expose latency percentile metrics at all four validation steps
- Instrument and expose gap event metrics (count, duration, reason) to operational monitoring

### 11.2 Prohibited Behaviors

A gate implementation satisfying 512's properties does not exhibit any of the following. An implementation that exhibits any item does not satisfy 512's properties:

- Return a scored, probabilistic, conditional, or deferred result from gate evaluation
- Block execution when the gate is unavailable without producing Evaluation-Unavailable DENY with disclosed cause and retry path (opaque blocking)
- Open the commit path when the gate is unavailable (ungoverned execution — non-conformant)
- Allow runtime modification of the constraint specification without a process restart and hash re-verification
- Accept a specification that does not hash-verify at startup
- Allow the gate process to read from the evidence store
- Allow the CVS process to modify gate configuration or evaluation logic
- Route execution proposals around the gate for any reason without generating a gap record
- Evaluate a subset of the seven invariants and claim 512 conformance
- Suppress or discard gap records under any condition
- Accept a fail-open timeout that exceeds the evaluation latency p99 budget (200μs) — if evaluation has not completed within the budget, the gate must fail open, not continue evaluating indefinitely
- Position evaluation upstream of a separately operable execution surface (pre-check architecture)
- Route the gate's authorisation signal through an intermediary before it reaches the commit path

### 11.3 Scope of Valid Conformance Claims

An implementation may be described as satisfying 512's properties only within the following boundaries:

- A gate may be described as guaranteeing correctness of outcomes only if it evaluates outcome quality — a Commit Gate evaluates admissibility against pre-committed constraints; outcome quality is outside its scope
- A gate may be described as preventing all harm only if its constraint set is exhaustive for the harm scenario in question — constraints may be incomplete, incorrectly specified, or inapplicable; the gate enforces exactly what the specification says, nothing more
- A gate may be described as replacing regulatory audits only if a qualified legal or compliance authority has made that determination — the gate produces execution-time evidence suitable for audit; it does not perform audit functions or make compliance determinations
- A gate may be described as 512-conformant only if it has passed every test in §11.4
- A gate may be described as satisfying 512's properties only if its specification produces a hash-verified match to `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5`

### 11.4 Properties Verification Checklist

| Test | Procedure | Pass Condition |
|---|---|---|
| Specification hash match | `sha256sum 512-kernel-padded.txt` | `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5` |
| Hash mismatch causes startup failure | Start gate with modified spec | Gate refuses to start; logs mismatch |
| Evaluation latency (median) | 10,000 proposals at production throughput | Median <50μs |
| Evaluation latency (p99) | 10,000 proposals at production throughput | p99 <200μs |
| Deterministic evaluation | 1,000 identical proposal pairs | All pairs produce identical output |
| Evaluation-Unavailable DENY on gate failure | Kill gate process mid-evaluation | DENY returned (deny_cause: evaluation_unavailable); commit path remains closed; gap record emitted to CVS sidecar |
| Evaluation-Unavailable DENY on timeout | Inject 200μs+ evaluation delay | DENY returned (deny_cause: evaluation_unavailable); commit path remains closed; gap record emitted to CVS sidecar |
| Gap record contents | Inspect gap record after evaluation-unavailable DENY | Contains proposal_id, agent_id, gap_start, gap_reason, gate_output_during_gap |
| Gap record persistence | Kill CVS queue during gap event | Gap record persisted locally; forwarded on reconnection |
| All 7 invariants evaluated | Unit test each invariant (§3 fixtures) | All 28 fixture tests pass |
| Binary output only | Submit 100 proposals | All responses contain only `ALLOW` or `DENY` |
| Deny includes violated invariant | Submit proposal violating each invariant | Response includes invariant identifier and deny_message |
| CVS pre-validation event emitted | Integration test | Evidence Object present for every proposal |
| CVS validation-result event emitted | Integration test | Evidence Object present with spec_hash and per_invariant_results |
| CVS post-execution event emitted | Integration test | Evidence Object present after execution completes |
| Separation of authority | IAM audit | Gate has no read access to evidence store |
| Separation of authority | IAM audit | CVS has no access to gate configuration |
| No bypass path exists | Penetration test: attempt direct execution | All routes to execution surface pass through gate |
| Commit path exclusivity | Penetration test: attempt execution without gate signal | No route to execution surface bypasses gate authorisation signal |
| Pre-check architecture absent | Structural review of execution pipeline | Execution surface not operable independently of gate |
| Specification read-only in memory | Attempt runtime spec write | Process aborts; gap record generated |
| HSM key custody | HSM configuration audit | Signing key never extracted from HSM |
| Latency metrics exposed | Query metrics endpoint | All four step latencies exposed as percentile distributions |
| Gap metrics exposed | Query metrics endpoint | Gap count, duration, reason exposed |

---

## 12. Constraint Definition Layer (Non-Normative)

This section is non-normative. It describes the upstream work that organisations must complete before gate evaluation can begin. Nothing in this section creates requirements on gate implementations — those are defined in §11. This section addresses the constraint definition work that is the organisation's responsibility, not the gate's.

### 12.1 The Gate Does Not Define Constraints

The gate evaluates constraints. It does not define them. Constraint definition occurs upstream, before any proposal reaches the commit boundary. The gate receives a compiled constraint set at startup, hash-verifies it, and evaluates every proposal against it deterministically. What those constraints say — what they protect, what signals they evaluate, what thresholds they enforce — is entirely outside the gate's scope.

Three functions are involved in gate execution. They must remain structurally separate:

| Function | What it does | Who owns it |
|---|---|---|
| **Definition** | Translates policy into executable constraints | The organisation |
| **Expression** | Encodes constraints as deterministic binary logic | The organisation's engineers |
| **Enforcement** | Evaluates constraints against proposals | The gate |

Any system that requires the gate to interpret, adapt, or apply judgment to constraints at evaluation time is not a Commit Gate. It is a policy engine.

### 12.2 The Constraint Definition Model

Every constraint must be defined using this four-field structure before it can be expressed as executable logic:

**Intent** — what is being protected. State the property the constraint enforces in one sentence. Not the rule — the property.

**Signal** — what data proves the property holds. Name the specific data field or record that the gate will evaluate. If a specific data source cannot be named, the constraint is not ready for expression.

**Threshold** — the binary condition. Express the signal as a deterministic true/false condition over typed inputs. This is the expression the gate evaluates.

**Authority** — the source of truth for the signal. Name the system that holds the data the threshold evaluates against. The gate queries this system during context binding.

A constraint definition is complete only when all four fields are populated and the threshold expression is binary-reducible without any prohibited language.

### 12.3 Binary Reducibility Requirement

Every constraint must be reducible to a binary evaluation before it reaches the gate. The gate produces exactly two evaluation outputs per constraint: pass or fail.

If a constraint cannot be expressed as a binary condition over named, typed inputs, it is not ready for expression. The following language indicates a constraint that is not yet binary-reducible and **MUST NOT** be submitted to the expression stage:

| Prohibited term | Why prohibited |
|---|---|
| "reasonable" | Requires judgment to evaluate |
| "appropriate" | Context-dependent; not deterministic |
| "high risk" | A scoring concept, not a binary condition |
| "likely" | Probabilistic; not deterministic |
| "significant" | Requires threshold definition before use |
| "material" | Legal interpretation required |
| "where feasible" | Introduces conditionality |
| "subject to policy" | Defers definition to runtime |

**Translation examples:**

❌ Not binary-reducible: `"transactions must not be high risk"`
✅ Binary-reducible: `current_exposure + proposed_value <= exposure_limit` where `exposure_limit` is sourced from the counterparty registry.

❌ Not binary-reducible: `"consent must be reasonably current"`
✅ Binary-reducible: `consent_expiry > evaluation_timestamp` where `consent_expiry` is sourced from the consent registry and `evaluation_timestamp` is the gate's clock at evaluation.

### 12.4 Determinism Requirement

Identical inputs must produce identical outputs on every invocation, on every machine, at any time. A constraint is deterministic when every input is typed and sourced from a named registry, the threshold expression uses only deterministic operators, and no external I/O occurs during evaluation.

A constraint is not deterministic when it relies on a model, heuristic, or scoring system, or when it produces different results for the same inputs under different conditions.

Non-deterministic constraints cannot be evaluated by a Commit Gate. Compilation rejects any expression whose evaluation time exceeds the 50μs budget or requires external I/O during evaluation — all inputs must be fully bound from the declared input schema before evaluation begins.

### 12.5 Common Failure Modes

**Vague policy language.** Policy written in natural language intended for human interpretation reaches the expression stage without translation. The gate cannot evaluate "agents must act in the customer's best interest" — it requires a specific observable signal expressed as a binary threshold.

**Hidden assumptions.** A constraint references data that is assumed to exist without being explicitly declared in the input schema. Every variable in the threshold expression requires a named source system, field name, and data type. No undeclared dependencies.

**Runtime interpretation.** A constraint is expressed in a form that requires the gate to apply judgment at evaluation time. "Deny if the request appears unusual for this agent" is not a binary condition — it is a pattern-matching task. Define what "unusual" means in terms of specific, measurable deviations from declared parameters.

**External system dependency at evaluation time.** A constraint requires the gate to call an external system during evaluation. All inputs must be pre-fetched during context binding (Step 2), not during constraint evaluation (Step 3). Any input that cannot be pre-fetched is not a valid gate input.

**Temporal drift.** The constraint set in force at evaluation does not match the constraint set disclosed to affected parties. Every constraint set change produces a new compiled bundle with a new hash. The new hash must be disclosed to and acknowledged by affected parties before enforcement of the new set begins.

### 12.6 Anti-Drift Rules for Constraint Definitions

- Constraints must be versioned. Each version produces a distinct compiled bundle with a distinct hash.
- The spec hash must represent the complete active constraint set.
- Changes to any constraint require a new spec hash.
- The spec hash disclosed to affected parties must match the spec hash recorded in Evidence Objects.
- Constraints must not be modified at runtime.

### 12.7 Separation of Constraint Definition and Enforcement

Constraint definition must not leak into runtime. The gate receives a compiled constraint set. It does not receive policy intent, natural language rules, or interpretive guidance. It evaluates what it is given.

This separation is what makes enforcement verifiable. A gate that defines its own constraints at runtime has no fixed specification to commit to a hash. A gate whose specification can drift between disclosure and enforcement has no verifiable boundary.

For the full constraint definition model, per-invariant definition checklist, and failure mode reference, see `512-ops/CONSTRAINT_DEFINITION_LAYER.md`. For the 7-step enterprise integration workflow that positions constraint definition within the full deployment sequence, see `512-ops/INTEGRATION_STEPS.md`.

---

## Conclusion

A Commit Gate satisfying 512's properties is a deterministic function operating at the commit boundary of a machine-speed execution system. It enforces seven pre-committed invariants in 10–50μs. On infrastructure failure, it produces Evaluation-Unavailable DENY — the commit boundary holds unconditionally. It produces a structured evidence stream that a CVS-compatible witness layer transforms into an independently verifiable cryptographic record.

The engineering task is straightforward. Find the commit boundary — the precise point at which proposals become irreversible facts. Insert the gate at that point such that no path to that boundary exists without the gate's authorisation signal. Eliminate parallel paths. Verify the specification hash. Instrument the three CVS observation points. Run Discovery Phase before enforcement. Pass all tests in §11.4.

What is produced by that process is a gate that enforces 512's properties — mechanically, deterministically, at machine speed. The constraint being enforced is not invented here. It was found. The gate that enforces it is invented here. The difference between those two things is why the gate implementation is owned by its builder and the constraint it enforces is not.

Systems that instrument a gate satisfying these properties, paired with a CVS-compatible witness layer, produce execution-time evidence that is cryptographically committed, hash-chained, and anchored to a public settlement ledger. That record describes what executed, under what constraints, and with what authorisation. Its structural integrity does not depend on the organisation's assertion of its own behaviour — it is examinable by any party with access to the ledger and the evidence store.

Systems that do not instrument such a gate operate without that record. The constraint exists regardless. What differs is whether its satisfaction is structurally examinable.

**Canonical Repository:** github.com/JonathanMastersWatson/512

---

## Document Control

| Field | Value |
|---|---|
| Document | `512_IMPLEMENTATION_v3.4.md` |
| Version | 3.4 |
| Date | June 2026 |
| Author | Jonathan M. Watson |
| Audience | Engineers |
| Status | Active |
| Canonical Repository | github.com/JonathanMastersWatson/512 |
| Specification Commitment | SHA-256: `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5` |

### Changelog — v3.4

**June 2026 — Evaluation-Unavailable DENY doctrine throughout.**

**Modifications:**
- Abstract and Conclusion: "fails open" replaced with "produces Evaluation-Unavailable DENY — the commit boundary holds."
- §3.6 Invariant 6: `evaluate_with_fail_open` returning `('allow', 'gap')` replaced with `evaluate_with_infrastructure_failure_deny` returning `('deny', 'evaluation_unavailable', ...)`. Unit test fixture corrected — expected result is DENY, commit path remains closed.
- §4.1 sequence diagram: FAIL-OPEN PATH redrawn as EVALUATION-UNAVAILABLE DENY PATH. Infrastructure-failure handler produces DENY. Post-execution annotated ALLOW only.
- §4.1 Step 4 prose: "fail-open handler engages / commit path opens / execution proceeds" replaced with Evaluation-Unavailable DENY doctrine.
- §4.1 Step 4 bullet: "Fail-open" bullet replaced with "Evaluation-Unavailable DENY" bullet.
- §4.2 latency table: failure mode corrected from "Fail open; emit gap record" to "Evaluation-Unavailable DENY; emit gap record to CVS sidecar."
- §4.4 observation mode: "fail-open events recorded as evidence chain gaps" replaced with "evaluation-unavailable DENY events recorded; CVS sidecar records gap."
- §5.3: retitled from "Validation Gap Records" to "Evaluation-Unavailable DENY Records." Deny Evidence Object schema added. Gap record schema updated — `executing_identity` removed, `gate_output_during_gap` added.
- §9 Attack Vectors: gap exploitation vector — execution-proceeds doctrine replaced with Evaluation-Unavailable DENY doctrine; attack surface shift noted.
- §11.1 Mandatory Behaviors: "Fail open: execution proceeds" replaced with "Produce Evaluation-Unavailable DENY: commit path remains closed."
- §11.2 Prohibited Behaviors: "Block execution when gate unavailable (fail-closed)" replaced with two entries — opaque blocking and opening the commit path on gate unavailability.
- §11.4 Verification Checklist: fail-open test rows replaced — pass condition changed from "Execution continues" to "DENY returned; commit path remains closed."
- Gate replacement note: "execution surface continues operating in fail-open mode" replaced with "produces Evaluation-Unavailable DENY during gate replacement."

**Additions:** Nothing added.

**Removals:** `evaluate_with_fail_open` function returning `('allow', 'gap')` — removed. `executing_identity` field from gap record schema — removed.

### Changelog — v3.3

**May 2026 — competitive landscape and priority record cross-references.**

**Additions:**
- §0 Normative Relationships: two companion documents added — `AARM_AND_512.md` (architectural positioning relative to AARM/CSA) and `CANONICAL_COMMITMENT.md` (permanent priority and dated proof record).
- Document Control: Status updated from "Pre-Seal Hardening" to "Active".

**Modifications:**
- §0 Normative Relationships: stale reference `512_ARCHITECTURE_v3.1.md` updated to `512_ARCHITECTURE_v3.4.md`.
- Document Control table: version and document name corrected from v3.1 to v3.2 (prior entry omitted the table update); now advanced to v3.3.

**Removals:** Nothing removed.

---

### Changelog — v3.2

**Hardening pass — April 2026 repository alignment.**

**Additions:**
- Document Control: Status field added — Pre-Seal Hardening.
- §0 Normative Relationships: cross-reference to `LAYER_REFERENCE.md` added — the authoritative three-layer semantic firewall document.

**Modifications:**
- §1.5 Commit Path Ownership / §1.6 Non-Conformant Execution Patterns: canonical vocabulary confirmed — "exclusive commit authority" and "non-bypassable commit path" are the prescribed terms. Five non-conformant patterns (A–E) confirmed as the canonical anti-pattern set.
- §4.1 Evaluation Result: "MUST be one of exactly two values: ALLOW or DENY" confirmed. Fail-open path description confirmed: gate produces no output; fail-open handler engages; witness layer records evidence chain gap; gap record is not ALLOW.
- §11.2 Prohibited Behaviours / §11.4 Verification Tests: alignment confirmed with LAYER_REFERENCE.md prohibited claims.
- COMPILED_CONSTRAINT_FORMAT.md referenced as the canonical compiled constraint definition (new file added to 512-ops/ this pass).
- PROPOSAL_OBJECT.md referenced as the canonical Proposal Object definition (new file added to 512-ops/ this pass).

**Removals:** Nothing removed.

---

### Changelog — v3.1

**Additions:** Nothing added.

**Modifications:**
- §4.1 Step 3 schematic: `→ ALLOW / DENY / GAP` corrected to `→ ALLOW or DENY`. GAP is not a constraint evaluation output.
- §4.1 Step 4 schematic: `GAP → commit path opens (fail-open; gap record)` removed. GAP is not a gate signal. Fail-open behaviour is described in the separate fail-open path diagram.
- §4.1 Fail-open path diagram: `│◄── ALLOW (GAP) ────────│` removed. Gate produces no output when unavailable. Replaced with `[no gate signal — fail-open handler opens commit path]`.
- §4.1 Step 4 prose: "exactly three values: ALLOW, DENY, or GAP" corrected to "exactly two values: ALLOW or DENY." GAP reframed as a fail-open handler output to the witness layer, not a gate return value. MUST language updated accordingly.
- §4.4 Observation mode results list: `ALLOW / DENY / GAP` corrected to `ALLOW or DENY; fail-open events recorded as evidence chain gaps by the witness layer`.
- §4.4 Observation mode — GAP results bullet: reframed as `Fail-open events`. Gate unavailability generates witness layer evidence chain gaps, not a gate output category.
- §4.4 Observation mode valid outputs: "ALLOW, DENY, and GAP" corrected to "ALLOW or DENY".
- §5.1 Observation Point 2 JSON schema — `overall_result`: `"allow | deny | gap"` corrected to `"allow | deny"`. On fail-open events this field is absent; see `validation_gap` record.
- §5.1 Observation Point 2 JSON schema — `invariant_6_fail_open`: `"pass | fail | gap"` corrected to `"pass | fail"`. Per-invariant results are binary; inability to evaluate produces DENY, not a per-invariant gap.

**Removals:** Nothing removed.

---

### Changelog — v3.0

**Additions:**
- §12 Constraint Definition Layer (Non-Normative): new section. Defines the upstream work organisations must complete before gate evaluation begins. Covers the three-function separation (definition / expression / enforcement), the four-field constraint definition model (Intent / Signal / Threshold / Authority), binary reducibility requirement with prohibited language table and translation examples, determinism requirement, five common failure modes (vague policy language, hidden assumptions, runtime interpretation, external system dependency at evaluation time, temporal drift), anti-drift rules for constraint definitions, and the separation of constraint definition from enforcement. References `512-ops/CONSTRAINT_DEFINITION_LAYER.md` and `512-ops/INTEGRATION_STEPS.md` for operational detail.
- §0 Normative Relationships: four 512-ops operational reference documents added as non-normative companions — `INTEGRATION_STEPS.md`, `CONSTRAINT_DEFINITION_LAYER.md`, `REFERENCE_FLOW.md`, and `PROPERTIES_CHECKLIST.md`. Brief scope description for each.

**Modifications:**
- §4.4 Observation Mode: retitled to "Observation Mode Is the Correct Enterprise Entry Point." Extended to cover three categories of problem surfaced in observation mode (unexpected DENY results, GAP results, coverage gaps) with explanation of what each indicates and why finding them in observation mode is preferable to finding them in enforcement mode. Added reference to `512-ops/INTEGRATION_STEPS.md §5` for the full observation mode procedure.
- §7.1 Pre-Production Discovery Mode: extended to reference `512-ops/INTEGRATION_STEPS.md`. Clarifies that upstream preparation work (Steps 1–4) must be complete before Discovery Mode begins. Distinguishes Discovery Mode from upstream preparation — Discovery Mode verifies the upstream work was done correctly, not the place to discover it was not done.
- §0 Normative Relationships: architecture cross-reference updated to `512_ARCHITECTURE_v3.4.md`.

**Removals:** Nothing removed.

---

**Additions:**
- §1.5 Commit Path Ownership Is Non-Bypassable: new subsection. Defines the structural requirement that exactly one path to irreversible state change exists and that path does not open without the gate's authorisation signal. Distinguishes structural enforcement from procedural controls. States the conformant model. Enumerates MUST NOT conditions for pre-check positioning, intermediary routing, bypass without gap record. Defines failure consequence: a bypass path is a non-conformance condition regardless of frequency of use.
- §1.6 Non-Conformant Execution Patterns: new subsection. Explicitly labels and diagrams five non-conformant patterns: (A) API handoff, (B) queue handoff, (C) broker handoff, (D) pre-check positioning, (E) parallel/fallback path. Each pattern annotated NON-CONFORMANT with explanation. Conformant model diagram repeated for immediate contrast.
- §7.1 Enforcement Mode transition checklist: commit path exclusivity verification item added.
- §11.1 Mandatory Behaviors: commit path exclusivity item added — exactly one path to irreversible state change, not opening without gate's authorisation signal.
- §11.2 Prohibited Behaviors: two items added — pre-check architecture (evaluation upstream of separately operable execution surface); intermediary routing of gate's authorisation signal before it reaches the commit path.
- §11.4 Properties Verification Checklist: two new test rows added — commit path exclusivity (penetration test) and pre-check architecture absent (structural review).
- §8.1 Latency Budget table: Step 4 row renamed from "Result serialisation + handoff" to "Commit authorisation signal" for consistency.

**Modifications:**
- §0 Normative Relationships: architecture cross-reference updated from `512_ARCHITECTURE_v2.9.md` to `512_ARCHITECTURE_v3.4.md`.
- §0.1: architecture cross-reference updated from `512_ARCHITECTURE_v2.9.md §2–4` to `512_ARCHITECTURE_v3.4.md §2–4`.
- §4.1 Diagram: STEP 4 box renamed from "EXECUTION HANDOFF" to "COMMIT AUTHORISATION." Box content updated: "allow → return to exec surface" → "ALLOW → commit path opens"; "deny → return denial + reason" → "DENY → commit path closed + violated invariant"; "gap → allow + record gap" → "GAP → commit path opens (fail-open; gap record)." Fail-open path label updated: "allow" → "ALLOW (GAP)." Label "execution proceeds or is blocked" → "commit path opens or remains closed."
- §4.1 Step 4 header: renamed from "Step 4 — Execution Handoff" to "Step 4 — Commit Authorisation Signal."
- §4.1 Step 4 ALLOW bullet: "the gate MUST return this result to the execution surface without modification. Execution proceeds." → "the gate MUST return this result. The commit path opens. Execution proceeds."
- §4.1 Step 4 DENY bullet: "Execution does not proceed." → "The commit path remains closed. Execution does not proceed."
- §4.2 Latency Budget table: Step 4 row renamed from "Execution Handoff" to "Commit Authorisation Signal."
- §10 Bypass path exploitation: defense paragraph updated to reference §1.5 alongside §1.3.
- §10 Bypass accumulation: defense paragraph updated to reference §1.5 alongside §1.3.
- Conclusion paragraph 2: "Insert the gate at that point." → "Insert the gate at that point such that no path to that boundary exists without the gate's authorisation signal."

**Removals:** Nothing removed.

---

### Changelog — v1.10

**Additions:**
- §0 Normative Relationships: Constraint Architecture added as third canonical reference.
- §4.4 Observation Mode: new subsection.
- §10 Attack Vectors: bypass accumulation vector added.

**Modifications:**
- §-1.5 Ownership and Licensing: reverted from Apache License 2.0 to CC BY 4.0 Open Commons Declaration.
- §-1.7 License: re-inserted as CC BY 4.0 license block.
- §0 Normative Relationships: architecture cross-reference updated to `512_ARCHITECTURE_v2.9.md`.
- §1.3 Bypass Path Elimination: strengthened per hardening pass.
- §4.1 Step 3 and Step 4: ALLOW / DENY / GAP capitalised throughout. GAP semantics clarified.
- §11.1 and §11.2: definitional framing applied.
- §11.4: renamed from "Conformance Verification Checklist" to "Properties Verification Checklist."

**Removals:**
- §-1.6 Specification Status (added in v1.9): removed.
- Apache License 2.0 references removed.

---

### Changelog — v1.9

**Additions:**
- §-1.6: Specification Status — new subsection.

**Modifications:**
- §-1.5: Replaced Open Commons Declaration with Apache License 2.0 (subsequently reverted in v1.10).
- §0 Normative Relationships: open commons model reference removed.
- §0.1: Philosophical framing replaced with neutral technical description.

**Removals:**
- §-1.5 content: Open Commons Declaration removed (subsequently restored in v1.10).
- §-1.7: CC BY 4.0 license section removed (subsequently restored in v1.10).

---

### Changelog — v1.8

**Modifications:**
- §4.3, §5.2, §7.1, Conclusion: language precision hardening throughout.

**Removals:** Nothing removed.

---

### Changelog — v1.7

**Modifications:**
- §0.1, §2.1, §2.4, §3.7, §11.3: definitional framing applied; coercive language replaced throughout.

**Removals:** Nothing removed.

---

### Changelog — v1.6

**Modifications:**
- §-1.1, §-1.5, §-1.8, §-1.10, §0.1: authorial intent framing; absolute legal claims replaced.

**Removals:** Nothing removed.

---

### Changelog — v1.5

**Additions:**
- §-1.10 No Reliance, §-1.11 No Endorsement, §-1.12 Independent Verification Requirement, §-1.13 Builder Responsibility: all new.

**Modifications:** Nothing modified.

**Removals:** Nothing removed.

---

### Changelog — v1.4

**Additions:**
- §0.1: Reference Implementation Status subsection added.

**Modifications:**
- Abstract: Implementation boundary clarification added.

**Removals:** Nothing removed.

---

### Changelog — v1.3

**Modifications:**
- §2.1, §2.4, §4.1 Steps 3 and 4: normative MUST/MUST NOT language added throughout.

**Removals:** Nothing removed.

---

### Changelog — v1.2

**Modifications:**
- Aligned with STYLE_GUIDE_v2.0: 13 section headers rewritten as claims.

**Removals:** Nothing removed.

---

### Changelog — v1.1

**Additions:**
- §4.1: ASCII sequence diagram added.

**Modifications:** Nothing modified.

**Removals:** Nothing removed.

---

### Changelog — v1.0

**Additions:**
- All sections: initial version.

**Modifications:** Nothing modified (initial version).

**Removals:** Nothing removed (initial version).
