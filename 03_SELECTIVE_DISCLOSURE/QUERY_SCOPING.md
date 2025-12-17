# Query Scoping

This document defines how disclosure queries are scoped, bounded, and constrained within the evidence sidecar architecture.

Query scoping ensures that disclosure remains precise, proportional, and non-invasive.

---

## Purpose

Query scoping exists to:

- prevent over-disclosure,
- limit evidence exposure to relevant material,
- and protect systems from exploratory or abusive inquiries.

Disclosure without scope is indistinguishable from surveillance.

---

## Scope as a First-Class Constraint

Every disclosure request must be explicitly scoped.

A request without scope must not be fulfilled.

Scope defines:
- what evidence is eligible for disclosure,
- what evidence is excluded,
- and the boundaries of interpretation.

---

## Required Scope Dimensions

A valid disclosure query must specify, at minimum:

### 1. Temporal Scope

The time window to which the request applies.

Temporal scope must:
- define clear start and end bounds,
- align with recorded observation time,
- and include any gaps within that interval.

Open-ended temporal queries are prohibited.

---

### 2. Evidence Path Scope

The specific evidence chain, stream, or source under inquiry.

This may include:
- a system identifier,
- a channel or process identifier,
- or a sidecar instance reference.

Global or system-wide queries are disallowed by default.

---

### 3. Evidence Type Scope

The classes of Evidence Objects to be disclosed.

This may include:
- specific event types,
- segment-level evidence,
- or attestation records.

Unbounded evidence-type queries are prohibited.

---

## Optional Scope Dimensions

Additional scope constraints may include:

- sidecar instance identifiers,
- specific hash prefixes,
- settlement anchor references,
- or known gap markers.

Optional constraints further reduce disclosure surface area.

---

## Excluded Scope

Queries must explicitly exclude:

- unrelated systems,
- unrelated time windows,
- unrelated evidence classes,
- and non-relevant metadata.

Exclusion is as important as inclusion.

---

## Rejection of Overbroad Queries

The Disclosure Kernel must reject queries that are:

- vague,
- unbounded,
- exploratory,
- or disproportionate to the stated purpose.

Rejection is a valid and expected outcome.

---

## Scope Validation

Before disclosure, the system must:

- validate scope completeness,
- confirm scope feasibility,
- and record the scope parameters.

Invalid or incomplete scopes must not be silently corrected.

---

## Scope Transparency

Disclosed evidence must include:

- the exact scope definition used,
- confirmation that no additional evidence was considered,
- and disclosure of any scope limitations.

This allows recipients to assess completeness.

---

## Abuse Resistance

Query scoping serves as a defense against:

- fishing expeditions,
- mass extraction attempts,
- and coercive discovery tactics.

The architecture prioritizes proportionality over convenience.

---

## Summary

Query scoping ensures that disclosure answers the question asked — and nothing else.

Precision protects both transparency and autonomy.
