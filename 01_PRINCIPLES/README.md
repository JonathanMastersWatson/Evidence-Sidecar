# Principles

This folder defines the **non-negotiable architectural principles** that constrain all compliant implementations.

Principles describe *invariants*, not features.

---

## Role in the Architecture

The principles:

- define hard boundaries,
- prevent authority creep,
- and constrain downstream design choices.

If a design violates these principles, it is not compliant.

---

## Contents

- `FAIL_OPEN.md`
- `WITNESS_ONLY.md`
- `VOLUNTARY_SYSTEMS.md`
- `AUTHORITY_LIMITS.md`

Each document defines a single invariant.

---

## Normative Status

Principles are normative.

They are referenced by `CONFORMANCE.md` and apply globally.
