# Scope Document

**Stage:** Scope Definition (1.4)  
**Intent:** `261119-multimodal-research-assi`  
**Confirmation:** Q1–Q7 consolidated summary confirmed **Looks correct** (20 November 2026)  
**Upstream:** `intent-statement.md`, `feasibility-assessment.md`, `constraint-register.md`, `raid-log.md`  
**Status:** Draft for Stage 4 human review — **not** Stage 4 approved  
**Revision:** Gate Request Changes remediation (20 November 2026) — PARTIAL findings addressed in scope + backlog ACs

Evidence labels: **VERIFIED** (confirmed Stage 4 answers / approved upstream), **ASSUMED**, **UNKNOWN**, **NOT_VERIFIED**, **OPEN**.

## Purpose

Define the in/out boundary and release slices for the Multi-Agent Multimodal Research Assistant under the enterprise AI-DLC workflow, without selecting vendors, closing Stage 3 conditions, authorizing Construction, or importing Project 2 code.

## Confirmed decisions (Q1–Q7)

| ID | Decision | Source |
| --- | --- | --- |
| Q1 | Architecture-validation MVP includes four agents, four routes, parallel Both + synthesis once, citation separation, mock/stub providers, UI-01, and minimal UI-02 | VERIFIED |
| Q2 | Must-have vs nice-to-have MoSCoW cut per below | VERIFIED |
| Q3 | Capability dependency graph (isolation foundations; Supervisor → agents; Both → parallel retrieval → one synthesis; UI-01 → API; UI-02 → real artifacts) | VERIFIED |
| Q4 | Dependency-first, risk-aware sequencing | VERIFIED |
| Q5 | No hard deadline without an explicit later decision; 14–20 weeks provisional and non-binding | VERIFIED |
| Q6 | Separate architecture-validation MVP, production V1, and advanced/future | VERIFIED |
| Q7 | All nine Stage 3 CONDITIONAL GO conditions remain OPEN in this document | VERIFIED |

## Release slices

### Architecture-validation MVP (in scope for first complete end-to-end demo)

Delivers a **small but complete** workflow proving the architecture without claiming production readiness:

- Supervisor routes **RAG**, **Web**, **Both**, **Neither**
- **Both** executes RAG and Web **concurrently**, with a **deterministic join/barrier**, explicit timeout/cancellation/partial-failure outcomes, then **exactly one** Response Synthesis; concurrency and invocation count must be automated before VERIFIED (**I-06 remains OPEN** until then)
- **Multimodal RAG** (text **and** image) and Web retrieval as **independent contracts** with replaceable / mock providers; ingest/index/retrieve with source references; tenant/authorization boundaries enforced
- Grounded answer path with **internal vs external** evidence separation and citations; **fail-closed** (no fabricated web results or citations; provider failure/empty/timeout/malformed → structured errors, not silent success)
- **UI-01** architecture-validation surface: query submission, document upload, ingestion status, research history, response, citations, provenance, route visibility, and structured error feedback (see IB-08 MVP vs V1 split)
- **UI-02** minimal surface that **reads actual AI-DLC lifecycle artifacts** and shows truthful stage status, approvals, evidence, and unresolved risks — **never invents PASS, completion, or approval states**
- Security foundations: **authentication**, **RBAC**, **authorization**, tenant-aware access control, provenance, auditability, observability (architectural presence even if first demo uses one tenant); cross-tenant access denied across ingestion, retrieval, storage, API, and agent execution
- Provider-neutral interfaces; mock/stub providers acceptable

**Out of architecture-validation MVP:** live-provider production validation, **production security verification gate** (IB-11), broad enterprise connectors, rich analytics, optional agents, named compliance certification, hard delivery date.

### Production V1 (subsequent release; gated)

In addition to MVP capabilities, production V1 requires separately verified:

- Live model and web-search provider behavior behind the same interfaces
- **Separate production security verification gate** (IB-11): authentication, RBAC, authorization, and tenant isolation **test evidence**, including zero cross-tenant access across ingestion, retrieval, storage, API, and agent execution
- Applicable enterprise NFRs (security, audit, reliability, observability) with evidence
- UI-01 production verification column (IB-08): live authn/RBAC and hardened upload/ingest controls
- Selected V1 connectors only after an extensible connector framework exists and connectors are named
- Resolution or accepted carry-forward of Stage 3 conditions with Product Owner / Security approval

Production V1 is **not** authorized by this Scope Definition alone.

### Advanced / future (explicitly out of V1 essentials)

- Named broad enterprise connector sets beyond the eventual V1 list
- Live-provider optimization / vendor-specific tuning
- Rich admin analytics
- Optional additional agents
- Features that would require closing Stage 3 unknowns without evidence

## In scope (Must)

| Capability | Notes |
| --- | --- |
| Four agents | Supervisor, Multimodal RAG, Web Search, Response Synthesis |
| Four routes | RAG, Web, Both, Neither |
| Parallel Both + safe join + synthesis once | Concurrent retrieval, deterministic barrier, timeout/cancel/partial-failure rules, exactly one synthesis; I-06 OPEN until verified |
| Multimodal RAG | Text and image ingestion, indexing, retrieval, source references |
| Fail-closed evidence path | No fabricated web results or citations; structured errors on failure |
| Provenance and citation separation | Internal vs external; validation harness FAIL closed |
| Authentication, RBAC, authorization, tenant isolation | Foundations in MVP; production verification is a separate gate (IB-11) |
| UI-01 | Query, upload, ingest status, history, response, citations, provenance (MVP vs V1 per IB-08) |
| UI-02 | Real lifecycle evidence only; no invented PASS |
| Provider-neutral interfaces | No premature vendor lock-in |

## Out of scope (this Ideation scope boundary)

| Item | Disposition |
| --- | --- |
| Selecting production model / web / vector / cloud vendors | Deferred (Stage 3 conditions; DEC-02, DEC-03) |
| Named compliance regime and residency set | Deferred (DEC-01, DEC-07); controls still mandatory |
| Hard delivery deadline | None without explicit later decision (Q5) |
| Project 2 code import / merge | **Out** — reference-only (I-07, DEC-08 OPEN) |
| Treating mock path as production GO | **Out** (R-02; Stage 3 condition 8) |
| AWS provisioning from Ideation | **Out** (account UNKNOWN; condition 1) |
| Inventing UI-02 PASS / approval states | **Out** — prohibited |

## MoSCoW summary

| Priority | Items |
| --- | --- |
| **Must** | Four agents; four routes; parallel Both + safe join; synthesis once; multimodal RAG; fail-closed evidence; provenance; authentication + RBAC + authorization + isolation; UI-01; UI-02 (truthful) |
| **Should** | Extensible connector framework; live-provider adapters behind interfaces; isolation test harness design |
| **Could** | Rich analytics; optional agents; provider-specific tuning |
| **Won't (now)** | Broad connector set in first slice; closing Stage 3 conditions without evidence; Project 2 lift-and-shift |

## Sequencing (dependency-first, risk-aware)

1. Security, tenant isolation, authorization, provenance, audit, observability foundations  
2. Four-agent path with mocks/stubs and replaceable interfaces  
3. UI-01 core research journey  
4. UI-02 (may develop in parallel with research workflow; depends on real artifacts)  
5. Live providers and selected V1 connectors (production V1 path)

UI-02 must not block architecture-validation of the agent path, but MVP **includes** a minimal truthful UI-02.

## Value stream (logical)

`Authenticated research request → Supervisor route → (RAG and/or Web) → Response Synthesis once → Answer with separated citations → UI-01 presentation`  
Parallel track: `AI-DLC artifacts / gates / RAID → UI-02 truthful status` (no fabricated PASS).

## Carry-forward from Stage 3 and RAID (OPEN)

All nine Stage 3 CONDITIONAL GO conditions remain **OPEN**:

1. AWS account existence UNKNOWN  
2. Compliance regime and residency undecided  
3. Production providers, stack, cloud services unselected  
4. V1 integration targets unconfirmed  
5. Budget, cost ceiling, timeline, team capabilities open  
6. Organizational blockers UNKNOWN  
7. Demo reuse requires evidenced gap analysis — **still OPEN** (preliminary assessment CONDITIONALLY ACCEPTED as architecture evidence only; does **not** close condition 7 or DEC-08)  
8. Mock feasibility ≠ live validation ≠ production readiness  
9. Cross-tenant isolation must be implemented and tested before production  

Additional OPEN items carried forward with existing status:

| ID | Item | Status |
| --- | --- | --- |
| I-06 | Project 1 starter sequential Both vs approved parallel Both | OPEN |
| I-07 | Project 2 assessment CONDITIONALLY ACCEPTED as preliminary evidence only | OPEN (as recorded) |
| D-03 | Demo gap analysis | Preliminary recorded; not full closure |
| DEC-08 | Demo component reuse | OPEN — no import authorized |
| A-01 | Parallel Both + synthesis once baseline | ASSUMED / binding for design |

Project 2 (`...\multimodal_research_assistant\multimodal_research_assistant`) remains **reference-only**. No code integration is authorized by this document.

## Timeline

- Provisional planning estimate **14–20 weeks** for enterprise production V1 remains **non-binding**  
- No hard deadline is imposed by Scope Definition  
- Schedule ownership: later Team Formation / Delivery Planning (D-06, DEC-06)

## Explicit non-claims

- This document does **not** approve Stage 4 completion until the human gate  
- This document does **not** authorize Construction, AWS provisioning, deployment, or Project 2 merge  
- Nothing herein is VERIFIED application behavior, PASS, or production GO  

## Traceability

| Scope element | Upstream |
| --- | --- |
| Four agents / routes / parallel Both | Intent Statement; Feasibility; Q1–Q4 |
| UI-01 / UI-02 | Intent Statement; Q1–Q2 |
| Isolation / NFRs | Intent Statement; Feasibility security; Q2, Q7 |
| Mock vs live | Feasibility Q8; Stage 3 conditions 8–9; Q4, Q6 |
| Release slices | Q1, Q6 |
| No hard deadline | Q5; DEC-06 |
| Stage 3 conditions open | Q7; raid-log Stage 3 conditions |
| Project 2 reference-only | Feasibility Q7; C-13; DEC-08; I-07; assessment review |
