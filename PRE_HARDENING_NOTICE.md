# Pre-Hardening Notice — CVS Repository

This repository represents a pre-seal hardening pass of the CVS
(Cryptographic Verification Sidecar) specification.
The architectural constraints defined herein are directionally stable
and reflect the intended evidence formation model.

However:

- Language is still being tightened to eliminate ambiguity at the
  evidence boundary
- Implementation guidance is being refined to prevent misinterpretation
- Formal normative specification (MUST / MUST NOT compliance framework)
  is in progress

This repository SHOULD NOT be treated as a final, version-sealed
specification.

Implementations based on this repository must assume that:

- wording may be further hardened
- constraints may be clarified but not relaxed
- non-conformant patterns identified here will remain non-conformant
  in final versions

A formal versioned and hash-sealed release will follow this hardening
phase.

Until then, this repository should be used as:

- a directional implementation constraint reference
- a correction layer for misinterpretations
- a pre-normative architectural guide

---

**End of pre-seal notice.**
