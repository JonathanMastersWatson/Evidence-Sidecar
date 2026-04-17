# CHANGELOG

## Purpose
This file records **structural and documentary changes** to the
Evidence-Sidecar (CVS) repository.
It exists to:
- preserve historical integrity
- prevent silent revisionism
- allow reviewers to track evolution

---

## [2026-04-17] — GAP Attribution Hardening Pass

### Objective
Correct an instance where GAP was listed as a Commit Gate output
in the layer separation section of ANTI_DRIFT.md.

512 is binary. The gate produces exactly two outputs: ALLOW or DENY.
GAP is a CVS witness layer classification applied to ungoverned
periods in the evidence chain. It is not a gate output under any
operational state.

### Files Modified
- `ANTI_DRIFT.md`

### Change
- §1.1 Commit Gate (Enforcement Layer):
  "Produces binary output only: allow / deny / gap"
  → "Produces binary output only: ALLOW or DENY"

### Correct Separation Established
- 512 produces: ALLOW or DENY
- CVS records: the ALLOW or DENY result from 512, AND classifies
  any ungoverned execution periods as evidence chain gaps

### Notes
All other sections in ANTI_DRIFT.md were correctly scoped and
are unchanged. This pass was coordinated with a parallel hardening
pass across six files in the 512-main repository.

---

## Change Policy
- Substantive changes require a new dated entry
- Clarifications may be added but original text is not
  retroactively altered
- Historical architecture documents are immutable

---

## Versioning Note
This repository does not follow semantic versioning.
Changes are historical, not product-based.
