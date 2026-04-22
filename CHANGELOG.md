# CHANGELOG
## Purpose
This file records **structural and documentary changes** to the
Evidence-Sidecar (CVS) repository.
It exists to:
- preserve historical integrity
- prevent silent revisionism
- allow reviewers to track evolution
---
## [2026-04-22] — Proof Object Terminology and Conformance Hardening Pass

### Objective
Two issues identified and corrected in this pass, coordinated with
a parallel hardening pass in the 512-main repository.

**Issue 1 — Ambiguous "gap" term in PROOF_OBJECT_INTEGRITY.md.**
Element 3 (Decision Record) described per-constraint results as
"satisfied / not satisfied / gap". The word "gap" at the
per-constraint level conflated two distinct concepts: a
per-constraint unevaluated state (a specific constraint could not
be evaluated because a required input was unavailable) and a
witness layer evidence chain gap (the gate itself was unavailable
and no evaluation occurred at all). These are structurally different
conditions and must not share a term.

**Issue 2 — Version-specific canon references in CONFORMANCE.md.**
The canonical specification was referenced by specific version
strings (CVS_ARCHITECTURE_v2.7.md, CVS_IMPLEMENTATION_v2.2.md).
As canon documents evolve, this required CONFORMANCE.md to be
updated on every version bump. Replaced with a version-agnostic
reference to the 08_CANON/ directory, which always contains the
current canonical versions.

Additionally, conformance test 2.1 (Event completeness) did not
account for fail-open events, where the validation-result
observation point is absent and a gap_record replaces it. The
test pass/fail conditions were updated to correctly distinguish
evaluated events from fail-open events.

### Files Modified
- `02_EVIDENCE_MODEL/PROOF_OBJECT_INTEGRITY.md`
- `CONFORMANCE.md`

### Changes Applied

**PROOF_OBJECT_INTEGRITY.md:**
- Element 3 Decision Record: "gap" replaced with "unevaluated"
- Clarifying note added distinguishing per-constraint unevaluated
  state from witness layer gap records

**CONFORMANCE.md:**
- Canon document references de-versioned: specific version strings
  replaced with version-agnostic reference to 08_CANON/ directory
- Checklist test 2.1: pass condition qualified for fail-open events
  (pre-validation and gap_record emitted; validation-result absent
  and not required)
- Checklist test 5.1: pass condition updated from "gap is recorded"
  to "gap record emitted to witness layer" for precision

### Correct Distinction Established

| Term | Meaning |
|---|---|
| Per-constraint unevaluated | Gate was functioning; specific constraint could not be evaluated due to missing input |
| Witness layer gap record | Gate was unavailable; no evaluation occurred; ungoverned period recorded by CVS |

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
