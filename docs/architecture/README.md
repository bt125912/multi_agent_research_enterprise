# Architecture

Browser -> FastAPI -> LangGraph Supervisor -> RAG and/or Web -> Synthesis -> response.
Ingestion -> validation -> parsing -> chunking -> embeddings -> vector/object stores.

Starter graph supports all four routes, but retrieval/web adapters are unavailable. Do not deploy as a research system until addressed.
