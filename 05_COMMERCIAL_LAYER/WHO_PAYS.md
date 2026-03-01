# Who Pays

This document defines economic responsibility for funding settlement
within the Cryptographic Verification Sidecar (CVS) specification.

The canonical CVS specification is defined by:

- `CVS_ARCHITECTURE_v2.7.md`
- `CVS_IMPLEMENTATION_v2.2.md`

If conflict exists, the canonical specification governs.

This document is normative with respect to funding separation,
not economic policy.

---

## Principle

Funding responsibility generally aligns with risk exposure.

The party that benefits from reduced ambiguity,
reduced liability exposure,
or improved defensibility
typically funds settlement anchoring.

Cost alignment supports structural sustainability.

---

## Primary Payer: Evidence Producer

In many deployments, the primary payer is:

- the system operator,
- the content publisher,
- the exchange,
- the organization whose outputs may be disputed.

These parties benefit from:

- improved evidentiary posture,
- reduced dispute uncertainty,
- clearer audit trails.

---

## Secondary Payers

Settlement costs MAY be allocated to:

- upstream providers,
- downstream distributors,
- contractual counterparties,
- ecosystem participants.

Such arrangements are contractual and external to CVS.

The architecture does not mandate allocation models.

---

## Verification Independence

Verification MUST NOT require payment by third parties.

Any party MUST be able to:

- independently verify evidence,
- inspect receipts,
- validate integrity.

Verification independence preserves neutrality.

---

## Operating Cost Classification

Settlement costs MAY be treated as:

- operational expenditure,
- compliance expenditure,
- risk mitigation expense.

The CVS specification does not define accounting treatment.

---

## Risk-Based Allocation

Settlement costs MAY be allocated based on:

- evidence volume,
- settlement frequency,
- operational characteristics.

Allocation models MUST NOT affect evidence integrity.

---

## Insurance Context

In insured environments:

- settlement costs MAY be recognized as risk controls,
- influence underwriting assessments,
- affect policy conditions.

The CVS specification does not define insurer obligations.

---

## Voluntary Adoption

Participation in evidence settlement is voluntary.

Organizations choosing not to anchor evidence
retain operational autonomy.

CVS does not impose funding obligations.

---

## Scope Limitation

This document:

- does not mandate pricing structures,
- does not require specific payers,
- does not define contractual arrangements.

It defines structural funding alignment only.

---

## Summary

Settlement requires funding.

Funding responsibility typically aligns with risk exposure.

Economic allocation remains external to evidence integrity.
