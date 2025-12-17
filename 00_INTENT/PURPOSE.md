# Purpose

This repository defines a reference architecture for **independent, fail-open evidence sidecars**.

The purpose of this work is to specify how digital systems may produce **verifiable, court-defensible evidence of what occurred**, without interfering with the operation, performance, or authority of those systems.

This repository does not define a product, platform, or service.  
It defines **constraints, invariants, and architectural rules** that enable independent evidence to exist alongside complex systems where trust failure is catastrophic.

---

## Why This Exists

Modern digital systems increasingly operate under conditions where:

- outcomes are disputed after the fact,
- internal logs are no longer trusted,
- synthetic generation obscures provenance,
- regulatory, legal, and insurance scrutiny is unavoidable,
- and system liveness cannot be compromised for compliance.

In such environments, traditional approaches to logging, monitoring, and governance fail because they are:

- inline with execution,
- controlled by system owners,
- mutable after the fact,
- or operationally fragile.

This repository defines an alternative pattern:
an **external witness**, operating in parallel, that records evidence without authority over the system it observes.

---

## The Witness Function

The core function described here is the **witness function**.

A witness:
- observes events,
- measures time and order,
- records cryptographic evidence,
- and produces immutable receipts.

A witness does **not**:
- execute actions,
- enforce policy,
- approve outcomes,
- or determine truth.

This distinction is foundational.

The system acts.  
The sidecar witnesses.  
Evidence is produced without control.

---

## Fail-Open as a First Principle

The evidence sidecar defined by this repository **must be fail-open**.

At no point may the operation, availability, or correctness of the observed system depend on the sidecar’s availability.

If the sidecar fails:
- the system continues to operate,
- the failure itself becomes observable,
- and any resulting evidence gap is detectable.

Fail-open behavior is mandatory.  
Fail-closed behavior is disallowed.

This requirement exists because evidence systems that interrupt execution are rejected by operators, engineers, and regulators alike.

---

## Independence and Trust

Evidence produced by a system is inherently weaker than evidence produced **about** a system.

For evidence to be credible:
- it must be externally verifiable,
- resistant to insider modification,
- and independently anchored.

This repository therefore defines architectures in which evidence is:

- generated outside the control plane,
- cryptographically chained,
- and anchored to a neutral public settlement layer.

Trust is not asserted.  
Trust is inferred from constraints.

---

## Audience

This repository is written for:

- engineers designing high-availability systems,
- architects responsible for compliance and auditability,
- legal and risk teams evaluating evidentiary strength,
- CFOs and insurers assessing operational risk,
- regulators defining reasonable technical controls.

It is not written for end users, activists, or marketing audiences.

---

## Scope

This repository applies to any domain where:

- events matter after they occur,
- disputes are resolved retrospectively,
- and operational continuity is paramount.

This includes, but is not limited to:

- broadcast and digital media,
- financial markets and exchanges,
- AI training and inference systems,
- supply chains and logistics,
- healthcare diagnostics,
- public sector and electoral infrastructure.

Domain-specific mappings are provided elsewhere in this repository.

---

## Relationship to 512

This work is **compatible with**, but **independent of**, the 512 kernel.

512 defines high-level constraints around voluntariness, transparency, contestability, and authority limits.

This repository defines **one possible realization** of those constraints:  
the production of independent, fail-open evidence.

No part of this repository modifies, extends, or governs 512.

---

## What Success Looks Like

This work is successful if:

- multiple vendors implement it independently,
- regulators reference its principles without naming vendors,
- insurers recognize it as a qualifying control,
- and systems without independent witnesses appear increasingly negligent.

Adoption is expected to be quiet, incremental, and inevitable.

No central authority is required.
