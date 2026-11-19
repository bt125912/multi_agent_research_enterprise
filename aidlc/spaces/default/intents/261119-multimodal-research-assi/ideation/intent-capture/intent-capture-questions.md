# Intent Capture Questions

## Sources

- [desc] Initial description: "Continue the official AWS AI-DLC 2.11.4 workflow for the Multi-Agent Multimodal Research Assistant. Inspect the installed AWS AI-DLC instructions, current lifecycle state, completed artifacts, pending approvals and supported harness extension points. Resume from the actual current workflow checkpoint. Do not restart completed stages or invent a custom lifecycle. Use README.md, CONTENT.md, ACCEPTANCE_CRITERIA.md and docs/architecture/ARCHITECTURE_REFERENCE.md as project reference material, where present. Preserve the four mandatory capabilities: Supervisor Agent routes RAG, Web, Both or Neither; Multimodal RAG Agent retrieves text and images with source references; Web Search Agent uses a supplied search tool or mock API; Response Synthesis combines, deduplicates and distinguishes internal and external evidence. Within the official AI-DLC workflow, assess component ownership, LangGraph orchestration, API Gateway, Model Gateway, ingestion, retrieval, data stores, security, deployment and acceptance criteria AC-01 through AC-20. Use the framework prescribed artifact locations, naming conventions, stage transitions and human approval checkpoints. Do not create parallel governance structures or overwrite framework-owned files. For each capability distinguish VERIFIED, IMPLEMENTED_NOT_TESTED, PARTIAL, MISSING and BLOCKED, based on actual repository evidence. Complete only the work authorized by the current AI-DLC stage. Do not begin Construction, modify application code, deploy, or push commits without explicit approval."
- [scope] Workflow-selected scope: `enterprise`.

## Q1. [Product] What business problem is this initiative solving?

The request names a research assistant and four capabilities. This question fixes the problem those capabilities exist to solve.

A. People need one grounded answer that keeps internal documents distinct from external web evidence
B. An existing research process is too slow or inconsistent for the people who depend on it
C. The existing starter must be assessed and governed before any further build
D. Not yet defined
E. Not applicable
X. Other (please specify)

[Answer]: X. Other (please specify): A secure, scalable, multi-tenant research platform that combines internal organizational knowledge and external web information while preserving evidence provenance and organizational isolation.

## Q2. [Product] Who is the customer?

This decides whose pain the first version is accountable for.

A. Internal researchers or analysts in one organization
B. External customers of a product
C. Both internal users and external customers
D. Not yet defined
E. Not identified
X. Other (please specify)

[Answer]: X. Other (please specify): Enterprise research and knowledge-management teams, as customers of that platform.

## Q3. [Product] What pain are those people experiencing?

Success and scope depend on the pain, not on a technology choice.

A. Answers are not tied to sources they can check
B. Internal material and web results are gathered separately and combined by hand
C. They cannot rely on the current starter for a real research answer
D. Not yet defined
E. Not identified
X. Other (please specify)

[Answer]: X. Other (please specify): Answers are not tied to sources they can check, and one organization's evidence must not be mixed with another's.

## Q4. [Product] What does success look like for this first version?

Name the outcome a reviewer can check. Measurable targets that are not chosen yet stay open.

A. One question returns one answer, and internal sources stay distinct from external sources
B. The four routes — internal only, web only, both, and neither — are specified and can be reviewed
C. Success measures are not chosen yet
D. Not yet defined
E. Not applicable
X. Other (please specify)

[Answer]: A. One question returns one answer, and internal sources stay distinct from external sources. Proposed planning baselines, not measured results: routing accuracy 100% on a labeled route set with parallel Both and synthesis once; citation validity 100% of citations resolve to a returned source; grounded answer quality at least 95% on a labeled set; text and image Recall@5 at least 90% separately; p95 latency at or under 20 seconds for a completed research request in the agreed staging profile; availability 99.9% of research requests over a rolling 30 days excluding an approved provider outage; zero cross-tenant reads in the authorization test set; cost is measured in USD per request and has no approved ceiling. Proposed product outcomes, pending this stage's approval: UI-01 lets a researcher submit a question, upload documents and images, see ingestion status and RAG, Web, Both, and Neither execution, read one grounded answer with citations and separate internal and external source previews, and review research history, with tenant-aware authentication and authorization plus agent status, errors, and retry feedback. UI-02 lets the engineering roles see the actual lifecycle phase and stage, official approval checkpoints, requirements traceability, work-package progress, four-agent capability status, automated testing and quality evidence, risks, assumptions, decisions, and deployment and production readiness. UI-02 reads lifecycle artifacts and verification evidence. It does not hardcode progress or invent a PASS status.

## Q5. [Product] Why is this initiative happening now?

The trigger decides what this pass must settle before later design.

A. There is an opportunity to offer a research assistant
B. The existing starter needs a governed path from assessment to a later build
C. Regulation, audit, or compliance pressure
D. Not yet defined
E. Not identified
X. Other (please specify)

[Answer]: A. There is an opportunity to offer a research assistant

## Q6. [Product] Who are the key stakeholders, and what does each care about?

Only people you name here will appear in the stakeholder map.

A. A product owner and the people who will ask research questions
B. A product owner, the people who ask questions, and a security or compliance reviewer
C. One person is both the owner and the user
D. Not identified
E. Not yet defined
X. Other (please specify)

[Answer]: X. Other (please specify): Product Owner, Enterprise Architect, AI Engineering Lead, Security/Compliance Reviewer, QA Lead, and Release Approver, plus researchers, analysts, knowledge workers, and administrators. Names are TBD. Proposed users, pending this stage's approval: researchers, analysts, and knowledge workers use UI-01, and administrators use its tenant-aware access. The Product Owner, Enterprise Architect, AI Engineering Lead, Security/Compliance Reviewer, QA Lead, and Release Approver use UI-02.

## Q7. [Product] Who decides scope and priority, and who influences those decisions?

This separates the person who can approve a change from people who advise.

A. One product owner decides; others advise
B. A named group must agree before scope changes
C. Not yet defined
D. Not identified
E. Not applicable
X. Other (please specify)

[Answer]: X. Other (please specify): Product Owner decides business scope and priority. Enterprise Architect is accountable for architecture decisions. AI Engineering Lead is accountable for agent implementation. Security/Compliance Reviewer must agree security and compliance controls. QA Lead owns verification evidence. Release Approver authorizes production. Names are TBD.

## Q8. [Product] What communication or reporting is required besides the workflow approval checkpoints?

This covers status reporting to people outside the approval gates.

A. The approval checkpoints are enough
B. A regular written status is also required
C. No additional reporting
D. Not yet defined
E. Not applicable
X. Other (please specify)

[Answer]: X. Other (please specify): AI-DLC artifacts remain the approval authority. Checkpoint reporting also shows lifecycle status, traceability, work-package status, automated verification, security and quality gates, risks, dependencies, assumptions, infrastructure and model cost, and production readiness. GitHub Projects and the Excel workbook do not approve stages. UI-02 is the proposed product surface for that visibility, and it reads actual lifecycle artifacts and verification evidence.

## Q9. [Product] What should this first version leave out?

The workflow scope is already enterprise. This question is only about the product boundary. The four named capabilities stay in the request unless you explicitly set them aside here.

A. Production deployment, live customer traffic, and operations
B. Anything beyond the four named research capabilities and an evidence-based assessment of the existing starter
C. Separation between organizations, and regulated-audit evidence
D. Not yet defined
E. None
X. Other (please specify)

[Answer]: X. Other (please specify): The first production release does not select a model vendor, web-search provider, exact cloud service, or named compliance regime. It does not leave out the four capabilities or the enterprise security controls. UI-01 and UI-02 are proposed product scope, not exclusions. Detailed UX design, API contracts, and implementation planning for both are deferred to later official stages. This stage does not change application code.

## Q10. [Product] Which compliance obligations apply to this first version?

Facts about your obligations cannot be inferred from an empty project-rules file.

A. No specific regulation applies to this first version
B. Personal data must be protected, and the exact regime is not named yet
C. Not yet defined
D. Not applicable
E. Not identified
X. Other (please specify)

[Answer]: X. Other (please specify): Privacy, data classification, tenant isolation, audit logging, retention, residency, and access control are required. The named legal regime is not chosen.

## Q11. [Product] Who must the first version serve?

This is the customer boundary, not a deployment design.

A. One organization and one group of users
B. Many organizations whose information must stay separate
C. A single user on one machine
D. Not yet defined
E. Not identified
X. Other (please specify)

[Answer]: B. Many organizations whose information must stay separate

## Q12. [Product] What outcome must be approved before any application change?

Construction is not authorized. This records what you need from the work before a build.

A. An approved problem statement, customer, success measure, and product boundary
B. An approved inception plan that traces requirements to acceptance evidence, still with no application changes
C. Not yet defined
D. Not applicable
E. None
X. Other (please specify)

[Answer]: B. An approved inception plan that traces requirements to acceptance evidence, still with no application changes

## Consolidated Summary Confirmation

Does this all look correct before I generate the artifact?

- Looks correct
- Request changes

[Answer]: Looks correct

## Requested Changes Feedback

What should change?

[Answer]: Include two proposed product-scope additions in Intent Capture. UI-01 Enterprise Research Assistant Workspace: research question input, document and image upload, ingestion status, Internal RAG, Web, Both, and Neither execution visibility, grounded answers with citations, internal and external source previews, research history, tenant-aware authentication and authorization, and agent execution status, errors, and retry feedback. UI-02 AI-DLC Engineering Control Center: lifecycle phase and stage tracking, official approval checkpoint visibility, requirements traceability, work-package implementation progress, four-agent capability status, automated testing and quality evidence, risks, assumptions, and decisions, and deployment and production readiness. Record business purpose, target users, and expected outcomes. Defer detailed UX design, API contracts, and implementation planning. The Control Center must read actual lifecycle artifacts and verification evidence and must not hardcode progress or invent PASS statuses. Do not modify application code or begin Construction. Continue preparing the Intent Statement and Stakeholder Map and stop at the Stage 1.1 approval checkpoint.

## Assumption Confirmation

These statements stay assumptions until you accept them. Acceptance does not turn an assumption into a measured result or a closed decision.

- Role names for Product Owner, Enterprise Architect, AI Engineering Lead, Security/Compliance Reviewer, QA Lead, and Release Approver are not assigned. [assumption]
- The model vendor, web-search provider, exact cloud services, named compliance regime, and cost ceiling are not chosen. [assumption]
- The routing, citation, grounding, retrieval, latency, availability, tenant-isolation, and cost figures are planning baselines and have not been measured. [assumption]
- UI-01 and UI-02 are proposed product scope. Their detailed UX design, API contracts, and implementation planning are deferred to later stages. [assumption]
- The existing demo is not the target production architecture, and no capability in this intent is recorded as VERIFIED, PASS, or GO. [assumption]

A. Accept assumptions
B. Convert to follow-up questions

[Answer]: A. Accept assumptions
