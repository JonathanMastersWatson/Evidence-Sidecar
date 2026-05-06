# Relationship to 512

512 and CVS-EBI are separate by design.

512 is the execution-boundary authority.

CVS-EBI is the evidence emission interface for the witness layer.

---

## 512 Responsibilities

512 performs:

- enforcement
- admissibility evaluation
- commit-time decisioning
- synchronous gate control
- binary outcome emission

512 outputs:

```text
ALLOW | DENY
```

512 does not output `GAP`.

---

## CVS-EBI Responsibilities

CVS-EBI defines how CVS records evidence after observing a boundary event.

CVS-EBI performs:

- witness object formation
- deterministic evidence hashing
- witness-chain continuity
- Merkle leaf creation
- anchoring preparation
- proof validation support
- gap evidence recording

CVS-EBI does not perform admissibility.

---

## Separation Rule

512 decides whether an action is allowed to become real.

CVS proves what happened at the boundary.

If CVS can influence the decision, the witness is no longer independent.

If the witness is no longer independent, the proof is weaker.
