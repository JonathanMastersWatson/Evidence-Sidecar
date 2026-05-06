# Failure and Gap Semantics

## Purpose

This document defines witness-layer gap behavior.

A gap is evidence about degradation in the witness path.

A gap is not a gate decision.

GAP is never a valid 512 output token.

---

## Core Rule

The witness layer fails open relative to execution.

CVS may record that evidence production degraded, but it must not halt, block, reverse, or alter execution.

---

## Gap Examples

Witness-layer gaps include:

- witness unavailable
- delayed anchoring
- storage outage
- hash mismatch
- runtime crash during evidence emission
- chain continuity break
- Merkle batch delay
- anchor service unavailable
- local queue saturation

---

## Required Gap Behavior

When the witness detects a gap, it must:

- record the gap condition
- preserve available continuity metadata
- emit recovery evidence when possible
- avoid silent discard of evidence state
- avoid reinterpretation of execution meaning

---

## Prohibited Gap Behavior

The witness must not:

- halt execution
- convert execution to DENY
- request gate reevaluation
- mutate prior evidence objects
- hide or overwrite gap state
- silently discard pending evidence
- claim unavailable evidence was successfully anchored

---

## Gap Field Rules

When `gap_detected` is `false`:

```json
{
  "gap_detected": false,
  "gap_reason": null,
  "gap_start": null,
  "gap_end": null
}
```

When `gap_detected` is `true`:

```json
{
  "gap_detected": true,
  "gap_reason": "ANCHOR_DELAYED",
  "gap_start": "timestamp",
  "gap_end": null
}
```

`gap_end` may remain `null` while the gap is unresolved.

---

## Recovery Rule

If the witness recovers from a gap, it should emit a recovery Evidence Object or recovery manifest that identifies:

- prior known evidence hash
- first evidence hash after recovery
- gap reason
- gap start
- gap end
- recovered batch ids, if applicable

Recovery metadata must not rewrite earlier Evidence Objects.

---

## Chain Break Rule

If `previous_evidence_hash` cannot be linked to the prior evidence object, the witness must flag a continuity gap.

The next Evidence Object may continue from the last known valid hash or explicitly start a new chain segment.

The chain segment boundary must be visible to validators.

---

## Anchoring Delay Rule

Delayed anchoring is not evidence failure by itself.

It becomes a gap when the witness runtime or profile declares the delay beyond acceptable operational bounds.

Anchor delay must not modify execution semantics.
