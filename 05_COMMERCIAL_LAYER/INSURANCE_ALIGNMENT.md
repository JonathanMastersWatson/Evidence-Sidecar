# Insurance Alignment

This document explains how independent, fail-open evidence infrastructure aligns with insurance underwriting, claims handling, and risk pricing.

The goal is to make the evidentiary value legible to insurers without turning the sidecar into a compliance authority.

---

## Purpose

Insurance markets price uncertainty.

In high-liability digital systems, the dominant cost driver is not frequency of incidents, but:

- inability to reconstruct events,
- inability to prove non-tampering,
- and inability to establish chain of custody.

Independent evidence reduces uncertainty and compresses tail risk.

---

## The Insurer’s Core Questions

Insurers and underwriters typically need answers to:

1. What happened?
2. When did it happen?
3. Can the insured prove it?
4. Was evidence altered or withheld?
5. Can causality and sequence be reconstructed?
6. Is there an independent record outside the insured’s control?

Internal logs rarely satisfy these questions under dispute.

---

## Evidence as a Qualifying Control

Independent evidence sidecars can be treated as a **qualifying control** because they:

- are external to the execution path,
- are resistant to insider modification,
- and can be verified independently.

Fail-open behavior matters because it prevents the control itself from creating operational risk.

---

## Underwriting Benefits

Evidence sidecars can improve underwriting by enabling:

- reduced ambiguity in incident narratives,
- faster claims resolution,
- lower forensic investigation costs,
- reduced fraud exposure,
- and clearer liability allocation between parties.

These benefits are structural and do not depend on business domain.

---

## Claims Handling Benefits

In claims contexts, the sidecar supports:

- reconstruction of event timelines,
- identification of gaps or interruptions,
- verification of evidence integrity,
- and rapid determination of what is provable.

Claims become less dependent on testimony and internal documentation.

---

## Premium, Deductible, and Coverage Implications

This architecture can support insurer pricing logic such as:

- premium reductions for systems with independent witnesses,
- deductible reductions for provable incident timelines,
- higher coverage limits where auditability is demonstrably strong,
- exclusion tightening where evidence controls are absent.

This repository does not prescribe insurance terms; it enables them.

---

## Fraud and Misrepresentation Resistance

Fraud is often enabled by:

- post-hoc alteration of logs,
- selective omission,
- or inability to prove continuity.

Hash chaining, detectable gaps, and external receipts reduce these attack surfaces.

---

## Non-Goals

Insurance alignment does not mean:

- insurers control disclosure,
- insurers gain access by default,
- or evidence is automatically shared.

Selective disclosure and scope controls remain mandatory.

---

## Summary

Insurance does not require perfect systems.

It requires provable systems.

Independent, fail-open evidence reduces uncertainty, accelerates claims resolution, and materially improves insurability without introducing operational fragility.
