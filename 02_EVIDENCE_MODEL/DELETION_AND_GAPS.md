# Deletion and Gaps

This document defines how deletion, interruption, and absence are represented
within the Cryptographic Verification Sidecar (CVS) specification.

The canonical CVS specification is defined by:

- `CVS_ARCHITECTURE_v2.7.md`
- `CVS_IMPLEMENTATION_v2.2.md`

If conflict exists, the canonical specification governs.

This document is normative.

The ability to detect absence is as important as the ability to record presence.

---

## Principle of Detectable Absence

CVS MUST treat deletion and interruption as first-class conditions.

An independent verifier MUST be able to determine whether:

- evidence once existed and was removed,
- evidence should have existed but does not,
- evidence production was interrupted.

Silent deletion is non-conformant.

---

## No Silent Deletion

Evidence Objects MUST NOT be:

- removed without trace,
- overwritten without detection,
- truncated without observable consequence.

Any modification to stored evidence MUST itself generate a new
Evidence Object representing that action.

---

## Immutable Chains and Deletion

Once an Evidence Object has been chained:

- it MUST NOT be deleted from the logical record,
- even if physical storage is reclaimed.

If physical deletion is required (e.g., retention expiry):

- the deletion MUST be represented as evidence,
- the hash chain MUST remain intact,
- the deletion event MUST be observable.

Logical continuity is preserved even if storage changes.

---

## Gap Representation

Gaps in evidence MAY occur due to:

- sidecar failure,
- network partition,
- power loss,
- operator intervention,
- intentional disengagement.

When a gap occurs:

- it MUST be explicitly represented,
- its duration SHOULD be bounded where possible,
- normal operation MUST resume with a clear boundary.

Gaps MUST NOT be silently repaired.

---

## Gap Markers

Implementations MAY use explicit gap markers to indicate:

- start of interruption,
- end of interruption,
- known cause (if available).

Gap markers MUST be chained like all other Evidence Objects.

---

## Distinguishing Absence Types

Where technically feasible, evidence SHOULD distinguish between:

- observed absence (sidecar operational, no events),
- unobserved absence (sidecar unavailable),
- intentional disengagement,
- storage loss.

Clear categorization improves interpretability.

---

## Retention and Pruning

Retention policies MAY require evidence pruning.

When pruning occurs:

- the act of pruning MUST be recorded,
- the chain MUST remain verifiable,
- historical anchors MUST remain intact.

Retention policies MUST NOT alter historical integrity.

---

## Scope Limitation

Deletion and gap representation:

- do not prove intent,
- do not establish causation,
- do not guarantee legal sufficiency.

They preserve structural transparency only.

---

## Summary

Deletion without trace collapses integrity.

CVS ensures that:

- absence is detectable,
- interruption is visible,
- modification leaves evidence.

A visible gap is acceptable.  
An invisible deletion is not.
