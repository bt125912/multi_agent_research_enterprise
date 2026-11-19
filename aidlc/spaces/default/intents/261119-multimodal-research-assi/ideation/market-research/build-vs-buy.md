# Build versus Buy

Verification date: 19 November 2026. This assessment records the confirmed answer in the Market Research questions and the approved boundary in `intent-statement.md`. It does not approve a vendor, a cloud service, a compliance regime, a cost ceiling, or a delivery date.

## Confirmed direction

Build the four-agent research workflow, UI-01, and UI-02. The Supervisor routes RAG, Web, Both, or Neither. Both runs RAG and Web in parallel. Response Synthesis runs once. Multimodal RAG keeps text and image provenance. Enterprise security, tenant isolation, observability, scalability, and availability stay in scope as product requirements, not as completed controls.

Buy or partner only for replaceable model, web-search, and cloud services. No provider is selected.

This direction is a Product Owner decision from Question 6. It is not a market-share finding.

## Alternatives considered

| Alternative | Result | Why |
| --- | --- | --- |
| Build the workflow and both workspaces. Keep model, web search, and cloud services replaceable. | Selected as the planning direction | Question 6. The four capabilities and both workspaces are mandatory in `intent-statement.md`. |
| Buy a complete assistant and do not build the four capabilities | Rejected for this product | Question 6 did not select it. The retrieved products do not state the required route set, parallel Both, one synthesis step, and UI-02. Whether they could be configured to do so is UNKNOWN. |
| Build nothing until a market-size study exists | Not selected | The audience is confirmed. TAM, SAM, SOM, customer counts, and revenue remain UNKNOWN and do not by themselves remove the approved scope. |

## What the retrieved market shows

Glean, Microsoft 365 Copilot, Gemini Enterprise, and Perplexity Enterprise describe grounded enterprise answers, and some expose a web or connector path. Amazon Q Business documents grounded, cited answers for existing customers. Its own pages say it is no longer open to new customers. ChatGPT Enterprise sells an enterprise chat workspace with custom pricing and stated admin controls. Sources, prices, and gaps are in `competitive-analysis.md`. Perplexity's organization-file limit is a conflict between two Help Center pages and is not used here as a current entitlement.

Those offers are reasons a buyer might not need a new product. They are not proof that any offer meets this product's route, provenance, tenancy, and control-center requirements. Replacing the whole product with one of them would drop approved scope unless a later evaluation shows otherwise. That evaluation is open.

## Cost uncertainty

| Item | Status | Owner |
| --- | --- | --- |
| This product's cost per request and any dollar ceiling | UNKNOWN. Not approved | Product Owner |
| Glean seat price | UNKNOWN on the retrieved pages | Not a selected vendor |
| Microsoft 365 Copilot add-on | $30 per user per month, paid yearly, plus a qualifying Microsoft 365 plan. Marketing price. Contract price UNKNOWN | Not a selected vendor |
| Gemini Enterprise Business | Starting at $21 per user per month on the retrieved page. Other editions UNKNOWN | Not a selected vendor |
| ChatGPT Enterprise | Custom. Public seat price UNKNOWN | Not a selected vendor |
| Perplexity Enterprise Pro and Max | $40 or $325 per seat per month, or $400 or $3,250 per year. Published seat prices. API use is not included. Discounts may exist for teams of 250 or more. The 500-file repository is not a verified current entitlement | Not a selected vendor |
| Amazon Q Business | Lite $3 or Pro $20 per user per month, plus index units at $0.140 or $0.264 per hour. Published extras: $0.003 per image, $0.006 per audio minute, $0.050 per video minute, and $200 for 30,000 anonymous-use units. Index charges continue until the index is deleted. Not open to new customers. Existing customers can continue. Contract price UNKNOWN | Not a selected vendor |
| Model and web-search charges above any seat price | UNKNOWN for a future design | Product Owner, after a vendor is proposed |

Using a published seat price as this product's cost would be unsupported. The 14–20 week planning estimate remains provisional for Team Formation and Delivery Planning.

## Lock-in and ownership

Choosing one model, web-search, or cloud provider before the architecture stages would convert a replaceable option into lock-in. Question 6 keeps those options open. The Enterprise Architect owns the later architecture trade-offs, including ECS Fargate versus EKS and API Gateway VPC Link, which are recorded for Infrastructure Design and are not decided here. The Security/Compliance Reviewer must agree the control set. The QA Lead owns verification evidence. The Release Approver authorizes production. Names for those roles are still unassigned.

## Decision still open

No build-versus-buy conclusion says the product is commercially viable. No compliance regime is chosen. The EU AI Act, GDPR, India's DPDP Act, the California CCPA as amended, and the NIST AI RMF were retrieved as research candidates in `market-trends.md`. Their applicability to this product is UNKNOWN. No competitor is rejected for a weakness that was not stated by its own page. Amazon Q Business remains unselected. Its new-customer closure is a published limitation, not a vendor decision for this product.
