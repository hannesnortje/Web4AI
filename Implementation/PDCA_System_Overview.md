## PDCA System Overview (CMM3/CMM4 Operational Model)

This document explains how the PDCA system works in the Web4Articles codebase: where it lives, how to use the CLI, how dual links are enforced, how the RAG “short-term memory” is consulted, and how the execution loop runs test-first until green before documenting with a PDCA.

---

### 1) Components and Locations

- PDCA core component: `Web4Articles/components/PDCA/0.3.6.1/src/ts/layer2/DefaultPDCA.ts`
- Training topics tests: `Web4Articles/components/PDCA/0.3.6.1/test/pdca.trainai.test.ts`
- PDCA how-to guide: `Web4Articles/scrum.pmo/roles/_shared/PDCA/howto.PDCA.md`
- Sessions and historical PDCAs: `Web4Articles/scrum.pmo/project.journal/**` and `Web4Articles/components/PDCA/0.3.6.1/session/**`
- Root readme: `Web4Articles/README.md`

What this means:
- The PDCA behavior and CLI entry points are implemented in `DefaultPDCA.ts`.
- Training material (trainAI topics) and their structure are validated through tests.
- Journal PDCAs constitute the historical data that the RAG system will index in Phase 2.

---

### 2) Core CLI Commands (Agent-Facing)

Run these via the PDCA CLI wrapper (project scripts/runner) or directly when integrated into the toolchain.

- `pdca trainAI [topic]`
  - Shows PDCA training content by topic; with no topic, it lists all topics and how-tos (PDCA, dual links, reporting protocol, test-first, etc.).
  - Purpose: teach/refresh the agent in a pretrained state to re-align with the process and reporting discipline.

- `pdca queryTrainAI "your query" [topic]`
  - Queries training topics (RAG-like recall) for immediate guidance; used for short-term memory during sessions.
  - Purpose: enforce “query before acting/reporting” to prevent CMM2 behavior.

- `pdca setSession <sessionPath>`
  - Sets the current working session directory used by other PDCA operations.

- `pdca test [scope] [...refs]`
  - Executes tests; scope can be `all`, `file`, `describe`, `itCase`. Used for test-first gating and selective runs.

- `pdca cmm3check <pdcaFile>` / `pdca cmm3checkSession [sessionPath]`
  - Validates PDCA(s) against CMM3 compliance rules (template/version, sections, dual links, QA Decisions, link correctness, etc.).

- Dual-link helpers:
  - `pdca getDualLink <file>`: Generates a correct dual link for a file.
  - `pdca getDualLinkRelativePath <from> <to>`: Calculates correct relative paths.
  - `pdca fixDualLinks [target]`: Scans and auto-fixes dual links to comply with the standard.

---

### 3) Dual Link Standard (Verification-First Links)

- Required format in markdown: `[GitHub](https://...) | [§/path](project-root-relative-path)`
- Principles:
  - GitHub link must be valid and pushed (verifiable by others).
  - Local link is project-root-relative using `§` notation for easy navigation.
  - Never use `file://` or missing `§` (CMM2 violation).
- Tooling:
  - Use `pdca getDualLink` to generate links.
  - Use `pdca fixDualLinks` to auto-fix existing documents.
  - `cmm3check` includes checks for dual link presence and correctness.

---

### 4) RAG Usage as Short-Term Memory

The agent operates in a pretrained state and must “relearn” operating procedures on session start:

1. `pdca trainAI` (list topics; read relevant how-to content such as PDCA, dual links, reporting, test-first).
2. `pdca queryTrainAI "<your question>"` (immediately consult for reporting format, dual-link rules, and any assumptions).
3. Query whenever you’re about to report/decide/assume; align early to avoid rework.

This enforces the contract: memory != RAG. Always query RAG to align actions and reports.

---

### 5) Session Setup and Baseline

1. Source environment as needed (env files).
2. Read project root `README.md` to understand structure/current context.
3. Set session path:
   - `pdca setSession /absolute/or/project/relative/path`
4. Establish a baseline truth test suite:
   - Ensure tests exist and currently fail for unimplemented behavior (quality gate).
   - Use `pdca test` to run, record failures as intended baseline.

---

### 6) Execution Loop (Test-First Until Green)

Repeat until all intended tests pass:

1. Plan:
   - Query `trainAI` and `queryTrainAI` for domain/process guidance.
   - Identify minimal set of failing tests that define the objective.
2. Do (Implement):
   - Implement code guided by the failing tests.
3. Check (Run Tests):
   - `pdca test` to verify progress; keep iterating until green.
4. Act (Harden/Refactor):
   - Fix dual links in any new/modified docs or code references: `pdca fixDualLinks`.
   - Validate with `pdca cmm3check` (or session variant).

Once green:
- Document the loop as a PDCA (template-compliant), include dual links to artifacts, and push.
- If new knowledge is created, integrate back into training (see Section 7).

---

### 7) Reporting Protocol (Concise, Verifiable, Dual-Linked)

- Always query: `pdca queryTrainAI "How should I report task completion?"` before reporting.
- Report format:
  - Facts only, no speculative summary.
  - Include dual links to changed files and relevant evidence (tests, commits).
  - Include `git status` (clean) and branch.
  - STOP. Await user instruction; do not self-close loops.

Anti-patterns (avoid):
- Elaborate summaries, decorative formatting, nested boxes.
- Reporting without prior RAG query.

---

### 8) CMM3 Compliance Highlights

- PDCA template version/sections must match exact standard.
- QA Decisions present or explicitly “All clear, no decisions”.
- Dual links validated and working; no TBD placeholders.
- Git commit/push protocol followed (links must be verifiable on remote).
- Filename formats adhere to `YYYY-MM-DD-UTC-HHMM(.feature)?.pdca.md` where applicable.

Use:
- `pdca cmm3check <pdcaFile>` and/or `pdca cmm3checkSession` to enforce before closing a session.

---

### 9) Evidence and Traceability

- Training topics and their structure are covered by tests in `pdca.trainai.test.ts`.
- The PDCA component exposes all relevant CLI methods (trainAI, queryTrainAI, setSession, fixDualLinks, test, cmm3check, etc.).
- Journal PDCAs under `scrum.pmo/project.journal/**` are the primary historical records and will be indexed in Phase 2’s RAG bootstrap.

---

### 10) Quickstart Checklist for a New Agent Session

1. `pdca trainAI` → skim topics; open “PDCA”, “dual-links”, “report”.
2. `pdca queryTrainAI "how to report and dual links"` → align reporting format.
3. `pdca setSession /path/to/session` → establish context.
4. Create/identify failing tests that define the objective.
5. Implement until tests pass (`pdca test`).
6. Fix/validate dual links (`pdca fixDualLinks`, `pdca cmm3check`).
7. Write PDCA document (template compliant) with dual links; commit and push.
8. If new learnings: update training topics/materials accordingly.

---

### 11) Relationship to Phase 2 (RAG Bootstrap)

- The PDCA markdowns are the core training corpus to be chunked and embedded into ChromaDB.
- SQLite stores temporal metadata; SQLite Graph stores relationships (e.g., PRECEDES) for breadcrumb/path queries.
- `queryTrainAI` is conceptually aligned with RAG queries; Phase 2 formalizes the three-tier retrieval for broader sources (PDCAs, TypeScript, tool examples).


