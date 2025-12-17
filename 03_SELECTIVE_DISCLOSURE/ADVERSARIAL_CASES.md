# Adversarial Cases

This document defines how the Disclosure Kernel behaves under adversarial conditions.

Adversarial cases are expected, not exceptional.

The architecture must remain defensible when disclosure requests are hostile, coercive, or misaligned with system interests.

---

## Purpose

Adversarial cases exist when:

- disclosure is demanded under pressure,
- requests are framed to extract more than necessary,
- or incentives exist to distort or overreach.

This document ensures that selective disclosure remains bounded even in conflict.

---

## Adversarial Actors

Adversarial disclosure requests may originate from:

- litigants seeking leverage,
- regulators exceeding mandate,
- counterparties engaged in dispute,
- insiders attempting exfiltration,
- or external attackers probing systems.

The architecture must assume adversarial intent by default.

---

## Fishing Expeditions

Requests that seek to:

- explore broadly,
- identify unrelated issues,
- or extract large volumes of evidence

are classified as fishing expeditions.

Such requests must be rejected unless narrowly scoped and justified.

---

## Coercive Discovery

In legal or regulatory contexts, coercion may take the form of:

- implied penalties,
- accelerated deadlines,
- or ambiguous scope demands.

The Disclosure Kernel must enforce scope strictly, regardless of external pressure.

Scope violations are not softened by urgency.

---

## Scope Inflation Attacks

Adversaries may attempt to:

- expand time windows incrementally,
- chain multiple adjacent requests,
- or aggregate small disclosures into a larger whole.

The system must:

- track cumulative disclosure,
- detect scope inflation patterns,
- and apply proportionality controls.

---

## Payload Extraction Attempts

Requests framed as evidence verification may attempt to:

- reconstruct payloads,
- infer proprietary logic,
- or correlate evidence with external data.

The architecture must ensure that:

- hashes remain one-way,
- payload reconstruction is infeasible,
- and inference surfaces are minimized.

---

## Selective Omission Pressure

Adversaries may seek to:

- exclude inconvenient gaps,
- hide interruptions,
- or demand “clean” narratives.

The Disclosure Kernel must include all gaps within scope.

Continuity may not be implied.

---

## Replay and Context Shifting

Disclosed evidence may be reused out of context.

To mitigate this:

- disclosures must be bound to specific requests,
- scope definitions must accompany evidence,
- and reuse outside that scope must be detectable.

---

## Insider Abuse

Insiders may attempt to:

- authorize overbroad disclosures,
- bypass scoping controls,
- or selectively leak evidence.

The system must:

- log disclosure events,
- record scope parameters,
- and make disclosure actions auditable.

---

## Refusal as a Valid Outcome

Refusal to disclose is a valid and expected behavior.

The architecture must support:

- explicit refusal responses,
- documented reasons for refusal,
- and evidence of refusal integrity.

Disclosure is not unconditional.

---

## Legal Defensibility

In adversarial contexts, the system must be able to demonstrate that:

- disclosure followed predefined constraints,
- no discretionary expansion occurred,
- and proportionality was enforced consistently.

Consistency is the strongest defense.

---

## Summary

Adversarial pressure reveals hidden authority.

This architecture resists such pressure by design.

Disclosure remains bounded, even when demands are not.
