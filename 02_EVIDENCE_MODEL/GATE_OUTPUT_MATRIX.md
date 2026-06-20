# Gate Output Matrix

This document defines the complete set of gate completion states
and the corresponding witness layer classifications.

It exists to eliminate semantic slippage between:

- gate outputs (ALLOW or DENY — produced by the gate)
- evidence chain gaps (produced by the witness layer)
- per-constraint unevaluated states (per-constraint, not gate-level)

These are distinct. They must not be conflated in documentation,
implementation, or evidence records.

---

## The Core Rule

The gate produces exactly two output values:

- **ALLOW** — all seven invariants evaluated and satisfied
- **DENY** — one or more invariants evaluated and not satisfied

There is no third gate output value.

When the gate cannot complete evaluation, the infrastructure-failure
handler produces **DENY** (deny_cause: evaluation_unavailable).
The commit path remains closed. The CVS sidecar records the
unavailability period as an **evidence chain gap**. That gap record
is a CVS sidecar record — not a gate output.

---

## Matrix

| Scenario | Gate evaluation completed? | Per-constraint evaluation complete? | Gate result present in Evidence Object? | Witness layer classification |
|---|---|---|---|---|
| **Normal — ALLOW** | Yes | Yes — all seven pass | Yes — ALLOW | Validation Result event emitted; Evidence Object contains ALLOW, spec hash, per-invariant pass results |
| **Normal — DENY** | Yes | Yes — one or more fail | Yes — DENY | Validation Result event emitted; Evidence Object contains DENY, spec hash, per-invariant results, violated constraint detail |
| **Evaluation-Unavailable DENY — gate unavailable** | No | No — evaluation did not begin or complete | Yes — DENY (evaluation_unavailable) | DENY Evidence Object emitted with failure cause and retry path; CVS sidecar emits gap record; commit path remains closed; execution does not proceed |
| **Per-constraint unevaluated** | Yes (partial) | No — one or more constraints could not be evaluated due to missing input | Yes — DENY (or no overall result if gate cannot resolve) | Validation Result event emitted with unevaluated indicators per affected constraint; see §Per-Constraint Unevaluated below |
| **Sidecar unavailable** | Gate state independent | Gate state independent | Gate result may exist locally | Witness layer gap in evidence chain; Evidence Objects queued locally; gap resolved on sidecar recovery |

---

## Scenario Detail

### Normal — ALLOW

All seven invariants evaluated. All seven pass.

Gate emits: ALLOW  
Witness emits: Validation Result (Observation Point 2) containing:
- `overall_result`: ALLOW
- `spec_hash`: hash of active compiled constraint set
- `per_invariant_results`: pass for each of I1–I7
- `evaluation_duration_us`: gate evaluation time

Evidence Object contains all three observation points linked by
`correlation_id`. No gap record is produced.

---

### Normal — DENY

All seven invariants evaluated. One or more fail.

Gate emits: DENY  
Witness emits: Validation Result (Observation Point 2) containing:
- `overall_result`: DENY
- `spec_hash`: hash of active compiled constraint set
- `per_invariant_results`: pass or fail per invariant
- `violated_constraint_detail`: the specific invariant(s) and
  condition(s) that failed
- `evaluation_duration_us`: gate evaluation time

A DENY is not a lesser event. It is evidence that the constraint
enforced correctly. DENY records are anchored with the same
integrity guarantees as ALLOW records.

Execution does not proceed. Commit path remains closed.

---

### Evaluation-Unavailable DENY — Gate Unavailable

The gate is unavailable or evaluation timed out. Evaluation did
not complete. The infrastructure-failure handler produces DENY
(deny_cause: evaluation_unavailable). The commit path remains
closed. Execution does not proceed.

Gate emits: DENY (deny_cause: evaluation_unavailable)  
Infrastructure-failure handler emits: DENY Evidence Object to witness layer  
CVS sidecar emits: gap record containing:
- `gap_start`: timestamp when gate became unavailable
- `gap_end`: timestamp when gate recovered
- `gap_duration_seconds`: duration of unavailability period
- `gap_reason`: gate unavailable / evaluation timeout / other
- `gate_output_during_gap`: deny_evaluation_unavailable
- `spec_hash`: hash of constraint set that would have been evaluated

**A gap record is not an ALLOW.** Constraint satisfaction was not
established. The commit boundary held — execution did not proceed.

The DENY Evidence Object contains:
- `overall_result`: DENY
- `deny_cause`: evaluation_unavailable
- `failure_cause`: gate unavailable / evaluation timeout / other
- `retry_permitted`: true
- `spec_hash`: hash of active compiled constraint set

Validation Result (Observation Point 2) is present for this event
and contains the Evaluation-Unavailable DENY. The gap record is
a supplementary CVS sidecar record documenting the unavailability
period.

See `512-core/KERNEL/I6_CONSTITUTIONAL_ELABORATION.md` for the
authoritative elaboration of the Evaluation-Unavailable DENY doctrine.
---

### Per-Constraint Unevaluated

The gate was functioning. Evaluation began. One or more specific
constraints could not be evaluated because a required input was
unavailable during context binding.

This is distinct from fail-open. The gate did not fail. A specific
constraint input was missing.

Gate behaviour: depends on `failure_mode_on_missing_input` declared
in the compiled constraint:
- If `DENY`: gate produces DENY; the unevaluated constraint is
  recorded as the violated constraint
- If `UNEVALUATED`: constraint is recorded as unevaluated; overall
  result depends on whether remaining constraints produced ALLOW

Witness emits: Validation Result containing unevaluated indicators
per affected constraint.

**An unevaluated constraint is never treated as pass or allow.**
A missing input is not consent. A missing input is not satisfaction.

This state must not be confused with an evidence chain gap:

| | Per-constraint unevaluated | Evidence chain gap |
|---|---|---|
| Gate functioning? | Yes | No |
| Evaluation attempted? | Yes | No |
| Gate result present? | Yes (DENY or partial) | No |
| Caused by | Missing constraint input | Gate unavailability |
| Witness record | Validation Result with unevaluated indicators | Gap record |

---

### Sidecar Unavailable

The gate may be functioning. The CVS sidecar is unavailable.

Gate behaviour: unaffected — the gate is structurally independent
of the sidecar. ALLOW or DENY is produced normally.

Witness behaviour: Evidence Objects are queued locally by the
fail-open handler. When the sidecar recovers, queued objects are
forwarded and the gap in the evidence chain is resolved.

If local queuing also fails: an evidence chain gap is recorded
for the period of total unavailability.

Execution is never blocked by sidecar unavailability.

---

## Critical Semantic Rules

These rules apply across all implementations. They are not
configuration options.

**Rule 1 — Unevaluated is never pass.**
A per-constraint unevaluated result does not satisfy the
constraint. It does not contribute to an ALLOW. Any system that
treats an unevaluated constraint as satisfied has broken the
binary model.

**Rule 2 — Gap record is not a gate output.**
An evidence chain gap record is produced by the witness layer,
not the gate. It records that evaluation did not occur. It is not
ALLOW. It is not DENY. It has no gate-output semantics.

**Rule 3 — Gap record and unevaluated are distinct.**
Do not conflate per-constraint unevaluated state with an overall
evidence chain gap. One occurs within a functioning evaluation
pass. The other records that no evaluation occurred.

**Rule 4 — ALLOW requires all seven.**
An ALLOW result is only valid when all seven invariants were
evaluated and all seven passed. An ALLOW with any unevaluated
constraint is a non-conformant result.

**Rule 5 — Gap records confirm the commit boundary held.**
Under the Evaluation-Unavailable DENY doctrine, execution does
not proceed during gate unavailability. The gap record documents
the unavailability period and confirms that DENY was produced
and the commit path remained closed — not that execution occurred
without evaluation.

---

## Relationship to Other Documents

- `ANTI_DRIFT.md §1.1` — gate output model and fail-open
  behaviour defined
- `ANTI_DRIFT.md §2.1` — observation point model and fail-open
  observation path
- `02_EVIDENCE_MODEL/PROOF_OBJECT_INTEGRITY.md` — Element 3
  (Decision Record) and per-constraint unevaluated semantics
- `CONFORMANCE.md` test 2.1 — event completeness requirements
  for evaluated and fail-open events
- `512-main/512-ops/COMMIT_BOUNDARY_REFERENCE.md §4` — gate
  binary output model from the enforcement layer perspective
- `512-main/LAYER_REFERENCE.md` — what each layer produces and
  must not claim
