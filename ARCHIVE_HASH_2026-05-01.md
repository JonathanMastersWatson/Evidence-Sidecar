# CVS Repository Archive Hash

This document records the cryptographic hash of the sealed repository
archive produced on 2026-05-01, following the hardening and BUILDERS
phase.

---

## Archive Details

| Field | Value |
|---|---|
| File | `Evidence-Sidecar-main-2026-05-01.zip` |
| Date sealed | 2026-05-01 |
| Algorithm | SHA-256 |
| Hash | `70297B8808522B01B0A1E7822E550F4A21B742C16DA7D098218FB9FA3968040C` |

---

## What This Hash Covers

This hash covers the complete repository state as downloaded from
`github.com/JonathanMastersWatson/Evidence-Sidecar` on 2026-05-01,
following the May 2026 hardening pass which included:

- `CANONICAL_COMMITMENT.md` — new, permanent priority record
- `VCP_AND_CVS.md` — new, parallel development acknowledgment
- `PRE_HARDENING_NOTICE.md` — updated to sealed status record
- `LIVING_DOCUMENTS.md` — updated to reflect sealed release
- `README.md` — pre-hardening banner removed
- `ANTI_DRIFT.md` — pre-hardening banner removed
- `CONFORMANCE.md` — pre-hardening banner removed
- `00_INTENT/NON_GOALS.md` — pre-hardening banner removed
- `CANON_HASHES.md` — updated with May 1 seal hash
- `BUILDERS/` — new folder with full reference document suite:
  - `README.md`
  - `CVS_ARCHITECTURE_v3.2.md`
  - `CVS_IMPLEMENTATION_v2.7.md`
  - `VCP_AND_CVS.md`
  - `512_CVS_ENTERPRISE_v1_0.md`
  - `UNINSURABLE_BY_DESIGN.md`

Repository status: **Active**
Pre-hardening phase: **Closed**

---

## Verification

To verify this hash, download the archive and run:

```powershell
(Get-FileHash "Evidence-Sidecar-main-2026-05-01.zip" -Algorithm SHA256).Hash
```

The output must match the hash recorded above exactly.

---

## Prior Sealed Archive

| Date | File | SHA-256 |
|---|---|---|
| 2026-03-24 | `Evidence-Sidecar-main-2026-03-24.zip` | `0DA1ABA3A7257B636C0A364920C5CE643843257D217C0DBD68BA5DB64712BE17` |
| 2026-05-01 | `Evidence-Sidecar-main-2026-05-01.zip` | `70297B8808522B01B0A1E7822E550F4A21B742C16DA7D098218FB9FA3968040C` |

Full priority record: `CANONICAL_COMMITMENT.md` at repo root.
