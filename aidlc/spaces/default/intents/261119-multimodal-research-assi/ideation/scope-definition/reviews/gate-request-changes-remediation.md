# Stage 4 Gate — Request Changes Remediation

**Date:** 20 November 2026  
**Decision:** Request Changes (human) — Stage 4 **not** approved  
**Artifacts updated:** `scope-document.md`, `intent-backlog.md`  
**Preserved OPEN:** Stage 3 conditions 1–9; I-06; I-07; D-03; DEC-08; Project 2 reference-only; 14–20 weeks non-binding

## Remediation map

| Gate PARTIAL | Change | Where |
| --- | --- | --- |
| IB-01 / IB-11 security | Named authentication, RBAC, authorization; tenant-aware ACL; cross-tenant denial across ingestion/retrieval/storage/API/agents; IB-11 as separate production security gate | `intent-backlog.md` IB-01/IB-11 detail; `scope-document.md` MVP + V1 + Must table |
| IB-05 safe join | Concurrent Both; deterministic barrier; timeout/cancel/partial-failure; exactly one synthesis; automated concurrency + invocation-count tests; I-06 stays OPEN | `intent-backlog.md` IB-05; `scope-document.md` MVP bullets |
| IB-02 multimodal | Text + image; ingest/index/retrieve/source-ref ACs; tenant/authz boundaries | `intent-backlog.md` IB-02; scope Must + MVP |
| Fail-closed IB-03/05/10 | No fabricated web/citations; provider failure/empty/timeout/malformed; structured errors; no silent success | `intent-backlog.md` IB-03, IB-10, cross-cutting rule; scope MVP |
| IB-08 UI-01 | Query, upload, ingest status, history, response, citations, provenance; MVP vs V1 verification columns | `intent-backlog.md` IB-08; scope MVP + V1 |

## Non-changes (preserved)

- All nine Stage 3 CONDITIONAL GO conditions remain OPEN  
- Project 2 reference-only; DEC-08 / D-03 / I-06 / I-07 unresolved as recorded  
- Architecture-validation MVP vs production V1 vs advanced/future separation  
- UI-02 never invents PASS  
