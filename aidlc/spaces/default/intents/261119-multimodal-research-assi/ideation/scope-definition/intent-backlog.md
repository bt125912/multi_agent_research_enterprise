# Intent Backlog

**Stage:** Scope Definition (1.4)  
**Companion:** `scope-document.md`  
**Status:** Draft for Stage 4 human review — **not** Stage 4 approved  
**Revision:** Gate Request Changes remediation (20 November 2026) — PARTIAL ACs strengthened  
**Prioritization:** MoSCoW primary; WSJF-style relative order within Must (higher = earlier)

Proto-Units below are planning items for later Units Generation / Delivery Planning. They do not authorize Construction.

## Priority legend

| MoSCoW | Meaning in this backlog |
| --- | --- |
| Must | Required for architecture-validation MVP and/or production V1 essentials |
| Should | Important for production V1; may follow MVP |
| Could | Advanced / future |
| Won't | Explicitly deferred or prohibited now |

## Backlog items (summary)

| ID | Proto-Unit / Capability | MoSCoW | Slice | Depends on | WSJF | Trace |
| --- | --- | --- | --- | --- | --- | --- |
| IB-01 | Enterprise security foundations: authentication, RBAC, authorization, tenant isolation, audit, provenance, observability | Must | MVP foundations → V1 verified | — | 1 | Intent NFRs; Feasibility security; Q2–Q4; Stage 3 #9 |
| IB-02 | Provider-neutral **multimodal** RAG contract + mock/stub (text + image) | Must | MVP | IB-01 | 2 | Intent Multimodal RAG; Q3–Q4; Feasibility Q8 |
| IB-03 | Provider-neutral Web contract + mock/stub (fail-closed) | Must | MVP | IB-01 | 2 | Intent Web; Q3–Q4; Feasibility Q8 |
| IB-04 | Supervisor four-route decisions | Must | MVP | IB-02, IB-03 | 3 | Intent Supervisor; Q1–Q2 |
| IB-05 | Parallel Both, deterministic safe join, single synthesis | Must | MVP | IB-02, IB-03, IB-04 | 3 | Intent Both; Q1–Q4; **I-06 OPEN** |
| IB-06 | Response Synthesis with internal/external separation | Must | MVP | IB-05 | 4 | Intent Synthesis; Q1–Q2 |
| IB-07 | Research API exposing the workflow | Must | MVP | IB-04–IB-06 | 5 | Intent; Q3 |
| IB-08 | UI-01 Enterprise Research Workspace (MVP vs V1 split) | Must | MVP + V1 verify | IB-07 | 6 | Intent UI-01; Q1–Q2 |
| IB-09 | UI-02 truthful lifecycle control center (minimal) | Must | MVP | Real AI-DLC artifacts | 6 | Intent UI-02; Q1–Q3 |
| IB-10 | Citation / provenance validation + fail-closed harness | Must | MVP→V1 | IB-06 | 7 | Intent metrics; ACCEPTANCE |
| IB-11 | Isolation / authentication / RBAC / authorization test suite | Must | **Production V1 security gate** | IB-01 | 8 | Stage 3 #9; R-01; D-08 |
| IB-12 | Live provider adapters (model, web) | Should | Production V1 | IB-02, IB-03; DEC-02 | 9 | Stage 3 #3, #8; Q6 |
| IB-13 | Extensible connector framework | Should | Pre-V1 connectors | IB-01 | 10 | Feasibility; Q6 |
| IB-14 | Selected V1 enterprise connectors | Should | Production V1 | IB-13; DEC-04 | 11 | Stage 3 #4; DEC-04 OPEN |
| IB-15 | Resolve I-06 (parallel Both vs starter sequential) | Must | Design before/at Construction | IB-05 | 3 | I-06; A-01 — **I-06 remains OPEN** until verified |
| IB-16 | Rich admin analytics | Could | Advanced/future | IB-08 | — | Q2, Q6 |
| IB-17 | Optional additional agents | Could | Advanced/future | IB-04 | — | Q2, Q6 |
| IB-18 | Provider-specific tuning | Could | Advanced/future | IB-12 | — | Q2, Q6 |
| IB-19 | Project 2 lift-and-shift / code merge | Won't | — | — | — | I-07; DEC-08; Stage 3 #7 |
| IB-20 | Hard calendar deadline for V1 | Won't | — | — | — | Q5; DEC-06 |

## Acceptance criteria detail (remediated)

### IB-01 — Enterprise security foundations

**Must include explicit naming of:** authentication, **RBAC**, and authorization (not “authz” alone).

| Criterion | Requirement |
| --- | --- |
| Authentication | Every research, ingest, and admin action requires an authenticated principal (design in MVP; live IdP may be stubbed in architecture-validation) |
| RBAC | Role-based access control defines permitted actions for researcher, admin, and engineering roles (names may remain unassigned per Intent) |
| Authorization | Authorization checks enforce tenant-aware access control on every protected operation |
| Tenant-aware access | Tenant context is bound to the principal; no cross-tenant data visibility by default |
| Cross-tenant denial | Cross-tenant access is **denied** across **ingestion, retrieval, storage, API, and agent execution** |
| Audit / provenance | Security-relevant events and evidence provenance are recorded; no invented security PASS |
| Observability | Foundations for logs/metrics/traces of security-relevant failures |

**Slice:** Architectural foundations in **architecture-validation MVP** (may use one tenant for demo if multi-tenant-ready). **Production security verification** (live IdP, full RBAC test evidence, isolation suite) is a **separate release gate** via **IB-11** — not claimed by MVP alone.

### IB-11 — Production security verification gate

| Criterion | Requirement |
| --- | --- |
| Scope | Authentication, RBAC, authorization, and tenant isolation **test evidence** |
| Cross-tenant | Zero successful cross-tenant reads/writes in the agreed authorization test set across ingestion, retrieval, storage, API, and agent execution |
| Gate | Required before **production V1 GO**; does not close Stage 3 condition 9 until evidence exists |
| Separation | Distinct from MVP foundations (IB-01); mock/demo security ≠ production verification |

### IB-05 — Parallel Both and safe join

| Criterion | Requirement |
| --- | --- |
| Concurrency | When route = Both, RAG and Web retrieval **execute concurrently** (not sequential) |
| Deterministic join/barrier | A defined barrier waits for both branches (or their terminal failure/timeout states) before synthesis; join order of completion does not change semantic outcome |
| Timeout | Each branch has an explicit timeout; on timeout the branch terminates with a structured failure/empty outcome — not a fabricated result |
| Cancellation | Cancellation of the parent request cancels in-flight branches where supported; no orphaned silent success |
| Partial failure | If one branch fails or times out and the other succeeds, synthesis still runs **at most once**, using successful evidence plus structured failure metadata; answer must not pretend the failed branch succeeded |
| Synthesis count | **Exactly one** Response Synthesis invocation per applicable research request (including Both, and routes that reach synthesis) |
| Automated verification | Tests must assert concurrency (or equivalent instrumentation) and **invocation count = 1** for synthesis before marking IB-05 VERIFIED |
| I-06 | **I-06 remains OPEN** until implementation is verified against the approved parallel baseline; starter sequential Both is not the approved design |

### IB-02 — Multimodal RAG

| Criterion | Requirement |
| --- | --- |
| Modalities | Explicitly supports **text and image** modalities |
| Ingestion | Accepts approved document/image types into the tenant-scoped corpus path (mock OK in MVP) |
| Indexing | Text and images are indexed with modality metadata and source references |
| Retrieval | Query may return text and/or image evidence with scores/references; empty corpus returns empty set — **no fabricated hits** |
| Source references | Every returned item includes a resolvable source reference |
| Tenant / authz | Retrieval and ingest respect IB-01 tenant and authorization boundaries |

### IB-03 — Web contract (fail-closed)

| Criterion | Requirement |
| --- | --- |
| No fabrication | Never invent URLs, snippets, or web evidence |
| Empty / unset | Unset mock or empty provider → empty external set |
| Provider failure | HTTP/provider errors → structured failure; empty or error-tagged external set — **not** a successful invented answer |
| Timeout | Exceeded timeout → structured timeout outcome; no silent success |
| Malformed response | Invalid JSON/schema → reject/fail-closed; do not coerce into fake hits |
| Synthesis handoff | Failures surface as structured warnings/errors to IB-05/IB-06/IB-10 |

### IB-10 — Citation / provenance validation (fail-closed)

| Criterion | Requirement |
| --- | --- |
| No fabricated citations | Citations must resolve to returned evidence; unresolved citations **FAIL** |
| Provenance validation | Origin (internal/external) and reference required for cited items |
| Operational failures | Provider failure, empty result, timeout, malformed response must not be converted into a successful research result with invented sources |
| Structured errors | Harness records structured error codes/outcomes for missing provenance |

### IB-05 / IB-03 / IB-10 — Fail-closed rule (cross-cutting)

Operational failures (provider down, empty, timeout, malformed) **must not** silently become successful research results with fabricated web results or citations.

### IB-08 — UI-01 Enterprise Research Workspace

| Capability | Architecture-validation MVP | Production V1 verification |
| --- | --- | --- |
| Query submission | **Required** | Required + verified UX/NFR |
| Document upload | **Required** (minimal path; may use mock ingest) | Required + validated type/size/malware controls |
| Ingestion status | **Required** (show status including failure) | Required + accurate async job states |
| Research history | **Required** (tenant-scoped list/detail minimal) | Required + retention/ACL verified |
| Response display | **Required** | Required |
| Citations | **Required** | Required + citation validity evidence |
| Provenance / internal vs external | **Required** | Required |
| Route visibility (RAG/Web/Both/Neither) | **Required** | Required |
| Tenant-aware authn/RBAC/authz hooks | Design + demo binding **Required** | Live authentication/RBAC **verified** via IB-11 |
| Agent status / errors / retry feedback | **Required** (structured errors visible) | Required + operational SLOs |

UI-01 Must for scope; MVP delivers the research journey above without claiming production security or live-provider GO.

## Dependency graph (summary)

```text
IB-01 foundations (authn, RBAC, authz, isolation)
  ├─ IB-02 multimodal RAG ─┐
  ├─ IB-03 Web fail-closed ─┼─ IB-04 Supervisor ─ IB-05 parallel Both + safe join ─ IB-06 Synthesis ─ IB-07 API ─ IB-08 UI-01
  └─ IB-11 production security gate              │
                                                 └─ IB-10 citation/provenance fail-closed
AI-DLC artifacts ──────────────────────────────── IB-09 UI-02
IB-02/03 ─ IB-12 live adapters (V1)
IB-01 ─ IB-13 connector framework ─ IB-14 V1 connectors
IB-05 ↔ IB-15 resolve I-06 (I-06 OPEN until verified)
```

## Slice mapping

| Slice | Backlog IDs |
| --- | --- |
| Architecture-validation MVP | IB-01–IB-10 (foundations + mocks), IB-15 (design), IB-08 MVP column |
| Production V1 | IB-11 security gate; IB-12; IB-13–IB-14 when named; IB-08 V1 column; Stage 3 conditions with evidence |
| Advanced / future | IB-16–IB-18 |
| Explicit Won't now | IB-19, IB-20 |

## Requirement traceability matrix (RTM)

| Requirement (upstream) | Backlog coverage |
| --- | --- |
| Supervisor RAG/Web/Both/Neither | IB-04, IB-05 |
| Parallel Both + synthesis once + safe join | IB-05, IB-06, IB-15 |
| Multimodal RAG text+image + source refs | IB-02, IB-06, IB-10 |
| Web search tool or mock; fail-closed | IB-03, IB-12 |
| Internal vs external evidence | IB-06, IB-10 |
| UI-01 research workspace (query, upload, status, history, citations) | IB-08 |
| UI-02 control center; no invented PASS | IB-09 |
| Authentication, RBAC, authorization, tenant isolation | IB-01, IB-11 |
| Provider-neutral; mock early | IB-02, IB-03, IB-12 |
| Stage 3 nine conditions OPEN | Carried in `scope-document.md`; not closed here |
| Demo reference-only / DEC-08 | IB-19 Won't; I-07; D-03; DEC-08 OPEN |
| I-06 parallel vs sequential | IB-05, IB-15; **OPEN** until verified |

## Open issues affecting backlog

| ID | Impact on backlog | Status |
| --- | --- | --- |
| I-06 | IB-05 / IB-15; no VERIFIED parallel Both until implementation proves concurrency + join + single synthesis | **OPEN** |
| I-07 / DEC-08 / D-03 / Stage 3 #7 | No Project 2 import | **OPEN** |
| Stage 3 #1–#6, #8–#9 | Production V1 gated; MVP may proceed with mocks and foundations | **OPEN** |
| DEC-02–DEC-07 | Provider, cloud, connectors, budget, schedule, residency | **OPEN** |

## Non-claims

- No backlog item is VERIFIED as implemented by this document  
- Empty or demo code in Project 1/2 is not acceptance evidence  
- Stage 4 gate remains for human Approve / Request Changes  
- 14–20 week estimate remains provisional and non-binding (IB-20)  
