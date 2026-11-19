# Competitive Analysis

Verification date for every source below: 19 November 2026. A publication or update date is recorded when the reopened page showed one. These pages are vendor documentation, not a determination of the customer's legal jurisdiction.

This comparison serves the approved `intent-statement.md`: a secure multi-tenant research platform that combines internal knowledge and external web information, with the four mandatory capabilities, parallel Both, synthesis once, UI-01, and UI-02. Named products are candidates from the confirmed questions. A missing capability in this table means it was not found in the retrieved pages. It is not a verified weakness.

## Method

Each material claim is marked VERIFIED, INFERRED, or UNKNOWN. VERIFIED means the cited page stated it. INFERRED means a limited reading of that page. UNKNOWN means this pass did not retrieve a source for it. Public prices are list or marketing prices. Negotiated enterprise prices are UNKNOWN for every candidate.

## Candidate coverage

| Candidate | Category | Retrieved primary page | Dollar price found |
| --- | --- | --- | --- |
| Glean | Internal-knowledge assistant | Vendor docs and product page | No public seat price found |
| Microsoft 365 Copilot | Internal knowledge plus optional web | Microsoft pricing and Learn pages | Published add-on price |
| Google Gemini Enterprise | Hybrid enterprise assistant | Google Cloud docs and product page | Published starting price |
| ChatGPT Enterprise | Enterprise chat workspace | OpenAI pricing, help, and privacy pages | Custom pricing only |
| Perplexity Enterprise | Web research plus internal files | Perplexity Help Center | Published seat prices |
| Amazon Q Business | Enterprise knowledge assistant | AWS docs, pricing page, and product page | Published subscription, index, and media prices. Not open to new customers |

No other competitor was researched. Market share is UNKNOWN for all six.

## Comparison

| Topic | Glean | Microsoft 365 Copilot | Gemini Enterprise | ChatGPT Enterprise | Perplexity Enterprise | Amazon Q Business |
| --- | --- | --- | --- | --- | --- | --- |
| Internal retrieval | VERIFIED | VERIFIED for the paid add-on | VERIFIED | UNKNOWN as a general connector set. Company Knowledge is named | VERIFIED for org files and connectors | VERIFIED |
| External web | VERIFIED that citations can follow web search. Scope UNKNOWN | VERIFIED as optional Bing-backed web search | VERIFIED as Ground with Google Search and Web Grounding | UNKNOWN | VERIFIED. Web can be selected or deselected | VERIFIED as an HTTPS web crawler. Model knowledge is a separate control and is not live web |
| Text and images | VERIFIED image understanding on Assistant. Image retrieval scope UNKNOWN | Image retrieval UNKNOWN. Image generation is a different claim | VERIFIED media generation. Image retrieval UNKNOWN | UNKNOWN | VERIFIED that PNG and JPEG are not Internal Knowledge Search types. Attach-to-query behavior is a separate page | VERIFIED image processing on Pro, and images among indexed file types |
| Citations | VERIFIED | Web-search query citations are documented for Copilot Chat. Enterprise-data citations were not stated on the pricing page | VERIFIED for Deep Research source-cited reports. General chat citations UNKNOWN | UNKNOWN | The internal-knowledge article describes answers with citations. It does not use the word inline | VERIFIED |
| Tenant or permission controls | VERIFIED source permissions | VERIFIED enterprise data protection and admin web-search control | VERIFIED IAM, SSO, and source ACLs | VERIFIED SSO, SCIM, and RBAC on the pricing page | Admin and seat controls VERIFIED. Cross-tenant isolation UNKNOWN | VERIFIED permission-aware responses and IAM |
| Parallel RAG and Web, then one synthesis | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | INFERRED source picker can use web, org files, both, or neither. Parallel execution and a single synthesis step were not stated | UNKNOWN |
| Public price | UNKNOWN | VERIFIED marketing price | VERIFIED starting price | VERIFIED as custom | VERIFIED published seat prices | VERIFIED published list prices |

## Glean

Glean's product page says search covers 100+ tools, results are real-time and permissions-aware, and answers are grounded in company knowledge. The same page also says 275+ app connectors. No publication date was shown. Status VERIFIED. Publisher: Glean. URL: https://www.glean.com/enterprise-search

Glean's Enterprise Flex documentation describes per-user monthly seats, unlimited enterprise search, and a pooled FlexCredits balance for premium models and agent runs. The retrieved page lists image understanding, document upload, and agent orchestration as Assistant or Agent capabilities. It does not state a dollar seat price. Dollar price UNKNOWN. Status VERIFIED for the packaging description. Page date: last updated 18 November 2026. Publisher: Glean. URL: https://docs.glean.com/glean-enterprise-flex-pricing

Glean's citation guide says citations point to a document, file, or person and do not grant new access. Citations can follow company sources or web search. If no retrieval tool is used, a response may have no citation. Status VERIFIED. Page date: last updated 13 November 2026. Publisher: Glean. URL: https://docs.glean.com/user-guide/assistant/glean-chat/glean-chat-citations/glean-citations

Deep-linked citations, where offered, point to a passage in enterprise content. The developer guide says they are available starting in the fourth quarter of 2025, REST support is in beta, and they are not provided for pure world-knowledge or web-search answers. Status VERIFIED. Publisher: Glean. URL: https://developers.glean.com/guides/chat/deep-linked-citations

Whether Glean runs an internal index and live web in parallel, then synthesizes once, is UNKNOWN.

## Microsoft 365 Copilot

Microsoft's enterprise pricing page lists Copilot Chat as included with an eligible Microsoft 365 subscription, and Microsoft 365 Copilot as an add-on at $30.00 per user per month, paid yearly. A qualifying Microsoft 365 license is separate. The same page says prices shown are for marketing purposes only and may not reflect the actual list price because of currency, country, and region. No publication date was shown. Status VERIFIED as a published marketing price, not a negotiated contract. Publisher: Microsoft. URL: https://www.microsoft.com/en-us/copilot/pricing/enterprise

The add-on includes chat grounded in business data. Web data is also a listed grounding row. The pricing page does not state citations for those business-data answers. Status VERIFIED for the grounding table. The same URL.

Microsoft Learn says web search is optional, uses Bing, and can be turned off by an admin policy. The generated Bing query is not the full user prompt and does not include entire Microsoft 365 files. The same page says web-search query citations appear in Microsoft Copilot Chat, are not available in the Copilot pane inside a Microsoft 365 app such as Word or PowerPoint, and the queries remain in the chat thread for 24 hours. That is web-search citation evidence, not evidence of citations for enterprise-data answers. No publication date was shown. Status VERIFIED. Publisher: Microsoft. URL: https://learn.microsoft.com/en-us/copilot/plan/manage-public-web-access

Copilot Search is described as search across Microsoft 365 and connected sources for users with an eligible Copilot license, at no extra cost. Copilot Answers might include references. The page does not say every enterprise answer has a citation. No publication date was shown. Status VERIFIED. Publisher: Microsoft. URL: https://learn.microsoft.com/en-us/copilot/manage/copilot-search-overview

Image retrieval, explicit parallel internal-and-web execution, and one synthesis step are UNKNOWN.

## Google Gemini Enterprise

Google Cloud documentation lists permission-aware enterprise search, grounding on Google and third-party data, Ground with Google Search, Web Grounding, media generation, no-code agents, and enterprise security. A comparison table says prompts and enterprise data are not used to train foundation models, access is managed with IAM and SSO, and data residency values include `us`, `eu`, and `global`. Status VERIFIED for those listed features. Publisher: Google Cloud. URL: https://docs.cloud.google.com/gemini/enterprise/docs/editions

A second Google Cloud page describes Gemini Enterprise as search across enterprise data and an agent platform for multi-step tasks. Status VERIFIED. URL: https://docs.cloud.google.com/gemini/enterprise/docs/choose-product

The Business edition page describes source-cited Deep Research reports and connectors such as Microsoft 365, Google Workspace, Jira, GitHub, HubSpot, and Slack. Status VERIFIED. URL: https://cloud.google.com/gemini-enterprise/business

The Gemini for Work page shows a starting price of $21 per user per month for Gemini Enterprise Business edition. Negotiated price and the price of Standard, Plus, and Frontline are UNKNOWN from the pages used here. Status VERIFIED for the $21 starting figure only. Publisher: Google Cloud. URL: https://cloud.google.com/ai/gemini-for-work

Whether internal retrieval and live web run in parallel and then synthesize once is UNKNOWN.

## ChatGPT Enterprise

OpenAI's business pricing page says Enterprise pricing is custom and lists SCIM, role-based access controls, custom retention, encryption in transit and at rest, no training on business data by default, and data residency in ten regions. Status VERIFIED. Publisher: OpenAI. URL: https://openai.com/business/pricing/

OpenAI's enterprise privacy page says customers own inputs and outputs where law allows, models are not trained on that data by default, and ChatGPT Enterprise has completed a SOC 2 Type 2 audit. Status VERIFIED as OpenAI's statement. Page date: updated 8 January 2026. URL: https://openai.com/enterprise-privacy/

OpenAI's security page says the business products have SOC 2 Type 2, ISO/IEC 27001 and ISO/IEC 42001 certifications as described there, and support customer compliance with named privacy laws. That is the vendor's statement about its own controls. It does not select a compliance regime for this product. Status VERIFIED as a vendor claim. URL: https://openai.com/security-and-privacy/

The help center lists Company Knowledge, agents, and Deep Research among standard Enterprise seat features, and says seat terms depend on the agreement. How Company Knowledge retrieves text and images, and whether web evidence is included, are UNKNOWN from the retrieved text. On 19 November 2026 the page displayed "Updated: 17 days ago" and recorded a feature change on 2 April 2026. URL: https://help.openai.com/en/articles/8265053-what-is-chatgpt-enterprise

A public per-user dollar price is UNKNOWN.

## Perplexity Enterprise

Perplexity's pricing FAQ says Enterprise Pro is $40 per seat per month or $400 per seat per year, and Enterprise Max is $325 per seat per month or $3,250 per seat per year. Discounts may be available for teams of 250 or more, and for schools, nonprofits, and government. API use is not included. Status VERIFIED as published seat prices, not a negotiated contract. Page date: last modified 6 November 2026. Publisher: Perplexity. URL: https://www.perplexity.ai/help-center/en/articles/10352986-enterprise-pricing-and-billing-frequently-asked-questions

The plan guide says Enterprise Pro includes internal knowledge search through shared spaces and centrally governed file connectors, and that enterprise data is not used for model training. The same page says the Organization File Repository is being retired on 1 October 2026 and is not available as a new Enterprise entitlement. Status VERIFIED for those statements. Page date: last modified 17 November 2026. URL: https://www.perplexity.ai/help-center/en/articles/11187416-which-perplexity-subscription-plan-is-right-for-you

The internal-knowledge article says administrators upload organization files, users can choose Web, Org Files, both, or neither, and the article lead says answers include citations. It also says administrators can upload up to 500 organization files. That 500-file statement conflicts with the plan guide's retirement notice. The current entitlement for a new buyer is not verified. Status: source selection and the citation lead are VERIFIED; the 500-file limit is a conflict, not a current entitlement. Page date: last modified 17 November 2026. URL: https://www.perplexity.ai/help-center/en/articles/10352958-what-is-internal-knowledge-search-for-enterprise

The same article does not say the two sources run in parallel or that synthesis runs once. That routing behavior is UNKNOWN. Whether the both-sources control is equivalent to this product's Both route is INFERRED only as a similar user choice, not as the same orchestration.

A Perplexity workshop page says PNG and JPEG are not Internal Knowledge Search file types and can instead be attached to a query. Status VERIFIED for that page. URL: https://www.perplexity.ai/hub/workshops/financial-research-and-analysis

## Amazon Q Business

AWS documentation says Amazon Q Business answers from enterprise data, keeps responses permission-aware, and provides citations. Admins can limit responses to enterprise data or allow enterprise data plus model knowledge. Model knowledge is the model's own knowledge. It is not live web evidence. The same page says Amazon Q Business is no longer open to new customers. No publication date was shown. Status VERIFIED. Publisher: AWS. URL: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/what-is.html

The web-experience guide says answers include source citations with a title, URL, and snippet. It also says Amazon Q Business is no longer open to new customers. A note on that page is dated 31 October 2024 and concerns direct access to the model. Status VERIFIED. URL: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-web-experience.html

The web-crawler connector indexes public or internal HTTPS websites. Status VERIFIED as a crawl connector. It is not evidence of a live web-search route on every question, and it is not the same control as model knowledge. The page also says Amazon Q Business is no longer open to new customers. URL: https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-webcrawler.html

The pricing page lists Lite at $3 per user per month and Pro at $20 per user per month. A Starter Index unit is $0.140 per hour and an Enterprise Index unit is $0.264 per hour. Index charges continue until the index is deleted. Pro includes image responses when image processing is selected. The same page lists image extraction at $0.003 per image, audio at $0.006 per minute, and video at $0.050 per minute. Anonymous embedded use is priced at $200 for 30,000 units per month, with 2 units per ChatSync call or embedded prompt. These are published list prices. They are not this product's cost, and negotiated discounts are UNKNOWN. The page says existing Amazon Q Business customers can continue using the current service. No publication date was shown. Status VERIFIED. Publisher: AWS. URL: https://aws.amazon.com/q/business/pricing/

The product page describes answers over documents, images, audio, and video, with citations, and a starting figure of $3 per user per month. Its end-of-support notice says Amazon Q Business is no longer available to new customers. Status VERIFIED. URL: https://aws.amazon.com/q/business/

New-customer availability is VERIFIED as closed on these AWS pages. Existing-customer continuation is VERIFIED on the pricing page. Amazon Q Business is not a selected vendor.

## Differentiation hypothesis

The approved product requires an explicit RAG, Web, Both, or Neither route, parallel execution for Both, one synthesis step, text and image provenance, UI-01, and UI-02 tied to lifecycle evidence. None of the retrieved pages states that combination. Whether any candidate sells it is UNKNOWN. Treating the absence of those words as a competitor weakness would be unsupported.

## Open items

Public prices above are not a total cost of ownership. Index, media, credit, model, and connector charges can exceed the seat price. Amazon Q Business list extras are the image, audio, video, and anonymous-use prices stated above. Contract terms, data-residency commitments for a named customer jurisdiction, and multimodal retrieval quality are UNKNOWN unless a row above marks them VERIFIED. The Perplexity organization-file repository's current entitlement remains a conflict between two Perplexity pages.
