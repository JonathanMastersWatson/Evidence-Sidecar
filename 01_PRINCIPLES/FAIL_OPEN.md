# Fail-Open Principle

The evidence sidecar defined in this repository **must be fail-open**.

Fail-open behavior is a foundational, non-negotiable constraint.  
Any architecture that violates this principle is non-compliant with this work.

---

## Definition

A system is **fail-open** if, upon failure of the evidence sidecar:

- the observed system continues operating normally,
- no execution path is blocked,
- no output is delayed or altered,
- and no authority is transferred to the sidecar.

The absence of evidence is observable.  
The absence of execution is not permitted.

---

## Rationale

High-availability systems prioritize liveness above all else.

Broadcast facilities, financial exchanges, healthcare systems, AI inference engines, and public infrastructure cannot tolerate interruptions caused by auxiliary systems, regardless of intent.

Evidence systems that interfere with execution are:

- operationally rejected by engineers,
- legally risky,
- and economically indefensible.

Fail-open is therefore not a preference.  
It is a requirement for adoption.

---

## Evidence vs Execution

This architecture draws a strict boundary between:

- **execution paths**, which produce outcomes, and
- **evidence paths**, which record what occurred.

The sidecar must exist exclusively on the evidence path.

At no point may the sidecar:

- gate execution,
- authorize actions,
- or enforce compliance.

Any design that merges execution and evidence invalidates the witness function.

---

## Failure Modes

Fail-open behavior must hold under all failure conditions, including:

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
- and evidence gaps remain detectable after the fact.

---

## Observable Absence

Fail-open does not imply silent failure.

When the sidecar is unavailable, this absence must itself be observable through:

- missing hash segments,
- discontinuities in time ordering,
- or explicit gap markers.

An unobservable failure is a defect.  
A visible gap is acceptable.

---

## Legal and Regulatory Implications

From a legal perspective, fail-open behavior ensures that:

- the sidecar cannot be accused of causation,
- outages cannot be attributed to compliance tooling,
- and evidence gaps are explainable rather than hidden.

From a regulatory perspective, fail-open designs demonstrate proportionality:
the system prioritizes continuity while still producing auditable artifacts.

---

## Engineering Implications

To satisfy fail-open requirements:

- evidence generation must be asynchronous,
- settlement must be decoupled from execution,
- storage must tolerate partial failure,
- and no inline dependencies may exist.

Architectures relying on synchronous verification or mandatory signing before execution are explicitly disallowed.

---

## Prohibited Patterns

The following patterns violate the fail-open principle and are prohibited:

- inline cryptographic signing
- synchronous ledger writes
- mandatory proof-of-validity before execution
- compliance gates that block output
- control-plane dependencies on evidence services

Such designs transform witnesses into authorities.

---

## Summary

Fail-open behavior ensures that:

- systems remain live under all conditions,
- evidence production never becomes a point of failure,
- and trust is earned through resilience, not control.

A witness that can stop a system is no longer a witness.

Fail-open is not optional.
