# Example: a working CVS witness

A minimal, runnable CVS witness in pure Python — standard library only, no
dependencies. It implements the semantics of `witness-runtime/WITNESS_INTERFACE.md`
at example grade: ingest events, chain them, emit receipts, detect coverage
gaps, and verify independently.

Run it:

```
python3 demo.py
python3 verify.py demo-log.jsonl demo-receipts.jsonl dos.json
```

`demo.py` runs a scripted end-to-end scenario (deterministic clock, no
network) and finishes by invoking the verifier. `demo-log.jsonl`,
`demo-receipts.jsonl`, and `demo-anchor.json` are the committed outputs of
that run — fixtures you can verify without running the demo.

## What the demo shows

1. Witness initializes against `dos.json`; the manifest hash is recorded in
   the log's genesis line. Coverage claims are valid only against the
   declared manifest.
2. A 512-style constraint evaluation (`check_4` ALLOW, priced → obligation)
   is ingested on `checkout-api`; its outcome (net settlement, decimal
   strings) arrives on `payout-rail` under the same `correlation_id`,
   threading the sequence the way the 512 emitter's evidence objects do.
3. A malformed event from an undeclared surface is **rejected and recorded** —
   the witness does not drop it silently. Rejection is evidence.
4. The feeder runs a PULSE ping sweep: one pulse fans out, each answering
   surface returns a self-naming receipt, the shared `pulse_id` threads the
   fan. The witness originates nothing — `pulse.py` is feeder code.
5. The witness's own batch tick marks `agent-inbox` silent past its DOS
   threshold: a `coverage_gap_detected` event goes **into the chain**.
   Silence is evidence.
6. The surface resumes; a `coverage_gap_closed` event records the duration.
7. The batch anchor payload is printed — in production this exact record's
   `batch_root` is submitted to XRPL.
8. The independent verifier recomputes every hash, re-links the chain,
   re-checks every receipt signature, and pairs every gap open/close.

## Buildable now, with existing technology

Nothing in this example waits on a breakthrough. Each CVS mechanism is a
commodity primitive:

| CVS needs | Commodity answer | In this example |
|---|---|---|
| Tamper-evident append-only log | SHA-256 hash chain — the same primitive as git and Certificate Transparency | `witness.py` chain |
| Content-addressed receipts | hash of canonical JSON — git objects, IPFS CIDs | `receipt_id` |
| Witness authentication | Ed25519 signatures — SSH, Signal, TLS certs; the demo substitutes HMAC-SHA256 with a local key and labels it | `signature` field |
| Declared Observation Surface | a JSON manifest, hashed and anchored | `dos.json` + `dos_hash` in genesis |
| Absence-as-evidence | compare last-seen against the declared threshold; emit an event | `check_gaps()` |
| Settlement anchoring | one batch hash per period to XRPL — or any public ledger | `batch_root()` → `demo-anchor.json` |
| Feeder delivery | the HTTPS POST the feeder already makes | `ingest()` / `pulse.py` |
| Independent verification | recompute the hashes from the log + manifest; anyone can | `verify.py` |
| Time | timestamps are feeder-supplied data; the witness adds observation time as metadata | explicit timestamps, scripted clock |

No new cryptography, no new consensus, no trusted hardware, no AI. A
competent backend engineer builds the production version in weeks; the hard
part was never the code — it was deciding what the witness must *not* do.

## What this example is NOT

- Not production cryptography: HMAC-SHA256 stands in for Ed25519 witness
  signatures. The substitution is labeled on every receipt.
- Not a network service: the witness is a class with two entry points
  (`ingest`, `check_gaps`). Production wraps it in whatever transport the
  feeder uses; the witness itself never dials out.
- Not multi-tenant, not WORM-backed, not clock-synchronized. The log is a
  file; the anchor is printed, not submitted.
- Not the rebuild: the production witness rebuild (Ed25519-chained evidence,
  Merkle batching, XRPL anchoring) is the production path. This example is
  the fastest way for a developer to hold the whole loop in their head.

## Files

- `witness.py` — the witness: ingest, hash chain, receipts, gap detection,
  batch anchor record
- `pulse.py` — feeder-side PULSE sweep (not the witness; the witness never
  originates traffic)
- `verify.py` — independent verifier: recomputes everything, trusts nothing
- `demo.py` — scripted end-to-end run with a deterministic clock
- `dos.json` — example Declared Observation Surface manifest
- `demo-log.jsonl`, `demo-receipts.jsonl`, `demo-anchor.json` — committed
  outputs of the demo run; verify them directly
