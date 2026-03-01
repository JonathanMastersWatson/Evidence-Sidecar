# Fail-Open Principle

The Cryptographic Verification Sidecar (CVS) defined in this repository
MUST operate in fail-open mode.

Fail-open behavior is a foundational, non-negotiable architectural constraint.

The canonical CVS specification is defined by:

- `CVS_ARCHITECTURE_v2.7.md`
- `CVS_IMPLEMENTATION_v2.2.md`

If conflict exists, the canonical specification governs.

---

## Definition

A system is fail-open if, upon failure of the CVS:

- the observed system continues operating normally,
- no execution path is blocked,
- no output is delayed or altered,
- no authority is transferred to the sidecar.

The absence of evidence is observable.  
The absence of execution is not permitted.

---

## Rationale

High-availability systems prioritize liveness.

Broadcast facilities, financial exchanges, healthcare systems, AI inference engines,
and public infrastructure cannot tolerate interruptions caused by auxiliary systems.

Evidence systems that interfere with execution are:

- operationally rejected,
- architecturally unstable,
- economically indefensible.

Fail-open is a prerequisite for adoption.

---

## Evidence vs Execution Boundary

CVS draws a strict boundary between:

- execution paths (which produce outcomes), and
- evidence paths (which record what occurred).

The sidecar exists exclusively on the evidence path.

At no point may the sidecar:

- gate execution,
- authorize actions,
- enforce policy,
- condition output on verification.

Any design that merges execution and evidence collapses the witness boundary
and is non-conformant.

---

## Failure Modes

Fail-open behavior MUST hold under failure conditions including:

- power loss
- network partition
- ledger unavailability
- software crash
- clock desynchronization
- key rotation failure
- resource exhaustion

In all cases:

- execution continues,
- failures are recorded when possible,
- evidence gaps remain detectable.

---

## Observable Absence

Fail-open does not imply silent failure.

When the sidecar is unavailable, the absence MUST be observable through:

- missing hash segments,
- discontinuities in time ordering,
- explicit gap markers.

An unobservable failure is a defect.  
A visible gap is acceptable.

---

## Engineering Implications

To satisfy fail-open requirements:

- evidence generation MUST be asynchronous,
- settlement MUST be decoupled from execution,
- storage MUST tolerate partial failure,
- no inline execution dependencies may exist.

Architectures relying on synchronous verification or mandatory settlement
before execution are non-conformant.

---

## Non-Conformant Patterns

The following architectural patterns violate the fail-open constraint:

- inline cryptographic signing within execution flow,
- synchronous ledger writes required for output,
- mandatory proof-of-validity before execution,
- compliance gates embedded in execution paths,
- control-plane dependencies on evidence services.

Such designs transform witnesses into authorities.

---

## Scope Limitation

Fail-open is an architectural constraint.

It does not:

- guarantee uptime,
- prevent outages,
- determine legal liability,
- ensure regulatory approval.

It preserves separation between execution and witness.

---

## Summary

Fail-open ensures:

- systems remain live under failure,
- evidence production never becomes a blocking dependency,
- authority remains bounded.

A witness that can stop a system is no longer a witness.

Fail-open is not optional.
