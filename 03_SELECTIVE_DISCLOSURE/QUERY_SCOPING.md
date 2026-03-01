# Query Scoping

This document defines how disclosure queries are scoped, bounded, and constrained
within the Cryptographic Verification Sidecar (CVS) specification.

The canonical CVS specification is defined by:

- `CVS_ARCHITECTURE_v2.7.md`
- `CVS_IMPLEMENTATION_v2.2.md`

If conflict exists, the canonical specification governs.

This document is normative.

Query scoping ensures that disclosure remains precise, proportional,
and structurally bounded.

---

## Purpose

Query scoping exists to:

- prevent over-disclosure,
- limit evidence exposure to relevant material,
- preserve system autonomy,
- maintain structural proportionality.

Disclosure without scope collapses the minimal revelation boundary.

---

## Scope as a First-Class Constraint

Every disclosure request MUST be explicitly scoped.

A request lacking scope MUST NOT be fulfilled.

Scope defines:

- which evidence is eligible for disclosure,
- which evidence is excluded,
- the boundaries of structural extraction.

Scope governs eligibility, not interpretation.

---

## Required Scope Dimensions

A valid disclosure query MUST specify, at minimum:

### 1. Temporal Scope

The time window to which the request applies.

Temporal scope MUST:

- define explicit start and end bounds,
- align with recorded observation time,
- include any gaps within that interval.

Open-ended temporal queries are non-conformant.

---

### 2. Evidence Path Scope

The specific evidence chain, stream, or source under inquiry.

This MAY include:

- system identifiers,
- channel or process identifiers,
- sidecar instance references.

Unbounded global queries SHOULD be rejected unless explicitly justified
and structurally permitted.

---

### 3. Evidence Type Scope

The classes of Evidence Objects to be disclosed.

This MAY include:

- specific event types,
- segment-level evidence,
- attestation records.

Unbounded evidence-type queries are non-conformant.

---

## Optional Scope Dimensions

Additional scope constraints MAY include:

- sidecar instance identifiers,
- specific hash prefixes,
- settlement anchor references,
- known gap markers.

Optional constraints further narrow disclosure boundaries.

---

## Explicit Exclusion

Queries SHOULD explicitly exclude:

- unrelated systems,
- unrelated time windows,
- unrelated evidence classes,
- non-relevant metadata.

Exclusion clarifies boundaries.

---

## Rejection of Overbroad Queries

The Disclosure Kernel MUST reject queries that are:

- vague,
- unbounded,
- exploratory in structure,
- structurally disproportionate.

Rejection is a valid structural outcome.

---

## Scope Validation

Before disclosure, the system MUST:

- validate scope completeness,
- confirm structural feasibility,
- record the scope parameters as part of the disclosure event.

Invalid or incomplete scopes MUST NOT be silently expanded.

---

## Scope Transparency

Disclosed evidence SHOULD include:

- the exact scope definition applied,
- confirmation that extraction respected defined boundaries,
- any structural limitations encountered.

This enables independent assessment of completeness.

---

## Scope Limitation

Query scoping:

- does not determine authorization policy,
- does not evaluate legal proportionality,
- does not assess legitimacy of requesters.

It enforces structural extraction boundaries only.

---

## Summary

Query scoping ensures that disclosure answers the defined question —
and nothing beyond it.

Precision preserves both transparency and autonomy.
