# Adversarial Behavior

This document defines how the evidence sidecar architecture behaves under intentional, malicious, or strategically deceptive behavior.

Adversarial behavior is assumed.

---

## Purpose

The purpose of this document is to ensure that:

- the architecture remains defensible under bad faith,
- manipulation attempts are detectable,
- and no single actor can silently distort the record.

Trust is earned by surviving adversaries.

---

## Threat Model

Adversarial behavior may originate from:

- system operators,
- insiders with elevated access,
- external attackers,
- counterparties in dispute,
- or authorities exerting pressure.

The architecture assumes adversarial incentives exist.

---

## Insider Manipulation

Insiders may attempt to:

- suppress evidence,
- alter logs,
- selectively disclose records,
- or disable observation.

The architecture mitigates this by:

- externalizing evidence generation,
- hash chaining,
- detectable gaps,
- and public settlement receipts.

Suppression becomes visible.

---

## Selective Observation Attacks

Adversaries may attempt to:

- enable observation only during favorable periods,
- disable the sidecar during risky operations,
- or restart observation opportunistically.

Such behavior creates gaps.

Gaps are evidence.

---

## Time Manipulation

Adversaries may attempt to:

- alter clocks,
- fabricate timestamps,
- or reorder events.

Time ordering, disclosed clock state, and chain integrity expose such attempts.

Perfect time is not required; honest time is.

---

## Evidence Flooding

Adversaries may attempt to:

- overwhelm the system with noise,
- dilute meaningful events,
- or obscure key evidence.

Batching, scoping, and minimal revelation mitigate this.

Noise does not erase structure.

---

## Disclosure Abuse

Adversaries may attempt to:

- coerce over-disclosure,
- bypass scope controls,
- or misuse disclosed evidence.

Selective disclosure, scope enforcement, and auditability constrain abuse.

---

## Settlement Manipulation

Adversaries may attempt to:

- delay settlement strategically,
- time anchoring opportunistically,
- or suppress receipts.

Deferred settlement is observable.

Delay does not erase history.

---

## Coercion and Authority Pressure

Adversarial pressure may include:

- legal threats,
- regulatory overreach,
- or contractual coercion.

The architecture responds by:

- enforcing predefined constraints,
- rejecting overbroad requests,
- and producing defensible refusals.

Constraint is protection.

---

## Verification Under Adversity

Even under adversarial conditions, an independent verifier must be able to:

- reconstruct what was observed,
- identify what was missing,
- and assess integrity honestly.

Adversarial pressure must not produce false continuity.

---

## Summary

Adversaries cannot be prevented.

They can only be exposed.

This architecture does not eliminate bad behavior — it makes it visible.
