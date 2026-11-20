# AWS AI-DLC Setup & Operating Procedure

**Cursor IDE | Windows PowerShell | Version-aware installation**

Official source: https://awslabs.github.io/aidlc-workflows/guide/01-getting-started/

This guide installs and operates the AWS Labs AI-DLC workflow for Cursor. It does **not** provision AWS cloud infrastructure. Local Ideation does **not** require an AWS account.

---

## 1. Purpose and boundaries

| Do | Do not |
|---|---|
| Install / refresh the AI-DLC harness for Cursor | Infer that setup creates AWS accounts, VPCs, or deployable stacks |
| Validate with `doctor` and `/aidlc --status` | Treat doctor health as production readiness |
| Follow official stage gates and approvals | Restart a running intent to “fix” diagnostics |
| Keep secrets out of shared config and git | Auto-approve gates or invent PASS / VERIFIED |

---

## 2. Prerequisites

- Windows 10/11 with a normal (non-administrator) PowerShell session
- Cursor installed, signed in, and able to open this project
- Git installed and on `PATH`
- Project backed up or committed before configuration changes
- Network access to official GitHub release assets (for first-time native install)
- For this repository’s Cursor harness tools: **Bun** on `PATH` (hooks and `bun .cursor/tools/aidlc.ts` require it)

---

## 3. Install native CLI (PowerShell) — first-time / machine install

```powershell
git --version
irm https://github.com/awslabs/aidlc-workflows/releases/latest/download/install.ps1 | iex
aidlc version
```

**Security:** Inspect downloaded scripts before execution if your organization requires it. Run as your normal user. Close and fully restart Cursor after installation so it inherits the updated `PATH`.

Node.js is not required for the native install. This project’s Cursor hooks still need **Bun**.

---

## 4. Configure project for Cursor

### New folder only

```powershell
mkdir MyProject
cd MyProject
git init
aidlc config --harness cursor
aidlc doctor
```

### Existing Git repository (this project)

```powershell
cd D:\New_test\multi_agent_research_enterprise_starter\multi_agent_research_enterprise
git status
```

If AI-DLC is **already configured and running**, prefer diagnostics over reconfiguration:

```powershell
bun .cursor/tools/aidlc.ts doctor
bun .cursor/tools/aidlc.ts --status
# or, when native CLI is on PATH:
aidlc doctor
```

Do **not** re-run `git init` or blindly reconfigure. If you must refresh:

```powershell
aidlc config --harness cursor
# then review:
git status
git diff
```

---

## 5. Validate in Cursor

1. Open this repository root in Cursor.
2. In Agent Chat: `/aidlc --doctor` (or `/aidlc doctor`).
3. Run `/aidlc --status` for phase, stage, guards, and completion.
4. Confirm harness files where applicable:
   - `.cursor/hooks.json`
   - `.cursor/cli.json`
   - `.cursor/rules/aidlc.mdc`
   - `.cursor/rules/aidlc-phase-*.mdc`
5. Confirm workflow records under `aidlc/spaces/default/intents/…` and that stage approvals are in the audit trail.

### Project-local Bun diagnostics (verified for this layout)

```powershell
bun .cursor/tools/aidlc.ts doctor
bun .cursor/tools/aidlc.ts --version
bun .cursor/tools/aidlc.ts engine status
```

Alternate utility entry (also present in this repo):

```powershell
bun .cursor/tools/aidlc-utility.ts doctor
bun .cursor/tools/aidlc-utility.ts help
```

Use `help` (not `--help`) for `aidlc-utility.ts`. Prefer `bun .cursor/tools/aidlc.ts doctor` as the primary project-local check used by this install’s onboarding.

---

## 6. Start a new workflow (new project only)

In Cursor Agent Chat:

```text
/aidlc Build a secure enterprise research assistant with a Supervisor, multimodal RAG, Web Search, and Response Synthesis agent, plus two UIs.
```

Select the plan/scope offered by the installed version. Follow clarification, summary confirmation, artifact verification, and explicit approval gates.

**Do not** use initialization to reset this running Multi-Agent Research Assistant intent.

---

## 7. Existing project: safe verification (this repository)

As of the last status check:

- **Stage 3 Feasibility & Constraints:** APPROVED (CONDITIONAL GO)
- **Stage 4 Scope Definition:** Running (clarification in progress)
- **Next after Scope Definition:** Team Formation

Run diagnostics and status **read-only**. Do **not**:

- Restart Intent Capture
- Create a new intent to replace the current one
- Close Stage 3 CONDITIONAL GO conditions without evidence
- Skip Stage 4 summary confirmation or invent Stage 4 approval

Preserve all unresolved Stage 3 conditions and the official Stage 4 summary-confirmation gate.

---

## 8. Operating controls

| Rule | Meaning |
|---|---|
| Stage complete only when APPROVED | Official workflow gate / audit evidence |
| Sensor PASS | Configured checks only — not all business claims |
| UNKNOWN / NOT_VERIFIED | Record explicitly; never fabricate PASS |
| Separate approval | Before source changes, infra, deploy, commit, or push when a stage forbids them |
| Secrets | Keep out of shared configuration and recordings |

---

## 9. Troubleshooting workflow: diagnose before fixing

1. **Baseline** — `git status --short --branch`, `/aidlc --status`, `bun .cursor/tools/aidlc.ts --version`, doctor output.
2. **Matching diagnostic** — Bun project tool if Bun + `.cursor/tools/aidlc.ts` exist; else native `aidlc doctor`; Cursor chat only when supported.
3. **Classify** — ERROR / WARNING / INFO / NOT_VERIFIED with exact messages and paths.
4. **Read-only checks** — root, git, `.cursor` rules/hooks/tools, intent folder, diaries, approval evidence.
5. **Plan fixes** — command, expected file changes, rollback, validation; obtain approval before changing active config or source.
6. **Apply only authorized fixes** — no reinits, stage resets, broad upgrades, auto-approvals, cloud provision, deploy, commit/push without ask.
7. **Rerun the same diagnostic** and compare before/after; confirm workflow stage unchanged unless authorized.

---

## 10. Common failure patterns

| Symptom | Check | Safe response |
|---|---|---|
| `bun: command not found` | `Get-Command bun`; `bun --version` | Install Bun, or use native `aidlc` if available |
| Missing `.cursor/tools/aidlc.ts` | `Test-Path .cursor/tools/aidlc.ts` | Inspect layout; do not invent files |
| Unknown `doctor` | `bun .cursor/tools/aidlc.ts --help` or `aidlc-utility.ts help` | Use only supported commands |
| `aidlc` not recognized | `Get-Command aidlc`; `aidlc version` | Fix PATH; restart shell and Cursor |
| Cursor `/aidlc` unavailable | Rules + harness install | Confirm workspace root; avoid reinit |
| Stage approval mismatch | Audit / `aidlc-state.md` vs informal notes | Official audit is authoritative |
| Doctor warnings only | Capture each check | Fix verified blockers with approved changes |
| AWS account unknown | Repo + cloud evidence | Keep UNKNOWN; local Ideation can continue |

---

## 11. Official references

- https://github.com/awslabs/aidlc-workflows
- https://awslabs.github.io/aidlc-workflows/guide/01-getting-started/
- https://awslabs.github.io/aidlc-workflows/guide/harnesses/cursor/
- https://github.com/awslabs/aidlc-workflows/blob/main/docs/guide/12-cli-commands.md
- Project onboarding rule: `.cursor/rules/aidlc-onboarding.mdc`
- Command details: [COMMAND_REFERENCE.md](./COMMAND_REFERENCE.md)

---

## 12. Ready-to-paste read-only diagnostic prompt

```text
Review the existing AWS AI-DLC project in READ-ONLY mode.

1. Confirm repository root and installed workflow version.
2. Check whether .cursor/tools/aidlc.ts and/or aidlc-utility.ts exist and Bun is available.
3. If supported, run: bun .cursor/tools/aidlc.ts doctor
4. If supported, also try: bun .cursor/tools/aidlc-utility.ts doctor and/or aidlc doctor
5. Compare the diagnostics and report errors/warnings individually.
6. Confirm Stage 3 is APPROVED and Stage 4 Scope Definition remains RUNNING (or report the actual current stage).
7. Verify Stage 3 conditions and approval evidence are preserved.
8. Propose targeted fixes with expected changes and rollback steps.

STOP. Do not repair, reconfigure, reinitialize, advance stages, commit,
push, provision AWS resources, or deploy without explicit approval.
```

---

## 13. Provenance

Adapted from `AWS_AI_DLC_Cursor_Setup_Process_Guide_Expanded_Commands.docx` (20 November 2026). Command surfaces were checked against this repository’s `.cursor/tools/` layout (`aidlc.ts`, `aidlc-utility.ts`) and a live `aidlc 2.11.4` doctor run. This document does not claim every historical troubleshooting command was executed successfully in prior sessions.
