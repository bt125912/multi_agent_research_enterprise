# RAID Log

Verification date: 19 November 2026. RAID entries support Feasibility for the approved `intent-statement.md`. Market Research unknowns and conflicts remain in force via `competitive-analysis.md`, `market-trends.md`, and `build-vs-buy.md`.

Status values: **Open**, **Accepted**, **Mitigating**. Evidence labels: **VERIFIED**, **ASSUMED**, **UNKNOWN**, **NOT_VERIFIED**.

## Risks

| ID | Risk | Impact | Likelihood | Mitigation | Owner | Status | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R-01 | Cross-tenant leakage across auth, storage, cache, logs, or agents | Critical | Medium until tested | Isolation as a hard constraint; authorization tests before production | Security/Compliance Reviewer; QA Lead | Open | Requirement VERIFIED; test results UNKNOWN |
| R-02 | Treating mock feasibility as production readiness | High | Medium | Explicit gate between mock path and live-provider validation | Product Owner; QA Lead | Open | Feasibility Q8 VERIFIED |
| R-03 | Premature stack or vendor lock-in | High | Medium | Provider-neutral interfaces; no stack selection in Ideation | Enterprise Architect | Open | Feasibility Q3, Q8 VERIFIED |
| R-04 | Compliance regime chosen late | High | Medium | Keep controls mandatory; regime decision owned by Security/Compliance | Security/Compliance Reviewer | Open | Applicability UNKNOWN |
| R-05 | Integration list never finalized | High | Medium | Extensible connectors; decide V1 connectors in later stages | Product Owner; Enterprise Architect | Open | List UNKNOWN |
| R-06 | Demo reused without gap analysis | Medium | Medium | Brownfield reference only; reuse only after evidenced gap analysis | AI Engineering Lead; QA Lead | Open | Decision VERIFIED |
| R-07 | Cost exceeds unapproved ceiling | Medium | UNKNOWN | Measure USD per request; set ceiling when approved | Product Owner | Open | Ceiling UNKNOWN |
| R-08 | 14–20 week plan slips | Medium | UNKNOWN | Keep estimate provisional; set schedule in Delivery Planning | Product Owner; Delivery | Open | Estimate ASSUMED |
| R-09 | AWS account or cloud readiness assumed wrongly | Medium | Medium | Account existence UNKNOWN; do not provision from Ideation | Enterprise Architect; Platform | Open | NOT_VERIFIED account |
| R-10 | Organizational blocker appears late | Medium | UNKNOWN | Keep blockers as UNKNOWN, not “none” | Product Owner | Open | Q5 VERIFIED as unknown |
| R-11 | Perplexity org-file repository conflict or Amazon Q new-customer closure misread as product weakness | Low | Low | Preserve Market Research conflict and availability wording | Product Owner | Accepted | Market Research VERIFIED claims |

## Assumptions

| ID | Assumption | Status | If wrong |
| --- | --- | --- | --- |
| A-01 | Parallel Both and synthesis once remain the Both-route baseline | ASSUMED | Revisit routing design in Domain / Functional Design |
| A-02 | Build workflow and UIs; replaceable providers remain the commercial direction | ASSUMED / confirmed product decision | Reopen build-vs-buy |
| A-03 | Mock path is enough to finish Ideation feasibility | ASSUMED | Require live providers earlier |
| A-04 | Planning metric baselines stay unmeasured until test evidence exists | ASSUMED | Do not claim PASS |
| A-05 | Role names remain unassigned until Team Formation | ASSUMED | Assign owners when known |
| A-06 | Market Research UNKNOWN items stay unknown until new evidence | ASSUMED | Update Market Research only with approval |

## Issues

| ID | Issue | Status | Notes |
| --- | --- | --- | --- |
| I-01 | AWS account existence not established from project files | Open | Preferred Q6 answer A deferred; recorded as Not yet identified |
| I-02 | Team skill profile not confirmed | Open | Delivery risk |
| I-03 | Organizational blockers not identified | Open | Must not be read as “no blockers” |
| I-04 | Integration systems not listed | Open | Blocks precise integration design, not Ideation exit if accepted open |
| I-05 | EUR-Lex Official Journal HTML NOT_VERIFIED (HTTP 403) in Market Research verification | Open | Summaries cited; full OJ text still NOT_VERIFIED |

## Dependencies

| ID | Dependency | Needed for | Status |
| --- | --- | --- | --- |
| D-01 | Approved Intent Statement | All Feasibility conclusions | VERIFIED available |
| D-02 | Approved Market Research package | Competitive and buy/build context | VERIFIED available |
| D-03 | Later gap analysis of the demo | Any reuse recommendation | Not started |
| D-04 | Provider selection (model, web search, vector) | Live validation and production | Open |
| D-05 | Compliance regime decision | Production authorization path | Open |
| D-06 | Team Formation and Delivery Planning | Timeline, budget, staffing | Open |
| D-07 | Named V1 connector list | Integration delivery | Open |
| D-08 | Authorization and isolation test evidence | Production GO | UNKNOWN |

## Decision register (open)

| ID | Decision | Options in play | Owner | Status |
| --- | --- | --- | --- | --- |
| DEC-01 | Named compliance regime | Candidates in `market-trends.md`; none selected | Security/Compliance Reviewer | Open |
| DEC-02 | Model / embedding / vector / web-search providers | Replaceable; mock allowed now | Product Owner; Enterprise Architect | Open |
| DEC-03 | Exact cloud services and account | Unselected; account UNKNOWN | Enterprise Architect | Open |
| DEC-04 | V1 integration systems | Still to be listed | Product Owner | Open |
| DEC-05 | Cost ceiling | None approved | Product Owner | Open |
| DEC-06 | Delivery schedule | 14–20 weeks provisional only | Product Owner; Delivery | Open |
| DEC-07 | Residency region set | Undecided; isolation mandatory | Security/Compliance Reviewer | Open |
| DEC-08 | Demo component reuse | Only after gap analysis | AI Engineering Lead; QA Lead | Open |
| DEC-09 | Stage 3 Feasibility completion | Approved 19 November 2026 with CONDITIONAL GO for continuing Ideation | Product Owner | Accepted |

## Stage 3 approval conditions (preserved)

Recorded at Stage 3 gate approval. These conditions remain open and binding for later stages:

1. AWS account existence remains UNKNOWN.
2. Compliance regime and residency regions remain undecided.
3. Production providers, technology stack, and cloud services remain unselected.
4. V1 integration targets remain unconfirmed.
5. Budget, cost ceiling, timeline, and team capabilities remain open.
6. Organizational blockers remain UNKNOWN.
7. Existing demo reuse requires an evidenced gap analysis.
8. Mock-based feasibility does not establish live-provider validation or production readiness.
9. Cross-tenant isolation must be implemented and tested before production.

No decision in this register except DEC-09 is closed by Stage 3 approval.
