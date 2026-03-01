# Commercial Layer

This folder defines how settlement is funded
within the Cryptographic Verification Sidecar (CVS) specification.

The canonical CVS specification is defined by:

- `CVS_ARCHITECTURE_v2.7.md`
- `CVS_IMPLEMENTATION_v2.2.md`

If conflict exists, the canonical specification governs.

The commercial layer defines funding mechanics for settlement
without altering evidence integrity.

---

## Role in the Architecture

The commercial layer:

- funds settlement operations,
- attributes anchoring costs,
- supports financial auditability.

It is structurally separated from:

- evidence generation,
- hash chaining,
- disclosure semantics,
- settlement finality.

Financial flows MUST NOT influence evidence behavior.

---

## Separation Principle

Economic models MAY vary.

However, commercial mechanisms MUST NOT:

- alter Evidence Object structure,
- modify hash chaining semantics,
- condition disclosure behavior,
- introduce execution dependencies.

Funding is external to integrity.

---

## Contents

This folder includes:

- `WALLET_MODEL.md`
- `WHO_PAYS.md`
- `ACCOUNTING_AND_TAX.md`
- `INSURANCE_ALIGNMENT.md`

Each document addresses economic coordination,
not architectural authority.

---

## Normative Status

This folder is normative with respect to separation of concerns.

Commercial design choices MUST preserve:

- fail-open behavior,
- witness-only authority,
- structural independence of evidence.

---

## Scope Limitation

The commercial layer:

- does not mandate pricing models,
- does not define revenue structures,
- does not endorse specific economic strategies.

It defines funding boundaries only.

---

## Summary

Settlement requires funding.

Funding must remain structurally independent from evidence integrity.

Economic flows support anchoring —
they do not influence truth.
