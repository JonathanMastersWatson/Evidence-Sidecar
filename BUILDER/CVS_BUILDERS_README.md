# BUILDERS

This folder contains the reference documents for organisations and engineers
building on top of the CVS Cryptographic Verification Sidecar architecture.

CVS is an invented witness architecture, open-licensed under Apache 2.0.
The documents here define what it is, how to build a conformant implementation,
and how it relates to independently developed parallel systems.

---

## Contents

| Document | Audience | Purpose |
|---|---|---|
| `CVS_ARCHITECTURE_v3.2.md` | CTO / Board | What CVS is — the three-plane architecture, Evidence Object model, fail-open principle, open commons model |
| `CVS_IMPLEMENTATION_v2.7.md` | Engineer | How to build a conformant CVS implementation — Access Plane, Interpretation Plane, integration patterns, conformance requirements |
| `VCP_AND_CVS.md` | CTO / Architect | Parallel development acknowledgment — VeritasChain Protocol (VCP) and CVS are independent parallel developments; priority and differentiators documented |
| `512_CVS_ENTERPRISE_v1_0.md` | CTO / CFO / Board | Enterprise executive brief — the execution boundary problem and what 512/CVS resolves |

---

## Where to Start

**If you are a CTO or board member:** Read `CVS_ARCHITECTURE_v3.2.md` first.
Then `512_CVS_ENTERPRISE_v1_0.md` for the financial and operational case.

**If you are an engineer:** Read `CVS_ARCHITECTURE_v3.2.md` §1–3 for the
architectural model, then `CVS_IMPLEMENTATION_v2.7.md` for the build reference.

**If you are evaluating CVS relative to VCP or other witness architectures:**
Read `VCP_AND_CVS.md` first.

---

## What Is Not Here

The operational reference documents — selective disclosure, settlement layer,
industry mappings, evidence model — are in the numbered folders at repo root.

The priority record establishing CVS's prior art status is `CANONICAL_COMMITMENT.md`
at repo root.

The 512 Commit Gate specification that CVS is designed to witness lives at
`github.com/JonathanMastersWatson/512`.

---

*CVS BUILDERS reference documents | github.com/JonathanMastersWatson/Evidence-Sidecar*
*Apache 2.0 — open commons. Build freely. Own what you build.*
