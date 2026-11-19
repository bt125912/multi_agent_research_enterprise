# Multi-Agent Multimodal Research Assistant — Enterprise Starter

A clean **application starter** for AWS AI-DLC Inception and iterative Construction. It does **not** include or claim to install the official AWS AI-DLC framework. No production-readiness certification is implied.

## Local start

1. Install Python 3.12+, Node.js 20+, and Bun >=1.4.4 for the separate AWS AI-DLC Copy Channel.
2. `cd apps/research-api && python -m venv .venv` then activate the venv and `pip install -e ".[dev]"`.
3. `uvicorn research_api.main:app --reload --port 8000`.
4. In another terminal: `cd apps/research-web && npm install && npm run dev`.
5. Visit http://localhost:5173. The API at http://localhost:8000 supports a **demo deterministic supervisor** and returns explicit unavailable states for RAG and live web search. It does not fabricate citations.
6. `pytest` in `apps/research-api` for starter tests.

## Official AWS AI-DLC integration (after checking release integrity)

Run from a PowerShell terminal where Bun works, using your separately verified release archive:

```powershell
$project = (Resolve-Path .).Path
bun "D:\New_test\aws-aidlc\release\runtime\cursor\install.ts" "$project"
bun .cursor/tools/aidlc-utility.ts doctor
```

Only run if `runtime/cursor/install.ts` exists, after reviewing the installer and its effects. Restart Cursor, run `/aidlc --doctor`, and start Inception. Do not copy `.cursor` or `aidlc` from the AWS source checkout.

## Design notes

- `agents/` is logical agent source code; `orchestration/` is LangGraph state and graph composition.
- Initial production deployment should package the agents in the Python API process; ingestion worker is a separate process when implemented.
- Vector DB, object store, web provider, OIDC, telemetry, and persistent checkpointing are **not yet integrated**. See `docs/requirements/ACCEPTANCE.md`.
- The included deterministic API is a safe, runnable scaffold, not an enterprise research engine.

## Architecture and Acceptance

- [Architecture Reference](docs/architecture/ARCHITECTURE_REFERENCE.md)
- [Component Contracts](CONTENT.md)
- [Acceptance Criteria](ACCEPTANCE_CRITERIA.md)
