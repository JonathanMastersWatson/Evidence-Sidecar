# CVS Adoption and Migration Guide

This document describes a practical, low-risk path for organizations to adopt
the Cryptographic Verification Sidecar (CVS).

The canonical CVS specification is defined by:

- `CVS_ARCHITECTURE_v2.7.md`
- `CVS_IMPLEMENTATION_v2.2.md`

If conflict exists, the canonical specification governs.

Adoption is incremental, voluntary, and reversible.

---

## Purpose

The purpose of this guide is to:

- enable quiet, low-friction adoption,
- avoid disruptive system changes,
- reduce organizational resistance.

No “big bang” deployment is required.

---

## Guiding Principles for Adoption

Adoption should:

- preserve existing system behavior,
- introduce no new execution dependencies,
- avoid mandatory disclosure commitments,
- remain fail-open at every stage.

Evidence is added alongside systems, not inside them.

---

## Phase 1 — Observe Only

**Objective:** Establish independent observation without settlement or disclosure.

Actions:

- deploy CVS in observe-only mode,
- record Evidence Objects locally,
- enable hash chaining,
- do not anchor to a settlement ledger,
- do not expose disclosure interfaces.

Outcomes:

- zero operational risk,
- internal validation of evidence model,
- baseline visibility into gaps and failures.

This phase can run indefinitely.

---

## Phase 2 — Local Persistence and Review

**Objective:** Validate integrity and failure behavior.

Actions:

- persist evidence chains durably,
- simulate sidecar failure and recovery,
- verify gap detection,
- test independent verification workflows.

Outcomes:

- confidence in fail-open behavior,
- confidence in transparent failure reporting.

No external dependencies are introduced.

---

## Phase 3 — Deferred Settlement

**Objective:** Introduce public anchoring without changing operations.

Actions:

- batch Evidence Objects,
- anchor cryptographic commitments to a settlement ledger,
- treat settlement as asynchronous and deferrable,
- monitor cost and latency characteristics.

Outcomes:

- public proof of existence,
- predictable operating cost,
- no change to execution paths.

---

## Phase 4 — Selective Disclosure (Internal)

**Objective:** Exercise disclosure controls safely.

Actions:

- enable Disclosure Kernel internally,
- generate scoped disclosures for test cases,
- validate minimal revelation behavior,
- audit disclosure logging.

Outcomes:

- confidence in proportional transparency,
- defensible refusal behavior.

No external disclosure is required.

---

## Phase 5 — External Disclosure (As Needed)

**Objective:** Support real-world inquiries.

Actions:

- respond to regulatory, legal, or contractual requests,
- disclose only scoped evidence paths,
- include gaps and delays transparently,
- provide independent verification instructions.

Outcomes:

- reduced dispute ambiguity,
- faster resolution,
- improved credibility.

---

## Adoption Anti-Patterns

The following patterns conflict with CVS design principles:

- inline enforcement logic within the sidecar,
- mandatory settlement before execution,
- full log export pipelines,
- unconditional disclosure defaults,
- claims of correctness or truth guarantees.

These patterns alter architectural intent and are non-conformant.

---

## Exit and Reversibility

At all phases:

- sidecar removal must not affect execution,
- evidence generation may be stopped at any time,
- settlement may be paused or discontinued,
- gaps remain observable.

Exit is always preserved.

---

## Scope Limitation

This document does not:

- guarantee regulatory approval,
- guarantee evidentiary admissibility,
- replace legal counsel,
- mandate institutional change.

Adoption decisions remain organizational choices.

---

## Summary

Adoption is a gradient, not a switch.

Organizations adopt independent witnesses when it creates value —
and discontinue when it does not.

CVS is designed to preserve that freedom.
