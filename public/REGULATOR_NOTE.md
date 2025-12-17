# Regulator Note

This document describes the evidence sidecar architecture in regulatory and oversight terms.

It is intended for technical regulators, auditors, and policy technologists.

---

## Regulatory Context

Regulators increasingly require:

- auditability,
- traceability,
- and post-event reconstruction.

However, inline enforcement and mandatory controls introduce operational risk and resistance.

This architecture avoids that tradeoff.

---

## Core Properties

The evidence sidecar is:

- independent of execution,
- fail-open by design,
- non-authoritative,
- and externally verifiable.

It observes systems without governing them.

---

## Proportionality

The architecture supports proportional oversight by enabling:

- narrowly scoped disclosure,
- minimal data revelation,
- and defensible refusal of overbroad requests.

This aligns with data minimization and due process principles.

---

## Independence

Evidence is generated outside the control plane of the observed system and anchored publicly.

This reduces reliance on self-attestation without imposing centralized authority.

---

## Failure Transparency

Failures are not concealed.

Gaps, interruptions, and delays are observable and disclosed.

This improves credibility rather than weakening it.

---

## Vendor Neutrality

The architecture is:

- technology-agnostic,
- vendor-neutral,
- and non-proprietary.

Multiple independent implementations are expected.

---

## Regulatory Value

This approach enables regulators to:

- verify integrity without micromanaging systems,
- assess compliance retrospectively,
- and reduce adversarial friction.

It strengthens oversight without expanding control.

---

## Summary

This architecture does not regulate behavior.

It makes behavior **auditable after the fact**, without disrupting operations.

That distinction matters.
