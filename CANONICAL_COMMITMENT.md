# CANONICAL COMMITMENT RECORD

**Jonathan M. Watson | 512 / CVS Architecture**
**Version 1.0 | May 2026**

---

## Purpose

This document is a permanent, self-contained priority record for the 512 Commit Gate
specification and the CVS Cryptographic Verification Sidecar architecture.

It records three independent layers of proof for each:

1. **GitHub public commit** — the date the content became publicly readable
2. **XRPL genesis anchor** — an immutable transaction on a public, decentralized
   ledger that cannot be backdated, independently verifiable by any party
3. **Canonical hash commitment** — the SHA-256 binding of the specification content
   to a specific, verifiable artefact

This document exists because priority dates matter. The open commons model for 512
and CVS depends on prior art status — the ability to demonstrate that the
specifications were publicly available before any competing system, patent filing,
or standards claim. This record is that demonstration.

No party may claim ownership over the 512 constraint set or the CVS base
architecture. No party may patent them. The dates recorded here establish why.

---

## 512 — COMMIT GATE SPECIFICATION

### Genesis Commit

| Field | Value |
|---|---|
| Repository | `github.com/JonathanMastersWatson/512` |
| Commit message | "512 genesis: immutable constraint kernel and reference documents" |
| Commit hash | `4f5bc5d` |
| Date | **December 28, 2025** |
| Author | Jonathan M. Watson (JonathanMastersWatson) |
| Visibility | Public — readable by any party from this date |

### XRPL Genesis Anchor

| Field | Value |
|---|---|
| Commit message | "Add XRPL genesis anchor receipt" |
| Commit hash | `d5e82ec` |
| Date | **December 28, 2025** |
| Ledger | XRP Ledger (XRPL) — public, decentralized, deterministic finality |
| XRPL Transaction ID | `6A77FE134F71D24CE6ADF67F8DF6F0C60F150EB5DF33B6F8923A2F30490CE7CB` |
| Verification | Any party may independently verify this transaction on the XRPL |

The XRPL anchor provides a second, independent proof layer that does not depend
on GitHub's infrastructure, timestamps, or continued availability. The transaction
on the XRP Ledger is immutable. It predates all significant competing systems
found in the public record as of May 2026.

### Canonical Kernel Commitment

| Field | Value |
|---|---|
| File | `512-core/KERNEL/512-kernel-padded.txt` |
| Size | 512 bytes (exact, UTF-8, no BOM) |
| SHA-256 | `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5` |

This hash binds the seven invariants to a specific, verifiable artefact. Any
claimed instance of 512 may be independently verified against this hash. A gate
executing against a different constraint set is not canonical 512 — the hash
mismatch is mechanically detectable by any party.

### March 2026 Sealed Archive

| Field | Value |
|---|---|
| File | `512-main-2026-03-24.zip` |
| Date sealed | 2026-03-24 |
| SHA-256 | `DF27F6C5C8DDBBD5341FB15EA943D92B3388331B386C26F44A145673F6C8D218` |

This hash covers the complete 512 repository state as of the March 24, 2026
hardening pass. The kernel content and SHA-256 hash have not changed since
the December 28, 2025 genesis commit.

---

## CVS — CRYPTOGRAPHIC VERIFICATION SIDECAR

### Genesis Commit

| Field | Value |
|---|---|
| Repository | `github.com/JonathanMastersWatson/Evidence-Sidecar` |
| Commit message | "Initial publication of Evidence Sidecar reference architecture" |
| Commit hash | `32cbd9b` |
| Date | **December 17, 2025** |
| Author | Jonathan M. Watson (JonathanMastersWatson) |
| Visibility | Public — readable by any party from this date |

CVS was publicly committed **11 days before** the 512 genesis commit, and
**27 days before** the first known independently developed competing system
(VeritasChain Protocol, published January 13, 2026).

### Apache 2.0 Declaration

| Commit | Date | Description |
|---|---|---|
| `b9d0cff` | February 28, 2026 | "README: declare CVS canon + Apache 2.0" |

The Apache 2.0 license was formally declared on February 28, 2026. The license
declaration date does not alter the prior art date. The content was publicly
readable from December 17, 2025. Prior art status is established by public
availability, not by license application date.

### Canonical CVS Specification Commitment

| Commit | Date | Description |
|---|---|---|
| `a7762a9` | February 28, 2026 | "Establish canonical CVS specification and SHA-256 hashes" |

### March 2026 Sealed Archive

| Field | Value |
|---|---|
| File | `Evidence-Sidecar-main-2026-03-24.zip` |
| Date sealed | 2026-03-24 |
| SHA-256 | `0DA1ABA3A7257B636C0A364920C5CE643843257D217C0DBD68BA5DB64712BE17` |

This hash covers the complete Evidence-Sidecar repository state as of the
March 24, 2026 hardening pass.

---

## PRIORITY TIMELINE — COMPARATIVE RECORD

The following timeline records the 512/CVS publication dates against all
significant independently developed competing systems identified as of May 2026.

| Date | Event | System |
|---|---|---|
| **Dec 17, 2025** | **CVS genesis public commit** (`32cbd9b`) | **CVS** |
| **Dec 28, 2025** | **512 genesis public commit** (`4f5bc5d`) | **512** |
| **Dec 28, 2025** | **512 XRPL genesis anchor** (`d5e82ec`) | **512** |
| Jan 5, 2026 | 512 canonical documentation established | 512 |
| Jan 13, 2026 | VeritasChain Protocol (VCP) v1.0 published | Competitor — CVS layer |
| February 2026 | AARM (arXiv 2602.09433) published | Competitor — 512 layer |
| February 2026 | PunkGo "Right to History" (arXiv 2602.20214) published | Competitor — CVS layer |
| February 28, 2026 | CVS Apache 2.0 formally declared | CVS |
| 2026 | AINOVA / LungClaw (Zenodo DOI: 10.5281/zenodo.18704803) published | Competitor — 512 layer |
| April 2026 | Nidus (arXiv 2604.05080) published | Competitor — 512 layer |

512 and CVS predate every significant competing system identified.

The convergence of independent systems in early 2026 is noted. Multiple
independent researchers arriving at similar architectural patterns within months
of each other is consistent with the "discovered constraint" characterisation of
512 — the constraint exists independent of any single author, and its recognition
by multiple independent parties confirms its universal character.

---

## WHAT THIS RECORD ESTABLISHES

**For 512:**

No party may patent the 512 constraint set, the seven invariants, the binary
ALLOW/DENY output model, the fail-open requirement, the stateless evaluation
model, the fixed 512-byte specification size as architectural invariant, or the
canonical hash commitment mechanism. These were publicly disclosed on
December 28, 2025. Any patent application filed after that date on these elements
faces this record as prior art.

**For CVS:**

No party may patent the CVS sidecar architecture, the three-plane separation
model (Capture/Access/Interpretation), the hash-chained Evidence Object structure,
the Merkle batch anchoring to a public settlement ledger, or the administrative
independence requirement as described in the CVS specification. These were
publicly disclosed on December 17, 2025. Any patent application filed after
that date on these elements faces this record as prior art.

**What this record does not establish:**

This record does not prevent patents on derivative implementations, managed
services, specific hardware integrations, certification systems, marketplace
architectures, or any other implementation built on top of the open 512/CVS
base. Derivative implementations are fully patentable and commercialisable
by their creators. See `512_ARCHITECTURE §6` and `CVS_ARCHITECTURE §-1.5`
for the complete open commons model.

---

## INDEPENDENT VERIFICATION

Any party may independently verify this record without trusting the repository
operator:

**GitHub commits:** All commits listed above are publicly visible at:
- `github.com/JonathanMastersWatson/512/commits/main`
- `github.com/JonathanMastersWatson/Evidence-Sidecar/commits/main`

GitHub commit timestamps are independently verifiable. The "Verified" badge
on commits confirms GPG signature by the author at time of commit.

**XRPL anchor:** The genesis anchor transaction
`6A77FE134F71D24CE6ADF67F8DF6F0C60F150EB5DF33B6F8923A2F30490CE7CB`
is independently verifiable on the XRP Ledger without any access to GitHub
or any infrastructure controlled by the author. Any XRPL explorer can confirm
the transaction date and content.

**SHA-256 hash:** Any party may download `512-core/KERNEL/512-kernel-padded.txt`
from the public repository and compute:

```powershell
(Get-FileHash "512-kernel-padded.txt" -Algorithm SHA256).Hash
```

The result must equal `7B08C024B77A24830C15E7952D6E54BED383AA960F4C74A71FF95CE51F4D80F5`.
Any deviation indicates the file has been modified and is not canonical 512.

**Sealed archives:** The March 2026 sealed archive hashes may be verified by
downloading the respective repository archives and computing SHA-256. Results
must match the values recorded in this document exactly.

---

## MAINTENANCE

This document is append-only. Entries are not modified after the fact.

If additional anchoring events occur — new ledger anchors, formal registration,
standards body submissions — they are appended below with date and reference.

| Date | Event | Reference |
|---|---|---|
| December 28, 2025 | XRPL genesis anchor | Transaction `6A77FE134F71D24CE6ADF67F8DF6F0C60F150EB5DF33B6F8923A2F30490CE7CB` |
| March 24, 2026 | 512 repository sealed | Archive SHA-256: `DF27F6C5C8DDBBD5341FB15EA943D92B3388331B386C26F44A145673F6C8D218` |
| March 24, 2026 | CVS repository sealed | Archive SHA-256: `0DA1ABA3A7257B636C0A364920C5CE643843257D217C0DBD68BA5DB64712BE17` |
| *(append future anchoring events here)* | | |

---

*512 / CVS Canonical Commitment Record | Version 1.0 | May 2026*
*Author: Jonathan M. Watson*
*This document is released under CC BY 4.0 (512 repository) and*
*Apache 2.0 (Evidence-Sidecar repository) consistent with each*
*repository's licensing posture.*
*This document is included in both repositories.*
