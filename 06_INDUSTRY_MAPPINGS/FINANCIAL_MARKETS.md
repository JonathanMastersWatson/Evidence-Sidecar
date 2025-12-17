# Financial Markets

This document maps the evidence sidecar architecture to financial markets, exchanges, trading venues, clearing systems, and post-trade infrastructure.

Financial markets are a critical domain because disputes are frequent, stakes are high, and timelines are unforgiving.

---

## Scope

This mapping applies to:

- trading venues and exchanges,
- alternative trading systems,
- clearing and settlement infrastructure,
- market data distribution,
- risk management and surveillance systems.

It is applicable across asset classes.

---

## The Market Integrity Problem

Financial systems rely on:

- high-speed execution,
- complex routing,
- and layered intermediaries.

When disputes arise, reconstruction depends on:

- internal logs,
- fragmented records,
- and institution-controlled narratives.

This creates ambiguity precisely where precision is required.

---

## Sidecar Placement

In market environments, the sidecar operates:

- out-of-band from execution engines,
- observing order lifecycle events,
- capturing sequencing and timing,
- without introducing latency.

The sidecar must never participate in order matching, routing, or execution.

---

## Evidence Objects in Market Context

Market Evidence Objects may represent:

- order receipt,
- order modification or cancellation,
- execution reports,
- trade confirmations,
- market data publication events.

Payload details (price, size, counterparty) are not stored unless required by scope.

---

## Time Ordering and Latency Sensitivity

Markets are time-critical.

The sidecar must:

- preserve strict internal ordering,
- disclose clock synchronization state,
- record observation time precisely,
- and surface any drift or anomaly.

False precision is more damaging than disclosed uncertainty.

---

## Gaps and System Events

Market systems experience:

- halts,
- volatility interruptions,
- failovers,
- and network partitions.

The sidecar must:

- record these events explicitly,
- surface gaps in evidence,
- and avoid narrative smoothing.

Interruptions are part of the record.

---

## Selective Disclosure in Markets

Disclosure requests may originate from:

- regulators,
- counterparties,
- clearing houses,
- or internal investigations.

The Disclosure Kernel enables:

- bounded time-window extraction,
- proof of order handling sequence,
- verification of non-alteration,
- without revealing proprietary strategies.

---

## Surveillance and Compliance Alignment

The sidecar complements, but does not replace:

- surveillance systems,
- regulatory reporting,
- or compliance tooling.

It provides independent evidence that internal systems behaved as claimed.

---

## Dispute Resolution

In disputes involving:

- trade breaks,
- execution priority,
- or best execution claims,

independent evidence strengthens reconstruction without privileging any participant’s internal logs.

---

## Regulatory Considerations

Market regulators require:

- auditability,
- fairness,
- and post-event reconstruction.

Fail-open evidence sidecars satisfy these needs without interfering with market function.

---

## Summary

Financial markets move too fast for inline trust.

Independent witnesses restore clarity after the fact — where markets actually settle disputes.
