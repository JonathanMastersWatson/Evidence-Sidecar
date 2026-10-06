#!/usr/bin/env python3
"""Independent verifier. Recomputes everything; trusts nothing the witness claims.

Usage: python3 verify.py <log.jsonl> <receipts.jsonl> <dos.json>

Checks:
  1. DOS manifest hash matches the hash the witness recorded at init
  2. every event hash recomputes; prev_hash linkage and seq are intact
  3. every receipt recomputes (id + signature) and points at a real chain head
  4. every coverage_gap_closed matches a preceding open coverage_gap_detected
  5. no event class outside the DOS declarations (except witness classes)

Exit 0 iff all checks pass.
"""

import hashlib
import hmac
import json
import sys

sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
from witness import canonical, sha256_hex, WITNESS_EVENT_CLASSES  # noqa: E402

KEY = b"example-hmac-key-not-a-secret"


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ((" — " + detail) if detail else ""))
    return ok


def main(log_path, receipts_path, dos_path):
    ok = True
    with open(dos_path) as f:
        dos = json.load(f)
    dos_hash = sha256_hex(canonical(dos))
    declared = {s["surface_id"]: set(s["event_classes"]) for s in dos["surfaces"]}

    events = []
    genesis = None
    with open(log_path) as f:
        for line in f:
            line = line.strip()
            if line:
                obj = json.loads(line)
                if obj.get("type") == "witness_init":
                    genesis = obj
                else:
                    events.append(obj)

    ok &= check("genesis records DOS hash", genesis is not None)
    if genesis:
        ok &= check("DOS hash matches manifest", genesis["dos_hash"] == dos_hash,
                    genesis["dos_hash"][:12])

    prev = "GENESIS"
    chain_ok = True
    for i, e in enumerate(events):
        recomputed = sha256_hex(canonical({k: v for k, v in e.items() if k != "event_hash"}))
        if not (e["seq"] == i and e["prev_hash"] == prev and e["event_hash"] == recomputed):
            ok &= check("chain link #%d" % i, False, "seq/linkage/hash mismatch")
            chain_ok = False
            break
        prev = e["event_hash"]
        cls, sid = e["event_class"], e["surface_id"]
        if e["state"] == "rejected":
            # A rejection is evidence: it must name its reason, not pass declaration.
            if not e.get("reject_reason"):
                ok &= check("event #%d rejection" % i, False, "rejected without reason")
                chain_ok = False
                break
            continue
        allowed = (cls in WITNESS_EVENT_CLASSES and sid == "witness") or (
            sid in declared and cls in declared[sid])
        if not allowed:
            ok &= check("event #%d declaration" % i, False, "%r on %r" % (cls, sid))
            chain_ok = False
            break
    if chain_ok:
        ok &= check("hash chain intact (%d events)" % len(events), True)

    by_seq = {e["seq"]: e for e in events}
    n_receipts = 0
    receipts_ok = True
    with open(receipts_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            n_receipts += 1
            core = {k: r[k] for k in ("seq", "event_hash", "chain_head", "witness_id", "state")}
            rid_ok = sha256_hex(canonical(core)) == r["receipt_id"]
            sig_ok = hmac.new(KEY, r["receipt_id"].encode("utf-8"),
                              hashlib.sha256).hexdigest() == r["signature"]
            head_ok = r["seq"] in by_seq and by_seq[r["seq"]]["event_hash"] == r["chain_head"] == r["event_hash"]
            if not (rid_ok and sig_ok and head_ok):
                ok &= check("receipt %s" % r["receipt_id"][:12], False, "id/signature/head mismatch")
                receipts_ok = False
                break
    if receipts_ok:
        ok &= check("receipts verify (%d)" % n_receipts, n_receipts > 0)

    open_gaps = set()
    gaps_ok = True
    for e in events:
        if e["event_class"] == "coverage_gap_detected":
            open_gaps.add(e["payload"]["surface_id"])
        elif e["event_class"] == "coverage_gap_closed":
            sid = e["payload"]["surface_id"]
            if sid not in open_gaps:
                gaps_ok = False
                break
            open_gaps.discard(sid)
    ok &= check("gap open/close pairing", gaps_ok)

    print("ALL CHECKS PASS" if ok else "VERIFICATION FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3]))
