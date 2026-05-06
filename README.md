# CVS Evidence Boundary Interface (CVS-EBI)

CVS-EBI defines the deterministic evidence emission interface for the Cryptographic Verification Sidecar witness layer.

It defines how independently verifiable evidence is formed beside an execution boundary.

CVS-EBI is not a logging system, observability layer, telemetry framework, monitoring product, policy engine, or execution gate.

The architectural rule is absolute:

```text
512 decides.
CVS proves.
```

512 is synchronous, authoritative, and commit-time.

CVS is asynchronous, observational, and non-authoritative.

CVS-EBI exists so that execution-boundary decisions can later be independently proven without trusting the runtime that produced them.

---

## Repository Structure

```text
/evidence-spec/      Canonical Evidence Object schema and hashing rules
/witness-runtime/    Witness runtime interface and fail-open behavior
/proof-validation/   Independent proof validation and replay rules
/diagrams/           Canonical Mermaid topology and sequence diagrams
/docs/               Explanatory architecture notes
```

---

## Non-Negotiable Principles

- CVS never participates in execution decisions.
- CVS never blocks execution.
- CVS never modifies execution flow.
- CVS never introduces latency into the commit path.
- CVS remains separable from the gate.
- CVS evidence must be independently verifiable.
- Evidence generation must be deterministic.
- Evidence must be hash-stable.
- Evidence must support cryptographic anchoring.
- Evidence must support proof portability.
- Witness generation must tolerate partial infrastructure failure.

---

## Core Boundary Separation

512 performs admissibility evaluation and emits a binary decision:

```text
ALLOW | DENY
```

CVS observes the decision event and emits deterministic evidence.

CVS does not add a third gate state.

GAP is a witness-layer evidence condition only. GAP is never a gate output token.

---

## What CVS-EBI Produces

A canonical Evidence Object containing:

- execution identity
- proposal linkage
- decision linkage
- invariant result reference
- specification identity
- deterministic hashes
- monotonic timing evidence
- optional anchoring metadata
- witness metadata
- fail-open gap evidence

The object is designed for:

- reproducible hashing
- Merkle batching
- timestamping
- anchoring
- audit reconstruction
- selective disclosure
- offline verification
- replay validation

---

## Conformance Rule

An implementation conforms to CVS-EBI only if it preserves the separation between enforcement and witnessing.

Any implementation that allows the witness layer to alter, block, reinterpret, or influence execution is non-conformant.
