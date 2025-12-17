# Broadcast and Media

This document maps the evidence sidecar architecture to broadcast and digital media production, distribution, and publication systems.

Broadcast media is a canonical use case because it combines:
- real-time execution,
- irreversible public impact,
- regulatory scrutiny,
- and increasing synthetic manipulation risk.

---

## Scope

This mapping applies to:

- live broadcast production,
- recorded news and programming,
- digital-first media outlets,
- OTT and FAST channels,
- and downstream platform distribution.

It is technology-agnostic and vendor-neutral.

---

## The Broadcast Problem

Broadcast systems face unique evidentiary challenges:

- live execution cannot be paused for verification,
- content provenance is often disputed after transmission,
- internal logs are mutable and operator-controlled,
- and liability attaches retroactively.

Traditional compliance logging records *what was aired*, not *how it came to be aired*.

---

## Sidecar Placement

In broadcast environments, the sidecar operates:

- out-of-band from the signal path,
- observing streams, events, and control signals,
- without inline dependency.

Typical observation points include:
- live program output,
- ingest feeds,
- playout systems,
- and newsroom automation events.

Inline insertion is prohibited.

---

## Evidence Objects in Broadcast Context

Broadcast Evidence Objects may represent:

- video or audio segment observation,
- live program continuity,
- ingest or handoff events,
- control-room automation actions,
- or transmission boundaries.

Payload content is never stored.

---

## Time and Synchronization

Broadcast systems rely on precise timing.

The sidecar must:

- record observation time,
- disclose clock source and sync state,
- preserve ordering across segments,
- and surface any timing anomalies.

Declared timecodes may be recorded but are not trusted.

---

## Gaps and Failures

In live environments, failures are expected.

When:
- feeds drop,
- control systems restart,
- or networks partition,

the sidecar must:
- continue to fail-open,
- record gaps explicitly,
- and resume chaining without concealment.

---

## Selective Disclosure in Media

Disclosure requests may arise from:

- regulators,
- courts,
- insurers,
- platforms,
- or internal review.

The Disclosure Kernel enables:

- extraction of specific time windows,
- proof of unaltered broadcast,
- visibility into handoff points,
- without revealing content or editorial processes.

---

## Liability and Risk Alignment

Evidence sidecars support broadcast risk mitigation by:

- establishing chain of custody,
- demonstrating non-interference,
- shifting liability upstream when appropriate,
- and reducing ambiguity in disputes.

They do not certify truth or editorial correctness.

---

## Platform Distribution

Downstream platforms increasingly assess content provenance.

Evidence receipts enable:

- independent verification,
- provenance signaling,
- and resistance to false takedowns.

Verification does not require platform trust in the broadcaster.

---

## Regulatory Considerations

Broadcast regulators require:

- continuity,
- reliability,
- and auditability.

Fail-open evidence sidecars satisfy these requirements without introducing operational risk.

---

## Summary

Broadcast media demonstrates why independent witnesses are necessary.

Live systems cannot pause for truth —  
but truth must still be provable afterward.
