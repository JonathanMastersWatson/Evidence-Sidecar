# Living Documents

This file identifies documents in the CVS repository that are dynamic —
subject to ongoing revision, hardening, or alignment updates.

Living documents are not frozen. They may not always be in full
alignment with each other during active hardening phases. Implementers
should treat them as directional references, not sealed specifications.

---

## Current Living Documents

| Document | Location | Why Dynamic |
|---|---|---|
| `CVS_ARCHITECTURE` | `/08_CANON/` | CTO/Board-level architecture reference. Under active language hardening. Version-bumped on content change. |
| `CVS_IMPLEMENTATION` | `/08_CANON/` | Engineer-level build reference. Under active normative framework development. Version-bumped on content change. |
| `ANTI_DRIFT.md` | Repo root | Expanded as new drift patterns are identified. |
| `CONFORMANCE.md` | Repo root | Updated as conformance criteria are hardened. |

---

## What Living Means

A living document:

- reflects the current best understanding of the architecture or pattern
- may be revised without a major version bump during hardening phases
- will converge toward a sealed version at the end of the current hardening pass
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
| `LEGAL_NOTICE.md` | Legal posture — fixed |
| `LICENSE` | Apache 2.0 — fixed |
| `NOTICE` | Attribution record — fixed |
| `UPSTREAM.md` | Upstream reference record — fixed |
| `PRIMITIVE_BOUNDARY.md` | Defines the fixed scope boundary of the CVS primitive — not subject to revision |

---

## Sealed Release

At the end of the current hardening pass, living documents will be
version-sealed. `PRE_HARDENING_NOTICE.md` will be updated to reflect
sealed status and a new archive hash will be committed.

See `PRE_HARDENING_NOTICE.md` for current hardening phase status.
