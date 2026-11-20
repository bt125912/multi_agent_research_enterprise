# AWS AI-DLC command reference (this repository)

Two command surfaces may exist. They are **not** interchangeable. Prefer the command that matches files present on disk.

| Surface | When to use |
|---|---|
| Native `aidlc` | Machine install from AWS Labs release; available on `PATH` after installer |
| `bun .cursor/tools/aidlc.ts …` | **Primary** project-local entry for this Cursor harness |
| `bun .cursor/tools/aidlc-utility.ts …` | Alternate project-local utility (doctor, status, intent helpers) |
| Cursor chat `/aidlc …` | Agent Chat only — not PowerShell |

---

## A. Environment checks (PowerShell)

```powershell
Get-Location
git --version
git status --short --branch
Get-Command bun -ErrorAction SilentlyContinue
bun --version
Get-Command aidlc -ErrorAction SilentlyContinue
aidlc version
Test-Path .cursor/tools/aidlc.ts
Test-Path .cursor/tools/aidlc-utility.ts
Get-ChildItem .cursor/tools -Filter "aidlc*.ts" | Select-Object -First 20 Name
```

**Interpretation**

- If `bun` is missing, do not run Bun utilities.
- If a tool file is missing, do not invent a replacement.
- If `aidlc` is missing, fix PATH / install per official docs before changing the project.

---

## B. Project-local Bun diagnostics (preferred here)

```powershell
bun .cursor/tools/aidlc.ts doctor
bun .cursor/tools/aidlc.ts doctor --verbose
bun .cursor/tools/aidlc.ts --version
bun .cursor/tools/aidlc.ts --status
bun .cursor/tools/aidlc.ts engine status
bun .cursor/tools/aidlc.ts update --check
```

```powershell
bun .cursor/tools/aidlc-utility.ts doctor
bun .cursor/tools/aidlc-utility.ts help
bun .cursor/tools/aidlc-utility.ts version
bun .cursor/tools/aidlc-utility.ts status
```

Note: `aidlc-utility.ts` uses `help`, not `--help`.

---

## C. Native CLI

```powershell
git --version
irm https://github.com/awslabs/aidlc-workflows/releases/latest/download/install.ps1 | iex
aidlc version
aidlc config --harness cursor
aidlc doctor
```

On an already running project: prefer read-only doctor/status first. Do not reinstall or reconfigure without need, backup, and approval. Review installer scripts under your security policy.

---

## D. Cursor Agent Chat (not PowerShell)

```text
/aidlc --doctor
/aidlc doctor
/aidlc --status
/aidlc --version
```

Availability depends on the installed harness. Enter these in Cursor Agent Chat only.

---

## E. What this project currently uses

Verified in this workspace:

| Check | Result |
|---|---|
| `.cursor/tools/aidlc.ts` | Present |
| `.cursor/tools/aidlc-utility.ts` | Present |
| Bun | Present on PATH |
| Primary doctor command | `bun .cursor/tools/aidlc.ts doctor` |
| Installed version (last check) | `aidlc 2.11.4` |

Native `aidlc` may or may not be on `PATH` depending on the machine install; project work does not require it when Bun + `.cursor/tools/aidlc.ts` work.
