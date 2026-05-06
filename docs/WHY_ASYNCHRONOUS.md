# Why CVS Is Asynchronous

CVS must remain asynchronous because evidence generation cannot be allowed to add latency to the execution commit path.

The gate must preserve deterministic execution behavior.

The witness must preserve independent evidence behavior.

Those are different jobs.

---

## Hot Path Rule

The execution path is:

```text
proposal -> 512 evaluation -> ALLOW/DENY -> irreversible commit
```

CVS observes this path but does not sit inside it.

---

## Why This Matters

If CVS blocks execution, then evidence infrastructure becomes execution authority.

That creates four problems:

1. The witness is no longer independent.
2. Gate latency becomes dependent on evidence infrastructure.
3. Temporary anchor or storage failure can halt execution.
4. Proof generation becomes mixed with admissibility.

That is non-conformant.

---

## Correct Failure Behavior

If the witness fails, the gate continues.

The witness records the failure as evidence-layer gap state.

This preserves the distinction between:

- execution admissibility
- evidence availability

They are related, but not the same.
