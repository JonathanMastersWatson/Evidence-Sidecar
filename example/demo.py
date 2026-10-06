#!/usr/bin/env python3
"""Scripted end-to-end run of the example CVS witness.

Deterministic clock: timestamps are data, supplied explicitly. No sleeps,
no network, no randomness except the pulse_id (which is just a label).

Run:  python3 demo.py
Then: python3 verify.py demo-log.jsonl demo-receipts.jsonl dos.json
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from witness import Witness  # noqa: E402
from pulse import run_pulse  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, "demo-log.jsonl")
RECEIPTS = os.path.join(HERE, "demo-receipts.jsonl")
ANCHOR = os.path.join(HERE, "demo-anchor.json")
T0 = datetime(2026, 10, 6, 19, 30, 0, tzinfo=timezone.utc)


def ts(dt):
    return dt.isoformat()


def main():
    for p in (LOG, RECEIPTS):
        if os.path.exists(p):
            os.remove(p)
    receipts = []

    def save_receipt(r):
        receipts.append(r)
        with open(RECEIPTS, "a") as f:
            f.write(json.dumps(r, sort_keys=True) + "\n")

    w = Witness(os.path.join(HERE, "dos.json"), LOG)
    print("[1] witness initialized — DOS manifest hash: %s" % w.dos_hash[:16])

    # A 512-style constraint evaluation, then its outcome: one correlation_id
    # threads the sequence, the way the 512 emitter's three evidence objects do.
    r, _ = w.ingest(
        {"surface_id": "checkout-api", "event_class": "512_constraint_evaluation",
         "correlation_id": "corr-001",
         "payload": {"check": "check_4", "decision": "ALLOW",
                     "priced": True, "obligation_ref": "iou-corr-001"},
         "feeder_timestamp": ts(T0)}, observed_at=ts(T0))
    save_receipt(r)
    print("[2] 512_constraint_evaluation (check_4 ALLOW, priced) — receipt %s" % r["receipt_id"][:12])

    r, _ = w.ingest(
        {"surface_id": "payout-rail", "event_class": "outcome",
         "correlation_id": "corr-001",
         "payload": {"settled_net": "1250.00", "currency": "USD"},
         "feeder_timestamp": ts(T0 + timedelta(seconds=10))},
        observed_at=ts(T0 + timedelta(seconds=10)))
    save_receipt(r)
    print("[3] outcome (net settlement) — same correlation_id threads the sequence")

    # A malformed event: recorded as rejected, NOT dropped. Rejection is evidence.
    r, _ = w.ingest(
        {"surface_id": "unknown-surface", "event_class": "outcome",
         "correlation_id": "corr-002", "payload": {},
         "feeder_timestamp": ts(T0 + timedelta(seconds=20))},
        observed_at=ts(T0 + timedelta(seconds=20)))
    save_receipt(r)
    print("[4] event from undeclared surface → REJECTED and recorded (state=%s)" % r["state"])

    # PULSE ping sweep, feeder-originated. agent-inbox stays silent.
    t_pulse = T0 + timedelta(seconds=30)
    report = run_pulse(w, ts(t_pulse), silent_surfaces=("agent-inbox",))
    for resp in report["responses"]:
        save_receipt(resp["receipt"])
    print("[5] PULSE sweep %s — %d surfaces answered, silent: %s"
          % (report["pulse_id"], len(report["responses"]), ", ".join(report["silent"])))

    # The witness's own batch tick marks silence against the declaration.
    # agent-inbox threshold is 120s; the others are 900s.
    t_gap = t_pulse + timedelta(seconds=180)
    detected = w.check_gaps(ts(t_gap))
    for g in detected:
        print("[6] coverage_gap_detected(%s) — chained as event #%d; silence is evidence"
              % (g["payload"]["surface_id"], g["seq"]))

    # The silent surface resumes. The gap closes with its duration, on the record.
    t_back = t_gap + timedelta(seconds=60)
    r, extra = w.ingest(
        {"surface_id": "agent-inbox", "event_class": "512_constraint_evaluation",
         "correlation_id": "corr-003",
         "payload": {"check": "check_2", "decision": "ALLOW"},
         "feeder_timestamp": ts(t_back)}, observed_at=ts(t_back))
    save_receipt(r)
    for g in extra:
        print("[7] coverage_gap_closed(%s) — silent %ss, chained as event #%d"
              % (g["payload"]["surface_id"], g["payload"]["gap_duration_s"], g["seq"]))

    # Batch anchor: this exact payload is what production submits to XRPL.
    anchor = w.anchor_record(ts(t_back + timedelta(seconds=5)))
    with open(ANCHOR, "w") as f:
        json.dump(anchor, f, indent=2, sort_keys=True)
    print("[8] anchor payload — batch_root=%s… (%d events)"
          % (anchor["batch_root"][:16], anchor["event_count"]))

    # Independent verification: recompute everything, trust nothing.
    print("[9] verifying…")
    out = subprocess.run(
        [sys.executable, os.path.join(HERE, "verify.py"), LOG, RECEIPTS,
         os.path.join(HERE, "dos.json")],
        capture_output=True, text=True)
    print(out.stdout.strip())
    return out.returncode


if __name__ == "__main__":
    sys.exit(main())
