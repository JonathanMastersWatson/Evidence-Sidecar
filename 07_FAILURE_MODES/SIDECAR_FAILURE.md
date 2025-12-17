# Sidecar Failure

This document defines how the evidence sidecar behaves when it fails.

Failure is not exceptional.  
It is expected, observable, and non-catastrophic.

---

## Purpose

The purpose of this document is to ensure that:

- sidecar failure does not compromise system execution,
- failure is detectable after the fact,
- and no false continuity is implied.

An evidence system that hides its own failure is untrustworthy.

---

## Definition of Sidecar Failure

Sidecar failure includes, but is not limited to:

- process crashes,
- power loss,
- storage exhaustion,
- clock desynchronization,
- network unavailability,
- key access failure,
- or internal logic errors.

Failure may be partial or total.

---

## Fail-Open Enforcement

Upon sidecar failure:

- the observed system must continue operating,
- no execution path may be blocked,
- no output may be delayed or altered.

The sidecar has no authority to fail closed.

---

## Failure Detection

Sidecar failure must be:

- detectable by independent verification,
- surfaced as evidence gaps,
- and not silently healed.

Absence must be visible.

---

## Gap Creation

When the sidecar is unavailable:

- evidence gaps must be created,
- gap boundaries must be clear,
- and resumption must be explicit.

Implicit continuity is prohibited.

---

## Recovery Behavior

Upon recovery:

- a new Evidence Object must mark resumption,
- recovery time must be recorded,
- and chain continuity must reflect interruption.

Recovery does not retroactively repair gaps.

---

## Failure Attribution

Where possible, failure may be attributed to:

- sidecar instance failure,
- environmental causes,
- or external dependency loss.

Attribution must be descriptive, not interpretive.

---

## No Backfilling

Evidence must not be backfilled after failure.

Synthetic reconstruction of missed evidence is prohibited.

Historical honesty is preserved by admitting absence.

---

## Settlement During Failure

If settlement is unavailable during sidecar failure:

- local evidence chains must persist,
- settlement may be deferred,
- and delay must be observable.

Failure of settlement must not cascade.

---

## Legal and Audit Implications

Explicitly recorded failures:

- strengthen credibility,
- reduce accusations of concealment,
- and support honest testimony.

Silence creates suspicion.

---

## Summary

A failing witness that admits failure is credible.

A witness that pretends continuity is not.
