# AI Systems

This document maps the evidence sidecar architecture to AI training, inference, deployment, and decision-support systems.

AI systems require independent evidence because their outputs are increasingly opaque, probabilistic, and disputed after the fact.

---

## Scope

This mapping applies to:

- model training pipelines,
- inference services (batch and real-time),
- agentic and autonomous systems,
- decision-support and recommendation engines,
- embedded and edge AI deployments.

It is model-agnostic and framework-independent.

---

## The AI Accountability Problem

AI systems present unique evidentiary challenges:

- outputs are non-deterministic,
- models evolve over time,
- internal state is not human-auditable,
- and explanations are often post-hoc.

When harm, bias, or failure is alleged, reconstruction is difficult.

Internal logs are insufficient and frequently contested.

---

## Sidecar Placement

In AI systems, the sidecar operates:

- out-of-band from inference execution,
- observing input-output boundaries,
- capturing invocation timing and sequencing,
- without inspecting model internals.

The sidecar must never alter prompts, weights, or outputs.

---

## Evidence Objects in AI Context

AI Evidence Objects may represent:

- model invocation events,
- inference request boundaries,
- output emission events,
- model version changes,
- deployment or rollback events.

Payloads (prompts, embeddings, outputs) are not stored.

---

## Model Versioning and Drift

AI systems evolve continuously.

The sidecar must:

- record model identifiers and versions,
- surface transitions between versions,
- and detect unrecorded changes.

This enables retrospective attribution of behavior.

---

## Time and Causality

AI outputs may influence downstream systems.

The sidecar preserves:

- temporal ordering of invocations,
- sequencing across dependent systems,
- and observable gaps.

It does not infer causality or intent.

---

## Gaps and Failure Modes

AI systems experience:

- degraded performance,
- partial outages,
- fallback behaviors,
- and silent failures.

The sidecar must:

- record interruptions,
- surface evidence gaps,
- and avoid reconstructive storytelling.

---

## Selective Disclosure in AI Systems

Disclosure requests may arise from:

- regulators,
- litigants,
- customers,
- or internal governance bodies.

The Disclosure Kernel enables:

- proof of invocation and timing,
- confirmation of model version at decision time,
- verification of non-alteration,
- without revealing training data or prompts.

---

## Bias, Harm, and Liability Claims

The sidecar does not assess bias or harm.

It provides:

- evidence of what model was used,
- when it was invoked,
- and how outputs were produced procedurally.

Interpretation remains external.

---

## Regulatory Alignment

Emerging AI regulation increasingly demands:

- traceability,
- auditability,
- and accountability.

Fail-open evidence sidecars provide these properties without constraining innovation.

---

## Summary

AI systems cannot explain themselves.

Independent witnesses make their behavior reconstructible — after the fact, where accountability lives.
