# CHANGELOG
## Purpose
This file records **structural and documentary changes** to the
Evidence-Sidecar (CVS) repository.
It exists to:
- preserve historical integrity
- prevent silent revisionism
- allow reviewers to track evolution
---
## [2026-04-23] — Vocabulary Lock, Layer Reference, and Gate Output Matrix Pass

### Objective
CVS-side pass coordinated with the 512-main vocabulary lock and
schema hardening pass. Three issues addressed: prescribed vocabulary
not present in ANTI_DRIFT.md; version-specific canon references in
README.md; missing explicit gate output / witness classification
matrix.

### New Files
- `02_EVIDENCE_MODEL/GATE_OUTPUT_MATRIX.md`

### Files Modified
- `ANTI_DRIFT.md`
- `README.md`

### Changes Applied

**ANTI_DRIFT.md:**
- §1 Layer Separation: introductory paragraph added referencing
  512-main/LAYER_REFERENCE.md as the authoritative three-layer
  definition
- §1.1 Commit Gate: "exclusive commit authority" and
  "non-bypassable commit path" introduced as canonical terms;
  fail-open behaviour described: gate produces no output when
  evaluation cannot complete; witness layer records the ungoverned
  period as an evidence chain gap
- §1.2 Witness Layer: bullet added: "Records ALLOW or DENY results
  from the gate, and classifies ungoverned periods as evidence
  chain gaps"
- §2.1 Valid Observation Points: fail-open observation path made
  explicit — Pre-Validation emitted; Validation Result absent on
  fail-open; gap record replaces it; Post-Execution emitted.
  Cross-reference to GATE_OUTPUT_MATRIX.md added.
- §2.2: closing sentence updated to require gap record emission
  on fail-open events
- §15: "Proof-based compliance" → "Proof-based conformance"
- Relationship to Other Documents: expanded to full related docs
  list; canon reference de-versioned to /08_CANON/ directory

**README.md:**
- Canonical Specification: version-specific filenames replaced
  with version-agnostic pattern referencing /08_CANON/ directory
- What CVS Is Not: "compliance badge" → "conformance badge"
- Reference section: UPSTREAM.md description updated; new entry
  for 02_EVIDENCE_MODEL/GATE_OUTPUT_MATRIX.md added

**02_EVIDENCE_MODEL/GATE_OUTPUT_MATRIX.md (new):**
Complete matrix of gate completion states and witness layer
classifications. Four scenarios defined:

| Scenario | Gate completed? | Gate result present? | Witness classification |
|---|---|---|---|
| Normal evaluation | Yes | ALLOW or DENY | Validation Result event |
| Fail-open | No | None | Evidence chain gap record |
| Per-constraint unevaluated | Yes (partial) | DENY | Validation Result with unevaluated indicators |
| Sidecar unavailable | — | — | Gap in evidence chain; local queue |

Critical semantic rules stated:
- per-constraint unevaluated is never treated as pass or allow
- evidence chain gap is not a gate output
- gap record and unevaluated are distinct — do not conflate
- ALLOW requires all seven constraints evaluated and passed

### Vocabulary Lock Status (CVS repo)

| Term | Documents |
|---|---|
| exclusive commit authority | ANTI_DRIFT.md §1.1 |
| non-bypassable commit path | ANTI_DRIFT.md §1.1 |
| evidence chain gap | ANTI_DRIFT.md §1.1, §1.2, §2.1; GATE_OUTPUT_MATRIX.md |
| unevaluated (per-constraint) | GATE_OUTPUT_MATRIX.md; PROOF_OBJECT_INTEGRITY.md |
| ALLOW / DENY only | ANTI_DRIFT.md §1.1; CONFORMANCE.md; GATE_OUTPUT_MATRIX.md |

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
