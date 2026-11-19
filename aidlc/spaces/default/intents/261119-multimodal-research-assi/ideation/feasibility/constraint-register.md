# Constraint Register

Verification date: 19 November 2026. Sourced from `intent-statement.md`, confirmed Feasibility answers, and Market Research artifacts (`competitive-analysis.md`, `market-trends.md`, `build-vs-buy.md`). Constraints are requirements or limits on the solution. They are not architecture selections.

| ID | Type | Constraint | Binding | Status | Evidence / owner |
| --- | --- | --- | --- | --- | --- |
| C-01 | Product | Four agents: Supervisor (RAG / Web / Both / Neither), Multimodal RAG, Web Search, Response Synthesis | Hard | VERIFIED requirement | `intent-statement.md` |
| C-02 | Product | Both runs RAG and Web in parallel; synthesis once | Hard | ASSUMED planning baseline | `intent-statement.md` |
| C-03 | Product | Text and image retrieval with provenance; internal vs external sources kept distinct | Hard | VERIFIED requirement | `intent-statement.md` |
| C-04 | Product | UI-01 and UI-02 in first production release; UX/API deferred | Hard | VERIFIED proposed scope | `intent-statement.md` |
| C-05 | Security | Multi-tenant isolation across authentication, authorization, ingestion, retrieval, storage, caching, logs, and agent execution | Hard | VERIFIED requirement | Feasibility Q9 |
| C-06 | Security | Privacy, classification, audit, retention, residency, access control required | Hard | VERIFIED requirement | `intent-statement.md` |
| C-07 | Compliance | Named legal or assurance regime not chosen | Open | UNKNOWN applicability | Feasibility Q2; `market-trends.md` |
| C-08 | Build | Build workflow and both UIs; buy/partner only for replaceable model, web search, cloud | Hard | VERIFIED product decision | `build-vs-buy.md`; Market Research Q6 |
| C-09 | Integration | Multiple enterprise systems still to be listed; extensible connector framework; not all integrations in V1 | Soft on list / Hard on extensibility | List UNKNOWN | Feasibility Q1 |
| C-10 | Technology | Do not prematurely select implementation stack | Hard for this stage | Open | Feasibility Q3 |
| C-11 | Providers | Provider-neutral interfaces for LLM, embeddings, vector retrieval, web search | Hard direction | ASSUMED | Feasibility Q8 |
| C-12 | Providers | Mock/stub acceptable for early feasibility; live providers unselected | Soft for Ideation / Hard before production | VERIFIED decision | Feasibility Q8 |
| C-13 | Brownfield | Demo is reference only; not production baseline; gap analysis before reuse | Hard | VERIFIED decision | Feasibility Q7; Intent assumptions |
| C-14 | Delivery | Timeline and budget open until Team Formation and Delivery Planning | Soft | Open | Feasibility Q4 |
| C-15 | Delivery | 14–20 week estimate provisional only | Soft | ASSUMED estimate | Market Research diary; Feasibility Q4 |
| C-16 | Financial | Cost ceiling not approved | Soft | UNKNOWN | `intent-statement.md` |
| C-17 | Platform | Exact AWS or other cloud services unselected | Open | UNKNOWN | Feasibility Q6; Intent |
| C-18 | Platform | AWS account existence | Open | UNKNOWN / NOT_VERIFIED | Repo: no account id; terraform README says nothing provisioned |
| C-19 | Organization | Organizational blockers | Open | UNKNOWN | Feasibility Q5 |
| C-20 | Organization | Team skill profile | Open | UNKNOWN | Feasibility Q3 |
| C-21 | Market | Preserve Market Research UNKNOWN items, conflicts, and deferred decisions | Hard | VERIFIED carry-forward | Market Research package |
| C-22 | Ideation | No application code, AWS provisioning, deploy, or push from this stage without separate authorization | Hard | VERIFIED process | Product Owner instructions |

## Notes

- Hard means the Product Owner has bound the product or this stage to the constraint.
- Soft or Open means the item constrains planning but is not yet a fixed approved value.
- Resolving C-07, C-09 list, C-16, C-17, C-18, C-19, and C-20 is required before an unconditional production GO. It is not required to leave Ideation after a Stage 3 approval that keeps them open.
