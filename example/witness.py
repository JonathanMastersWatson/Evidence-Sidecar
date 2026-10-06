#!/usr/bin/env python3
"""Example CVS witness. Standard library only.

Implements the semantics of witness-runtime/WITNESS_INTERFACE.md at example
grade: it receives events, chains them, and emits receipts. It never executes
application logic, never originates traffic, never polls. The ONLY entry
points are ingest() and check_gaps(), both called by someone else.

Example-grade substitutions (labeled wherever they appear):
  - HMAC-SHA256 with a local key instead of Ed25519 witness signatures
  - JSONL file instead of a WORM store
  - batch root printed instead of submitted to XRPL
"""

import hashlib
import hmac
import json
import os
from datetime import datetime, timezone

# The only event classes the witness may originate itself (self-directed acts:
# gap deadlines are evaluation, not elicitation). Everything else must arrive
# through ingest(), from a feeder, against a declared surface.
WITNESS_EVENT_CLASSES = {"coverage_gap_detected", "coverage_gap_closed"}
WITNESS_SURFACE_ID = "witness"


def canonical(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def parse_ts(ts: str) -> datetime:
    return datetime.fromisoformat(ts)


class Witness:
    def __init__(self, dos_path, log_path,
                 witness_id="example-witness-01",
                 key=b"example-hmac-key-not-a-secret"):
        self.witness_id = witness_id
        self.key = key
        self.log_path = log_path
        with open(dos_path) as f:
            self.dos = json.load(f)
        self.dos_hash = sha256_hex(canonical(self.dos))
        self.surfaces = {s["surface_id"]: s for s in self.dos["surfaces"]}
        self.events = []
        self.open_gaps = set()
        self.last_seen = {}
        if os.path.exists(log_path):
            self._replay()
        else:
            self._append({"type": "witness_init",
                          "witness_id": witness_id,
                          "dos_hash": self.dos_hash})

    # -- log -----------------------------------------------------------
    def _append(self, obj):
        with open(self.log_path, "a") as f:
            f.write(canonical(obj) + "\n")

    def _replay(self):
        with open(self.log_path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)
                if obj.get("type") == "witness_init":
                    if obj["dos_hash"] != self.dos_hash:
                        raise ValueError("DOS manifest changed under this log")
                    continue
                self.events.append(obj)
                cls = obj["event_class"]
                if cls == "coverage_gap_detected":
                    self.open_gaps.add(obj["payload"]["surface_id"])
                elif cls == "coverage_gap_closed":
                    self.open_gaps.discard(obj["payload"]["surface_id"])
                elif obj["state"] == "witnessed":
                    self.last_seen[obj["surface_id"]] = obj["observed_at"]

    # -- ingest: the witness's only inbound door -----------------------
    def ingest(self, event, observed_at):
        """Record one feeder-supplied event. Returns (receipt, extra_events).

        extra_events carries a coverage_gap_closed event when this ingest
        resumes a surface that had an open gap. Rejected events are recorded,
        not dropped: a rejection is evidence too.
        """
        state, reason = self._validate(event)
        seq = len(self.events)
        prev_hash = self.events[-1]["event_hash"] if self.events else "GENESIS"
        payload = event.get("payload", {})
        body = {
            "seq": seq,
            "prev_hash": prev_hash,
            "surface_id": event.get("surface_id"),
            "event_class": event.get("event_class"),
            "correlation_id": event.get("correlation_id"),
            "payload": payload,
            "payload_hash": sha256_hex(canonical(payload)),
            "feeder_timestamp": event.get("feeder_timestamp"),
            "observed_at": observed_at,
            "state": state,
        }
        if reason:
            body["reject_reason"] = reason
        body["event_hash"] = sha256_hex(canonical(
            {k: v for k, v in body.items() if k != "event_hash"}))
        self.events.append(body)
        self._append(body)

        extra = []
        sid = event.get("surface_id")
        if state == "witnessed" and sid in self.surfaces:
            self.last_seen[sid] = observed_at
            if sid in self.open_gaps:
                self.open_gaps.discard(sid)
                extra.append(self._witness_event(
                    "coverage_gap_closed", observed_at,
                    {"surface_id": sid,
                     "gap_duration_s": int((parse_ts(observed_at)
                                            - parse_ts(self._gap_start(sid))).total_seconds())}))
        return self._receipt(body), extra

    def _validate(self, event):
        cls = event.get("event_class")
        if cls in WITNESS_EVENT_CLASSES and event.get("surface_id") == WITNESS_SURFACE_ID:
            return "witnessed", None
        sid = event.get("surface_id")
        if sid not in self.surfaces:
            return "rejected", "undeclared surface: %r" % (sid,)
        if cls not in self.surfaces[sid]["event_classes"]:
            return "rejected", "event class %r not declared for surface %r" % (cls, sid)
        if not event.get("correlation_id"):
            return "rejected", "missing correlation_id"
        return "witnessed", None

    def _gap_start(self, surface_id):
        for e in reversed(self.events):
            if (e["event_class"] == "coverage_gap_detected"
                    and e["payload"]["surface_id"] == surface_id):
                return e["payload"]["silent_since"]
        return self.dos["declared_at"]

    # -- receipts ------------------------------------------------------
    def _receipt(self, body):
        core = {"seq": body["seq"],
                "event_hash": body["event_hash"],
                "chain_head": body["event_hash"],
                "witness_id": self.witness_id,
                "state": body["state"]}
        receipt_id = sha256_hex(canonical(core))
        sig = hmac.new(self.key, receipt_id.encode("utf-8"),
                       hashlib.sha256).hexdigest()
        return {"receipt_id": receipt_id, **core, "signature": sig,
                "sig_note": "example-grade HMAC-SHA256; production uses Ed25519"}

    # -- gap detection: evaluation, not elicitation --------------------
    def check_gaps(self, now_iso):
        """Mark silence against the declaration. Called by the operator's own
        batch tick (a self-directed act). Asks the feeder nothing."""
        detected = []
        for sid, spec in self.surfaces.items():
            last = self.last_seen.get(sid, self.dos["declared_at"])
            silent_s = (parse_ts(now_iso) - parse_ts(last)).total_seconds()
            if silent_s > spec["silence_threshold_s"] and sid not in self.open_gaps:
                self.open_gaps.add(sid)
                detected.append(self._witness_event(
                    "coverage_gap_detected", now_iso,
                    {"surface_id": sid, "silent_since": last,
                     "threshold_s": spec["silence_threshold_s"]}))
        return detected

    def _witness_event(self, cls, observed_at, payload):
        seq = len(self.events)
        prev_hash = self.events[-1]["event_hash"] if self.events else "GENESIS"
        body = {"seq": seq, "prev_hash": prev_hash,
                "surface_id": WITNESS_SURFACE_ID, "event_class": cls,
                "correlation_id": payload.get("pulse_id", "gap-%d" % seq),
                "payload": payload,
                "payload_hash": sha256_hex(canonical(payload)),
                "feeder_timestamp": None, "observed_at": observed_at,
                "state": "witnessed"}
        body["event_hash"] = sha256_hex(canonical(
            {k: v for k, v in body.items() if k != "event_hash"}))
        self.events.append(body)
        self._append(body)
        return body

    # -- anchoring -----------------------------------------------------
    def batch_root(self):
        return sha256_hex("\n".join(e["event_hash"] for e in self.events))

    def anchor_record(self, anchored_at):
        return {
            "batch_root": self.batch_root(),
            "event_count": len(self.events),
            "chain_head": self.events[-1]["event_hash"] if self.events else "GENESIS",
            "witness_id": self.witness_id,
            "dos_hash": self.dos_hash,
            "anchored_at": anchored_at,
            "note": ("example: print this record; production submits batch_root "
                     "to XRPL (or any public settlement ledger)"),
        }
