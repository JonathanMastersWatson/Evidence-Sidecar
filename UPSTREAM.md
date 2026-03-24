# Upstream: Constraint Architecture

CVS witnesses execution and produces independently verifiable evidence.

It does not define what is admissible. It does not enforce admissibility.
Those functions belong to the upstream layers.

---

## The Stack

| Layer | Function |
|---|---|
| Constraint Architecture | Defines what is admissible — the boundaries within which execution is permitted |
| 512 | Enforces admissibility at the commit boundary — binary, deterministic, at machine speed |
| CVS | Witnesses execution and produces independently verifiable evidence |

Constraint Architecture defines the world.
512 enforces it.
CVS proves it.

---

## Separation

CVS observes execution outcomes against declared constraints.
It does not define those constraints.
It does not validate whether those constraints are correctly formed.
It does not enforce them.

The formation of constraint boundaries — consent logic, authority
models, thresholds, domain-specific admissibility rules — is the
responsibility of the Constraint Architecture layer.

Errors in constraint definition are upstream failures, not CVS failures.

CVS will faithfully record adherence to incorrectly defined constraints.
That is by design. It is also the point: CVS proves what happened
against the declared boundary, regardless of whether that boundary
was correctly designed.

This property is what makes CVS evidence independently defensible.
The evidence does not depend on the correctness of the constraints —
only on whether the declared constraints were satisfied.

---

## Reference

Constraint Architecture is documented at:

https://github.com/JonathanMastersWatson/Constraint-Architecture

---

## What This Means for Implementers

If you are implementing CVS, the constraint boundary is an input,
not something CVS produces or validates.

Before instrumenting with CVS, the deploying organisation must
answer:

**What is the declared constraint boundary this system operates within?**

That question is answered upstream.
CVS proves adherence to the answer.
It does not produce or validate the answer.

If no constraint boundary is declared, CVS has nothing to prove
adherence to. Deploying CVS without a declared constraint boundary
produces evidence of execution without context — not evidence of
legitimate execution.
