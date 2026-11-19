# Feasibility & Constraints Questions

## Q1. [Architect] What existing systems must this integrate with?

This covers identity, document stores, ticketing, collaboration tools, and other enterprise systems the research platform would call or ingest from. Exact connector design stays for later stages.

A. Microsoft 365 and related enterprise content systems are the primary integration targets
B. Google Workspace and related systems are the primary integration targets
C. Multiple enterprise content and collaboration systems, still to be listed
D. Not yet identified
E. None in the first production release beyond the platform itself
X. Other (please specify)

[Answer]: C. Multiple enterprise content and collaboration systems, still to be listed. Design an extensible enterprise connector framework, but do not assume all integrations are required in the first production release.

## Q2. [Compliance] Are there regulatory or compliance requirements that bind this initiative?

Named regimes researched earlier remain candidates. Applicability is still UNKNOWN unless you select one here. Privacy, classification, tenant isolation, audit, retention, residency, and access control stay product requirements either way.

A. A named regime is required for the first production release (name it in Other or below)
B. Controls are required; the named regime stays undecided for now
C. Not yet identified
D. Not applicable
E. None
X. Other (please specify)

[Answer]: B. Controls are required; the named regime stays undecided for now. Preserve enterprise security, privacy, tenant isolation, authorization, auditability, reliability, scalability, and observability requirements. Market Research UNKNOWN items and deferred decisions stay preserved.

## Q3. [Architect] What is the team's current tech stack and skill profile?

This records skills and current tools for feasibility risk. It does not select the production architecture or approve a vendor.

A. Strong in Python, TypeScript/React, and cloud APIs; limited multi-agent production experience
B. Strong across backend, frontend, cloud, and security; multi-agent work is familiar
C. Not yet identified
D. Not applicable
E. None
X. Other (please specify)

[Answer]: C. Not yet identified. Evaluate candidate technologies without prematurely selecting the implementation stack.

## Q4. [Architect] What are the budget and timeline constraints?

The Market Research diary holds a provisional 14–20 week production planning estimate. That is not an approved schedule. Cost per request has no approved ceiling.

A. Keep the 14–20 week planning window as a constraint to validate; cost ceiling still open
B. Timeline and budget are both open until Team Formation and Delivery Planning
C. A hard deadline or hard budget already exists (state it in Other)
D. Not yet identified
E. None
X. Other (please specify)

[Answer]: B. Timeline and budget are both open until Team Formation and Delivery Planning. Treat the 14–20 week estimate as provisional and subject to feasibility validation. Cost ceiling remains open.

## Q5. [Architect] Are there organizational blockers?

Examples: change freeze, competing priorities, hiring lag, approval latency, or dependency on another program.

A. Yes. Material blockers exist (describe them in Other)
B. No material organizational blocker is known today
C. Not yet identified
D. Not applicable
E. None
X. Other (please specify)

[Answer]: C. Not yet identified. Do not interpret this as confirmation that no blockers exist.

## Q6. [Platform] What AWS services and accounts are currently in use?

Exact production services stay unselected. This records the current landscape for constraint analysis only.

A. An AWS account exists; specific services for this product are not yet chosen
B. Named AWS services and accounts are already in use for related work (list them in Other)
C. Not yet identified
D. Not applicable — AWS may not be the eventual cloud
E. None
X. Other (please specify)

[Answer]: C. Not yet identified. Preferred answer was A (AWS account exists; services unselected) only if account existence could be verified. Repo evidence: `infrastructure/terraform/README.md` states no AWS resources are provisioned; no account id was found in project files. Account existence is UNKNOWN.

## Q7. [Architect] How should the existing demo constrain Feasibility?

The approved Intent Statement says the demo is not the target production architecture and nothing in it is VERIFIED, PASS, or GO.

A. Treat the demo as a brownfield reference only; do not treat it as the production baseline
B. Prefer reusing demo components where feasible, still without marking them VERIFIED
C. Not yet identified
D. Not applicable
E. None
X. Other (please specify)

[Answer]: A. Treat the demo as a brownfield reference only; do not treat it as the production baseline. Assess the demo through a separate gap analysis before recommending component reuse. Nothing in the demo is VERIFIED, PASS, or GO.

## Q8. [Platform] What live dependencies are required for a production-like feasibility path?

Web Search needs a supplied live or mock provider. Model and vector store choices stay open.

A. A mock or stub path is acceptable for early feasibility; live providers stay replaceable and unselected
B. Live model and live web-search providers are required before Feasibility can conclude GO
C. Not yet identified
D. Not applicable
E. None
X. Other (please specify)

[Answer]: A. A mock or stub path is acceptable for early feasibility; live providers stay replaceable and unselected. Define provider-neutral interfaces for LLMs, embeddings, vector retrieval, and web search. Distinguish mock-based technical feasibility from live-provider validation and production readiness.

## Q9. [Compliance] What data-residency or tenancy constraint binds the first release?

Residency and tenant isolation are required product controls. The named region set is not chosen.

A. Multi-tenant isolation is required; residency region set stays open
B. A named residency region or region set is already required (state it in Other)
C. Not yet identified
D. Not applicable
E. None
X. Other (please specify)

[Answer]: A. Multi-tenant isolation is required; residency region set stays open. Maintain strict tenant isolation across authentication, authorization, ingestion, retrieval, storage, caching, logs, and AI-agent execution. Named residency regions remain undecided (UNKNOWN).

## Consolidated Summary Confirmation

Does this all look correct before I generate the artifact?

- Looks correct
- Request changes

[Answer]: Looks correct
