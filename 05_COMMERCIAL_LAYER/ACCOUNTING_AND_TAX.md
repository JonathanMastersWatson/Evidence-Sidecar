# Accounting and Tax Treatment

This document defines accounting and tax considerations
for settlement costs within the
Cryptographic Verification Sidecar (CVS) specification.

The canonical CVS specification is defined by:

- `CVS_ARCHITECTURE_v2.7.md`
- `CVS_IMPLEMENTATION_v2.2.md`

If conflict exists, the canonical specification governs.

This document is normative with respect to structural auditability,
not accounting policy.

---

## Purpose

Settlement costs MUST be:

- auditable,
- attributable,
- reconcilable within standard financial controls.

Unclear financial treatment introduces operational friction.

---

## Expense Classification

Settlement costs MAY be classified as:

- operating expenses,
- compliance-related expenditures,
- risk mitigation costs.

The CVS specification does not prescribe capitalization rules.

Accounting classification remains jurisdiction-specific.

---

## Cost Attribution

Settlement costs MUST be attributable to:

- specific systems,
- business units,
- customers,
- cost centers.

Attribution mechanisms MUST be deterministic and reproducible.

---

## Transaction Records

Each settlement transaction MUST produce:

- a verifiable transaction identifier,
- a timestamp,
- a recorded cost amount.

These records support financial reconciliation.

---

## Batch Accounting

When settlement is batched:

- individual Evidence Objects MUST remain traceable to batch costs,
- allocation methodologies MUST be documented,
- cost distribution MUST be auditable.

Batching MUST NOT obscure accountability.

---

## Tax Considerations

Settlement costs MAY be treated according to applicable tax regulations.

The CVS specification:

- does not prescribe tax treatment,
- does not guarantee deductibility,
- does not provide tax advice.

It supports documentation required for reporting.

---

## Reporting Artifacts

Implementations SHOULD be capable of generating:

- itemized expense reports,
- transaction summaries,
- machine-readable audit exports.

Reports SHOULD support both automated reconciliation
and human audit review.

---

## Revenue Neutrality

The settlement mechanism itself does not generate revenue.

Any monetization occurs external to the CVS architecture.

Settlement cost tracking is distinct from revenue recognition.

---

## Audit Readiness

Settlement-related accounting records MUST support:

- internal audit,
- external audit,
- regulatory review where applicable.

Auditability is a structural requirement.

---

## Scope Limitation

This document:

- does not define accounting standards,
- does not mandate tax positions,
- does not alter regulatory obligations.

It defines structural traceability requirements only.

---

## Summary

Settlement costs must integrate cleanly
into existing financial systems.

Financial clarity supports operational adoption.
