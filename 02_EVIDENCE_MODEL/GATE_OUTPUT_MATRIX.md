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

When the gate cannot complete evaluation, it produces **no output**.
The witness layer records the resulting ungoverned period as an
**evidence chain gap**. That gap record is a witness layer
classification — not a gate output.

---

## Matrix

| Scenario | Gate evaluation completed? | Per-constraint evaluation complete? | Gate result present in Evidence Object? | Witness layer classification |
|---|---|---|---|---|
| **Normal — ALLOW** | Yes | Yes — all seven pass | Yes — ALLOW | Validation Result event emitted; Evidence Object contains ALLOW, spec hash, per-invariant pass results |
| **Normal — DENY** | Yes | Yes — one or more fail | Yes — DENY | Validation Result event emitted; Evidence Object contains DENY, spec hash, per-invariant results, violated constraint detail |
| **Fail-open — gate unavailable** | No | No — evaluation did not begin or complete | No — gate produced no output | Evidence chain gap record emitted; gap duration, reason, and executing identity recorded; execution proceeded under Invariant 6 |
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

### Fail-Open — Gate Unavailable

The gate is unavailable or evaluation timed out. Evaluation did
not complete. The gate produces no output.

Execution proceeds because Invariant 6 requires fail-open behaviour.
Blocking execution on gate failure would itself be an I6 violation.

Gate emits: nothing  
Fail-open handler emits: gap record to witness layer  
Witness emits: evidence chain gap record containing:
- `gap_start`: timestamp of last successfully written Evidence Object
- `gap_end`: timestamp of first successfully written Evidence Object
  after recovery
- `gap_duration_seconds`: duration of ungoverned period
- `gap_reason`: gate unavailable / evaluation timeout / other
- `executing_identity`: identity executing during gap window
- `spec_hash`: hash of constraint set that would have been evaluated

**A gap record is not an ALLOW.** Constraint satisfaction was not
established. Execution proceeded because availability is prioritised
over blocking — not because the constraints passed.

Validation Result (Observation Point 2) is absent for this event.
The gap record replaces it in the evidence chain.

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

**Rule 5 — Execution during a gap is ungoverned, not allowed.**
Execution that proceeds during a gate unavailability period is
not evidence of satisfaction. It is evidence of an ungoverned
period. The gap record proves execution occurred without
constraint evaluation — not that execution was evaluated and
permitted.

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
