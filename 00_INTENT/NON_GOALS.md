# Non-Goals

This repository intentionally excludes a wide range of concerns that are commonly, but incorrectly, associated with evidence, transparency, governance, and trust.

These exclusions are deliberate.  
They exist to preserve neutrality, adoptability, and long-term legitimacy.

---

## This Is Not a Product

This repository does not define:

- a commercial offering
- a hosted service
- a vendor platform
- a software distribution
- an SDK or API
- a marketplace
- a licensing model

Commercial implementations may exist elsewhere.  
They are explicitly out of scope here.

This repository defines **constraints and reference architecture only**.

---

## This Is Not a Governance System

This repository does not:

- govern behavior
- enforce rules
- impose outcomes
- arbitrate disputes
- assign blame
- determine truth

It records evidence.  
It does not judge it.

Any interpretation of evidence occurs outside the scope of this work.

---

## This Is Not an Identity System

This repository does not define or require:

- identity frameworks
- authentication standards
- decentralized identifiers
- reputation systems
- credentialing mechanisms

Evidence may reference identities, but identity resolution is explicitly external.

---

## This Is Not a Control Plane

The evidence sidecar described here:

- does not intercept execution
- does not block actions
- does not approve transactions
- does not modify payloads
- does not influence outcomes

Any system in which the sidecar can alter execution is non-compliant with this architecture.

---

## This Is Not Inline Infrastructure

This repository explicitly excludes:

- inline processing
- mandatory signing before execution
- synchronous verification requirements
- blocking compliance gates

All evidence generation must occur **out-of-band**.

Fail-closed architectures are incompatible with this work.

---

## This Is Not Total Transparency

This repository does not advocate:

- full data disclosure
- radical transparency
- universal observability
- unrestricted access to logs
- exposure of proprietary systems

Selective disclosure is a core requirement.

Only the minimum evidence necessary to satisfy a specific inquiry should ever be revealed.

---

## This Is Not a Data Platform

This repository does not define:

- analytics pipelines
- dashboards
- visualization tools
- reporting systems
- machine learning workflows

Evidence produced under this architecture may be consumed by third-party tools, but those tools are outside scope.

---

## This Is Not a Blockchain Platform

This repository does not:

- promote cryptocurrency adoption
- define token economics
- manage assets
- perform execution on-chain
- store payload data on-chain

Distributed ledgers are used strictly as **public, neutral receipt layers**.

Ledger selection is constrained by technical properties, not ideology.

---

## This Is Not a Political or Ethical Statement

This repository does not:

- advocate social policy
- promote ideological positions
- frame problems morally
- appeal to values or beliefs

It addresses engineering, legal, and economic constraints only.

---

## This Is Not Mandatory

Nothing defined in this repository is compulsory.

Systems may operate without independent witnesses.

However, such systems must accept that:

- disputes will rely on internal logs,
- evidence credibility will be weaker,
- liability exposure will be higher,
- and insurance and regulatory scrutiny may increase.

Adoption is voluntary.  
Consequences are not.

---

## Why These Exclusions Matter

Each non-goal exists to ensure that this architecture:

- can be adopted without philosophical alignment,
- can be implemented by competing vendors,
- can survive regulatory and legal scrutiny,
- does not accumulate hidden authority,
- and does not collapse under its own ambition.

Anything not explicitly included here is presumed out of scope.

Future extensions must respect these boundaries or exist in separate
