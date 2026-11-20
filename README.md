# Multi-Agent Multimodal Research Assistant — Enterprise Starter

A clean **application starter** for AWS AI-DLC Inception and iterative Construction. It does **not** include or claim to install the official AWS AI-DLC framework. No production-readiness certification is implied.

## Local start

1. Install Python 3.12+, Node.js 20+, and Bun >=1.4.4 for the separate AWS AI-DLC Copy Channel.
2. `cd apps/research-api && python -m venv .venv` then activate the venv and `pip install -e ".[dev]"`.
3. `uvicorn research_api.main:app --reload --port 8000`.
4. In another terminal: `cd apps/research-web && npm install && npm run dev`.
5. Visit http://localhost:5173. The API at http://localhost:8000 supports a **demo deterministic supervisor** and returns explicit unavailable states for RAG and live web search. It does not fabricate citations.
6. `pytest` in `apps/research-api` for starter tests.

## Official AWS AI-DLC setup

Full Cursor + Windows PowerShell setup, diagnostics, and operating procedure:

- [docs/setup/README.md](docs/setup/README.md)
- [docs/setup/AWS_AI_DLC_Cursor_Setup_Guide.md](docs/setup/AWS_AI_DLC_Cursor_Setup_Guide.md)
- [docs/setup/COMMAND_REFERENCE.md](docs/setup/COMMAND_REFERENCE.md)

Quick health check from the repository root (Bun required for this harness):

```powershell
bun .cursor/tools/aidlc.ts doctor
bun .cursor/tools/aidlc.ts --status
```

In Cursor Agent Chat: `/aidlc --doctor` and `/aidlc --status`.

### Optional: configure from a verified release archive

```powershell
$project = (Resolve-Path .).Path
bun "D:\New_test\aws-aidlc\release\runtime\cursor\install.ts" "$project"
bun .cursor/tools/aidlc.ts doctor
```

Only run if `runtime/cursor/install.ts` exists, after reviewing the installer and its effects. Restart Cursor afterward. Do not copy `.cursor` or `aidlc` from an unverified source checkout. Prefer `aidlc doctor` / project-local doctor over blind reconfiguration when this project is already running.

Configuring AI-DLC does **not** provision AWS infrastructure.

## Design notes

- `agents/` is logical agent source code; `orchestration/` is LangGraph state and graph composition.
- Initial production deployment should package the agents in the Python API process; ingestion worker is a separate process when implemented.
- Vector DB, object store, web provider, OIDC, telemetry, and persistent checkpointing are **not yet integrated**. See `docs/requirements/ACCEPTANCE.md`.
- The included deterministic API is a safe, runnable scaffold, not an enterprise research engine.

## Architecture and Acceptance

- [Architecture Reference](docs/architecture/ARCHITECTURE_REFERENCE.md)
- [Component Contracts](CONTENT.md)
- [Acceptance Criteria](ACCEPTANCE_CRITERIA.md)
