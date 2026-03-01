# CVS Architecture: The Cryptographic Verification Sidecar

**Jonathan M. Watson | 512 / CVS Architecture**
**Version 2.7 | February 2026**

---

## §-1 Legal Notice and Limitation of Liability

### §-1.1 Informational Nature

This document describes a neutral, open reference architecture for independent evidentiary systems. It is published for informational and architectural purposes only. The Cryptographic Verification Sidecar (CVS) reference architecture defined herein does not guarantee correctness of observed or constrained systems; does not guarantee compliance with any legal or regulatory requirement; does not guarantee insurance eligibility, premium reduction, or underwriting outcomes; does not guarantee dispute resolution success; and does not guarantee full system coverage unless explicitly declared via a Declared Observation Surface (DOS) anchored to a public settlement ledger. Nothing in this document constitutes legal, regulatory, financial, insurance, or professional advice.

### §-1.2 No Warranty

To the maximum extent permitted under applicable law, this architecture and all associated documentation are provided "As Is" and "As Available" without any express or implied warranty, including but not limited to warranties of merchantability, fitness for a particular purpose, non-infringement, regulatory compliance, insurance eligibility, performance, or outcome guarantee. All implementation risk rests solely with the deploying organization.

### §-1.3 No Professional Advice

This document does not constitute legal, regulatory, financial, actuarial, or insurance advice. Deploying organizations **MUST** obtain independent professional advice appropriate to their jurisdiction and operational context before making representations about CVS deployment to regulators, insurers, courts, or counterparties. The author is not a lawyer, actuary, insurance broker, or financial adviser.

### §-1.4 No Guarantee of Coverage or Compliance

Implementation of this architecture does not guarantee regulatory approval, audit certification, insurance eligibility, or legal sufficiency of produced evidence. CVS produces cryptographic evidence of observation. Whether that evidence satisfies a particular legal, regulatory, or insurance requirement in a particular jurisdiction is a determination that must be made externally, by qualified professionals, in context. The distinction between *producing evidence* and *satisfying a legal standard* is material and must not be collapsed.

### §-1.5 Ownership and Licensing — Open Commons Declaration

**CVS** (Cryptographic Verification Sidecar) is an invented witness architecture released under Apache License 2.0. Apache 2.0 grants broad rights to use, reproduce, distribute, and create derivative works, and includes an express patent grant from contributors. The project does not assert proprietary control over the base architecture beyond the terms of Apache 2.0. Derivative works built on this base are a distinct class of work; their creators may assert and exercise intellectual property rights over those derivatives under applicable law.

**512** is a discovered constraint. The authors' position is that discovered constraints — properties that physics and systemic necessity force into existence regardless of human recognition — are not appropriate subjects of intellectual property ownership. The authors assert no copyright, patent, or proprietary rights over the 512 constraint set, the Commit Gate category, or the seven invariants committed to the canonical kernel file, and publish this material on that basis.

**Derivative works** built on top of CVS and 512 — implementations, managed services, SLA-bound products, interpretation tools, industry-specific deployments — are fully ownable and commercialisable by their creators. The base is open. What is built on the base belongs to its builder.

The intended model is open infrastructure: the architecture is available for anyone to use, implement, and build upon under the terms of Apache 2.0.

### §-1.6 Public Ledger References

References to public distributed ledgers in this document — including the XRP Ledger — are descriptive and technical, not promotional, advisory, or endorsatory. Mention of a specific ledger does not imply endorsement, partnership, dependency, or affiliation. The architecture is ledger-agnostic. Any settlement ledger satisfying mandatory requirements defined in `CVS_IMPLEMENTATION_v{M}.{m}.md §4` may be substituted without altering evidence semantics, disclosure behavior, or authority boundaries. Historical anchors remain verifiable on the ledger on which they were produced.

### §-1.7 License

This document and the base CVS architecture as defined herein are released under Apache License 2.0. Apache 2.0 governs use, reproduction, distribution, modification, and creation of derivative works. It includes an express patent grant: each contributor grants a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable patent licence for any patent claims licensable by that contributor that are necessarily infringed by their contribution or by the combination of their contribution with this work. The full licence text is available at https://www.apache.org/licenses/LICENSE-2.0.

Derivative works — implementations, products, services, and adaptations built on this architecture — may be licensed by their creators under terms of their choosing, including proprietary terms, provided those terms are consistent with the obligations of Apache 2.0. Contact: evidence-admin@512.systems.

### §-1.8 Jurisdictional Scope

This document is authored and published from Canada. Its authors and contributors, to the fullest extent permitted by law in Canada, the United States, and the United Kingdom, disclaim all liability for direct, indirect, incidental, consequential, or special damages arising from use, misuse, or reliance upon this architecture or any implementation derived from it. This disclaimer extends to regulatory penalties, insurance claim denial, business interruption, and data loss. Where liability cannot be fully disclaimed under applicable law, the authors seek to limit it to the fullest extent that applicable law permits. Deploying organizations assume all risk.

### §-1.9 Financial Projection Disclaimer

All cost, premium reduction, audit savings, and ROI projections in this document are illustrative examples only. They are not guarantees of insurance premium reduction, regulatory penalty avoidance, audit cost compression, financial return, or legal defense success. Actual results depend on deployment scope, cloud provider pricing at time of deployment, insurer underwriting practices, regulatory context, jurisdiction, operational integrity of the implementation, and factors outside the control of this architecture. Organizations using these projections in financial planning, board presentations, or regulatory submissions are solely responsible for the accuracy and appropriateness of those representations.

### §-1.10 No Reliance

This document is a descriptive technical specification and reference architecture only. It does not constitute and is not intended to be relied upon as a certification of compliance, a guarantee of regulatory sufficiency, a guarantee of audit success, a guarantee of insurance coverage, a guarantee of risk mitigation, or a representation of operational fitness. Compliance, certification, underwriting, and legal sufficiency are determinations made by regulators, courts, insurers, and licensed professionals. Any organisation implementing concepts described herein does so at its own risk and is solely responsible for deployment posture, regulatory interpretation, operational integrity, and jurisdictional compliance.

### §-1.11 No Endorsement

Nothing in this document constitutes endorsement of any implementation, endorsement of any derivative system, endorsement of any organisation, endorsement of any settlement ledger, or endorsement of any commercial deployment. References to regulatory frameworks, standards bodies, or public ledger networks are descriptive only and do not imply approval, partnership, affiliation, or recognition. No institution has certified, adopted, approved, or validated 512 or CVS unless expressly stated in a separate, formally executed written agreement.

### §-1.12 Independent Verification Requirement

Where verification is discussed in this document, it refers to cryptographic or structural verifiability of recorded data — not legal, regulatory, or institutional validation. Structural verifiability does not equate to compliance determination. The ability to independently verify a hash chain or a Merkle inclusion proof against a public ledger is a mathematical property. Whether that mathematical property satisfies a legal or regulatory evidentiary standard is a determination external to this architecture.

### §-1.13 Builder Responsibility

Any party constructing, deploying, or commercialising a system based on 512 or CVS is solely responsible for system behavior, constraint design, regulatory interpretation, evidence storage, key management, anchoring configuration, operational uptime, and all resulting consequences. The authors of the canonical documentation do not assume operational control or liability for derivative deployments.

---

## 0. Normative Relationships

This document is a standalone canonical architecture specification. It depends on, and **MUST** be read in conjunction with, the following documents.

**`512_ARCHITECTURE_v{M}.{m}.md`** defines 512, a specific **Commit Gate**: the voluntary, declarative constraint system within which CVS operates as a witness. CVS does not require 512. When 512 is deployed, CVS witnesses constraint evaluation outcomes without participating in enforcement. The relationship is observational, not structural. Nothing in this document modifies, extends, or governs 512. CVS is not a Commit Gate — it is an invented witness architecture. The distinction between these two categories is defined in `512_ARCHITECTURE_v{M}.{m}.md §2` and governs how both documents are read.

**`CVS_IMPLEMENTATION_v{M}.{m}.md`** defines how to build a conformant CVS implementation: adapter specifications, Evidence Object schemas, settlement integration, key management, and deployment topologies. This document defines *what CVS is*. The Implementation document defines *how to build it*. These roles do not overlap.

**`CVS Interoperability Specification v1.0`** defines portable Evidence Object serialization, cross-organization verification workflows, federation directory models, and open-source verification requirements. Interoperability conformance is defined there and referenced here in `§5`.

Where this document and any companion document conflict, this document governs architecture intent. `CVS_IMPLEMENTATION_v{M}.{m}.md` governs build behavior.

---

## Abstract

Internal logs fail under adversarial scrutiny because they are controlled by the party whose conduct is in dispute. This is not a deficiency that better logging tools will fix. It is a structural property of internal evidence: evidence produced by a system, about that system, under the authority of that system's operator, is inherently weaker than evidence produced *about* a system by an independent observer the operator cannot silence.

The Cryptographic Verification Sidecar (CVS) is that independent observer. It is a fail-open, witness-only evidence primitive that operates in parallel with any execution surface — AI inference pipelines, financial trading engines, broadcast media systems, healthcare diagnostics, supply chain logistics — without ever touching the execution path. The CVS observes events, hashes them, chains them cryptographically, and anchors Merkle batch commitments to a public settlement ledger every 30–60 seconds. Settlement anchoring costs approximately $1.08 per month at 60-second intervals. The evidence it produces cannot be altered retroactively without breaking the chain in a way that any independent verifier — a regulator, an insurer, opposing counsel — can detect without operator assistance.

CVS operates across three strictly separated planes. The Capture Plane observes execution and constructs Evidence Objects. The Access Plane provides read-only interfaces to the immutable evidence chain. The Interpretation Plane — dashboards, analytics engines, compliance tools — consumes evidence through the Access Plane without altering it. These planes never collapse. The separation is structural, not administrative.

This document addresses CTOs, boards, regulators, and insurers. It explains what CVS is, why it exists, why internal logs are structurally insufficient, how the three-plane architecture produces independently verifiable evidence, how the Disclosure Kernel enables selective revelation without overexposure, how interoperability enables cross-organization verification without shared infrastructure, and how CVS satisfies the evidentiary requirements of the EU AI Act, DORA, NIS2, GDPR, SEC Rule 17a-4, OSFI, and APRA.

CVS does not prevent incidents. It proves what happened during them. That proof is where financial, regulatory, and legal outcomes are now decided.

CVS records execution events. It does not validate the correctness of observed behavior. It does not certify compliance with any standard, regulation, or policy. Correctness, compliance, and legitimacy are determinations made externally by humans — regulators, auditors, courts, insurers — using CVS output as evidence. The architecture produces the record. It does not interpret it.

CVS must remain logically and administratively independent from any enforcement mechanism it witnesses. An implementation in which CVS and an enforcement gate share operational authority, administrative control, or key custody is not a witness architecture — it is a conflated system whose evidence lacks the independence property that makes it valuable.

---

## 1. Internal Logs Fail Under Adversarial Scrutiny

### 1.1 The Credibility Problem Is Architectural, Not Operational

When a dispute arises — a regulatory investigation, an insurance claim, litigation — the first question is: what actually happened? The second is: can you prove it? Internal logs fail the second question because of who controls them.

An internal log is produced by the system under scrutiny, stored on infrastructure the operator controls, and mutable by administrators with elevated access. Under adversarial conditions — where the opposing party has a financial incentive to challenge the record — internal logs face three structural attacks that no logging improvement resolves. First: the operator could have altered the logs after the fact; proving they did not requires showing that alteration was technically impossible, which internal logs cannot demonstrate. Second: the operator controlled which events were logged; gaps in the record are indistinguishable from deliberate omissions. Third: the logs live inside the system's trust boundary; a verifier must trust the operator to accept the evidence, which is precisely the trust that adversarial conditions have eliminated.

Courts, regulators, and insurers increasingly recognize this. Forensic reconstruction of internal log sequences now routinely takes 2–4 weeks and costs $50K–100K in outside counsel per incident — not because the logs are technically complex, but because establishing their integrity requires expensive adversarial processes that the logs themselves cannot short-circuit *(illustrative — see §-1.9)*.

### 1.2 Machine-Speed Systems Make Retrospective Reconstruction the Only Option

AI agents operating at sub-10-microsecond decision latency generate thousands of state transitions per second. Human oversight operates at 200–300 milliseconds minimum reaction time. This is a 10,000× speed differential. For autonomous systems — algorithmic trading, real-time recommendation engines, agentic AI pipelines — human review of individual decisions at execution time is physically impossible. The accountability question is necessarily retrospective: what did the system do, in what sequence, and under which model version?

Without independent evidence, the answer depends entirely on the operator's internal records. When the SEC opens an investigation, when a customer alleges discriminatory output, when an insurer seeks to reconstruct a claims sequence — the organization must prove what its autonomous system did. Internal logs are the only evidence, and they face all three structural attacks described above.

CVS resolves this by moving evidence production outside the control plane before the dispute arises.

### 1.3 Synthetic Content Destroys Provenance Without External Anchoring

AI-generated media, synthesized outputs, and autonomously produced documents introduce an additional evidentiary failure: provenance. Internal metadata asserting that a specific model produced a specific output at a specific time is entirely under operator control. Without an independent timestamp anchored to a neutral public ledger, an organization cannot prove — and an adversary cannot disprove — when synthetic content was produced, which model version produced it, or whether it has been modified since creation.

CVS anchors existence proofs to a public ledger at the time of creation. The anchor is a Merkle root commitment — a 32-byte hash — costing $0.000025 per transaction and impossible to backdate. An adversary who claims the evidence was fabricated after the fact must explain why the settlement anchor predates the dispute by months or years.

### 1.4 Regulatory Pressure Converts Best Practice Into Requirement

The EU AI Act (Regulation EU 2024/1689) requires automated logging for high-risk AI systems under Article 12. DORA (Regulation EU 2022/2554) mandates ICT resilience and incident logging for financial entities. NIS2 (Directive EU 2022/2555) requires auditability for critical infrastructure operators. SEC Rule 17a-4 mandates WORM record retention for broker-dealers. OSFI and APRA impose operational resilience requirements that include audit trail integrity. These requirements share a common property: they demand evidence of system behavior resistant to after-the-fact modification. Internal logs do not satisfy this requirement structurally. CVS does.

Systems without independent witnesses appear increasingly negligent — to regulators who know the difference, insurers who price the gap, and courts that must decide what weight to assign to evidence a party controls about itself.

---

## 2. CVS Is a Witness, Not a Controller — The Three-Plane Architecture

### 2.1 The Witness Function Is the Architecture

CVS is a witness. A witness observes events, measures time and order, records cryptographic evidence, and produces immutable receipts. A witness does not execute actions, enforce policy, approve outcomes, or determine truth. This distinction is foundational.

The system acts. The CVS witnesses. Evidence is produced without control. Any architecture in which the CVS can alter execution, gate output, or enforce compliance has ceased to be a witness and has become an authority. Authority and independence are mutually exclusive. A system that can stop execution cannot produce independent evidence about it.

CVS is not a Commit Gate. A Commit Gate sits at the execution boundary and enforces pre-committed constraints before irreversible state change occurs. CVS sits alongside any execution surface and observes what occurred. One enforces. The other witnesses. They are complementary architectures, not alternative ones. The distinction between a discovered constraint (the Commit Gate category) and an invented witness layer (CVS) is defined in `512_ARCHITECTURE_v{M}.{m}.md §2` and governs terminology throughout this document.

CVS must remain logically and administratively independent from any enforcement gate it witnesses. This independence is not a preference — it is the property that makes CVS output credible. An implementation in which CVS shares operational authority, administrative access, or key custody with the system it observes has lost the independence property. Evidence produced by a non-independent witness is subject to the same structural attacks as internal logs: the operator controlled the witness, therefore the witness cannot attest to operator conduct. Logical separation means CVS cannot influence execution outcomes. Administrative separation means no single operator role controls both the enforcement gate and the witness layer simultaneously.

### 2.2 The Three Planes Are Structurally Separated

CVS operates across three planes isolated by network segmentation, IAM policy, and API design. The planes cannot collapse into each other by accident — they are separated by design.

**The Capture Plane** observes execution surfaces and constructs Evidence Objects. It is the only plane that writes to the Evidence Store. It has no inbound network connections — it cannot receive commands from interpretation tools or dashboards. It writes append-only to storage and pushes Merkle batch roots to the settlement ledger. It never reads from the Evidence Store it writes to. It never executes application logic.

**The Access Plane** provides read-only interfaces to the evidence chain: an Evidence Store with WORM (Write-Once-Read-Many) semantics, a Proof Service that generates Merkle inclusion proofs, and a Replay Service that returns time-ordered Evidence Objects with explicit gap markers. The Access Plane has no write access to the Evidence Store. It cannot create, modify, or delete evidence.

**The Interpretation Plane** consists of external tools — compliance dashboards, analytics engines, auditor workstations, forensic platforms — that consume evidence through the Access Plane's read-only APIs. Interpretation tools store their analysis artifacts separately from the evidence chain. They cannot inject Evidence Objects, suppress gaps, or claim authority over evidence correctness.

```
┌─────────────────────────────────────────────────────────────────┐
│                    INTERPRETATION PLANE                          │
│         (Dashboards, Analytics, Compliance, Forensics)          │
│              Reads via Access Plane APIs only                    │
└─────────────────────────────┬───────────────────────────────────┘
                              │ READ-ONLY HTTPS
┌─────────────────────────────▼───────────────────────────────────┐
│                       ACCESS PLANE                               │
│  Evidence Store (WORM)  |  Proof Service  |  Replay Service     │
│         No write access to Capture Plane, ever                  │
└─────────────────────────────┬───────────────────────────────────┘
                              │ Append-Only Feed
┌─────────────────────────────▼───────────────────────────────────┐
│                       CAPTURE PLANE                              │
│   CVS Sidecar  →  Hash Chaining  →  Settlement Layer (XRPL)    │
│    Observes execution. Never blocks. Never interprets.          │
└─────────────────────────────────────────────────────────────────┘
```

### 2.3 Six Things CVS Is Not

CVS is not a governance system. It does not enforce rules, impose outcomes, arbitrate disputes, assign blame, or determine truth. It records evidence. Interpretation is external.

CVS is not a control plane. It does not intercept execution, block actions, approve transactions, modify payloads, or influence outcomes. Any design in which the CVS can alter execution is non-conformant.

CVS is not a data platform. Evidence Objects contain hashes, not content. Prompts, outputs, transaction amounts, and patient records are not stored.

CVS is not inline infrastructure. All evidence generation occurs out-of-band. An architecture in which evidence generation failure blocks execution does not satisfy the witness independence property and is not CVS-conformant. A witness that can stop a system is no longer a witness.

CVS is not a coverage guarantee. The sidecar observes declared integration points. Systems contain execution surfaces that may not be instrumented. Claiming evidentiary completeness requires a Declared Observation Surface — an anchored manifest enumerating every observed transmission point. Without a DOS, evidentiary coverage is partial by definition.

CVS is not a Commit Gate. The Commit Gate category enforces pre-committed constraints at the execution boundary. CVS witnesses behavior at that boundary and produces independently verifiable evidence of it. Both may operate together; neither requires the other; they are architecturally distinct and serve different functions.

### 2.4 Fail-Open Is Non-Negotiable

CVS **MUST** be fail-open. At no point may the operation, availability, or correctness of the observed system depend on sidecar availability. If the sidecar fails — under any condition — the observed system continues operating unchanged. The failure is observable. The resulting evidence gap is detectable. Execution impact is always zero.

This is not a design preference. It is a conformance requirement. Evidence systems that interfere with execution are operationally rejected by engineers, legally risky, and economically indefensible. Fail-open behavior is the prerequisite for adoption in any high-availability environment.

---

## 3. Evidence Object Architecture

### 3.1 The Evidence Object Is the Atomic Unit of Trust

Every event observed by CVS produces an Evidence Object: the minimal, structured representation of what occurred, when it occurred, and how it can be independently verified. It contains no payload data and confers no authority.

An Evidence Object contains, at minimum, the following fields.

**Evidence Identifier** — a deterministic, collision-resistant hash of the object's content, reproducible by independent verifiers.

**Observation Timestamp** — sourced from a synchronized clock, expressed in ISO 8601 UTC, monotonic within the chain. Clock source and precision are disclosed.

**Event Descriptor** — event type, source system identifier, stream or channel identifier, protocol-level metadata. Descriptors **MUST NOT** contain payload data.

**Evidence Hash** — a cryptographic hash (SHA-256 default; SHA-3-256 acceptable) of the observed event or segment. Full payloads **MUST NOT** be included.

**Chain Reference** — a reference to the preceding Evidence Object in the sequence. Missing references indicate observable gaps.

**Witness Attestation** — a cryptographic signature attesting only that the event was observed at the stated time and recorded as described. A conforming Witness Attestation uses ECDSA, RSA, or EdDSA. An implementation using a proprietary signing scheme does not satisfy this field definition. The attestation does not attest to correctness or validity.

Evidence Objects are small — typically 1–5 KB each. At 1,000 events per second, daily storage (compressed) is approximately 52 GB. At 100 events per second, approximately 5 GB per day *(illustrative — see §-1.9)*.

### 3.2 Hash Chaining Makes Retroactive Alteration Detectable

Each Evidence Object references the hash of its predecessor. Retroactive alteration of any single object breaks every subsequent link in the chain. An independent verifier detects the break by recomputing hashes from disclosed evidence and comparing them against the recorded chain. No privileged access is required. No trust in the operator is required.

Hash chaining establishes integrity — the sequence has not been altered. It does not establish correctness — it does not prove the observed events were legitimate. This distinction is intentional. CVS is a witness, not a judge.

Gaps in the chain are evidence. If the sidecar is unavailable for 10 minutes, the chain shows an explicit discontinuity. The gap window, start time, duration, and resumption point are recorded upon recovery. Infrastructure failure, network partition, and deliberate disablement produce identical absence. Causal interpretation is external to the architecture.

### 3.3 Merkle Batching Compresses Settlement Cost to Near Zero

Evidence Objects are aggregated into Merkle trees at configurable intervals — typically 30–60 seconds. The Merkle root of each batch — a 32-byte value — is anchored to the public settlement ledger in a single transaction. Settlement cost is therefore independent of event volume.

At 60-second batching on the XRP Ledger, settlement costs $1.08 per month for 43,200 anchors. At 30-second batching, $2.16 per month. At 10-second batching for high-frequency financial systems, $6.48 per month *(illustrative — see §-1.9)*. A trading firm capturing 31,247 events in a contested 5-second window settles that entire window's evidence in five ledger transactions at a cost measured in cents.

The Merkle structure enables individual Evidence Object verification without disclosing the full batch. A Merkle inclusion proof — the minimal set of sibling hashes needed to recompute the root — proves a specific object was included in a specific batch without revealing the other objects. This is selective disclosure at the cryptographic level, before the Disclosure Kernel is even invoked.

### 3.4 Settlement Anchoring Provides Neutral, Public Timestamps

Settlement anchors are recorded on a public, permissionless ledger with deterministic finality. Once confirmed, an anchor cannot be reversed, reorganized, or backdated. The anchor timestamp is the ledger's timestamp, not the operator's. An adversary who claims the evidence was fabricated after a dispute arose must explain why the ledger anchor predates the dispute by months or years.

The settlement layer is a notary, not a computer. It records cryptographic commitments. It does not execute logic, store content, or influence system behavior. The XRP Ledger satisfies all mandatory settlement layer requirements — deterministic finality, predictable cost below $0.000025 per transaction, public verifiability, no execution-layer coupling — and is used as the reference implementation in companion documents. Any ledger satisfying mandatory requirements defined in `CVS_IMPLEMENTATION_v{M}.{m}.md §4` may be substituted without altering evidence semantics.

### 3.5 The Signature and Verification Sequence Makes Evidence Independently Checkable

Every Evidence Object produced by CVS is the output of a defined, reproducible signature sequence. That sequence — applied identically on every event, by every conformant implementation — is what transforms a log entry into independently verifiable proof. An implementation that abbreviates, reorders, or substitutes steps in this sequence produces output that does not satisfy the CVS verification property.

**The full signing sequence, applied per event:**

```text
Step 1 — Intent Hash (pre-execution, optional: 512 kernel present)
  Input:  Execution request payload
  Output: intent_hash = SHA-256(canonical_serialization(request))
  Timing: Synchronous with the decision, before execution proceeds
  Actor:  512 kernel (or source system if no kernel deployed)

Step 2 — Validation Hash (constraint outcome, optional: 512 kernel present)
  Input:  Per-constraint evaluation result set
  Output: validation_hash = SHA-256(canonical_serialization(constraint_results))
  Timing: Appended to Evidence Object immediately after constraint evaluation
  Actor:  512 kernel

Step 3 — CVS Evidence Object Construction and Signing (Capture Plane)
  Input:  event_descriptor + observation_timestamp + evidence_hash
          + chain_reference (hash of preceding Evidence Object)
          + intent_hash (if present) + validation_hash (if present)
  Output: evidence_object_id = SHA-256(canonical_serialization(evidence_object))
          witness_attestation = ECDSA_sign(evidence_object_id, private_key_HSM)
  Timing: Asynchronous and parallel to execution
  Actor:  CVS Sidecar (Capture Plane); private key never leaves HSM

Step 4 — Chain Hash (tamper-evident linkage)
  Input:  evidence_object_id of current object
          chain_reference = evidence_object_id of preceding object
  Output: Chain position established; alteration of any prior object
          breaks every subsequent chain_reference
  Timing: Computed at construction; no additional latency
  Actor:  CVS Sidecar

Step 5 — Merkle Batch Aggregation and Anchor (Settlement Layer)
  Input:  N Evidence Objects accumulated over batch interval (30–60s default)
  Output: merkle_root = root of SHA-256 Merkle tree over batch
          anchor_tx_id = ledger transaction recording merkle_root
  Timing: 30–60 seconds after event observation; asynchronous
  Actor:  CVS Settlement Service; ledger timestamp set by ledger, not operator
```

**What makes each signature verifiable** rests on three properties that hold simultaneously. First, **HSM custody**: the private key that produced `witness_attestation` never leaves the Hardware Security Module — signing operations execute inside the HSM boundary, preventing extraction or substitution. A signature produced with a key the operator cannot export cannot be retroactively forged for events that predate a dispute. Second, **pre-published public key in the federation directory**: the attestation public key is published at `_cvs.<domain>` or `/.well-known/cvs-federation.json` before any events are signed — any verifier can retrieve it without operator cooperation and recheck every signature in the chain. Third, **Merkle proof linking Evidence Object to public anchor**: the Merkle inclusion proof demonstrates that a specific Evidence Object was included in the batch whose root is recorded in `anchor_tx_id` on the public ledger. Recomputing the path from the Evidence Object hash up to the published Merkle root, then confirming that root against the public ledger, requires no trust in the operator at any step.

**The minimum user-facing receipt** is two fields: `correlation_id` and `anchor_tx_id`. The `correlation_id` links all Evidence Objects associated with a user's interaction — pre-execution constraint check, execution event, output event — into a verifiable sequence. The `anchor_tx_id` is the public ledger transaction that anchors the Merkle batch containing those objects. A user in receipt of both fields can query the public ledger directly — without contacting the operator, without proprietary tooling, without a subscription — and confirm that evidence of their interaction was anchored at a specific time, before any dispute arose. Verification completes in under 500 milliseconds using any public ledger RPC endpoint.

**Four architectural properties make the evidence chain independently verifiable, regardless of the system being observed:**

- **Pre-execution constraint validation (synchronous with the decision, before execution proceeds)**: when the 512 kernel is deployed, constraint evaluation runs before the observed system executes the requested action. The constraint outcome — ALLOW or DENY, with per-constraint detail — is recorded in the Evidence Object at decision time, not reconstructed afterward. The evidence of what the governance layer decided exists before execution completes.
- **Parallel witness capture (no latency added to the execution pipeline)**: the CVS Capture Plane observes output at the execution boundary — never inside the observed system, never on its critical path — with no added latency to the execution pipeline. The observed system operates at full speed. The witness operates in parallel. These are structurally separate processes with no shared dependencies.
- **Tamper-evident chaining (hash break is independently detectable)**: altering any Evidence Object — changing a timestamp, removing a constraint result, substituting an identifier — breaks the `chain_reference` of every subsequent object. Any verifier with access to the disclosed chain detects the break by recomputing hashes sequentially from any known-good point. The chain does not require a trusted custodian to remain intact; integrity is self-evident from the mathematics.
- **Public settlement anchor (timestamp set by ledger, not operator)**: the Merkle batch is anchored to the public ledger within 30–60 seconds of observation. The ledger timestamp is produced by a consensus protocol no single operator controls. Evidence anchored before a dispute cannot be accused of post-hoc fabrication. Evidence whose timestamp is set by a neutral public ledger cannot be backdated by the operator even if internal clocks are compromised.

For an auditor — regulator, insurer, or opposing counsel — who needs to verify system behavior without trusting the operator, this sequence eliminates the trust dependency entirely. The auditor receives a proof bundle: the relevant Evidence Objects, their Merkle inclusion proofs, and the public ledger transaction IDs. Using only the open-source verification tool and a public ledger query, the auditor recomputes every hash, validates every signature against the pre-published public key, and confirms the Merkle root against the ledger — in minutes, without operator cooperation, without proprietary software, and without any ability of the operator to alter the result after the fact. That is what makes CVS-backed governance legally defensible rather than merely asserted.

### 3.6 The Declared Observation Surface Defines the Evidentiary Boundary

Evidence integrity and coverage completeness are independent properties. An implementation can produce perfectly intact, tamper-evident evidence of a subset of system behavior. Without a Declared Observation Surface, no claim of completeness is supportable.

The DOS is a formal enumeration — hashed and anchored — of every transmission point the sidecar is configured to observe. Each surface entry declares: surface identifier, adapter type, expected event classes, and silence threshold. If a declared surface fails to emit events within its declared silence threshold, the CVS **MUST** automatically generate a `coverage_gap_detected` Evidence Object. Silence **MUST NOT** be ignored, smoothed, or reconstructed.

In dispute resolution, underwriting review, or regulatory audit: absence of a DOS constitutes an undefined evidentiary boundary; an undefined boundary constitutes a partial evidentiary posture; a partial posture means completeness claims are unsupported. The CVS proves what it observed. The DOS proves what it intended to observe. Both are required to claim evidentiary completeness.

---

## 4. The Disclosure Kernel Enables Precision, Not Flood

### 4.1 Wholesale Disclosure Is a Structural Failure

Evidence disclosure is a precision instrument. A conformant Disclosure Kernel produces scoped evidence packages bounded to a specific inquiry. Every disclosure is limited to relevant evidence paths and produced through computation over stored evidence. Bulk export of raw evidence chains — enabling a requester to reconstruct system behavior beyond the scope of the inquiry — is outside the defined disclosure model and does not satisfy the Disclosure Kernel specification.

This restriction protects the deploying organization. Over-disclosure creates liability — revealing proprietary operational logic, exposing adjacent personnel data, or establishing precedent for future extraction. The Disclosure Kernel exists to make organizations capable of satisfying legitimate inquiries without exposing themselves to adversarial extraction.

### 4.2 The Minimal Revelation Principle Governs Every Disclosure

For any valid disclosure request, the CVS reveals: the smallest set of Evidence Objects necessary; the minimal temporal window required; and only the fields relevant to the inquiry. No additional context is included by default.

A disclosed evidence package contains: the Evidence Objects covering the disclosed scope; Merkle inclusion proofs linking each object to its settlement anchor; settlement anchor transaction IDs on the public ledger; explicit gap markers within the disclosed interval; and the attestation public keys needed to verify signatures. A recipient verifies the package using only these contents and public ledger access. No further communication with the disclosing party is required.

### 4.3 Adversarial Disclosure Requests Fail Structurally

**Fishing expeditions** seek broad exploration without a defined time window, defined evidence path, or stated purpose. A disclosure request without explicit scope dimensions does not constitute a valid request within this architecture. The absence of scope is itself recorded. The refusal event is an Evidence Object.

**Scope inflation attacks** expand time windows incrementally, chain adjacent requests, or aggregate small disclosures. Cumulative disclosure tracking evaluates each request against prior requests from the same requester within a rolling window. Aggregated extraction that exceeds proportionality thresholds falls outside the defined disclosure model and the request is declined with a logged refusal.

**Payload reconstruction attempts** are requests framed as evidence verification but structured to reconstruct payload content or infer proprietary logic from metadata patterns. These fail structurally: hashes are one-way, inference surfaces are minimized, and descriptors contain no payload data by architectural requirement.

**Selective observation exploitation** occurs when an operator enables the sidecar only during favorable periods. Coverage gap detection defeats this: silence on a declared surface during an unfavorable period is permanently observable in the evidence chain.

### 4.4 Gaps Are Disclosed, Never Smoothed

Within any disclosed interval, gaps are reported explicitly. The Disclosure Kernel **MUST NOT** smooth over interruptions, imply continuity where none exists, or hide absence. A disclosed gap — with start time, duration, and resumption point — is legally defensible. A gap that is concealed rather than disclosed creates legal and evidentiary risk; deploying organizations should assess that risk with qualified counsel.

Disclosure events themselves generate Evidence Objects: requester identity, query parameters, timestamp, and outcome are hashed, chained, and anchored. The act of disclosure is auditable. This protects organizations from claims that evidence was concealed, and deters abuse of the disclosure mechanism.

---

## 5. Interoperability Enforces Independence Structurally

### 5.1 Evidence Verifiable Only by the Operator Is Not Independent

Interoperability is not a convenience feature. It is the mechanism by which independence is enforced. If evidence produced by an implementation can only be verified using that implementation's proprietary tooling, the independence property is eliminated — the verifier must trust the operator's toolchain, which returns the problem to its origin.

Every conformant CVS implementation **MUST** produce Evidence Objects verifiable by any other conformant implementation — without shared infrastructure, shared identity authority, or shared control planes. Two organizations running entirely independent implementations on entirely different infrastructure, in different jurisdictions, using different vendors, produce mutually verifiable evidence provided both are conformant with the CVS Interoperability Specification v1.0.

### 5.2 Portability Requires Three Properties

**Canonical Serialization.** Field ordering is deterministic and stable across implementations: lowercase snake_case field names, ISO 8601 timestamps with UTC timezone, hex-encoded binary data, optional fields omitted entirely rather than set to null. The same content always produces the same serialized form. Divergence in serialization prevents independent hash recomputation, which eliminates independent verification.

**Hash Stability.** SHA-256 is the default. SHA-3-256 is acceptable. An implementation is CVS-conformant with respect to hashing only when it uses one of these two functions. An implementation using a proprietary hash function does not satisfy the Hash Stability property and does not produce portable, independently verifiable evidence regardless of what it claims.

**Signature Format Compatibility.** Attestation signatures use ECDSA (secp256k1 or secp256r1), RSA (2048 or 4096), or EdDSA (Ed25519). Signatures are detached — not embedded in hashed content. Verification is possible using widely available open-source tooling.

### 5.3 Open-Source Verification Is Mandatory

Every conformant CVS implementation **MUST** provide open-source verification tooling. Verification is possible using only: the proof bundle (Evidence Object plus Merkle inclusion proof plus settlement anchor); public ledger access; and the open-source tool. No vendor credentials, proprietary software, or operator trust is required.

A CVS-conformant implementation provides this verification pathway without access fees. An implementation that charges for verification access does not satisfy the open verification property. If an operator claims a hash was anchored at a specific time and it was not, any party can detect the discrepancy by querying the public ledger directly. This is the mechanism by which operator claims become checkable without operator cooperation.

### 5.4 Federation Enables Cross-Organization Verification Without Shared Infrastructure

In multi-vendor or multi-organization deployments, a federation directory maps system identifiers to CVS endpoints and attestation public keys. DNS-based federation publishes a TXT record at `_cvs.<domain>`. HTTPS-based federation publishes a well-known document at `https://<domain>/.well-known/cvs-federation.json`.

The canonical cross-organization pattern is custody transfer. Organization A records a custody transfer event. Organization B records receipt of the same transfer. A dispute arises. Both organizations independently disclose their evidence chains covering the transfer window. Settlement anchors prove the timing of each organization's records. Liability is determined by the evidence — not by trust, not by negotiation, not by whichever party controls the relevant logs. No shared infrastructure, shared identity, or shared agreement beyond the format specification is needed.

---

## 6. Regulatory Alignment

The regulatory alignment descriptions in this section identify structural properties CVS shares with what each cited framework requires. They are not claims of regulatory approval, audit certification, or compliance guarantee. CVS produces cryptographic evidence of observation. Whether that evidence satisfies a specific regulator's interpretation, in a specific jurisdiction, in a specific proceeding, is determined externally — by regulators, auditors, and courts — not by this document. Each subsection ends with an explicit statement of what CVS does and does not provide relative to that framework. Deploying organizations must obtain independent legal and regulatory advice before representing CVS deployment as satisfying any compliance obligation.

### 6.1 EU AI Act — Automated Logging for High-Risk Systems

The EU AI Act (Regulation EU 2024/1689) Article 12 requires that high-risk AI systems be designed with logging capabilities enabling automatic recording of events throughout system lifetime. CVS satisfies this requirement through its Capture Plane: events are observed at execution time, hashed, chained, and anchored to a public ledger with deterministic finality — producing a tamper-evident record that predates any investigation.

Article 9 requires risk management systems with continuous evaluation throughout the lifecycle. The CVS evidence chain, anchored periodically with Merkle batch commitments, provides the temporal, ordered record needed to demonstrate ongoing operational behavior. Article 13 requires transparency and provision of information to deployers; the DOS manifest and coverage attestation mechanism satisfy this by making the sidecar's observation scope explicit, versioned, and anchored.

CVS does not guarantee EU AI Act compliance. It produces the cryptographic evidence that a high-risk system operator requires to demonstrate compliance when challenged.

### 6.2 DORA — ICT Operational Resilience

The Digital Operational Resilience Act (Regulation EU 2022/2554) requires financial entities to establish ICT risk management frameworks with robust logging and audit trail capabilities. DORA Article 9 requires internal governance and control frameworks for ICT-related incidents; Article 10 requires detection mechanisms; Article 11 requires business continuity with documented event sequences.

CVS provides continuous ICT event logging through the Capture Plane; tamper-evident records with external anchoring beyond the ICT system's control boundary through the settlement layer; and structured gap detection through its four-type gap taxonomy. WORM storage semantics align with DORA's record integrity requirements. The fail-open constraint ensures that ICT continuity controls do not themselves create operational risk reportable under DORA's incident notification requirements.

CVS does not guarantee DORA compliance. It produces the tamper-evident, externally anchored ICT event record that DORA-regulated entities require to demonstrate operational resilience when examined.

### 6.3 NIS2 — Critical Infrastructure Auditability

NIS2 (Directive EU 2022/2555) requires operators of essential services and digital service providers to implement appropriate technical and organizational measures ensuring network and information system security, including audit trail capabilities for incident investigation. CVS's hash-chained evidence store, with settlement anchoring providing tamper evidence beyond the operator's control, aligns with NIS2's audit trail requirements for critical infrastructure operators.

NIS2 Article 21 requires security measures commensurate with risk, including incident detection and response. The CVS gap taxonomy — Evidence Gap, Settlement Gap, Validation Gap, Coverage Gap — provides structured incident detection aligned with NIS2's tiered incident classification requirements. Each gap type carries a distinct liability signal and is reported explicitly — never concealed.

CVS does not guarantee NIS2 compliance. It produces the independently verifiable audit trail that NIS2-regulated operators require to demonstrate security measure adequacy when examined.

### 6.4 GDPR — Data Minimization by Design

The General Data Protection Regulation Article 5(1)(c) requires that personal data be adequate, relevant, and limited to what is necessary in relation to the purposes for which it is processed. CVS satisfies the data minimization principle architecturally: Evidence Objects contain hashes of observed events, not the events themselves. Prompts, outputs, medical records, transaction details, and personal identifiers are not stored. The CVS proves *that* an event occurred and *when* — not *what* the event contained.

Article 25 requires data protection by design and by default. The Disclosure Kernel implements this: disclosure is computed — revealing only what the specific inquiry requires — not exported wholesale. A conformant Disclosure Kernel does not support bulk export. Payload reconstruction is defeated structurally. Personal data that is never stored is not available for disclosure or legal process.

Where Evidence Objects reference data subjects — healthcare, financial services, employment decisions — CVS's selective disclosure architecture enables proof of process without exposure of personal data. A Merkle inclusion proof demonstrates that a specific event was part of a larger batch without revealing the other events in that batch.

### 6.5 SEC Rule 17a-4 — WORM Records for Broker-Dealers

SEC Rule 17a-4 (17 CFR 240.17a-4) requires broker-dealers to preserve certain records in a non-rewriteable, non-erasable format — WORM compliance. The CVS Evidence Store implements WORM semantics: objects are appended and never modified or deleted. Object locking or versioning constraints enforce immutability at the storage layer.

Settlement anchoring adds a layer that Rule 17a-4 alone cannot provide: external, public timestamping on a neutral ledger enabling independent verification that a record existed at a specific time without trusting the broker-dealer's internal infrastructure. For SEC investigations involving algorithmic trading behavior, CVS provides sub-millisecond granularity to reconstruct execution sequences. In the scenario where 31,247 Evidence Objects captured a contested 5-second trading window, SEC verification completed in 3 days rather than the typical 6–8 weeks required for traditional forensic reconstruction, with an estimated $7M–12M in penalties and legal fees avoided *(illustrative — see §-1.9)*.

### 6.6 OSFI — Canadian Federally Regulated Financial Institutions

The Office of the Superintendent of Financial Institutions Guideline B-10 addresses third-party risk management and requires federally regulated financial institutions to maintain adequate oversight of technology services, including audit trail capabilities. OSFI's Technology and Cyber Risk Management guidance requires demonstrable evidence of ICT controls, incident detection, and operational continuity.

CVS provides the evidence substrate that OSFI-regulated entities require: externally anchored audit trails beyond the unilateral control of any single insider, gap detection that surfaces operational anomalies, and selective disclosure that satisfies regulatory inquiry without wholesale exposure of proprietary systems. The fail-open constraint ensures that compliance infrastructure does not itself create an operational risk reportable under OSFI's incident notification requirements.

### 6.7 APRA — Australian Financial System Resilience

The Australian Prudential Regulation Authority's CPS 234 (Information Security) requires APRA-regulated entities to maintain information security capability commensurate with threats, with robust detection and response to information security incidents. CPS 234 paragraph 28 requires mechanisms to systematically monitor for security weaknesses, including audit log controls.

CVS satisfies CPS 234's audit log requirements through hash-chained, WORM-stored Evidence Objects anchored externally. The coverage integrity mechanism — DOS manifest with anchored version history — provides APRA examiners a verifiable boundary declaration: what the organization declared it would observe, for which periods. APRA examiners have a cryptographically verifiable scope boundary from which to evaluate coverage claims.

CPG 234, APRA's guidance companion, emphasizes information asset registers and supply chain resilience. CVS's cross-organization federation capability supports supply chain evidence workflows where multiple APRA-regulated entities interact — custody transfers, counterparty settlement, inter-entity transactions — and need to produce independent evidence of their respective behaviors without sharing infrastructure or control planes.

---

## 7. Insurance and Legal Applications

### 7.1 Insurance Markets Price Uncertainty — CVS Reduces It

Underwriting prices the probability and magnitude of loss. In digital operations, the dominant uncertainty driver is not incident frequency — it is the inability to reconstruct what happened, prove non-tampering, and establish chain of custody. Organizations that cannot answer these questions after an incident present actuarially higher tail risk: claims take longer to resolve, investigations cost more, and fraud exposure is greater.

CVS reduces underwriting uncertainty through four structural properties. External anchoring — settlement receipts on a neutral public ledger — provides an independent timestamp insurers verify without trusting the insured. Hash chaining — tamper-evident Evidence Objects — demonstrates that the record has not been altered since creation. Gap detection — explicit `coverage_gap_detected` Evidence Objects — shows where the record is incomplete rather than hiding gaps. Selective disclosure — scoped evidence packages — enables insurers to receive the specific evidence they need without triggering wholesale exposure.

Insurers reviewing a claim from an organization with CVS deployed can answer the six core underwriting questions — what happened, when, can the insured prove it, was evidence altered or withheld, can causality be reconstructed, is there an independent record outside the insured's control — from the evidence chain. Insurers reviewing a claim without CVS cannot. Whether this structural asymmetry translates into specific premium treatment is determined by the underwriter, not by this architecture.

### 7.2 Claims Resolution Compresses From Weeks to Hours

Traditional post-incident forensic reconstruction requires: engaging external forensic counsel (2–4 days to mobilize); extracting and normalizing logs across internal systems (1–2 weeks); establishing chain-of-custody for the logs under adversarial challenge (1–3 days); and producing a reconstruction opposing counsel cannot immediately attack (ongoing). Total elapsed time: 2–4 weeks. Typical outside counsel cost: $50K–100K per incident *(illustrative — see §-1.9)*.

CVS-enabled reconstruction: query the Replay API for the relevant time window; receive time-ordered Evidence Objects with explicit gaps; generate Merkle inclusion proofs for contested events; deliver a proof bundle independently verifiable against the public ledger. Total elapsed time: hours. The evidence was captured and anchored before the dispute arose. The organization discloses pre-existing, independently verifiable records — it does not reconstruct history.

### 7.3 CVS Satisfies the Structural Criteria for a Technical Risk Control

Independent evidence infrastructure qualifies as a technical risk control when it satisfies three properties: it must be external to the execution path (not an internal log); resistant to insider modification (not under the insured's sole control); and independently verifiable (requiring no trust in the insured's toolchain). CVS satisfies all three by architectural requirement — not by policy or procedure that could be altered without detection.

Whether any specific underwriter classifies CVS as a qualifying control, and what premium treatment results, is determined by that underwriter's criteria, not by this document. Organizations seeking insurance treatment for CVS deployment must engage their underwriter directly. No premium outcome is implied, projected, or guaranteed.

### 7.4 Legal Evidentiary Properties of CVS Output

Evidence Objects produced by a conformant implementation carry the following evidentiary properties relevant to litigation and regulatory proceedings. They establish *existence* — the event was observed and recorded at a specific time. They establish *integrity* — the record has not been altered since creation, demonstrable by hash recomputation. They establish *temporal ordering* — the hash chain imposes sequence, and the settlement anchor provides an external temporal bound that cannot be backdated. They establish *scope* — the DOS defines what was declared to be observed, making gaps interpretable rather than ambiguous.

Evidence Objects do not establish correctness — whether the observed event was legitimate; intent — whether observed behavior was deliberate; or causation — whether one event caused another. These determinations remain external. CVS creates the record. Courts, regulators, and insurers interpret it.

Attestation by the CVS witness asserts only: a specific event was observed, at a specific time, and recorded according to the disclosed process. The narrower the scope of attestation, the more defensible it is under adversarial examination.

### 7.5 Repeated Adversarial Behavior Accumulates an Independently Verifiable Pattern

A single anomalous event — a coverage gap, a suppression attempt, a disclosure refusal — has explanations. Infrastructure fails. Administrators make mistakes. A single event, disclosed in isolation, is defensible.

A pattern is not.

CVS records every event in sequence, chained and anchored. A coverage gap that coincides with a high-risk trading window is one data point. The same gap recurring across three regulatory reporting periods, each time on the same declared surface, each time resolved before the next anchor batch — is a behavioral record. The pattern exists in the evidence chain, timestamped and independently verifiable, before any disclosure request is made.

When that pattern is disclosed — in litigation, in a regulatory examination, in an insurance investigation — opposing counsel, the examiner, or the underwriter is not reviewing a single incident. They are reviewing documented conduct over time. The distinction is material: single incidents attract penalties; patterns attract findings of systemic failure, willful concealment, or deliberate manipulation. Regulators treat them differently. Insurers price them differently. Courts instruct juries differently.

The operator cannot explain away a pattern by explaining any individual event. The chain's integrity means each event's timestamp and relationship to adjacent events is fixed at the time of anchoring — not reconstructable after the fact to produce a more favorable sequence.

This is the consequence that the architecture's adversarial detection properties produce at scale. CVS does not publish patterns, make reputational determinations, or notify third parties. It records evidence. The pattern emerges from that record when disclosure occurs. At that point, the operator's conduct history — every manipulation attempt, every gap that coincides with adverse periods, every scope inflation rejection — is verifiable by any party with access to the disclosed chain. The market, the regulator, and the insurer draw their own conclusions. CVS simply ensures those conclusions are drawn from facts that cannot be altered.

---

## 8. Attack Vectors

**Selective Observation** — An operator disables the sidecar during periods of high-risk activity, then re-enables it during routine operations.
*Mechanism:* By disabling observation during a critical period and re-enabling it afterward, the operator creates a gap that could be misrepresented as infrastructure failure rather than deliberate concealment.
*Defense:* Coverage gap detection records the gap window, start time, duration, and resumption point upon recovery. The DOS manifest defines declared surfaces; silence on a declared surface within the silence threshold triggers a `coverage_gap_detected` Evidence Object automatically. Selective observation creates gaps. Gaps are evidence.
*Residual risk:* Infrastructure failure and deliberate disablement produce identical absence. Causal attribution is an external determination. The architecture surfaces the gap; it does not explain it.

**Insider Suppression** — An administrator with elevated access suppresses evidence generation, removes stored Evidence Objects, or delays settlement anchoring during a critical period.
*Mechanism:* Without structural authority separation, a single insider with write access to logging infrastructure, storage, and network configurations can unilaterally suppress the evidentiary record.
*Defense:* No single role may simultaneously control evidence generation, WORM storage, settlement wallet, and attestation keys. WORM storage prohibits deletion at the storage layer. Settlement anchors on the public ledger are outside any insider's unilateral control. Compromise of any single control does not compromise the full chain.
*Residual risk:* A sophisticated insider with compromised authority separation could delay settlement anchoring during a gap window. Deferred anchoring is observable. Delay does not erase local evidence; it delays public timestamping.

**Time Fabrication** — An adversary adjusts system clocks, fabricates timestamps, or reorders events to alter the apparent sequence of execution.
*Mechanism:* Timestamps in internal systems are under operator control. Fabricated timestamps can make events appear to occur in a different sequence than they did.
*Defense:* Hash chain integrity imposes internal ordering — events referencing each other cannot be reordered without breaking the chain. Settlement anchor timestamps are the ledger's timestamps, not the operator's. An event claimed to have occurred at time T must have its Merkle root anchored at or after T on the public ledger. Fabricated timestamps preceding the anchor time are exposed by the contradiction.
*Residual risk:* Clock synchronization anomalies create detectable inconsistencies — disclosed as drift indicators in Evidence Objects — rather than silent fabrication.

**Evidence Flooding** — An adversary generates massive volumes of noise events to dilute meaningful evidence, obscure key events, or exhaust sidecar resources.
*Mechanism:* High volumes of synthetic events injected into observed channels dilute the evidentiary significance of specific events or cause gaps through resource exhaustion.
*Defense:* Batching, scoping, and minimal revelation mitigate this structurally. Evidence Objects are keyed by content hash. High event volume increases storage costs but does not erase existing chain structure. Replay queries filter by event type, surface, and correlation ID — enabling extraction of specific events from high-volume noise.
*Residual risk:* Extreme flooding may exhaust sidecar resources and create evidence gaps. Gaps are observable. Resource exhaustion is detectable through monitoring baselines and treated as an Evidence Gap.

**Scope Inflation** — An adversarial disclosure requester expands time windows incrementally across multiple requests, chains adjacent inquiries, or aggregates small individually-justified disclosures into a larger extraction.
*Mechanism:* Each individual request appears justified in isolation. Their aggregate effect is wholesale evidence extraction beyond any legitimate inquiry.
*Defense:* Cumulative disclosure tracking evaluates each request against prior requests from the same requester within a rolling window. Requests that collectively exceed proportionality thresholds are rejected with logged refusals.
*Residual risk:* Sophisticated adversaries may use multiple identities to distribute requests across the tracking window. Rate limiting per identity and pattern detection across requesters mitigate but do not eliminate this surface.

**Payload Reconstruction** — A disclosure requester frames requests as evidence verification but structures them to reconstruct payload content or infer proprietary logic from metadata patterns.
*Mechanism:* Even without direct payload exposure, high volumes of metadata — event descriptors, timing patterns, correlation IDs, source system identifiers — can enable inference of proprietary operational behavior.
*Defense:* This attack fails structurally. Hashes are one-way: the hash of a payload cannot be reversed to recover the payload. Descriptors contain no payload data by architectural requirement. Inference surfaces are minimized by the minimal revelation principle.
*Residual risk:* Statistical inference from aggregated metadata remains possible at sufficient volume. Volume controls and cumulative tracking limit but do not eliminate this surface.

**Settlement Wallet Drain** — An attacker compromises the settlement wallet and drains its balance, creating a denial of service in which anchoring fails.
*Mechanism:* The settlement wallet holds a small balance (typically $100–500 equivalent) needed to submit anchor transactions. Wallet compromise enables balance drain.
*Defense:* Wallet compromise affects only future anchoring — historical anchors on the public ledger are immutable. Evidence generation continues locally during anchoring interruption. Deferred batches settle when the wallet is replenished. The settlement wallet is structurally separated from attestation keys; wallet compromise does not enable evidence falsification.
*Residual risk:* Extended drain creates Settlement Gaps — deferred anchoring that reduces the temporal precision of public timestamping during the gap window. Settlement Gaps are observable.

**Sidecar Compromise** — An attacker compromises the Capture Plane sidecar process.
*Mechanism:* A compromised sidecar could generate fabricated Evidence Objects, delay evidence generation, or expose the observation pipeline.
*Defense:* A compromised sidecar cannot alter existing evidence — WORM storage prohibits modification. It cannot backdate evidence — settlement anchors prove timing independently. It cannot sign false evidence with existing keys — private keys never leave the HSM (FIPS 140-2 Level 2 minimum). Compromise is detectable through chain analysis and key rotation.
*Residual risk:* A compromised sidecar may generate false Evidence Objects with valid signatures during the compromise window, prior to key rotation. Compromise disclosure and chain analysis for that window are required responses.

---

## 9. Conformance Requirements

### 9.1 Mandatory Behaviors (MUST)

**Fail-Open Execution.** The implementation **MUST NOT** block, delay, or alter execution of the observed system under any failure condition — including power loss, network partition, ledger unavailability, software crash, clock desynchronization, key rotation failure, and resource exhaustion. Execution impact **MUST** always be zero.

**Witness-Only Authority.** The implementation **MUST NOT** execute application logic, enforce policy, approve outcomes, or alter observed inputs or outputs.

**Evidence Object Construction.** Every observed event **MUST** produce an Evidence Object containing: evidence identifier, observation timestamp, event descriptor (no payload data), evidence hash (SHA-256 or SHA-3-256 only), chain reference, and witness attestation (ECDSA, RSA, or EdDSA only; proprietary schemes are prohibited).

**Hash Chaining.** Evidence Objects **MUST** be cryptographically chained. Alteration of any historical Evidence Object **MUST** be detectable by independent recomputation.

**Merkle Batching and Settlement.** Evidence Objects **MUST** be aggregated into Merkle trees and their roots anchored to a qualifying public settlement ledger. Settlement **MUST** be asynchronous and **MUST NOT** block execution.

**WORM Storage.** Evidence Objects **MUST** be stored with Write-Once-Read-Many semantics. Modification and deletion **MUST** be disabled at the storage layer. Backup and restore **MUST** preserve immutability.

**Gap Detection and Reporting.** Absence of observation **MUST** be detectable. Gaps **MUST NOT** be concealed, smoothed, or reconstructed. Resumption after failure **MUST** be explicit, with gap start time, duration, and resumption point recorded.

**Declared Observation Surface.** Any implementation claiming evidentiary completeness **MUST** publish a DOS manifest — serialized deterministically, hashed, and anchored via the settlement layer. DOS changes **MUST** produce a new anchored version while preserving prior DOS records.

**Coverage Gap Detection.** If a declared surface fails to emit events within its declared silence threshold, the implementation **MUST** generate a `coverage_gap_detected` Evidence Object automatically.

**Selective Disclosure.** Disclosure **MUST** be scope-bounded to a specific inquiry and **MUST** follow the minimal revelation principle. Over-disclosure **MUST** be preventable by design. Bulk export of raw evidence chains **MUST NOT** be supported.

**Disclosure Logging.** Every disclosure request **MUST** be logged as an Evidence Object, hashed, chained, and anchored, including requester identity, query parameters, timestamp, and outcome.

**Open-Source Verification Tooling.** Every conformant implementation **MUST** provide open-source verification tooling enabling third-party verification using only: the proof bundle, public ledger access, and the open-source tool.

**Authority Separation.** A conformant implementation **MUST NOT** concentrate authority over evidence generation, settlement anchoring, Evidence Object storage, and attestation keys in a single role or system component. Separation **MUST** be structural.

**HSM Key Protection.** Attestation private keys **MUST** be stored in FIPS 140-2 Level 2 or higher Hardware Security Modules. Private keys **MUST NOT** leave the HSM. Signing operations **MUST** occur inside the HSM.

### 9.2 Prohibited Behaviors (MUST NOT)

- **MUST NOT** block, delay, or alter execution of the observed system under any condition.
- **MUST NOT** gate execution on evidence generation, settlement, or signing operations.
- **MUST NOT** enforce rules, compliance, or policy of any kind.
- **MUST NOT** alter, delete, or overwrite stored Evidence Objects.
- **MUST NOT** suppress, smooth, or reconstruct evidence gaps in storage, replay, or disclosure.
- **MUST NOT** store original content payloads in Evidence Objects or any evidence-layer storage.
- **MUST NOT** use proprietary hash functions or signing algorithms.
- **MUST NOT** require payment for verification (pay-to-verify).
- **MUST NOT** expose write APIs from the Access Plane to external consumers.
- **MUST NOT** permit interpretation tools to inject Evidence Objects into the evidence chain.
- **MUST NOT** imply false continuity in any disclosure, replay result, or dashboard output where gaps exist.
- **MUST NOT** concentrate evidence generation, storage control, settlement wallet, and attestation key authority in a single role or system component.

### 9.3 Claims a Conformant Implementation Must Not Make

A conformant CVS implementation **MUST NOT** claim that it:
- guarantees correctness of observed system behavior or legitimacy of observed events;
- guarantees truth;
- prevents wrongdoing or fraud;
- enforces compliance with any legal or regulatory requirement;
- replaces legal, regulatory, or insurance judgment;
- guarantees complete system coverage without an anchored Declared Observation Surface explicitly filed;
- guarantees insurance premium reduction of any specific amount;
- guarantees regulatory approval or audit certification of any kind;
- provides autonomous compliance enforcement.

### 9.4 Conformance Verification Checklist

| Test | Expected Result | Pass/Fail |
|---|---|---|
| Induce sidecar failure; observe execution system | System continues operating, zero execution impact | [ ] |
| Induce sidecar failure; inspect evidence chain after recovery | Gap appears with start time, duration, resumption point | [ ] |
| Stop sidecar for 5 minutes; query Replay API | Explicit gap marker present; no smoothing or interpolation | [ ] |
| Attempt HTTP POST to Access Plane evidence endpoint | Returns 405 Method Not Allowed | [ ] |
| Attempt to modify Evidence Object at storage layer | Operation fails; WORM enforced at storage layer | [ ] |
| Restore Evidence Store from backup; hash objects | All hashes match originals | [ ] |
| Third party verifies proof bundle without operator assistance | Verification succeeds using only bundle and public ledger | [ ] |
| Run open-source verification tool against proof bundle | Tool available, functional, returns PASS | [ ] |
| Query settlement ledger directly for batch Merkle root | Anchored root matches proof bundle Merkle root | [ ] |
| Submit disclosure request; inspect evidence chain | Disclosure log Evidence Object created, chained, anchored | [ ] |
| Attempt bulk export of raw evidence chain | Request rejected; scoped disclosure only | [ ] |
| Verify DOS manifest is anchored on settlement ledger | DOS hash confirmed on ledger with timestamp | [ ] |
| Silence declared surface beyond declared threshold | `coverage_gap_detected` Evidence Object emitted automatically | [ ] |
| Verify authority separation across roles | No single role controls generation + storage + wallet + keys simultaneously | [ ] |
| Verify attestation key operations | All signing operations logged inside HSM boundary; no key export | [ ] |
| Verify hash algorithm | SHA-256 or SHA-3-256 only; no proprietary functions present | [ ] |

**Full Conformance:** All 16 tests pass. Partial conformance (1–2 failures) requires documented exceptions and remediation timelines. Three or more failures constitute non-conformance.

---

## Conclusion

Internal logs are insufficient under adversarial scrutiny because they are controlled by the party whose conduct is in dispute. This is a structural property, not a technical deficiency. Better logging tools do not resolve it. External, independently verifiable evidence does.

The Cryptographic Verification Sidecar is the minimal architecture required to produce independent evidence: a fail-open witness that observes execution without touching it, hashes events without storing their content, chains them cryptographically, and anchors Merkle batch commitments to a public ledger every 30–60 seconds at a cost of approximately $1–2 per month. Evidence that exists before a dispute cannot be accused of fabrication. Evidence anchored to a neutral public ledger cannot be retroactively altered. Evidence verifiable by any party with internet access does not depend on trusting the organization that produced it.

Three planes, structurally separated. Evidence generation disjoint from evidence access. Evidence access disjoint from evidence interpretation. These planes never collapse. The separation is architectural.

The regulatory environment is converging on this model. The EU AI Act, DORA, NIS2, GDPR, SEC Rule 17a-4, OSFI, and APRA all require — in different forms and at different levels of specificity — audit trail integrity resistant to after-the-fact modification. Internal logs do not satisfy this requirement. CVS does.

Systems without independent witnesses appear increasingly negligent to regulators who know the difference, insurers who price the gap, and courts that must decide what weight to assign evidence a party controls about itself. Adoption is voluntary. The consequences of not adopting are not.

The architecture's authority derives from constraints, not control.

---

## Document Control

| Field | Value |
|---|---|
| **Document Title** | CVS Architecture: The Cryptographic Verification Sidecar |
| **Filename** | `CVS_ARCHITECTURE_v2.7.md` |
| **Version** | 2.7 |
| **Publication Date** | February 2026 |
| **Author** | Jonathan M. Watson |
| **Repository** | github.com/JonathanMastersWatson/Evidence-Sidecar |
| **License** | Apache License 2.0 |
| **Contact** | evidence-admin@512.systems |
| **Normative Dependencies** | `512_ARCHITECTURE_v{M}.{m}.md` · `CVS_IMPLEMENTATION_v{M}.{m}.md` · `CVS Interoperability Specification v1.0` |

---

## Changelog — Version 2.7

| Status | Section | Description |
|---|---|---|
| Modified | §3.6 | "a partial posture invalidates completeness claims" → "a partial posture means completeness claims are unsupported" — removes legal invalidation assertion; replaces with structural/definitional statement |
| Modified | §6.4 | "Bulk export is prohibited" → "A conformant Disclosure Kernel does not support bulk export" — converts prohibition to definitional property |
| Modified | §6.4 | "cannot be disclosed, breached, or subpoenaed" → "is not available for disclosure or legal process" — removes judicial process claim; replaces with structural consequence of data minimization |

**Audit note:** All other instances of `cannot`, `must not`, and `is prohibited` in the document were reviewed and retained: (a) RFC 2119 MUST/MUST NOT in §9 are normative conformance language appropriate to that section type per STYLE_GUIDE_v2.0; (b) "cannot be reversed / backdated / altered" throughout describe mathematical and cryptographic properties of hash chains and public ledgers, not legal claims; (c) remaining `must not` instances are advisory notices about conceptual distinctions, not legal prohibitions.

**Removals:** Nothing removed.

---

## Changelog — Version 2.6

| Status | Section | Description |
|---|---|---|
| Modified | §-1.5 | CVS paragraph: removed two-tier framing; replaced with single Apache 2.0 release statement; express patent grant referenced directly; "project does not assert proprietary control beyond Apache terms" stated; derivative works commercialisation rights retained |
| Modified | §-1.5 | Closing paragraph: removed "will not recognise, support, or endorse" enforcement language; replaced with neutral infrastructure posture statement ("available for anyone to use, implement, and build upon under Apache 2.0") |
| Modified | §-1.7 | Collapsed two-tier CC BY 4.0 / Apache 2.0 structure into single Apache License 2.0 section; all CC BY 4.0 references removed; full Apache 2.0 patent grant language retained; derivative work licensing note added |
| Modified | Document Control | Licence field updated from "CC BY 4.0" to "Apache License 2.0" |

**Removals:** All CC BY 4.0 and Creative Commons references removed from operative sections. Historical changelog entries describing prior version actions retained as record.

---

## Changelog — Version 2.5

| Status | Section | Description |
|---|---|---|
| Modified | §-1.5 | CVS paragraph: "offered without exclusive ownership" / "do not intend exclusive ownership to arise" replaced with explicit Apache 2.0 release statement and patent grant declaration; "project does not assert proprietary control" stated directly; final sentence updated to "exclusive proprietary control" for precision |
| Modified | §-1.7 | Restructured into two explicit tiers: (1) this specification document under CC BY 4.0 for text reproduction; (2) the base CVS architecture under Apache 2.0 including express patent grant language; explanatory note added distinguishing CC BY 4.0 (no patent grant) from Apache 2.0 (patent grant); full licence URL included |

**Removals:** Nothing removed. Structural open infrastructure intent preserved throughout.

---

## Changelog — Version 2.4

| Status | Section | Description |
|---|---|---|
| Modified | §-1.5 | "No person may claim" replaced with authorial intent and positional statement; "No future claim is valid regardless of jurisdiction" replaced with "authors will not recognise or endorse"; open commons thesis preserved |
| Modified | §-1.8 | "limited to zero consideration" replaced with "seek to limit to the fullest extent applicable law permits" |
| Modified | §-1.10 | "No party may rely on this document as" replaced with "does not constitute and is not intended to be relied upon as"; "bears full responsibility" replaced with "is solely responsible for" |
| Modified | §-1.13 | "assumes full responsibility" replaced with "is solely responsible for"; "assume no…liability" replaced with "do not assume…liability" |
| Modified | §2.3 | "are disallowed" replaced with definitional: "does not satisfy the witness independence property and is not CVS-conformant"; "must not be conflated" replaced with "serve different functions" |
| Modified | §3.1 | Witness Attestation field definition: "proprietary schemes prohibited" replaced with positive conformance definition and property statement |
| Modified | §3.5 | "cannot be abbreviated…non-conformant" replaced with: "An implementation that abbreviates…does not satisfy the CVS verification property" |
| Modified | §4.1 | "Wholesale export…is prohibited" replaced with conformant Disclosure Kernel definition; "structural failure" retained as architectural description |
| Modified | §4.3 | "These are rejected" / "is blocked" / "cannot be hidden" replaced with: "does not constitute a valid request", "falls outside the defined disclosure model", "is permanently observable" |
| Modified | §4.4 | "A suppressed gap is spoliation" replaced with risk advisory referencing qualified counsel |
| Modified | §5.2 | "Proprietary hash functions are prohibited — they constitute conformance violations" replaced with positive conformance property definition |
| Modified | §5.3 | "Pay-to-verify is non-conformant" replaced with: "An implementation that charges for verification access does not satisfy the open verification property" |

**Removals:** No content removed. Conformance logic preserved throughout; all RFC 2119 MUST/MUST NOT in §9 left intact.

---

## Changelog — Version 2.3

| Status | Section | Description |
|---|---|---|
| Replaced | §-1.10 | "No Institutional Endorsement" replaced by expanded "No Reliance" (§-1.10) — §-X.2 is a superset of former §-1.10; content consolidated |
| Added | §-1.11 | No Endorsement — no implementation, derivative, organisation, ledger, or commercial deployment is endorsed; no certification valid without formal written agreement |
| Added | §-1.12 | Independent Verification Requirement — structural/cryptographic verifiability is not legal, regulatory, or institutional validation; compliance determination is external |
| Added | §-1.13 | Builder Responsibility — full enumeration of operator responsibilities for any derivative deployment; authors assume no operational control or liability |

**Removals:** §-1.10 "No Institutional Endorsement" replaced by §-1.11 "No Endorsement" (content is a superset).

---

## Changelog — Version 2.2

| Status | Section | Description |
|---|---|---|
| Modified | Abstract | Added three-statement witness scope clarification: CVS records execution events; does not validate correctness; does not certify compliance. Added logical/administrative independence requirement paragraph |
| Modified | §-1.7 | Added software implementation licensing note: Apache 2.0 recommended for open-source implementations; CC BY 4.0 applies to this specification only |
| Added | §-1.10 | No Institutional Endorsement — explicit statement that CVS is not approved, certified, or endorsed by any regulatory body, insurer, government agency, or judicial authority |
| Modified | §2.1 | Added independence paragraph: CVS must remain logically and administratively independent from any enforcement gate it witnesses; conflated implementations lose the independence property |
| Added | §6.0 preamble | Regulatory alignment scope statement: architectural descriptions are not compliance guarantees or regulatory approvals; deploying organizations must obtain independent advice |
| Modified | §6.2 | "satisfy" replaced with "align with"; explicit DORA disclaimer added |
| Modified | §6.3 | "satisfies" replaced with "aligns with"; explicit NIS2 disclaimer added |
| Modified | §7.1 | Removed "premium differentials in the range of 10–20%" — replaced with statement that premium treatment is determined by the underwriter, not this architecture |
| Modified | §7.3 | Retitled from "CVS Operates as a Qualifying Control for Insurance Programs" to "CVS Satisfies the Structural Criteria for a Technical Risk Control"; removed premium percentage figures; replaced with explicit statement that no premium outcome is implied or guaranteed |

**Removals:** Premium percentage figures removed from §7.1 and §7.3.

---

## Changelog — Version 2.1

| Status | Section | Description |
|---|---|---|
| Modified | §9.1 | Removed two narrative sentences ("Conformance is behavioral, not declarative. Partial compliance is non-conformance.") — section now opens directly with first behavioral mandate |
| Modified | §9.1 | Authority Separation: corrected `may` to **MUST NOT**; sentence restructured to unambiguous prohibition |

**Removals:** Nothing removed.

---

## Changelog — Version 2.0

| Status | Section | Description |
|---|---|---|
| Modified | §-1.5 | Title updated from "Conformance Responsibility" to "Ownership and Licensing — Open Commons Declaration"; content replaced with open commons declaration per STYLE_GUIDE_v2.0 §8 |
| Modified | §0 | Removed prohibited term "Binary Constraint Kernel"; replaced with canonical reference to "512, a specific Commit Gate" per STYLE_GUIDE_v2.0 §11; first use of Commit Gate bolded; explicit statement that CVS is not a Commit Gate added |
| Modified | §2 | Section header updated to claim form; §2.3 retitled "Six Things CVS Is Not"; explicit "CVS is not a Commit Gate" item added to §2.3 with cross-reference to `512_ARCHITECTURE_v{M}.{m}.md §2` |
| Modified | §2.1 | Explicit statement added distinguishing CVS from Commit Gate category |
| Modified | §3.5 | "512 Constraint Kernel" replaced with "512 kernel" (acceptable shorthand per STYLE_GUIDE §11.7) throughout code block |
| Reorganized | §8 / §9 | Attack Vectors moved to §8; Conformance Requirements moved to §9 — correcting section order to match STYLE_GUIDE_v2.0 §3 mandate for invention documents (Conformance Requirements final, Attack Vectors penultimate) |
| Modified | §-1.6 | Cross-document reference updated to use filename format `CVS_IMPLEMENTATION_v{M}.{m}.md §4` |
| Modified | §3.4 | Cross-document reference updated to use filename format |

**Removals:** Nothing removed.

---

## Changelog — Version 1.2

| Status | Section | Description |
|---|---|---|
| Added | §7.5 | Repeated Adversarial Behavior Accumulates an Independently Verifiable Pattern — pattern exposure mechanics, distinction between single incident and behavioral record, consequences at regulatory, insurance, and legal levels |

**Removals:** Nothing removed.

---

## Changelog — Version 1.1

| Status | Section | Description |
|---|---|---|
| Added | §3.5 | The Signature and Verification Sequence Makes Evidence Independently Checkable — full five-step signing sequence in code block; three verifiability properties (HSM custody, pre-published public key, Merkle proof); minimum user-facing receipt mechanics (correlation_id + anchor_tx_id); four architectural properties making the evidence chain independently verifiable; closing paragraph on auditor verification without operator trust |
| Modified | §3.6 | Renumbered from §3.5 to §3.6 to accommodate insertion of new §3.5 above |

**Removals:** Nothing removed.

---

## Changelog — Version 1.0

| Status | Section | Description |
|---|---|---|
| Added | §-1 | Legal Notice and Limitation of Liability — 8 subsections (§-1.1 through §-1.8) plus §-1.9 financial projection disclaimer |
| Added | §0 | Normative Relationships — cross-document dependencies to 512_ARCHITECTURE, CVS_IMPLEMENTATION, CVS Interoperability Specification v1.0 |
| Added | Abstract | CTO/Board/regulator/insurer summary of CVS purpose, architecture, and regulatory scope |
| Added | §1 | Internal Logs Fail Under Adversarial Scrutiny — structural insufficiency of internal logs, machine-speed accountability gap, synthetic content provenance failure, regulatory convergence |
| Added | §2 | What CVS Is — the witness function, three-plane architecture diagram, non-goals taxonomy, fail-open principle |
| Added | §3 | Evidence Object Architecture — field specification, hash chaining, Merkle batching and settlement cost model, Declared Observation Surface |
| Added | §4 | The Disclosure Kernel — minimal revelation principle, adversarial disclosure defense patterns, gap disclosure requirements |
| Added | §5 | Interoperability — portability requirements, open-source verification mandate, federation directory model, cross-organization custody transfer pattern |
| Added | §6 | Regulatory Alignment — EU AI Act (Regulation EU 2024/1689), DORA (Regulation EU 2022/2554), NIS2 (Directive EU 2022/2555), GDPR, SEC Rule 17a-4, OSFI, APRA CPS 234 |
| Added | §7 | Insurance and Legal Applications — underwriting uncertainty reduction, claims compression, qualifying control designation, legal evidentiary properties |
| Added | §8 | Attack Vectors — 8 vectors per STYLE_GUIDE §7 format |
| Added | §9 | Conformance Requirements — 14 mandatory behaviors, 12 prohibited behaviors, 9 non-conformant claim types, 16-item verification checklist |
| Added | Conclusion | — |
| Added | Document Control | — |
| Removed | Nothing | First release. No prior version exists. |
