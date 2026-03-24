# Disclosure Kernel Clarification

This document defines what the Disclosure Kernel is and is not.

It exists because the Disclosure Kernel is the most frequently
misinterpreted component of the CVS architecture. The misinterpretation
follows a consistent pattern: disclosure is treated as access control.
It is not.

---

## What the Disclosure Kernel Is

The Disclosure Kernel is a **proof minimisation mechanism**.

Its function is to enable a party to prove a specific claim about
execution without exposing the full evidence record.

It answers the question:
> "How much must be revealed to prove exactly this claim — and nothing more?"

The answer is always the minimum required for cryptographic verification
of that specific claim.

---

## What the Disclosure Kernel Is Not

The Disclosure Kernel is not:

- an access control system
- a permissions layer
- a role-based access control (RBAC) implementation
- an identity and access management (IAM) component
- a data filtering mechanism
- a privacy dashboard

These are valid systems. They solve real problems.
They are not CVS components.

An implementation that builds the Disclosure Kernel as an access control
layer has misunderstood the architecture at a fundamental level.
It is not CVS-Conforming regardless of what it is named.

---

## The Distinction in Practice

| Access Control | Disclosure Kernel |
|---|---|
| Grants or denies access to data | Proves a claim without exposing data |
| Operates on permissions | Operates on cryptographic proofs |
| Requires identity context | Requires only the claim to be proved |
| Output: allowed / denied | Output: proof / no proof |
| Controls who sees what | Controls what must be shown to prove what |
| Centralised authority model | Verifiable without trusted authority |

These are different problems. The Disclosure Kernel solves the right one.

---

## Valid Disclosure Kernel Behaviors

A CVS-Conforming Disclosure Kernel implementation MUST support:

### Selective Field Disclosure

Revealing a subset of fields from a Proof Object while proving the
unrevealed fields exist and are unmodified.

This is achieved through Merkle inclusion proofs, not field filtering.

### Claim Verification Without Full Exposure

A verifier MUST be able to confirm:
- a specific constraint was satisfied
- a specific action was within the declared boundary
- a specific event occurred at a specific time

Without receiving the complete Proof Object.

### Scoped Queries

A query against the evidence record MUST be answerable with
the minimum evidence required to answer it — not the full record.

### Multi-Party Disclosure

Different parties MAY receive different scoped proofs from the
same underlying evidence record.

This is not access control. Each party receives a cryptographic
proof of their specific claim. No party has privileged access to
the underlying record by virtue of their role.

---

## Prohibited Implementations

The following implementations are non-conformant:

- Disclosure controlled by user roles or permissions
- Evidence records gated behind authentication requirements
- Verification requiring operator approval or cooperation
- Disclosure scope defined by organisational hierarchy
- Any implementation where "who you are" determines "what you can verify"

In a CVS-Conforming implementation, verification is public and
permissionless. What varies is the scope of the claim being proved,
not the identity of the verifier.

---

## The Multi-Agency Disclosure Pattern

A common requirement in regulated environments is multi-agency
disclosure — the ability for multiple regulatory bodies to verify
claims about the same execution record without sharing full records
with each other.

CVS handles this correctly by design:

- Each agency receives a scoped Merkle proof for their specific claim
- No agency receives the full record
- No agency can determine what other agencies verified
- The underlying Evidence Object is never exposed
- Verification by one agency does not require cooperation from another

This is not a permissions model. It is a proof model.
Each agency proves their claim independently.

---

## Relationship to Other Documents

- `MINIMAL_REVELATION.md` — defines the principle underlying scoped disclosure
- `QUERY_SCOPING.md` — defines how queries are bounded
- `ADVERSARIAL_CASES.md` — covers coercive over-disclosure attacks
- `ANTI_DRIFT.md` — classifies access-control disclosure as non-conformant
- `CONFORMANCE.md` — tests 4.1 and 4.2 govern disclosure conformance

The canonical CVS specification (`CVS_ARCHITECTURE_v2.7.md`) governs
where any conflict exists.
