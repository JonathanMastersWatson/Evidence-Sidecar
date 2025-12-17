# Supply Chain

This document maps the evidence sidecar architecture to physical and digital supply chains, logistics networks, and provenance-sensitive manufacturing systems.

Supply chains require independent evidence because disputes arise at handoff boundaries, not within controlled domains.

---

## Scope

This mapping applies to:

- manufacturing and assembly lines,
- logistics and freight movement,
- warehousing and inventory systems,
- cold-chain and regulated goods,
- digital supply chains for software and data.

It spans both physical and digital assets.

---

## The Supply Chain Evidence Problem

Supply chains are fragmented by design.

They involve:

- multiple independent actors,
- sequential custody transfers,
- heterogeneous systems,
- and asymmetric incentives.

When loss, damage, delay, or tampering is alleged, internal logs are insufficient.

Each party controls only part of the story.

---

## Sidecar Placement

In supply chain environments, the sidecar operates:

- alongside handoff points,
- observing custody transfer events,
- recording time and sequence,
- without interfering with operations.

Typical observation points include:
- shipment dispatch,
- receipt confirmation,
- custody transfer,
- environmental threshold events,
- and exception handling.

---

## Evidence Objects in Supply Chain Context

Supply chain Evidence Objects may represent:

- custody transfer events,
- timestamped location observations,
- seal or container status changes,
- environmental boundary crossings,
- system-to-system handoffs.

Payloads such as manifests or content descriptions are not stored.

---

## Time, Location, and Sequence

The sidecar records:

- observation time,
- declared location identifiers,
- and sequence of custody events.

Location declarations are treated as untrusted input unless independently verifiable.

---

## Gaps and Discontinuities

Supply chains frequently experience:

- sensor outages,
- transit blackouts,
- delayed reporting,
- or system downtime.

The sidecar must:

- surface gaps explicitly,
- record loss of observation,
- and resume chaining without concealment.

Missing evidence is often the key fact.

---

## Selective Disclosure in Supply Chains

Disclosure requests may arise from:

- insurers,
- regulators,
- counterparties,
- or arbitration proceedings.

The Disclosure Kernel enables:

- extraction of specific custody intervals,
- proof of handoff timing,
- verification of non-alteration,
- without exposing commercial details.

---

## Dispute Resolution and Liability

Independent evidence supports:

- allocation of responsibility,
- isolation of loss points,
- reduction of finger-pointing,
- and faster resolution.

The sidecar does not assign fault.

---

## Regulatory and Compliance Context

Many supply chains operate under:

- safety regulations,
- environmental controls,
- or provenance requirements.

Fail-open evidence supports auditability without operational disruption.

---

## Summary

Supply chains fail at the seams.

Independent witnesses observe those seams — and make disputes resolvable.
