# CVS Repository Archive Hash

This document records the cryptographic hash of the sealed repository
archive produced on 2026-03-24, following the hardening pass.

---

## Archive Details

| Field | Value |
|---|---|
| File | `Evidence-Sidecar-main-2026-03-24.zip` |
| Date sealed | 2026-03-24 |
| Algorithm | SHA-256 |
| Hash | `0DA1ABA3A7257B636C0A364920C5CE643843257D217C0DBD68BA5DB64712BE17` |

---

## What This Hash Covers

This hash covers the complete repository state as downloaded from
`github.com/JonathanMastersWatson/Evidence-Sidecar` on 2026-03-24,
following the hardening pass which included:

- CONFORMANCE.md — extended with operational states, test checklist,
  non-goals, constraint formation responsibility
- ANTI_DRIFT.md — new, 15 sections including 9 hardening additions
- VERIFICATION_PROTOCOL.md — new, 6-step canonical verification protocol
- 02_EVIDENCE_MODEL/PROOF_OBJECT_INTEGRITY.md — new
- 02_EVIDENCE_MODEL/SPEC_HASH_BINDING.md — new
- 03_SELECTIVE_DISCLOSURE/DISCLOSURE_KERNEL_CLARIFICATION.md — new
- LEGAL_NOTICE.md — replaced with Apache 2.0 attribution and
  open commons declaration
- README.md — hardening banners removed, CVS-Conforming language
- UPSTREAM.md — new, three-layer stack reference

---

## Verification

To verify this hash, download the archive and run:
```powershell
(Get-FileHash "Evidence-Sidecar-main-2026-03-24.zip" -Algorithm SHA256).Hash
```

The output must match the hash recorded above exactly.

---

## Previous Archive

| Date | Hash |
|---|---|
| 2026-02-02 | `f3727dc7e69a380e81bf4f64b3357dc8a3deee06d294940142b8ec8d9c24f3b0` |

Previous archive records are maintained in `CANON_HASHES.md`.
