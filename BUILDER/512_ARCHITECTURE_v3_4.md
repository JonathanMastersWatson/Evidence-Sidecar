# 512: The Commit Gate — Reference Architecture

**Jonathan M. Watson | 512 / CVS Architecture**
**Version 3.4 | May 2026**
**Canonical Repository:** github.com/JonathanMastersWatson/512
**Canonical Kernel Commitment:** SHA-256: `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5`

---

## §-1 Legal Notice and Limitation of Liability

### §-1.1 Informational Nature

This document is provided for informational purposes only. It describes a discovered constraint and a reference architecture for witnessing that constraint — it does not constitute a product specification, a compliance certification, a standards mandate, or a legal instrument. Nothing in this document creates obligations on any party except as expressly agreed in a separate written agreement.

### §-1.2 No Warranty

This document and the architecture it describes are provided "as is," without warranty of any kind, express or implied, including but not limited to warranties of merchantability, fitness for a particular purpose, accuracy, completeness, or non-infringement. The authors and contributors make no representation that this document is free from defects, errors, or omissions.

### §-1.3 No Professional Advice

Nothing in this document constitutes legal, regulatory, financial, insurance, or engineering advice. Organisations evaluating whether their systems satisfy the properties described here must consult qualified legal counsel, compliance advisors, and licensed engineers appropriate to their jurisdiction and industry. The authors are not responsible for decisions made in reliance on this document.

### §-1.4 No Guarantee of Coverage or Compliance

This architecture does not guarantee regulatory compliance, insurance coverage, litigation defence, or audit passage. Compliance is a legal determination made by regulators and courts. Coverage is an underwriting determination made by insurers. This architecture provides a framework for understanding the constraints physics imposes on execution systems at scale — it does not make compliance determinations.

### §-1.5 Ownership and Licensing — Open Commons Declaration

**512** is a discovered constraint. The authors' position is that discovered constraints — properties that physics and scale force into existence regardless of human recognition — are not ownable in the manner of invented works. The authors assert no proprietary rights over the 512 constraint set, the Commit Gate category, or the seven invariants committed to the canonical kernel file, and do not intend to recognise exclusive proprietary claims asserted by any other party over those elements.

**CVS** (Cryptographic Verification Sidecar) is an invented witness architecture released as open infrastructure commons. The authors assert no exclusive ownership over the base CVS architecture.

**Derivative works** — gate implementations, managed services, SLA-bound products, interpretation tools, industry-specific deployments — are fully ownable and commercialisable by their creators. The base is open. What is built on the base belongs to its builder.

This documentation is released under Creative Commons Attribution 4.0 International (CC BY 4.0). Refer to §-1.7 for complete license terms.

### §-1.6 Public Ledger References

References to the XRP Ledger (XRPL) in this document are descriptive, not prescriptive. This architecture is ledger-agnostic. Any settlement ledger satisfying the mandatory technical properties — deterministic finality, predictable cost, public verifiability, and no execution-layer coupling — may be substituted without altering the architecture's semantics. References to XRPL do not imply endorsement, partnership, dependency, or affiliation.

### §-1.7 License

This document is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0). To view a copy of this license, visit https://creativecommons.org/licenses/by/4.0/. You are free to share and adapt this material for any purpose, including commercial use, provided appropriate credit is given: "512 Reference Architecture, Jonathan M. Watson, github.com/JonathanMastersWatson/512," a link to the license is provided, and any changes made are indicated.

### §-1.8 Jurisdictional Scope

This document has been prepared with reference to the laws and regulatory frameworks of Canada, the United States, and the United Kingdom. It is not legal advice in any jurisdiction. To the fullest extent permitted by applicable law, the authors disclaim all financial liability arising from use of this document or the architecture it describes. Organisations in other jurisdictions must assess applicability independently.

### §-1.9 Financial Projection Disclaimer

All cost, premium reduction, and ROI projections in this document are illustrative examples only. They are not guarantees of insurance premium reduction, regulatory penalty avoidance, financial return, or legal defence success. Actual results depend on deployment scope, insurer underwriting practices, regulatory context, and operational integrity of the implementation.

### §-1.10 No Reliance

This document is a descriptive technical specification and reference architecture only.

No party may rely on this document as:

- a certification of compliance,
- a guarantee of regulatory sufficiency,
- a guarantee of audit success,
- a guarantee of insurance coverage,
- a guarantee of risk mitigation,
- or a representation of operational fitness.

Compliance, certification, underwriting, and legal sufficiency are determinations made exclusively by regulators, courts, insurers, and licensed professionals.

Any organisation implementing concepts described herein does so at its own risk and bears full responsibility for deployment posture, regulatory interpretation, operational integrity, and jurisdictional compliance.

### §-1.11 No Endorsement

Nothing in this document constitutes:

- endorsement of any implementation,
- endorsement of any derivative system,
- endorsement of any organisation,
- endorsement of any settlement ledger,
- endorsement of any commercial deployment.

References to regulatory frameworks, standards bodies, or public ledger networks are descriptive only and do not imply approval, partnership, affiliation, or recognition.

No institution has certified, adopted, approved, or validated 512 or CVS unless expressly stated in a separate, formally executed written agreement.

### §-1.12 Independent Verification Requirement

Where verification is discussed, it refers to cryptographic or structural verifiability of recorded data — not legal, regulatory, or institutional validation.

Structural verifiability does not equate to compliance determination.

### §-1.13 Builder Responsibility

Any party constructing, deploying, or commercialising a system based on 512 or CVS assumes full responsibility for:

- system behaviour,
- constraint design,
- regulatory interpretation,
- evidence storage,
- key management,
- anchoring configuration,
- operational uptime,
- and all resulting consequences.

The authors of the canonical documentation do not exercise operational control over derivative deployments and, to the fullest extent permitted by applicable law, disclaim liability for consequences arising from such deployments.

---

## 0. Normative Relationships

This document is the CTO/Board-level reference for 512 and the Commit Gate category it instantiates. It establishes what 512 is, why physics forces it into existence, the structural properties that make it a new category of infrastructure — not a product, not a governance system, and not an invention — and the open commons model under which it is released.

The following canonical documents are normatively related to this one:

- **`CVS_ARCHITECTURE`** — Defines the Cryptographic Verification Sidecar: the reference witness layer for 512, independently useful, invented, and open-commons licensed. Evidence Object structure, hash-chaining, and XRPL anchoring semantics are defined there and not redefined here.
- **`512_IMPLEMENTATION`** — Defines how to build a system that satisfies 512's observable properties: constraint specification, validation execution, integration patterns, and deployment phases. Engineers read that document, not this one.
- **`Constraint-Architecture`** — Defines the upstream constraint discipline: what is admissible, consent logic, authority models, thresholds, and domain-specific admissibility rules. 512 enforces what Constraint Architecture declares. Constraint definition is outside the scope of this document. See https://github.com/JonathanMastersWatson/Constraint-Architecture.

The following operational reference documents in the 512 repository are non-normative companions to this document. They do not alter or extend the canonical specification — they define how organisations prepare workflows for gate execution:

- **`512-ops/INTEGRATION_STEPS.md`** — The 7-step enterprise integration workflow. Covers boundary identification, parallel path audit, Proposal Object definition, constraint definition, observation mode, enforcement transition, and evidence chain verification.
- **`512-ops/CONSTRAINT_DEFINITION_LAYER.md`** — How to translate policies into executable constraints. Defines the four-field constraint definition model, binary reducibility requirement, determinism requirement, and common failure modes.
- **`512-ops/REFERENCE_FLOW.md`** — The end-to-end sequence from intent declaration to anchored evidence. Covers all seven stages and the three CVS observation points.
- **`512-ops/PROPERTIES_CHECKLIST.md`** — Go-live verification instrument. Pre-enforcement and post-enforcement verification checklists.
- **`USE_CASES/ENTRY_POINTS/ENTERPRISE_PRACTITIONERS.md`** — Entry point for CTOs and Heads of AI preparing agentic workflows for Commit Gate execution.
- **`AARM_AND_512.md`** — Architectural positioning of 512 relative to AARM (arXiv 2602.09433) and the CSA Agentic Control Plane Initiative. Establishes that AARM governs the orchestration layer and 512 governs the commit boundary — complementary layers, not competing specifications.
- **`CANONICAL_COMMITMENT.md`** — Permanent priority record for 512 and CVS. Records genesis commit dates, XRPL anchor transaction, canonical kernel hash, and sealed archive hashes. The dated reference for any dispute, standards body submission, or ecosystem conversation referencing 512's prior art status.

This document takes precedence over none of these. Each document in the canonical set is authoritative within its defined scope.

Physics has forced a new category of infrastructure into existence.

When execution systems operate at machine speed — AI agents deciding in 10 microseconds, autonomous systems committing thousands of state changes per second — the moment between intent and irreversible consequence collapses below the threshold of human intervention. Governance mechanisms designed for human-speed execution do not slow down. They become structurally irrelevant.

The response to this is not a product. It is a constraint that physics makes inevitable: a **Commit Gate** — a minimal, immutable, binary mechanism positioned at the execution boundary, enforcing pre-committed rules before state change occurs, at speeds that make interpretation physically impossible.

512 is a specific Commit Gate. It was not invented. It was identified as the minimal constraint set that any legitimate execution system operating at civilisational scale satisfies, or does not — with the consequences that physics and scale impose. Its seven invariants derive from first principles about voluntary interaction, transparency, and exit rights — constraints that governed legitimate human systems long before machines existed at this speed. At machine speed, they are either enforced mechanically or they are not enforced at all.

512 is not subject to proprietary ownership — it is characterised here as a discovered constraint, not an authored artefact. It can be instantiated. Anyone may build a Commit Gate. If the gate sits at the commit boundary, executes in microseconds, carries an immutable specification, produces binary output, and enforces pre-committed constraints without interpretation — it is a Commit Gate. Whether it satisfies 512's specific invariants determines whether it is a 512-conforming Commit Gate.

To produce externally verifiable proof that a Commit Gate operated correctly, a witness layer is required. CVS is the reference witness layer for 512. It is an invention, openly licensed. Anyone may build a better one.

This document defines the category, establishes 512's position within it, describes the witness layer requirement, and explains the open commons model under which 512 and CVS are released.

---

## 1. Physics Forces the Commit Gate Into Existence

### 1.1 The Speed Gap Is a Physical Constant

The speed of light is approximately 299,792 kilometres per second. A photon travels from one end of a data centre to the other in nanoseconds. Human cognitive processing — the fastest possible reaction to a stimulus — requires 200 to 300 milliseconds minimum. That is not a design limitation. It is a physical constant, as fixed as the speed of light itself.

AI agents executing decisions at 10 microseconds operate 20,000 times faster than the minimum human reaction time. Autonomous trading systems commit state changes in microseconds. Manufacturing control systems adjust tolerances hundreds of times per minute. These are not edge cases. They are the operating conditions of any sufficiently scaled digital system in 2026, and the gap widens every year as compute advances while human biology does not.

This creates a physical impossibility that no governance framework designed for human-speed execution can resolve: **humans cannot intervene at machine speed.** Not with better tools. Not with faster processes. Not with more staff. The constraint is physical.

### 1.2 Execution Outrunning Intervention Produces Three Structural Failures

When a governance mechanism cannot reach the decision point before consequences become irreversible, three structural failures emerge — not as risks, but as certainties.

*Interpretation collapses at the commit boundary.* Compliance review requires judgment: applying rules, assessing context, weighing factors. At 10μs decision cycles generating 100,000 decisions per second, there is no time for judgment. Authority that requires interpretation cannot operate at machine speed. It does not slow the machine down. It becomes invisible to it.

*Post-hoc accountability loses evidentiary ground.* When disputes arise about what a machine did, reconstruction depends on evidence. At machine speed, systems generate millions of state transitions before anomalies are detected. Evidence that was not captured at execution time cannot be recovered with certainty later. Internal logs — mutable, selectively preserved, subject to administrator access — are not independent witnesses.

*Authority migrates upstream or disappears.* Rules that were interpreted during execution must become constraints enforced before execution, or they cease to function as rules. There is no third option. Governance architectures that do not adapt to this physical reality do not remain neutral — they become structurally unenforceable.

### 1.3 The Commit Boundary Is Where Authority Must Live

Every execution system has a commit boundary: the precise moment at which a proposed action becomes an irreversible state change. Before the commit boundary, actions are proposals. After it, they are facts. Human oversight of proposals is physically possible. Human oversight of committed facts is retrospective — valuable for learning, insufficient for prevention.

Authority that operates effectively at machine speed lives at the commit boundary. Not inside execution. Not after it. At it.

The mechanism that enforces authority at the commit boundary — immutable, binary, minimal, fast — is what this document calls a **Commit Gate**. Physics forces this mechanism into existence at scale. The question is not whether a Commit Gate exists in a given system. The question is whether it has been deliberately identified, specified, and made verifiable.

---

## 2. What a Commit Gate Is

### 2.1 Definition

A **Commit Gate** is a mechanism that:

- is positioned at the commit boundary — between authorisation and irreversible state change
- executes at machine speed: sub-50μs in software, sub-5μs in dedicated hardware
- carries an immutable specification — the constraint set cannot be modified at runtime
- produces binary output only: allow or deny
- enforces pre-committed constraints without interpretation, discretion, or judgment
- is minimal — the specification is small enough to be mechanically verified in its entirety
- fails open — when the gate is unavailable, execution continues and the gap is recorded

These are not design choices. They are the properties that the physics of the commit boundary forces on any mechanism that genuinely operates there. A mechanism that does not exhibit all of these properties is not a Commit Gate — it is something else: a monitoring system, a policy engine, a governance layer, a logging service.

### 2.2 A Commit Gate Is Not a Policy Engine, Governance Body, or Product

A Commit Gate is not:

- a **policy engine** — it does not define rules, interpret rules, or apply judgment to rules
- a **governance body** — it makes no decisions and exercises no discretion
- a **monitoring system** — it operates before execution, not after
- a **compliance system** — it enforces constraints; compliance is a legal determination made by humans
- a **control plane** — it does not alter execution; it permits or denies proposals
- a **product** — it is a discovered category of infrastructure, as TCP/IP is a discovered category

### 2.3 The Commit Gate Is a New Infrastructure Category

TCP/IP did not exist until someone formalised the constraints that physics imposes on packet routing across distributed networks. Those constraints existed before the formalisation. Packets that violated them failed to route. The formalisation made the constraints legible, implementable, and universally adopted.

The Commit Gate is the same category shift, one layer up. The constraint that physics imposes on execution systems at civilisational speed has always existed. Machines that violate it accumulate the liabilities that scale and irreversibility impose: unverifiable evidence, unresolvable disputes, regulatory exposure, and trust collapse. The formalisation — naming the category, defining its properties, identifying a specific instantiation — makes the constraint legible and instrumentable.

Anyone may build a Commit Gate. The category is not owned. Specific instantiations may be named, versioned, and referenced. 512 is one such instantiation.

### 2.4 Naming Discipline

The canonical term is **Commit Gate**. All variants — Binary Constraint Kernel, Execution Kernel, Validation Gate, Policy Gateway, Execution Restraint Governance, Legitimacy Gate — are prohibited in canonical documents. The rationale and prohibited terms table are defined in `STYLE_GUIDE §11`.

### 2.5 The Commit Gate Owns the Only Commit Path

A Commit Gate is defined by commit path exclusivity: there exists exactly one path to irreversible state change, and that path does not open without the gate's authorisation signal.

This property separates enforcement from observation. A mechanism that evaluates proposals correctly but permits the commit path to operate independently of its signal is a monitoring system — structurally indistinguishable in its evaluation logic from a Commit Gate, architecturally incapable of enforcement. Any evaluation result delivered to a downstream component for interpretation or application reintroduces the gap the gate exists to close. Decision and execution resolve within the same atomic context. A gap between them is a bypass.

The gap takes three common forms:

- **Decision–execution separation:** the gate evaluates and signals; a downstream component receives the signal and applies it to the execution surface. The downstream component is now the point at which the commit path can be reached independently.
- **Pre-check positioning:** the gate operates upstream of the commit boundary rather than at it. The commit boundary remains reachable by a path that did not pass through the gate.
- **Parallel execution paths:** administrative, emergency, or internal routes reach the execution surface without gate evaluation. These paths are outside gate control regardless of how infrequently they are used. The existence of the path, not its frequency of use, is the disqualifying condition.

A system exhibiting commit path exclusivity: the commit boundary requires the gate's authorisation signal as a structural prerequisite. That signal is not advisory. It is not delivered asynchronously to a downstream layer. There is no parallel path. Without the gate's allow signal, the commit boundary does not open.

This property is structurally verifiable. A system that does not exhibit it is not a Commit Gate deployment — it is a system with a monitoring layer attached to a separately governed execution surface.

### 2.6 Layer Independence

The 512 constraint grammar defines admissibility conditions only.

It does not provide:

- evidence persistence
- cryptographic anchoring
- ledger settlement
- external enforcement
- constraint definition (admissibility rules, consent logic, authority models)

Such capabilities are provided by independent architectures:

- Evidence persistence and ledger anchoring: cryptographic evidence systems such as CVS
- Constraint definition: the upstream Constraint Architecture discipline at https://github.com/JonathanMastersWatson/Constraint-Architecture

The upstream constraint definition work — translating policies into binary-reducible executable logic — is the organisation's responsibility and must be complete before gate evaluation begins. The gate does not define constraints. It evaluates them. The four-field constraint definition model (Intent, Signal, Threshold, Authority) and the binary reducibility requirement are defined in `512-ops/CONSTRAINT_DEFINITION_LAYER.md`. The 7-step integration workflow from boundary identification to verified evidence chain is defined in `512-ops/INTEGRATION_STEPS.md`.

The 512 specification remains logically independent from any specific evidence, settlement, or constraint-definition layer.

---

## 3. What 512 Is

### 3.1 512 Is a Specific, Discovered Commit Gate

512 is the Commit Gate identified through applied systems research conducted in late 2025. It is named for its maximum specification surface: **512 bytes** of immutable constraint definition — the smallest surface at which the constraint set fits without interpretation ambiguity, and the largest surface at which the specification remains mechanically verifiable without judgment.

512 was not designed by deriving requirements from first principles and building to specification. It was found: the recognition that the seven constraints described below are the minimal set that any execution system operating at civilisational scale satisfies, or does not — with the consequences that physics and scale impose, derived from the physical realities of machine speed, human latency, and the irreversibility of committed state.

The analogy is precise. Thomas Edison invented the light bulb — a designed artefact built to specification. Benjamin Franklin did not invent electricity — he identified a property of the physical world that existed independent of observation. 512 is in the second category. The constraint existed before it was named. Systems that violate it pay the price regardless of whether they know the name.

### 3.2 The Canonical Commitment

The 512 constraint set is committed to a specific, immutable file:

```
Path:   512-core/KERNEL/512-kernel-padded.txt
Size:   512 bytes (exact, UTF-8, no BOM)
SHA-256: 7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5
```

This hash binds the constraint set to a specific, verifiable artefact. A claimed instance of 512 may be described as canonical only if it validates against this hash. A gate executing against a different constraint set may be a valid Commit Gate — but it is a different instantiation, and may be described as canonical 512 only if the hash matches.

### 3.3 The Validation Sequence

A system satisfying 512's properties processes every execution request in four steps:

1. **Intent Declaration** — the proposing entity declares what it intends to execute: action type, parameters, scope
2. **Context Binding** — system state at proposal time is captured: timestamp, identity, environmental conditions, resource state
3. **Constraint Evaluation** — the seven invariants are evaluated against intent and context, producing allow or deny
4. **Commit Authorisation Signal** — the gate returns exactly one of two values: ALLOW (commit path opens) or DENY (commit path remains closed; denial recorded). The gate's signal is the structural prerequisite for the commit path — not a result delivered to a downstream layer for application. When the gate is unavailable or evaluation times out, the gate produces no output; the fail-open handler engages, the commit path opens, and the witness layer records the ungoverned period as an evidence chain gap. Execution proceeds under fail-open because availability is prioritised over blocking; constraint satisfaction was not established.

Evaluation completes in 10–50μs in software. For systems operating at sub-10μs timescales, FPGA-based gate hardware reduces evaluation to under 5μs.

---

## 4. The Seven Invariants

The seven invariants are committed to the canonical specification (SHA-256: `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5`). They derive from first principles about voluntary interaction, transparency, and exit rights — properties of legitimate human systems that predate digital execution by centuries. At machine speed, they are either enforced mechanically or they are not enforced. Real-time interpretation is physically impossible at these speeds. The invariants can only be pre-committed and evaluated deterministically.

Any modification to the invariants produces a different hash — making unauthorised alteration mechanically detectable by any party with access to the canonical repository.

### 4.1 Invariant 1: No Agent May Initiate Force or Fraud Against Any Human

**Requirement:** Autonomous systems executing at machine speed must not coerce, deceive, or harm humans through their actions.

**Rationale:** When agents act faster than human reaction time, coercive actions complete before detection. Traditional oversight assumes humans can intervene during execution. At machine speed, that assumption fails entirely. The invariant does not restrict what machines can do — it restricts what they can do *to humans* without human knowledge or consent.

**Enforcement:** The gate evaluates each proposal against declared force and fraud patterns encoded as executable constraints: unauthorised fund transfer above declared threshold, execution against non-consenting parties, deceptive output generation with known false parameters.

**Failure mode:** Agent completes a coercive or deceptive action before detection. Internal records document the harm. The organisation cannot demonstrate it attempted to prevent the action — only that it recorded the outcome.

### 4.2 Invariant 2: All Interactions Must Be Voluntary and Based on Explicit Consent

**Requirement:** No execution affecting a human party proceeds without documented, explicit, prior consent from that party.

**Rationale:** Implied consent, inferred consent, and "by continuing to use this service" constructions do not survive regulatory scrutiny under GDPR (Regulation EU 2016/679), PIPEDA, or emerging AI governance frameworks. Explicit consent enforced at the commit boundary is the only form of consent that is mechanically verifiable. Post-hoc consent documentation is assertion, not proof.

**Enforcement:** The gate validates that consent records exist and are current before permitting execution affecting the consenting party. Consent is a cryptographic attestation. Missing or expired consent produces a deny result.

**Failure mode:** System executes against parties who have not given documented, explicit consent. Regulatory challenge requires proof of consent that cannot be independently verified. The dispute becomes an interpretive contest the organisation is unlikely to win.

### 4.3 Invariant 3: Consent May Be Withdrawn — Exit Must Always Be Possible

**Requirement:** Any party that has given consent may withdraw it. Withdrawal must propagate to all active execution contexts within the declared propagation window.

**Rationale:** Consent that cannot be withdrawn is coercion extended over time. Exit must be functionally accessible — not merely theoretically available. Systems that make exit technically possible but operationally burdensome violate this invariant.

**Enforcement:** The gate validates that withdrawal mechanisms exist, that withdrawal propagates within defined bounds, and that no execution proceeds against a party in revoked-consent state. Tokens issued before revocation carry the revocation epoch at issuance; tokens presenting a stale epoch are denied.

**Failure mode:** User revokes consent. System continues executing against them because token validation does not check revocation epoch currency. Harm accumulates during the propagation gap. Liability attaches to the entire post-revocation execution window.

### 4.4 Invariant 4: All Contracts Must Be Explicit, Readable, and Equally Enforceable by All Parties

**Requirement:** Governing terms for any interaction must be stated in language both parties can read and understand, and must be legally enforceable by both parties on equal terms.

**Rationale:** Contracts of adhesion — terms drafted entirely by one party, requiring specialist expertise to interpret, with enforcement rights asymmetrically distributed — reflect the direction of regulatory travel across GDPR, the EU AI Act (Regulation EU 2024/1689), and consumer protection frameworks. Contracts that cannot be read and enforced by both parties are contracts that regulators and courts will progressively refuse to honour.

**Enforcement:** The gate validates that active contracts are machine-readable, have been acknowledged by both parties, and contain no enforcement asymmetry that would prevent the non-drafting party from asserting rights.

**Failure mode:** Organisation operates under terms the counterparty cannot read or enforce. Dispute arises. Terms are unenforceable. Regulatory investigation follows. The organisation's legal position does not survive examination.

### 4.5 Invariant 5: No Rules Governing Interaction May Be Hidden or Unilaterally Changed

**Requirement:** All constraints governing a relationship must be fully disclosed to all parties before execution. Rules may not be changed unilaterally. The canonical commitment hash proves which constraint set was active at any point in time.

**Rationale:** Unilateral rule changes enable bait-and-switch at machine speed. Rules change and propagate before affected parties detect them. The canonical hash commitment eliminates this attack surface: the constraint set is fixed, public, and independently verifiable. Any claimed update that does not match the canonical hash is not 512.

**Enforcement:** The gate validates that all active constraints are disclosed before execution proceeds. Updates require explicit consent from affected parties — not implied acceptance through continued use.

**Failure mode:** Operator changes rules without notice. Users claim they did not consent. Operator argues implicit acceptance. Without cryptographic proof of rule disclosure and explicit consent to changes, the dispute is unresolvable. The canonical hash record proves what rules were in effect and when.

### 4.6 Invariant 6: On Failure, Systems Must Fail Open, Reveal Governing Rules, and Default to Human Choice

**Requirement:** When constraint evaluation fails due to gate unavailability or internal error, execution continues — the failure is logged, governing constraints are disclosed, and humans receive the information needed to decide whether to proceed.

**Rationale:** Fail-closed systems create single points of failure and denial-of-service attack surfaces. They concentrate authority at the gate — whoever controls the gate controls all execution. Fail-open preserves operational continuity while ensuring failures are never silent. The constraint is not violated by gate failure — it is made observable.

**Enforcement:** The gate never blocks execution by failing closed. If it crashes or becomes unavailable, execution continues and the gap is recorded in the witness layer. When evaluation explicitly denies execution (constraint violated), the system discloses which constraint failed and why, enabling humans to understand the basis for denial.

**Failure mode:** Gate fails closed, blocking legitimate operations — a denial-of-service equivalent. Or gate fails silently, concealing constraint violations — creating evidentiary gaps exploitable by adversarial parties.

### 4.7 Invariant 7: The Specification Is Immutable — Adherence Is Binary

**Requirement:** The 512 specification cannot be modified. Evaluation either conforms to the canonical hash or it does not. Partial conformance does not exist.

**Rationale:** Mutable constraints enable drift: gradual relaxation through incremental modifications, each individually justified but collectively undermining the system. Immutability forces intentional forking — organisations that need different constraints must explicitly build a different gate with a different hash, making divergence visible and verifiable. Constraint drift becomes mechanically detectable rather than narratively deniable.

**Enforcement:** The canonical hash (`7B08C024...`) commits to the exact 512-byte specification. Any witness layer evidence includes the gate's specification hash, enabling independent verification that the canonical 512 specification — not a modified fork — was in effect.

**Failure mode:** Organisation deploys a modified gate claiming 512 conformance. Evidence appears to show constraint enforcement. Independent verifiers detect hash mismatch. The evidentiary record is compromised. The dispute shifts from "did you comply" to "did you fabricate compliance."

---

## 5. The Witness Layer Requirement

### 5.1 A Commit Gate Without a Witness Is Unverifiable

A Commit Gate enforces constraints. It does not, by itself, produce externally verifiable proof that it did so. A gate that operates correctly but leaves no independent record is operationally useful and evidentially worthless. When a dispute arises — about what executed, in what order, under what constraints — an unwitnessed gate cannot provide the cryptographic proof that separates a verifiable record from an assertion.

The witness layer is therefore not optional for any system requiring auditability. It is the component that transforms enforcement into proof.

### 5.2 CVS Is the Reference Witness Layer — Not the Only Valid One

CVS (Cryptographic Verification Sidecar) is the reference witness layer built for 512. It is an invention, openly licensed, non-ownable at the base layer. Its architecture, Evidence Object schema, hash-chaining model, and XRPL anchoring semantics are defined in `CVS_ARCHITECTURE` and are not redefined here.

Any witness architecture satisfying the properties defined in `CVS_ARCHITECTURE §2` is compatible with 512. A better CVS — faster anchoring, richer Evidence Object schema, lower infrastructure cost — would serve 512 better than CVS does. Building one is explicitly encouraged. An implementation may be described as CVS-conforming only if it satisfies the properties defined in `CVS_ARCHITECTURE §2`.

### 5.3 CVS Is Layered Above 512, Not Coupled to It

The relationship is not a coupling of equals. It is a layered architecture:

- **Constraint Architecture** defines what is admissible — consent logic, authority models, thresholds, domain constraints
- **Physics** forces the commit boundary into existence
- **512** defines the minimal constraint set a Commit Gate at that boundary satisfies, or fails to satisfy
- **CVS** is an invented witness layer that records what the gate did and makes that record independently verifiable
- **Derivatives** — managed services, SLA-bound implementations, interpretation tools — are built on CVS and are fully commercialisable

CVS does not make 512 work. CVS makes 512's operation *provable*. The gate enforces constraints whether or not anyone is watching. The witness records what the gate did so that independent parties can verify it later.

CVS can operate without a Commit Gate — it witnesses any event-emitting system. A Commit Gate can operate without CVS — enforcement continues regardless of whether evidence is captured. But a system claiming both enforcement and auditability requires both.

### 5.4 Separation of Authority Is Non-Negotiable

The gate enforces. The witness records. These roles do not merge in a correctly functioning architecture. A system that enforces constraints and controls its own evidence record can fabricate compliance — it can selectively record, modify, or delete evidence of its own operation. Independent authority between enforcement and witness is the structural property that makes the evidence trustworthy.

This separation is also why CVS is openly licensed. A proprietary witness layer controlled by the same organisation that controls the gate provides no independence. The value of CVS as a witness depends on its being outside the control of whatever it witnesses.

---

## 6. The Open Commons Model

### 6.1 512 and CVS Cannot Be Owned

512 is a discovered constraint. It is the authors' position that discovered constraints — properties of physical reality that exist independently of any author's contribution — are not appropriate subjects of proprietary ownership, for the same reason that gravity is not ownable: the property exists independent of any person's claim over it. The seven invariants describe what legitimate execution at machine speed requires. They were not authored into existence — they were identified as necessary conditions. Asserting exclusive ownership over a necessary condition of this kind would be, in the authors' view, a category error.

CVS is an invention, but it is deliberately released as open infrastructure. The strategic reason is that proprietary infrastructure does not scale to civilisational adoption. TCP/IP became the foundation of the internet economy because no single entity controlled it. SMTP became the foundation of email for the same reason. Linux became the foundation of cloud computing — and Red Hat sold for $34 billion — precisely because the base was free and the commercial value lived in implementations.

A proprietary CVS owned by a single entity would be evaluated as a vendor product, subject to procurement cycles, competitive substitution, and vendor lock-in concerns. An open CVS is infrastructure — capable of civilisational adoption, with commercial value residing in the ecosystem of services built on top.

### 6.2 Commercial Value Lives Entirely Above the Open Base

| Tier | What It Is | Ownable | Commercialisable |
|---|---|---|---|
| 512 / Commit Gate category | Discovered constraint | No | No |
| CVS base architecture | Invented witness layer, open commons | No | No |
| CVS derivatives | Implementations, managed services, SLA products, interpretation tools, industry deployments | Yes | Yes |

The base is permanently free. Commercial IP lives entirely in what is built on the base. Any organisation may build a managed CVS service, own that implementation entirely, wrap it in SLA contracts, sell it to enterprise clients, and retain all revenue. No royalties. No licensing fees. No permission required.

### 6.3 The Open Commons Model Produces an Ecosystem, Not a Product

In the SMTP analogy: SMTP is free. Gmail, Outlook, and Proofpoint are multi-billion dollar businesses. None of them own SMTP. All of them depend on it being universally adopted — and universal adoption is only possible because SMTP is free.

For 512 and CVS: the constraint is free. The evidence infrastructure is free. The managed compliance services, the regulatory reporting tools, the insurance underwriting integrations, the industry-specific interpretation layers — those are commercial. The potential scope of those services includes every organisation operating autonomous systems at machine speed. That is not a niche. It is the trajectory of the entire digital economy.

### 6.4 The Evidentiary Gap Compounds Without the Witness Layer

Every day an autonomous system operates without an independent witness layer is a day that cannot be reconstructed with cryptographic certainty. Disputes arising from actions taken during unwitnessed periods are resolved through weaker means — internal logs, testimony, forensic reconstruction — with correspondingly weaker evidentiary outcomes. The gap does not close retroactively. Systems that instrument a witness layer later cannot produce evidence for periods before instrumentation. The cost of the gap accumulates in proportion to execution volume. *(illustrative — see §-1.9)*

---

## 7. Regulatory Alignment

The following section describes structural characteristics of the 512 and CVS architecture that are relevant to several regulatory frameworks. These descriptions are not compliance assessments, legal opinions, or regulatory determinations. Whether a specific deployment satisfies any statutory obligation is a determination made by the relevant regulator, court, or licensed professional for the applicable jurisdiction. Readers should not construe any statement in this section as a guarantee of compliance, audit readiness, or regulatory sufficiency.

### 7.1 EU AI Act — Mandatory Logging for High-Risk Systems

EU AI Act Article 12 (Regulation EU 2024/1689) requires that high-risk AI systems implement automatic logging enabling auditability, traceability, and lifecycle monitoring. High-risk categories under Annex III include biometric identification, critical infrastructure, employment, essential services, law enforcement, migration, and administration of justice.

A system satisfying 512's properties, witnessed by a CVS-compatible layer, exhibits structural characteristics relevant to Article 12 through execution-time Evidence Object generation, hash-chained WORM storage, and public ledger anchoring. Evidence Objects are not internal records subject to modification — they are cryptographic commitments on a public settlement layer. Recording is automatic, occurring for every evaluation event including denials and validation gaps. Whether these characteristics satisfy Article 12 in any specific deployment is a determination for the applicable supervisory authority.

### 7.2 DORA — Digital Operational Resilience

EU Digital Operational Resilience Act (DORA, Regulation EU 2022/2554), applicable to financial entities from January 2025, requires ICT incident logging, incident response documentation, and demonstrable resilience testing. The fail-open behaviour of Invariant 6 aligns with DORA's operational continuity framing — execution does not block on gate failure. The Validation Gap record is structurally relevant to DORA's documentation of periods of degraded operation. CVS evidence chains produce tamper-evident incident records that are structurally consistent with DORA's reporting framework. Whether these characteristics satisfy DORA obligations in any specific deployment is a determination for the applicable competent authority.

### 7.3 SEC Rule 17a-4 — Electronic Records

SEC Rule 17a-4(f) (17 CFR § 240.17a-4(f)) requires broker-dealers to preserve electronic records in non-rewriteable, non-erasable format (WORM). CVS Evidence Objects stored in WORM-compliant append-only storage with hash-chain integrity exhibit structural characteristics relevant to this requirement. The hash chain ensures that tampering is detectable, not merely prohibited. Public ledger anchoring provides an additional independent verification mechanism structurally consistent with the SEC's audit trail access framework. Whether these characteristics satisfy Rule 17a-4 obligations in any specific deployment is a determination for the SEC or applicable legal counsel.

### 7.4 NIST AI Risk Management Framework

NIST AI RMF (NIST AI 100-1) identifies Govern, Map, Measure, and Manage as the four core functions of AI risk management. 512's invariants exhibit structural characteristics relevant to the Govern function — pre-execution constraint enforcement at the commit boundary. CVS evidence chains support behavioural reconstruction relevant to the Map function. Per-invariant evaluation results captured for every execution event support quantitative assessment relevant to the Measure function. Fail-open behaviour and Validation Gap records support active observation of constraint enforcement relevant to the Manage function. Whether these structural characteristics satisfy NIST AI RMF expectations in any specific context is a determination for the applicable risk management authority or licensed professional.

---

## 8. Properties Specification

The following properties are observable characteristics of any valid Commit Gate. These are not mandates. They describe what necessarily holds.

A Commit Gate satisfying 512's properties exhibits the following observable characteristics. A gate that does not exhibit them is not a Commit Gate. A gate that does not exhibit them *and* claims to be 512 is making a false claim independently detectable through hash verification.

### 8.1 Observable Properties

- **Sub-50μs evaluation latency** — A Commit Gate exhibits median evaluation time below 50μs and 99th-percentile evaluation time below 200μs. An instantiation failing this property is not a Commit Gate — it cannot operate at the commit boundary of a machine-speed system.
- **Deterministic evaluation** — The property holds when identical inputs (intent, identity, context, constraints) always produce identical output. An instantiation whose output varies under identical inputs is not a Commit Gate.
- **Fail-open under gate failure** — A Commit Gate exhibits continued execution when it crashes, becomes unavailable, or cannot complete evaluation, with the gap recorded in the witness layer. An instantiation that blocks execution on its own failure is not a Commit Gate.
- **Witness layer integration** — The property holds when every evaluation event — allow and deny — produces a witness Evidence Object containing the specification hash, per-invariant results, and execution correlation ID. An unwitnessed gate is operationally valid but evidentially unverifiable.
- **Binary evaluation output** — A Commit Gate evaluation produces exactly two outcomes: ALLOW or DENY. An instantiation returning scored, probabilistic, conditional, deferred, or any output other than these two is not a Commit Gate. When the gate is unavailable, it produces no output; the fail-open handler engages and the witness layer records the ungoverned period as an evidence chain gap.
- **Public settlement anchoring** — The property holds when witness evidence anchors to a public, deterministic-finality ledger. An instantiation anchoring to private or permissioned settlement does not provide independent verifiability.
- **All seven invariants evaluated on every proposal** — A Commit Gate satisfying 512's properties evaluates all seven invariants on every proposal without exception. An instantiation performing partial or selective invariant evaluation is not a 512-conforming Commit Gate. It may be a valid Commit Gate with a different constraint set, and may be described as 512-conforming only if all seven invariants are evaluated on every proposal.
- **Canonical hash match** — The property holds when the specification hash recorded in witness Evidence Objects matches `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5`. An instantiation recording a different hash is a different gate.
- **Commit path exclusivity** — The property holds when there exists exactly one path to irreversible state change and that path does not open without the gate's authorisation signal. An instantiation whose execution surface is reachable independently of the gate's signal — through a parallel path, downstream interpretation layer, or pre-check positioning — does not exhibit this property and is not a Commit Gate deployment.

### 8.2 Disqualifying Properties

The following are structural disqualifiers. A mechanism exhibiting any of them is not a Commit Gate, regardless of any other properties it satisfies.

- **Interpretive logic** — the mechanism applies judgment, context-sensitivity, or discretion to constraint evaluation. A Commit Gate evaluates pre-committed logic only.
- **State accumulation** — the mechanism retains memory of past evaluations, learned patterns, or accumulated counters across evaluation calls. A Commit Gate is stateless; context may be queried externally but is not held internally.
- **Governance authority** — the mechanism defines, modifies, or decides which constraints apply. A Commit Gate enforces a fixed, externally committed specification.
- **Execution participation** — the mechanism alters execution parameters, influences outcomes, or modifies proposals. A Commit Gate permits or denies; it does not act.
- **Selective evaluation** — the mechanism enforces constraints on some proposals but not others, or provides bypass pathways of any kind. The property holds only when evaluation applies uniformly to every proposal reaching the gate.
- **Commit path non-exclusivity** — the execution surface is reachable without passing through the gate's evaluation. A pre-check architecture, parallel path, or downstream handoff model does not satisfy the commit path ownership property.

### 8.3 Claims No 512-Conforming Instantiation May Make

A Commit Gate satisfying 512's properties does not make the following claims, and an instantiation using the following terms does not satisfy the property of accurate self-description:

- "This gate guarantees correctness" — a Commit Gate evaluates admissibility, not outcome quality
- "This gate prevents all harm" — the property holds for constraint enforcement; constraint sufficiency is a design responsibility, not a gate property
- "This gate replaces audits" — a Commit Gate provides execution-time evidence for audits; audit function is external
- "This gate grants compliance certification" — constraint enforcement is not a legal determination
- "This gate eliminates human oversight" — a Commit Gate moves oversight upstream to constraint design; oversight remains, at an earlier point in the lifecycle
- "512-compliant" — 512 has no compliance authority; a system either satisfies 512's properties or it does not
- "512-compatible" — compatibility implies partial satisfaction; satisfaction is binary
- "512-aligned" or "512-inspired" — there is no alignment spectrum; properties are binary
- "Spirit of 512" — there is no spirit; properties are observable or they are not
- "Partial conformance" — partial conformance does not exist; a system satisfies all seven invariants at every execution boundary or it does not

### 8.4 Properties Verification

| Property | Observable Indicator | Observable |
|---|---|---|
| Median evaluation latency <50μs | Load test: 10,000 proposals, measure median | Yes / No |
| 99th percentile latency <200μs | Load test: 10,000 proposals, measure 99th pct | Yes / No |
| Deterministic evaluation | 1,000 identical proposal pairs produce identical output | Yes / No |
| Fail-open under gate failure | Kill gate mid-execution; verify continuation and gap record | Yes / No |
| Gap recorded in witness layer | Inspect witness evidence after fail-open test | Yes / No |
| All 7 invariants evaluated per proposal | Unit test each invariant with pass/fail inputs | Yes / No |
| Witness Evidence Object generated per event | Integration test: verify Evidence Object per proposal | Yes / No |
| Evidence Object includes specification hash | Schema validation against Evidence Object | Yes / No |
| Specification hash matches canonical commitment | SHA-256 comparison against `7B08C024...` | Yes / No |
| Evidence anchored to public ledger | XRPL transaction verification for Merkle root | Yes / No |
| No bypass mechanism accessible | Penetration test: attempt selective evaluation | Yes / No |
| Deny result discloses failed invariant | Submit proposals violating each invariant; inspect response | Yes / No |
| Commit path exclusivity | Penetration test: attempt to reach execution surface without gate evaluation | Yes / No |

---

## 9. Attack Vectors

**Specification substitution** — an adversary replaces the canonical 512 specification with a modified version while continuing to claim 512 conformance.
*Mechanism:* Internal deployment of a gate executing against a modified constraint set. Witness layer evidence continues to be generated, appearing to show 512 enforcement.
*Defense:* Every CVS Evidence Object includes the gate's specification hash. Independent verifiers compare the recorded hash against the canonical commitment (`7B08C024...`). Hash mismatch is mechanically detectable by any party with access to the public ledger and the canonical repository.
*Residual risk:* An adversary who also controls the witness layer and the public settlement layer could fabricate matching hashes. This requires simultaneous compromise of three independent systems. The architecture separates these roles to make this attack require extraordinary resources.

**Intent declaration spoofing** — a proposing entity declares a benign intent but executes a harmful action after the gate allows the proposal.
*Mechanism:* The gate evaluates declared intent. If the execution layer does not enforce correspondence between declared intent and actual execution, the gate's allow result becomes advisory.
*Defense:* The CVS post-execution Evidence Object records the actual execution outcome. Divergence between declared intent and recorded outcome is detectable in the evidence chain. Enforcement of intent-execution correspondence is a deployment constraint defined in `512_IMPLEMENTATION §4.3`.
*Residual risk:* Evidence of divergence is available after the fact. Prevention of intent spoofing requires that the execution layer enforce declared bounds — an implementation responsibility, not a gate responsibility.

**Constraint specification ambiguity** — a constraint is specified with sufficient ambiguity that adversarially crafted inputs technically satisfy the constraint while producing harmful outcomes.
*Mechanism:* Constraint designers specify policy goals rather than binary executable logic. The resulting constraint passes specification review but contains edge cases exploitable under adversarial input.
*Defense:* The 512-byte specification limit forces distillation to executable logic. Compilation requires deterministic binary evaluation. Ambiguous constraints that cannot compile to deterministic logic are rejected at compilation.
*Residual risk:* Constraints that are syntactically deterministic but semantically incomplete — specifying the wrong thing precisely — are not detectable by the gate. Constraint design review by qualified architects is required before production evaluation.

**Validation gap exploitation** — an adversary deliberately triggers gate failure to create evaluation gaps during which unconstrained execution proceeds.
*Mechanism:* Resource exhaustion, network partition, or targeted denial-of-service against the gate. During the resulting gap, execution proceeds without constraint evaluation.
*Defense:* Validation gaps are first-class witness layer records. The gap, its duration, and the executing identity during the gap are all recorded. Post-gap forensic analysis identifies all executions that occurred without evaluation. Fail-open behaviour preserves operations but does not conceal the absence of enforcement.
*Residual risk:* Execution during a gap is unconstrained. Harms that occur during gaps are recorded but not prevented. Infrastructure resilience for the gate — defined in `512_IMPLEMENTATION §6.2` — is the primary mitigation.

**Selective gate bypass** — an operator routes specific requests around the gate, allowing unconstrained execution for selected request types or identities.
*Mechanism:* Modification of request routing so that certain requests reach the execution layer without passing through gate evaluation. No denial records exist. No gap records exist, because the gate was never reached.
*Defense:* Any request that reaches the execution layer without a corresponding witness Evidence Object creates a detectable absence. Evidence gap analysis identifies execution events with no associated evaluation record. CVS must be positioned to observe all execution pathways — coverage completeness is defined in `CVS_ARCHITECTURE §2`.
*Residual risk:* Bypass detection depends on witness layer coverage of the full execution surface. Execution pathways outside witness coverage produce neither evaluation records nor gap records.

**Bypass accumulation** — a system is built with the gate correctly positioned in the primary path, but exceptions accumulate over time until the gate is structurally irrelevant.
*Mechanism:* Emergency admin paths, operator override mechanisms, and direct execution surface access are added incrementally — each individually justified, collectively rendering the boundary ineffective. No single change breaks the architecture; the cumulative effect does.
*Defense:* All execution paths — including override paths — must route through gate evaluation or generate a gap record. An override path that skips evaluation without generating a gap record is indistinguishable from a bypass. The commit path exclusivity property requires that no parallel execution pathway exist without a corresponding gap record.
*Residual risk:* Bypass accumulation is the most common real-world failure mode and is not detectable by examining any single event. Periodic structural audits of all execution pathways — verifying that every route to the execution surface passes through or generates a record from the gate — are the primary mitigation. Procedures do not substitute for structural enforcement.

**Hash chain tampering** — an adversary modifies historical witness records to remove or alter evidence of constraint violations.
*Mechanism:* Internal access to the evidence store enables deletion or modification of Evidence Objects. Modified records are presented as authoritative history.
*Defense:* Hash chaining means any modification breaks the chain at that point. The break propagates forward — all subsequent hashes no longer validate against the modified ancestor. Public ledger anchoring provides an independent reference: the Merkle root anchored to XRPL cannot be retroactively modified, and the chain must validate from Evidence Objects to that root.
*Residual risk:* Modifications occurring after ledger anchoring are detectable. Modifications occurring before the next anchoring window (typically every 30 seconds) are not yet anchored. Real-time anchoring frequency determines the maximum window of undetectable modification.

---

## Conclusion

512 exists because physics makes it necessary. When execution systems operate at speeds where human intervention is physically impossible, authority does not vanish — it compresses to the commit boundary. Whatever sits at that boundary, enforcing pre-committed constraints before irreversible state change occurs, is a Commit Gate. Whether any specific system has deliberately instrumented one does not change whether the constraint applies. It changes whether the constraint is satisfied.

512 is one Commit Gate — the one identified through applied systems research in late 2025, defined by seven Lockean invariants that govern voluntary interaction at machine speed, committed to a 512-byte canonical specification, and released as open infrastructure commons. It is not subject to proprietary ownership. It can be instantiated. Anyone may build a better one.

To produce verifiable proof that a Commit Gate operated correctly, a witness layer is required. CVS is that layer — invented, openly licensed, commercialisable in derivative form by any organisation that builds on it. The base is infrastructure. The commercial value lives above it.

Systems that satisfy 512's properties and instrument a compatible witness layer produce execution-time evidence that is cryptographically provable, anchored to public settlement, and auditable by independent parties. Systems that do not satisfy these properties remain operational. But when disputes demand proof of what executed, in what order, under what constraints, at speeds no human could observe — the absence of a witness record is not a neutral fact. It is the defining feature of the evidentiary position.

The constraint exists. The witness infrastructure is available. The open commons model removes structural barriers to adoption. What remains is the recognition that machine-speed execution without a Commit Gate and witness layer is not ungoverned — it is governed by whatever physics and scale impose on systems that do not instrument their own accountability.

**Canonical Repository:** github.com/JonathanMastersWatson/512

---

## Document Control

| Field | Value |
|---|---|
| Document | `512_ARCHITECTURE_v3.4.md` |
| Version | 3.4 |
| Date | May 2026 |
| Author | Jonathan M. Watson |
| Audience | CTO / Board / Regulators |
| Status | Active |
| Canonical Repository | github.com/JonathanMastersWatson/512 |
| Specification Commitment | SHA-256: `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5` |

### Changelog — v3.4

**May 2026 — competitive landscape and priority record cross-references.**

**Additions:**
- §0 Normative Relationships: two companion documents added — `AARM_AND_512.md` (architectural positioning relative to AARM/CSA) and `CANONICAL_COMMITMENT.md` (permanent priority and dated proof record).
- Document Control: Status updated from "Pre-Seal Hardening" to "Active".

**Modifications:**
- Document Control table: version and document name corrected from v3.2 to v3.3 (prior entry omitted the table update); now advanced to v3.4.

**Removals:** Nothing removed.

---

### Changelog — v3.3

**Hardening pass — April 2026 repository alignment.**

**Additions:**
- Document Control: Status field added — Pre-Seal Hardening.

**Modifications:**
- §0 Normative Relationships: cross-reference to `LAYER_REFERENCE.md` added — the authoritative three-layer semantic firewall document defining Kernel / Commit Boundary / Witness Layer separation, functions, outputs, and prohibited claims.
- §3.3 / §5 (Commit Path Ownership): language aligned with canonical vocabulary: "exclusive commit authority" and "non-bypassable commit path" confirmed as the prescribed terms throughout. "Pre-check architecture" explicitly named as non-conformant in §8.2 Disqualifying Properties.
- §8.4 Properties Verification table: CANONICAL_IR.json row updated — note added that the canonical IR contains exactly 7 rules (I1–I7), corrected from a prior 9-rule version that incorrectly split I3 and I7.

**Removals:** Nothing removed.

---

### Changelog — v3.2

**Additions:** Nothing added.

**Modifications:**
- §3.3 Validation Sequence Step 4: corrected GAP attribution error. Gate return values corrected from "exactly one of three values: ALLOW, DENY, or GAP" to "exactly one of two values: ALLOW or DENY." Fail-open behaviour reframed: when the gate is unavailable, it produces no output; the fail-open handler engages and the witness layer records the ungoverned period as an evidence chain gap. GAP is not a gate return value under any operational state.
- §8.1 Observable Properties — Binary evaluation output: corrected GAP attribution error. Removed framing of GAP as "the third output." Corrected to: gate produces ALLOW or DENY only; when unavailable, produces no output; fail-open handler engages; witness layer records evidence chain gap.

**Removals:** Nothing removed.

---

### Changelog — v3.1

**Additions:**
- §0 Normative Relationships: five 512-ops operational reference documents added as non-normative companions — `INTEGRATION_STEPS.md`, `CONSTRAINT_DEFINITION_LAYER.md`, `REFERENCE_FLOW.md`, `PROPERTIES_CHECKLIST.md`, and `ENTERPRISE_PRACTITIONERS.md`. These define the upstream preparation layer for organisations preparing agentic workflows for Commit Gate execution.
- §2.6 Layer Independence: extended to reference the constraint definition layer explicitly. Clarifies that upstream constraint definition work — translating policies into binary-reducible executable logic — is the organisation's responsibility and must be complete before gate evaluation begins. Points to `512-ops/CONSTRAINT_DEFINITION_LAYER.md` and `512-ops/INTEGRATION_STEPS.md` for operational detail.

**Modifications:** Nothing modified.

**Removals:** Nothing removed.

---

**Additions:**
- §2.5 Commit Gate Owns the Only Commit Path: new subsection defining commit path exclusivity as a structural property of the Commit Gate category. Establishes that decision and execution resolve within the same atomic context; a gap between them is a bypass. Identifies three common failure forms: decision–execution separation, pre-check positioning, and parallel execution paths. States that the existence of a bypass path — not its frequency of use — is the disqualifying condition.
- §8.1 Observable Properties: commit path exclusivity added as ninth observable property. Defines the observable indicator (penetration test: attempt to reach execution surface without gate evaluation) and adds to verification table in §8.4.
- §8.2 Disqualifying Properties: commit path non-exclusivity added as sixth structural disqualifier.
- §8.4 Properties Verification: commit path exclusivity row added.
- §3.3 Validation Sequence Step 4: renamed from "Execution Handoff" to "Commit Authorisation Signal." Reframed to make clear the gate's signal is the structural prerequisite for the commit path — not a result delivered to a downstream layer for application. GAP semantics clarified inline.

**Modifications:**
- §2.5 Layer Independence renumbered to §2.6 (to accommodate new §2.5).

**Removals:** Nothing removed.

---

### Changelog — v2.9

**Additions:**
- §0 Normative Relationships: Constraint Architecture added as third canonical reference — defines the upstream admissibility layer (consent logic, authority models, thresholds, domain constraints). Reference: https://github.com/JonathanMastersWatson/Constraint-Architecture.
- §2.5 Layer Independence: constraint definition added to the exclusion list; Constraint Architecture identified as the upstream architecture providing that capability.
- §9 Attack Vectors: bypass accumulation vector added. Describes the most common real-world failure mode — correctly positioned gate with accumulating exception paths that collectively render the boundary ineffective. Mechanism, defense (single authority path, gap records for all override paths), and residual risk (structural audit requirement) documented in canonical format.

**Modifications:**
- §-1.5 Ownership and Licensing: reverted from Apache License 2.0 (applied in v2.8) to CC BY 4.0 Open Commons Declaration.
- §-1.7 License: reverted from Apache License 2.0 to CC BY 4.0 with canonical URL and precise attribution requirements.
- §3.3 Validation Sequence: step 4 outputs capitalised to ALLOW / DENY / GAP throughout. GAP semantics clarified.
- §5.3 CVS Is Layered Above 512: Constraint Architecture added at top of layer stack.
- §8.1 Observable Properties: binary output bullet retitled and corrected to reflect ALLOW/DENY/GAP structure.
- §8.3 Claims: five prohibited framing terms added from hardening pass ANTI_DRIFT.md.

**Removals:** Nothing removed.

---

### Changelog — v2.8

**Additions:**
- §2.5 Layer Independence: new subsection.

**Modifications:**
- §-1.5 Ownership and Licensing: replaced with Apache License 2.0 declaration (subsequently reverted in v2.9).
- §-1.7 License: replaced with Apache License 2.0 (subsequently reverted in v2.9).

**Removals:** CC BY 4.0 license terms removed from §-1.5 and §-1.7 (subsequently restored in v2.9).

---

### Changelog — v2.7

**Additions:**
- §7 opening preface added.

**Modifications:**
- §7.1–§7.4: regulatory framing language updated throughout; compliance determination statements added.

**Removals:** Nothing removed.

---

### Changelog — v2.6

**Modifications:**
- §3.2, §5.2, §8.1: enforcement prohibitions replaced with positive definitional conditions throughout.

**Removals:** Nothing removed.

---

### Changelog — v2.5

**Modifications:**
- §-1.5, §-1.8, §-1.13, Abstract, §6.1, Conclusion: absolute legal claims replaced with authorial position framing throughout.

**Removals:** Nothing removed.

---

### Changelog — v2.4

**Additions:**
- §-1.10 No Reliance, §-1.11 No Endorsement, §-1.12 Independent Verification Requirement, §-1.13 Builder Responsibility: all new.

**Modifications:** Nothing modified.

**Removals:** Nothing removed.

---

### Changelog — v2.3

**Additions:**
- §-1.10 No Reliance: new subsection.

**Modifications:**
- §-1.7, §0, Abstract, §1.3, §4 intro, §5.4, §6.1, §6.3, §7.1–§7.3, Conclusion: discovery-language and framing discipline applied throughout.

**Removals:** Nothing removed.

---

### Changelog — v2.2

**Modifications:**
- §8 Properties Specification: discovery-language discipline applied throughout.

**Removals:** Nothing removed.

---

### Changelog — v2.1

**Modifications:**
- §8 and §9 swapped to conform to STYLE_GUIDE §3 mandatory section order.
- Six subsection headers rewritten as claims per STYLE_GUIDE §5.

**Removals:** Nothing removed.
