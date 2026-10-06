#!/usr/bin/env python3
"""Feeder-side PULSE ping sweep. This is NOT the witness.

One pulse fans out to every declared surface; each answers with a self-naming
receipt; a shared pulse_id threads the whole fan into one observable event.
The witness never originates the pulse — in production this code is the
customer's feeder (their adapter, their HTTPS calls). The witness only
exposes ingest(); it records what arrives.

Absence is evidence: a declared surface silent past the sweep window is
marked silent here by the feeder AND caught by the witness's own gap
detection (check_gaps) against the DOS silence threshold.
"""

import os
import sys
import uuid

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from witness import Witness  # noqa: E402


def run_pulse(witness: Witness, now_iso: str, silent_surfaces=()):
    """Emit one pulse per declared surface. Returns the sweep report."""
    pulse_id = "pulse-" + uuid.uuid4().hex[:12]
    report = {"pulse_id": pulse_id, "responses": [], "silent": []}
    for spec in witness.dos["surfaces"]:
        sid = spec["surface_id"]
        if sid in silent_surfaces:
            report["silent"].append(sid)
            continue
        event = {"surface_id": sid,
                 "event_class": "pulse_response",
                 "correlation_id": pulse_id,
                 "payload": {"pulse_id": pulse_id, "surface_id": sid},
                 "feeder_timestamp": now_iso}
        receipt, _ = witness.ingest(event, observed_at=now_iso)
        report["responses"].append({"surface_id": sid,
                                    "receipt_id": receipt["receipt_id"],
                                    "receipt": receipt})
    return report
