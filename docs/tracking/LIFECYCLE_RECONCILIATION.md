# Lifecycle reconciliation

The workbook at `docs/tracking/AWS_AIDLC_Enterprise_End_to_End_Project_Tracker.xlsx` is a proposed tracking reference. It does not define the workflow. Installed Enterprise stages come from `.cursor/tools/data/stage-graph.json` and `.cursor/scopes/aidlc-enterprise.md`. Framework files were not changed.

The installed graph has 33 stages. Initialization has 3 stages and is already complete. The remaining 30 are the Enterprise stages with approval gates. The workbook also has 30 rows and the same phase counts (7, 9, 7, 7), but most names and the order do not match. Its own Tracking Guide says those titles are placeholders.

Nothing below is VERIFIED, PASS, or GO.

## Initialization (complete, not in the workbook)

| Installed stage | Workbook |
|---|---|
| Workspace Scaffold | Absent |
| Workspace Detection | Absent |
| State Initialization | Absent |

## Ideation

| Installed stage | Workbook row | Difference |
|---|---|---|
| Intent Capture & Framing | ID-01 Intent Capture & Framing | Same name. Status in the workflow is RUNNING, approval PENDING. |
| Market Research | ID-02 Market Research | Same name. Not started. |
| Feasibility & Constraints | ID-06 Solution Concept & Feasibility | Different name and position. |
| Scope Definition | None | Absent from the workbook. |
| Team Formation | None | Absent from the workbook. |
| Rough Mockups | None | Absent from the workbook. |
| Approval & Handoff | ID-07 Ideation Review & Approval | Different name. |
| None | ID-03 User & Stakeholder Discovery | Not an installed stage. |
| None | ID-04 Problem / Opportunity Validation | Not an installed stage. |
| None | ID-05 Value Proposition | Not an installed stage. |

## Inception

| Installed stage | Workbook row | Difference |
|---|---|---|
| Reverse Engineering | ID-04 Current-State Architecture | Different name. This is the first Inception stage for existing code. |
| Practices Discovery | None | Absent from the workbook. |
| Requirements Analysis | IN-02 Requirements Analysis | Same name, different position. |
| User Stories | None | Absent from the workbook. |
| Refined Mockups | None | Absent from the workbook. |
| Domain Design | None | Absent from the workbook. |
| Units Generation | IN-07 Delivery Decomposition & Estimates | Different name. Delivery Planning is a separate installed stage. |
| Contract Design | None | Absent from the workbook. |
| Delivery Planning | IN-07 Delivery Decomposition & Estimates | Combined in the workbook with decomposition. |
| None | IN-01 Requirements Discovery | Not an installed stage. |
| None | IN-03 NFR & Compliance Baseline | NFR Requirements and NFR Design are Construction stages. |
| None | IN-05 Target Architecture | Not an installed stage. |
| None | IN-06 Architecture Decisions & Threat Model | Not an installed stage. |
| None | IN-08 Acceptance / Verification Planning | Not an installed stage. |
| None | IN-09 Inception Review & Approval | Not an installed stage. Each stage has its own approval gate. |

## Construction

Installed stages, in order: Functional Design, NFR Requirements, NFR Design, Infrastructure Design, Code Generation, Build and Test, CI Pipeline.

The workbook instead lists Platform & API Foundation, Supervisor / LangGraph, Multimodal Ingestion & RAG, Web Search Integration, Response Synthesis & Citation Engine, Security / Observability / Integration, and Construction Verification & Approval. Those are proposed work packages. They are not the installed Construction stages. Construction is not authorized.

## Operation

| Installed stage | Closest workbook row | Difference |
|---|---|---|
| Deployment Pipeline | OP-01 Environment & Release Preparation | Different name. |
| Environment Provisioning | OP-02 Staging Deployment | Different name. |
| Deployment Execution | OP-06 Production Deployment & Monitoring | Different name. The workbook splits staging and production into separate rows. |
| Observability Setup | OP-06 Production Deployment & Monitoring | Folded into a deployment row. |
| Incident Response | None | Absent from the workbook. |
| Performance Validation | OP-04 Security / Performance / Resilience | Different name and broader scope. |
| Feedback & Optimization | OP-07 Operational Handover & Closure | Different name. |
| None | OP-03 Functional / E2E / RAG Evaluation | Not an installed stage. |
| None | OP-05 Production Readiness / UAT | Not an installed stage. |

## Current checkpoint

Intent Capture & Framing is RUNNING. Human approval is PENDING. No stage is GO.
