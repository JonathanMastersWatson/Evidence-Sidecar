# Ledger Unavailable

This document defines system behavior when the settlement ledger is unavailable, degraded, or unreachable.

Ledger unavailability must not compromise evidence generation or system execution.

---

## Purpose

The purpose of this document is to ensure that:

- settlement failures do not interrupt evidence production,
- ledger dependency does not become an execution dependency,
- and evidence integrity remains intact during outages.

Settlement is downstream of observation.

---

## Definition of Ledger Unavailability

Ledger unavailability includes:

- network partitions,
- validator outages,
- transaction submission failures,
- confirmation delays beyond defined bounds,
- or external connectivity loss.

Unavailability may be partial or intermittent.

---

## Separation of Evidence and Settlement

Evidence generation must be fully independent of ledger availability.

When the ledger is unavailable:

- Evidence Objects continue to be created,
- hash chains continue uninterrupted,
- and local persistence must be maintained.

Settlement is deferred, not skipped.

---

## Deferred Settlement

Deferred settlement must:

- preserve original observation times,
- maintain chain integrity,
- and record the duration of settlement delay.

Deferred settlement must never rewrite history.

---

## Observable Delay

Ledger unavailability must be observable through:

- delayed receipts,
- explicit settlement gap markers,
- or recorded retry attempts.

Silence is prohibited.

---

## No Synthetic Anchoring

When the ledger is unavailable:

- synthetic receipts must not be generated,
- timestamps must not be fabricated,
- and alternative anchoring must not be implied.

Honest delay is preferable to false certainty.

---

## Recovery and Resumption

When ledger access is restored:

- settlement resumes for queued batches,
- original batch ordering is preserved,
- and settlement timestamps reflect actual confirmation time.

Backdating is prohibited.

---

## Verification Implications

Independent verifiers must be able to:

- detect periods of deferred settlement,
- distinguish observation time from settlement time,
- and validate that no evidence was altered during delay.

---

## Legal Interpretation

Ledger unavailability does not invalidate evidence.

It may affect:
- freshness of public anchoring,
- but not internal integrity.

Disclosure of delay is essential for defensibility.

---

## Summary

The ledger is a notary, not a dependency.

When the notary is closed, events still occur.

Evidence waits. Reality does not.
