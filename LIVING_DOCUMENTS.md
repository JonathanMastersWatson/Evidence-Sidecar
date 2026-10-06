# Living Documents

This file identifies documents in the CVS repository that are dynamic —
subject to ongoing revision or alignment updates.

Living documents reflect the current best understanding of the architecture
or pattern. They will not relax constraints — only clarify or tighten them.

---

## Current Living Documents

| Document | Location | Why Dynamic |
|---|---|---|
| `CVS_ARCHITECTURE` | `/BUILDERS/` | CTO/Board-level architecture reference. Version-bumped on content change. |
| `CVS_IMPLEMENTATION` | `/BUILDERS/` | Engineer-level build reference. Version-bumped on content change. |
| `ANTI_DRIFT.md` | Repo root | Expanded as new drift patterns are identified. |
| `CONFORMANCE.md` | Repo root | Updated as conformance criteria are clarified. |

---

## What Living Means

A living document:

- reflects the current best understanding of the architecture or pattern
- will converge toward a sealed version at major release boundaries
- will not relax constraints — only clarify or tighten them

A living document does **not**:

- change the Evidence Object model
- alter the three canonical observation points
- modify the conformance requirements in ways that reduce stringency
- introduce new architectural claims not derivable from the CVS primitive

---

## Frozen Documents

The following are frozen and will not change:

| Document | Why Frozen |
|---|---|
| `CANON_HASHES.md` | Cryptographic fingerprint record — sealed |
| `CANONICAL_COMMITMENT.md` | Priority record — append-only |
| `LEGAL_NOTICE.md` | Legal posture — fixed |
| `LICENSE` | Apache 2.0 — fixed |
| `NOTICE` | Attribution record — fixed |
| `UPSTREAM.md` | Upstream reference record — fixed |
| `PRIMITIVE_BOUNDARY.md` | Defines the fixed scope boundary of the CVS primitive — not subject to revision |

---

## Sealed Release — May 2026

Hardening phase complete. All living documents have been version-sealed
as of May 2026. Repository status is Active. Pre-hardening banners and
notices have been removed. A new archive hash will be committed to
record the sealed state.

Archive hash record: `CANONICAL_COMMITMENT.md` at repo root.

---

## Doctrine Additions — October 2026 (unsealed)

Since the May 2026 seal, new witness doctrine has been settled and is not
yet in this repository: PULSE ping-sweep semantics (feeder-originated pulse,
shared pulse_id threading per-endpoint receipts into one observable event,
TTL as the enforced sweep window, absence-as-evidence via the Declared
Observation Surface's coverage-gap detection); the witness-initiation rule
(the witness may initiate only what witnessing requires — ledger-directed
and self-directed acts — never feeder-directed probes, triggers, or
polling); and the 512/CVS disjointness restatement (CVS witnesses
constraint-evaluation events, never executes application logic). A witness
rebuild is in progress; its code or an explicit pointer lands here before
the final seal.

## Final Seal — December 5, 2026 (planned)

A final seal of this repository is planned for December 5, 2026, alongside
final seals of the 512, Schema PRIME, and Machine Speed Papers repositories.
Each seal follows the established convention: archive hash, dated proof
record, XRPL anchoring. After the final seal these repositories stand as
tools and resources for future developers and as proof of originatorship.
