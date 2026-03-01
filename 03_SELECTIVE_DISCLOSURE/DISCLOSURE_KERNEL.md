# Disclosure Kernel

This document defines the Disclosure Kernel within the
Cryptographic Verification Sidecar (CVS) specification.

The canonical CVS specification is defined by:

- `CVS_ARCHITECTURE_v2.7.md`
- `CVS_IMPLEMENTATION_v2.2.md`

If conflict exists, the canonical specification governs.

This document is normative.

The Disclosure Kernel is the minimal, constrained mechanism by which
evidence may be revealed without exposing systems, payloads,
or irrelevant data.

Selective disclosure is required for CVS-Conforming implementations.

---

## Purpose

The Disclosure Kernel exists to:

- enable transparency without overexposure,
- support structured inquiry,
- preserve system autonomy and confidentiality.

It prevents evidence systems from becoming bulk export or surveillance mechanisms.

---

## Disclosure Is Computed, Not Dumped

Evidence MUST NOT be disclosed wholesale.

Disclosure MUST be:

- scoped to a specific inquiry,
- limited to relevant evidence paths,
- produced through computation over stored evidence.

Unbounded raw log export is non-conformant.

---

## Kernel Boundary

The Disclosure Kernel defines:

- what evidence structures may be disclosed,
- how disclosure artifacts are generated,
- what remains outside scope.

It does not define:

- who may request disclosure,
- how authorization is determined,
- how disclosed evidence is interpreted.

Those concerns remain external to CVS.

---

## Minimal Revelation Principle

For any disclosure request, the system MUST reveal:

- the smallest set of Evidence Objects necessary,
- the minimal temporal window required,
- only fields structurally relevant to the inquiry.

Additional context MUST NOT be included by default.

---

## Evidence Path Extraction

Disclosure operates by extracting evidence paths, defined as:

- a contiguous sequence of Evidence Objects,
- bounded by explicit start and end conditions,
- including any gaps within that interval.

Extracted paths MUST preserve:

- ordering,
- chain integrity,
- detectable absence.

---

## Proof Without Payload

Disclosed evidence MUST NOT include:

- original content payloads,
- proprietary business data,
- personal data,
- system internals.

Verification relies on:

- hashes,
- timestamps,
- attestations,
- settlement anchors (if present).

Payloads MAY be referenced but MUST NOT be embedded.

---

## Context Without Interpretation

The Disclosure Kernel MAY provide:

- structural context (ordering, continuity),
- cryptographic context (hashes, signatures),
- timing context.

It MUST NOT provide:

- analytical conclusions,
- narrative framing,
- assertions of correctness.

Interpretation remains external.

---

## Disclosure Formats

Disclosed evidence MUST be provided in:

- deterministic formats,
- stable canonicalized structures,
- machine-verifiable representations.

Human-readable output MAY be included but is secondary.

---

## Disclosure of Gaps

Gaps within the disclosed interval MUST be included.

Disclosure MUST NOT:

- smooth over interruptions,
- imply continuity where none exists,
- conceal absence.

A visible gap preserves integrity.

---

## Replay Resistance

Disclosed evidence SHOULD be bound to:

- a specific request context,
- a defined time window,
- a unique disclosure instance.

Binding prevents reuse outside its intended scope.

---

## Auditability of Disclosure

The act of disclosure SHOULD be:

- observable,
- recordable,
- auditable.

Disclosure events MAY generate their own Evidence Objects.

---

## Scope Limitation

The Disclosure Kernel:

- does not guarantee regulatory sufficiency,
- does not determine admissibility,
- does not enforce compliance.

It governs structural evidence extraction only.

---

## Summary

The Disclosure Kernel enables precision transparency.

It reveals what is necessary, and nothing beyond that boundary.

Transparency is bounded by design.
