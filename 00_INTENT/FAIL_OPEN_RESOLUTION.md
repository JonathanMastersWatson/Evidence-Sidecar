# Fail Open, Fail Closed, ALLOW, DENY, and the Evolution of Binary Governance

## Purpose

This document records the architectural evolution of the 512 Constitutional Model's treatment of failure, governance availability, transparency, and admissibility.

It exists as a historical and constitutional record.

The purpose is not merely to document the final decision. The purpose is to document the reasoning, challenges, adversarial reviews, contradictions, and discoveries that produced the final position.

Future readers should understand not only what was decided, but why.

---

# Background

From the earliest versions of 512, the system was intended to satisfy two principles simultaneously:

1. Prevent unauthorized or illegitimate machine-speed actions.
2. Prevent governance systems from becoming concealed sources of authority.

These principles were initially expressed through the concepts of:

* Fail Open
* Fail Closed
* Human Sovereignty
* Transparency
* Evidence
* Accountability

At the time, the architecture was heavily influenced by concerns around:

* Free speech
* Human agency
* Contestability
* Explainability
* Governance transparency

The assumption was that governance systems themselves represented a potential concentration of authority and therefore should not gain additional authority merely because they became unavailable.

This assumption led to the original interpretation of fail-open behaviour.

---

# The Original Fail-Open Interpretation

The early model proposed:

```text
Gate unavailable
↓
Execution continues
↓
CVS records a gap
```

The reasoning was simple:

A governance system should not acquire authority through its own absence.

If the gate failed, crashed, timed out, or became unavailable, the gate itself should not be able to halt the world.

Instead:

* execution continued
* the ungoverned period was recorded
* the CVS witness layer documented the event

This became known as:

```text
ALLOW + GAP
```

The gap record provided evidence that governance was unavailable during a specific period.

The philosophy was transparency rather than prevention.

---

# Why This Position Appeared Reasonable

Within free-speech and human-agency scenarios the model worked well.

Examples:

* content moderation
* recommendation systems
* information filtering
* advisory systems

In these environments:

```text
Execution continues
+
Transparency preserved
```

appeared preferable to:

```text
Execution blocked
because governance became unavailable
```

The CVS witness layer existed specifically to ensure that such periods were observable rather than concealed.

---

# The Introduction of Machine-Speed Commit Decisions

Over time the architecture expanded beyond transparency and speech-related scenarios.

The system began addressing:

* agentic execution
* financial transactions
* tool invocation
* autonomous commerce
* insurable machine-speed systems

The central question shifted.

The question was no longer:

> Should governance silence the user?

The question became:

> Should governance permit irreversible commitment?

This distinction proved critical.

---

# The $50,000 vs $500,000 Test

The decisive challenge emerged during a constitutional hardening review.

Scenario:

```text
Manifest Transfer Limit:
$50,000
```

Agent Proposal:

```text
Transfer:
$500,000
```

Simultaneously:

```text
Gate unavailable
Power loss
Network failure
Evaluation timeout
```

Under the original fail-open interpretation:

```text
Execution proceeds
CVS records gap
```

The transfer commits.

The CVS truthfully records that governance was unavailable.

However:

The money still moved.

The irreversible state change occurred.

The action was never evaluated.

No admissibility determination was established.

---

# The Discovery

The challenge exposed a flaw.

The CVS witness layer could prove that governance was absent.

It could not provide governance.

Recording an unauthorized transfer does not make the transfer authorized.

The architecture had unintentionally conflated:

```text
Evidence
```

with

```text
Authority
```

These are not equivalent.

The witness can prove what happened.

The witness cannot authorize what happened.

---

# The Definitional Error

The hardening review uncovered a deeper issue.

The architecture had quietly adopted the assumption:

```text
DENY
=
Invariant Failed
```

This assumption was never explicitly established.

It had simply emerged through discussion.

Once challenged, a different definition proved stronger:

```text
ALLOW
=
Permission to commit granted
```

```text
DENY
=
Permission to commit not granted
```

This distinction resolved the contradiction.

---

# The Revised Binary Model

Under the revised interpretation:

## ALLOW

All seven invariants:

* evaluated
* satisfied

Admissibility established.

Commit path opens.

---

## DENY

Permission to commit not granted.

Two causes exist:

### Constraint Failure

One or more invariants evaluated and failed.

Result:

```text
DENY
```

Reason:

Constraint violation.

---

### Evaluation Unavailability

Evaluation could not complete.

Examples:

* power loss
* hardware failure
* timeout
* network partition

Result:

```text
DENY
```

Reason:

Evaluation unavailable.

Constraint satisfaction was never established.

Admissibility remains unknown.

Commit path remains closed.

---

# Why This Preserves The Binary

The revised model does not introduce a third state.

There is no:

```text
ALLOW WITH WARNING
```

There is no:

```text
UNEVALUATED
```

There is no:

```text
SOFT DENY
```

Only:

```text
ALLOW
```

or

```text
DENY
```

The binary remains intact.

The reason for DENY varies.

The outcome does not.

---

# Impact on CVS

This review clarified the role of the Evidence Sidecar.

CVS is not a permission system.

CVS is not a governance engine.

CVS is not an authorization layer.

CVS is a witness.

Its purpose is to record:

* why ALLOW occurred
* why DENY occurred
* why evaluation failed
* which authority applied
* which rule was invoked

Gap records remain valuable.

Their meaning changed.

Originally:

```text
Gap
=
Execution proceeded while governance was unavailable
```

Revised:

```text
Gap
=
Governance availability event recorded
while commit authority remained closed
```

The gap becomes evidence.

Not permission.

---

# Impact on Fail-Open

The phrase "fail open" became overloaded over time.

Three different meanings became mixed together:

1. Governance availability
2. Transparency
3. Human sovereignty

This caused confusion.

The review ultimately concluded:

Fail-open language is appropriate for evidence layers and disclosure layers.

Fail-open language is not appropriate for commit authority.

Commit authority remains binary.

Admissibility must be established before commitment.

---

# I6 Remained Unchanged

Perhaps the most important discovery was that I6 itself never changed.

The wording remained:

> On failure, systems must fail open, reveal governing rules, and default to human choice.

The challenge was interpretive.

The review discovered that I6 was never fundamentally about execution outcomes.

I6 is about:

* transparency
* authority disclosure
* contestability
* human sovereignty

The constitutional violation is not:

```text
DENY
```

The constitutional violation is:

```text
DENY without explanation
```

or

```text
DENY through concealed authority
```

or

```text
DENY through authority laundering
```

Under the revised model:

Infrastructure failure can legitimately produce DENY.

I6 remains fully satisfied if the reason is disclosed.

Example:

```text
DENY

Reason:
Evaluation unavailable

Cause:
Power loss

Retry:
Permitted
```

Nothing is concealed.

Human choice remains available.

Authority remains visible.

I6 is preserved.

---

# Final Constitutional Position

The architecture now adopts the following interpretation:

```text
ALLOW
=
Admissibility established
```

```text
DENY
=
Permission to commit not granted
```

Constraint failure:

```text
DENY
```

Evaluation unavailable:

```text
DENY
```

The commit boundary remains binary.

CVS remains the witness.

I6 remains the transparency and sovereignty invariant.

The kernel remains unchanged.

Only the interpretation of failure evolved.

---

# Conclusion

The fail-open review began as a discussion about availability.

It ultimately became a discussion about authority.

The $50,000 versus $500,000 challenge demonstrated that evidence cannot substitute for governance and that witness systems cannot authorize irreversible actions.

The review reaffirmed the binary nature of 512.

The architecture remains:

```text
ALLOW
```

or

```text
DENY
```

Nothing else.

The reason for the decision may vary.

The obligation to explain it does not.
