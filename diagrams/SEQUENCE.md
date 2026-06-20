# Sequence Diagrams

## Proposal to Decision to Evidence

```mermaid
sequenceDiagram
    participant P as Proposal Source
    participant G as 512 Commit Gate
    participant C as Commit Target
    participant W as CVS Witness
    participant S as Evidence Store

    P->>G: Submit proposal
    G->>G: Evaluate invariants (K1–K7)
    G->>C: Emit ALLOW or DENY
    G-->>W: Emit witness event (async)
    W->>W: Construct Evidence Object
    W->>W: Calculate evidence_hash
    W->>W: Sign witness_attestation (HSM)
    W->>S: Store evidence
```

---

## Evaluation-Unavailable DENY — Gate Cannot Evaluate

This sequence models gate-layer failure: the gate itself cannot
evaluate. The infrastructure-failure handler produces DENY —
the commit path remains closed, execution does not proceed, and
the CVS sidecar records the unavailability period as a gap record.

This is distinct from witness-layer failure (see below).

```mermaid
sequenceDiagram
    participant P as Proposal Source
    participant G as 512 Commit Gate
    participant F as Infrastructure-Failure Handler
    participant C as Commit Target
    participant W as CVS Sidecar
    participant S as Evidence Store

    P->>G: Submit proposal
    G->>G: Attempt invariant evaluation
    G--xG: Gate unavailable or evaluation timeout
    G->>F: Engage infrastructure-failure handler
    F->>P: DENY (evaluation_unavailable, retry_permitted: true)
    Note over F,C: Commit path remains closed — execution does not proceed
    F-->>W: Emit DENY Evidence Object (async)
    F-->>W: Emit gap record (async)
    W->>W: Construct DENY Evidence Object (deny_cause: evaluation_unavailable)
    W->>W: Construct gap record (gate_output_during_gap: deny_evaluation_unavailable)
    W->>S: Store DENY evidence and gap record
    Note over W,S: DENY and gap permanently observable in evidence chain
```

---

## Witness-Layer Failure — Evidence Gap During Normal Execution

This sequence models witness-layer failure: the gate evaluated
correctly and emitted a decision, but the witness cannot write to
storage. Execution is not halted.

```mermaid
sequenceDiagram
    participant G as 512 Commit Gate
    participant C as Commit Target
    participant W as CVS Witness
    participant Q as Local Queue

    G->>C: Emit ALLOW or DENY
    G-->>W: Emit witness event (async)
    W->>W: Construct Evidence Object
    W->>Q: Attempt durable write
    Q--xW: Storage unavailable
    W->>W: Record gap evidence to local queue
    W->>Q: Queue gap evidence for retry
    Note over G,C: Execution is not halted by witness failure
    Note over W,Q: Evidence recovered on storage restoration
```

---

## Delayed Anchoring

```mermaid
sequenceDiagram
    participant W as CVS Witness
    participant M as Merkle Batcher
    participant A as Anchor Layer
    participant V as Validator

    W->>M: Emit merkle_leaf_hash
    M->>M: Build Merkle root
    M->>A: Submit anchor payload
    A--xM: Anchor delayed
    M->>W: Set anchor_status DELAYED
    W->>W: Preserve evidence object
    V->>W: Validate unanchored evidence
    Note over W,V: DELAYED status does not invalidate Evidence Object
```
