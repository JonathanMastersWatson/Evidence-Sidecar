# CVS AND VCP — PARALLEL DEVELOPMENT ACKNOWLEDGMENT

**Jonathan M. Watson | CVS Cryptographic Verification Sidecar**
**Version 1.0 | May 2026**

---

## Purpose

VeritasChain Protocol (VCP), published January 13, 2026 by the VeritasChain
Standards Organization, is architecturally similar to CVS. Both implement a
sidecar witness pattern with hash-chained events, Merkle anchoring, and
external ledger settlement. Both solve the same fundamental problem: producing
independently verifiable cryptographic evidence of system execution without
modifying or blocking that execution.

This document acknowledges VCP as an independent parallel development, states
CVS's priority position, and identifies the architectural properties that
distinguish the two systems.

Honest acknowledgment of parallel development strengthens the open commons
claim — when multiple independent actors converge on the same architecture
within weeks of each other, the architecture is a natural solution to the
problem, not an individual invention. That is precisely CVS's philosophical
position.

---

## Priority

CVS genesis commit: **December 17, 2025** (commit `32cbd9b`,
`github.com/JonathanMastersWatson/Evidence-Sidecar`)

VCP v1.0 published: **January 13, 2026**

CVS was publicly committed 27 days before VCP existed. This gap is documented
in `CANONICAL_COMMITMENT.md` with independent verification instructions.
Apache 2.0 was formally declared on February 28, 2026; the prior art date
is the genesis commit, not the license declaration date.

---

## What VCP and CVS Share

VCP and CVS arrived at the same core architectural pattern independently:

- **Sidecar deployment** — the witness layer operates alongside the observed
  system without modifying or blocking it
- **Hash-chained event records** — each captured event cryptographically
  references its predecessor, making chain tampering mechanically detectable
- **Merkle tree aggregation** — batches of events are aggregated into Merkle
  roots for efficient anchoring
- **External ledger anchoring** — cryptographic commitments are anchored to
  a public settlement ledger for independent verification
- **Tamper-evidence** — the architecture produces evidence that any third
  party can verify without trusting the operator
- **Non-blocking operation** — the witness layer does not sit in the execution
  path; failure creates detectable gaps rather than execution failures

The convergence on these properties by two independent projects within 27 days
is consistent with the view that the sidecar witness pattern is a discovered
architecture — the natural solution to the problem of producing independently
verifiable execution evidence without operational coupling.

---

## Where CVS and VCP Differ

The shared foundation aside, CVS and VCP diverge on four properties that
matter in high-assurance contexts.

### 1. Time Anchoring

**VCP** uses PTPv2 (IEEE 1588 Precision Time Protocol) for its highest
precision tier, with NTP and best-effort tiers below that. PTPv2 achieves
sub-microsecond precision within a network but synchronizes against network
time sources.

**CVS** requires a GPS-disciplined hardware oscillator as the time source
baseline. GPS-disciplined timing is externally referenceable — timestamps
are verifiable against any GPS receiver anywhere in the world, independent
of the operator's network infrastructure. A PTPv2 timestamp can be questioned
if the network time source is compromised. A GPS-disciplined timestamp is
anchored to atomic time signals from satellite infrastructure that no single
operator controls.

In regulatory, insurance, and legal evidence contexts, external referencability
matters. A timestamp that any party can independently verify against satellite
time without trusting any infrastructure controlled by the operator is a
structurally stronger proof than a network-synchronized timestamp.

### 2. Three-Plane Structural Separation

**VCP** does not define a structural separation between evidence capture,
evidence access, and evidence interpretation.

**CVS** enforces three structurally separated planes:

- **Capture Plane** — observes execution, constructs Evidence Objects, anchors
  commitments. No read access from external systems.
- **Access Plane** — provides read-only interfaces to the evidence chain.
  No write access to the Capture Plane. No interpretation logic.
- **Interpretation Plane** — external tools (dashboards, analytics, compliance
  systems) that consume evidence through the Access Plane. No modification
  authority over evidence.

This separation is enforced by network segmentation and IAM policy — structural
controls, not administrative procedure. The planes cannot collapse through
misconfiguration because the access controls are mechanically enforced.

The practical consequence: in CVS, no interpretation tool can modify captured
evidence, and no evidence modification can be disguised as an access operation.
In systems without this structural separation, the distinction between capture,
access, and interpretation exists only as administrative policy, which is
inadequate for high-assurance contexts.

### 3. Administrative Independence

**VCP** does not specify a requirement for administrative independence between
the witness layer and the observed system.

**CVS** makes administrative independence an architectural requirement. The
witness layer cannot share operational authority, key custody, or administrative
access with the system it witnesses. The operator of the observed system is not
the custodian of the evidence that system generates.

This property is what makes CVS evidence admissible in contexts where the
operator's own records would not be. An operator cannot suppress or alter CVS
evidence without detectable action against a system they do not administratively
control. The independence is structural, not procedural.

### 4. Disclosure Kernel

**VCP** does not define a selective disclosure mechanism.

**CVS** includes a Disclosure Kernel — a structured mechanism for selective
revelation of evidence to authorized parties without overexposure. A party
entitled to audit a specific event receives cryptographic proof of that event
without receiving the full evidence chain. The Disclosure Kernel allows CVS
to serve multiple parties with different access levels against the same
underlying evidence without creating multiple copies or revealing more than
each party's authorization permits.

---

## Comparative Summary

| Property | VCP | CVS |
|---|---|---|
| Genesis date | January 13, 2026 | **December 17, 2025** |
| Sidecar pattern | Yes | Yes |
| Hash-chained events | Yes | Yes |
| Merkle anchoring | Yes | Yes |
| External ledger anchor | Yes | Yes |
| Time source | PTPv2 / NTP / best-effort | GPS-disciplined hardware oscillator |
| Three-plane separation | Not defined | Structural — enforced by IAM and network segmentation |
| Administrative independence | Not specified | Architectural requirement |
| Selective disclosure | Not defined | Disclosure Kernel |
| Primary domain | Algorithmic trading / financial markets | Any execution surface |
| License | Standards organization model | Apache 2.0 — fully open |

---

## The Open Commons Context

VCP's existence confirms that the sidecar witness pattern is correct. Two
independent teams reached the same architecture within 27 days of each other.
That is not coincidence — it is convergence on a natural solution.

CVS is open under Apache 2.0. VCP is published under a standards organization
model. Both are available for implementation. The base sidecar pattern belongs
to neither — it is prior art predating both, established by CVS's December 17,
2025 genesis commit.

Derivative implementations of CVS — specific GPS hardware integrations,
managed witness services, certification wrappers, interpretation platforms —
are fully patentable and commercialisable by their creators. See
`CVS_ARCHITECTURE §-1.5` for the complete open commons model.

---

## Reference

VCP specification: VeritasChain Standards Organization, VCP v1.0 (January 2026)

CVS genesis commit: `32cbd9b` — December 17, 2025
CVS canonical specification commitment: commit `a7762a9` — February 28, 2026
CVS Apache 2.0 declaration: commit `b9d0cff` — February 28, 2026

Full prior art and competitive landscape analysis: `HEX/10_ip/512_CVS_PRIOR_ART_MAP.md`
Canonical commitment record: `CANONICAL_COMMITMENT.md`

---

*CVS and VCP — Parallel Development Acknowledgment | Version 1.0 | May 2026*
*Author: Jonathan M. Watson*
*Released under Apache 2.0 consistent with Evidence-Sidecar repository licensing.*
*This document does not constitute legal advice.*
