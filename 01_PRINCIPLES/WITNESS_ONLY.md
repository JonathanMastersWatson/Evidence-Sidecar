# Witness-Only Principle

The evidence sidecar defined in this repository **must function exclusively as a witness**.

It may observe, measure, record, and attest.  
It may not act, decide, enforce, or intervene.

This boundary is absolute.

---

## Definition of a Witness

A witness is an entity that:

- observes events as they occur,
- records evidence about those events,
- preserves ordering and time,
- and produces artifacts that can be verified independently.

A witness does not:

- initiate actions,
- authorize outcomes,
- alter system behavior,
- or influence execution paths.

The distinction between witnessing and acting is fundamental.

---

## Separation of Authority

The observed system retains full authority over:

- execution
- control
- policy
- outcomes
- error handling

The sidecar retains authority only over:

- evidence generation
- evidence integrity
- evidence availability (subject to fail-open constraints)

Any architecture that allows the sidecar to influence system authority violates this principle.

---

## No Decision-Making

The sidecar must not:

- validate correctness of events,
- assess compliance in real time,
- approve or reject actions,
- determine legitimacy,
- or flag outcomes as acceptable or unacceptable.

Evidence is produced without judgment.

Interpretation occurs elsewhere, after the fact.

---

## No Inline Placement

The witness-only principle prohibits:

- inline deployment
- mandatory signing before execution
- synchronous validation
- precondition checks

The sidecar must operate **out-of-band**, observing execution rather than participating in it.

---

## No Hidden Power

A system that can alter outcomes under the guise of observation is not a witness.

Hidden power emerges when:

- evidence systems become prerequisites for execution,
- compliance tools gain veto authority,
- or logging mechanisms silently modify behavior.

This repository explicitly forbids such designs.

Witnesses must be powerless by design.

---

## Insider Threat Model

The witness-only constraint exists in part to address insider risk.

If evidence is generated within the same authority boundary as execution:

- administrators may modify logs,
- operators may suppress events,
- or incentives may bias records.

An external witness reduces these risks by:

- operating independently,
- producing cryptographic chains,
- and anchoring evidence beyond local control.

---

## Court and Regulatory Implications

Evidence produced by a witness-only system carries greater credibility because:

- it did not control the system,
- it could not alter outcomes,
- and it has no incentive to misrepresent behavior.

This distinction is material in legal and regulatory proceedings.

---

## Prohibited Capabilities

The following capabilities are explicitly prohibited:

- real-time policy enforcement
- blocking or throttling execution
- inline content modification
- outcome classification
- automated dispute resolution

Adding such features transforms a witness into an authority.

---

## Summary

The sidecar exists to remember, not to decide.

It is intentionally limited, intentionally powerless, and intentionally external.

A witness that can act is no longer a witness.

Witness-only behavior is mandatory.
