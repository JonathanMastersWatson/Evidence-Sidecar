# Deletion and Gaps

This document defines how deletion, interruption, and absence are represented within the evidence sidecar architecture.

The ability to **detect absence** is as important as the ability to record presence.

---

## Principle of Detectable Absence

Evidence systems must treat deletion and interruption as first-class conditions.

It must be possible for an independent verifier to determine that:

- evidence once existed and was removed,
- evidence should have existed but does not,
- or evidence production was interrupted.

Silent deletion is prohibited.

---

## No Silent Deletion

Evidence Objects must not be:

- removed without trace,
- overwritten without detection,
- or truncated without observable consequence.

Any modification to stored evidence must itself generate evidence.

---

## Immutable Chains and Deletion

Once an Evidence Object has been chained:

- it must not be deleted from the logical record,
- even if physical storage is reclaimed.

If physical deletion is required (e.g. retention expiry):
- the deletion must be recorded,
- the hash chain must remain intact,
- and the deletion event must be observable.

---

## Gap Representation

Gaps in evidence may occur due to:

- sidecar failure,
- network partition,
- power loss,
- operator intervention,
- or intentional disengagement.

When a gap occurs:

- it must be explicitly represented,
- its duration must be bounded where possible,
- and normal operation must resume with a clear boundary.

Gaps must never be implicitly healed.

---

## Gap Markers

Implementations may use explicit gap markers to indicate:

- start of interruption,
- end of interruption,
- reason for interruption (if known).

Gap markers must be chained like all other Evidence Objects.

---

## Distinguishing Absence Types

Where possible, evidence should distinguish between:

- **observed absence** (sidecar operational, no events),
- **unobserved absence** (sidecar unavailable),
- **intentional disengagement**,
- **storage loss**.

Such distinctions improve forensic clarity.

---

## Retention and Pruning

Retention policies may require evidence to be pruned.

When pruning occurs:

- the act of pruning must be recorded,
- the chain must remain verifiable,
- and historical anchors must remain intact.

Retention must not erase accountability.

---

## Legal Implications

From a legal and regulatory perspective:

- detectable gaps weaken evidence credibility less than silent deletion,
- explicit absence supports honest testimony,
- and transparent loss reduces allegations of tampering.

An incomplete but honest record is stronger than a complete but falsified one.

---

## Summary

Deletion without trace is indistinguishable from fraud.

This architecture ensures that:

- absence is visible,
- loss is documented,
- and erasure cannot be hidden.

Gaps tell stories too.
