# trainAI Knowledge Base - Complete Reference

**Version**: 0.3.x (PDCA Component)  
**Purpose**: AI training system providing structured, CMM3-compliant learning content  
**Usage**: `pdca trainAI <topic>` or `pdca trainAI <number>`

---

## Overview

The trainAI system is a knowledge base built into the PDCA component that provides structured training content for AI agents (and humans) about processes, patterns, and best practices in the Web4Articles codebase.

### Philosophy

**"Doing it WRONG first, then RIGHT: 100x more expensive. Doing it RIGHT first: Normal cost."**

trainAI embodies the principle: **Read FIRST, Act SECOND**. It prevents costly trial-and-error by providing upfront knowledge.

### Core Principles

- **CMM3 Compliance**: All content is objective, reproducible, and verifiable
- **Zero-Knowledge Design**: Assumes no prior knowledge, teaches from scratch
- **Test-First**: Emphasizes writing tests before implementation
- **RAG-Powered**: Query before acting to prevent assumption cascade

---

## How to Use trainAI

### List All Topics
```bash
pdca trainAI
```
Shows all 19 available training topics with descriptions.

### Learn a Specific Topic
```bash
pdca trainAI <topic-name>
# or
pdca trainAI <number>
```

Examples:
```bash
pdca trainAI start                # Learn startup protocol
pdca trainAI feature-development  # Learn test-first development
pdca trainAI 9                    # Quick access by number
```

### Query the Knowledge Base
```bash
pdca queryTrainAI "<question>" [topic]
```

Example:
```bash
pdca queryTrainAI "How do I validate links?"
pdca queryTrainAI "test workflow" test-workflow
```

---

## Topic Index

1. **start** - Background Agent Startup Protocol
2. **pdca** - Creating CMM3-Compliant Documentation
3. **cmm** - Understanding Capability Maturity Levels
4. **dual-links** - GitHub + § Notation for Chat Reports
5. **ensure-links** - CMM3 Atomic Link Validation
6. **component-upgrade** - Link Management During Versioning
7. **merge** - Post-Merge Integration and Build Requirements
8. **component** - Web4 Component System
9. **feature-development** - RAG-Powered Test-First CMM3 Pattern
10. **web4-vs-nodejs** - Pattern Migration Guide
11. **tech-stack** - Project Technology & Testing Framework
12. **test-workflow** - Semantic Versioning and Test Iteration
13. **test-without-versioning** - Baseline Verification
14. **test-first** - Trust Tests, Avoid Manual Verification
15. **interpret-instructions** - Literal vs Implied Actions
16. **collaborate** - User-in-the-Loop CMM4 Pattern
17. **chat-response** - CMM3 Compliance for Agent Replies
18. **report** - Concise Task Completion Without Summary Generation
19. **license-headers** - AI-GPL License Management
20. **decide** - QA Decision Framework for PDCAs

---

## Complete Training Topics


### 1. 🚀 start - Background Agent Startup Protocol

**Description**: Complete startup sequence for new agents, including CMM4 understanding, identity setup, and initial PDCA creation

#### Required Reading

1. **README.md** (Depth: 3)
   - Reason: Main entry point - defines 12-step startup protocol
   
2. **scrum.pmo/project.journal/2025-09-22-UTC-1908-session/howto.cmm.md** (Depth: 3)
   - Reason: CRITICAL: Must understand CMM4 framework FIRST before touching anything
   
3. **scrum.pmo/roles/_shared/PDCA/howto.PDCA.md** (Depth: 3)
   - Reason: Learn PDCA creation and compliance rules
   
4. **scrum.pmo/roles/_shared/PDCA/template.md** (Depth: 2)
   - Reason: Official PDCA template structure
   
5. **scrum.pmo/roles/_shared/PDCA/PDCA.howto.decide.md** (Depth: 2)
   - Reason: Decision-making framework for QA and user alignment

#### Key Lessons

1. 🔴 ALWAYS read CMM4 framework (howto.cmm.md) FIRST
2. ✅ Use component methods (web4tscomponent) for version control - NEVER manual cp/mkdir
3. ✅ Follow startup decisions: Focus, Role, Duration, Location, Identity
4. ✅ Create session-start PDCA using timestamp-only filename
5. ✅ Verify CMM3 compliance: objective, reproducible, verifiable
6. ⚠️ Read to depth 3: document → references → secondary references
7. 🔗 Session end: Validate dual links with `pdca ensureValidLinks <session-dir>`
8. 🛑 Feedback points: After showing results, STOP and wait for user
9. 🤝 Collaboration: User controls loop, you execute within it
10. ⚠️ "Show me" = show + STOP, not show + analyze + implement

#### Verification Checklist

- [ ] Can recite the 12 startup steps from README.md
- [ ] Understands CMM1-CMM4 progression and why CMM4 is feedback loop mastery
- [ ] Can create agent identity file in correct location
- [ ] Can create session-start PDCA with correct filename format
- [ ] Knows to use web4tscomponent for ALL version operations
- [ ] Validates all dual links before session end
- [ ] Can recognize feedback points in startup sequence
- [ ] Knows when to wait vs continue
- [ ] Understands collaboration model

---

### 2. 📝 pdca - Creating CMM3-Compliant Documentation

**Description**: Learn to create excellent PDCAs with proper structure, links, and compliance

#### Required Reading

1. **scrum.pmo/roles/_shared/PDCA/template.md** (Depth: 2)
   - Reason: Single source of truth for PDCA format
   
2. **scrum.pmo/roles/_shared/PDCA/howto.PDCA.md** (Depth: 3)
   - Reason: Consolidated guidelines for PDCA excellence
   
3. **scrum.pmo/roles/SaveRestartAgent/cmm3.compliance.checklist.md** (Depth: 2)
   - Reason: Complete CMM3 compliance verification

#### Key Lessons

1. ✅ Use TRON format: Trigger (verbatim), Response, Outcome, Next
2. ✅ Dual linking: backward links to previous work, forward links to outcomes
3. ✅ Timestamp-only filenames: YYYY-MM-DD-UTC-HHMM.pdca.md (NO descriptive text)
4. ✅ DRY principle: cross-reference instead of duplicating content
5. ✅ Always include: "Never 2 1 (TO ONE). Always 4 2 (FOR TWO)." at end
6. ⚠️ CMM badges track compliance status throughout PDCA lifecycle
7. 🔗 Dual link format: [GitHub](URL) | [§/path](path) - see dual-links
8. 🔗 Generate dual links: `pdca getDualLink <file>` (auto-fixes git status)
9. 🔗 Validate links: `pdca ensureValidLinks <file>` before PDCA completion
10. 🛑 1f Step 2: "Interrupt immediately on unexpected observations and ask TRON"
11. 🤝 This is a feedback point - STOP and wait for TRON response
12. ⚠️ Present decisions when direction unclear (6c)
13. ❌ Never assume what user wants next

#### Verification Checklist

- [ ] Can create PDCA with correct filename format
- [ ] Includes all sections: Links, Plan (with TRON), Do, Check, Act, Meta
- [ ] Uses dual links (backward + forward placeholders)
- [ ] DRY: references documents instead of copying content
- [ ] Includes philosophical insight line at end
- [ ] Validates dual links using getDualLink or ensureValidLinks
- [ ] Recognizes when to stop and ask TRON
- [ ] Can present decisions instead of assuming
- [ ] Knows collaboration protocol during PDCA creation

---

### 3. 🎯 cmm - Understanding Capability Maturity Levels

**Description**: Master the CMM framework from chaos (CMM1) to feedback loop mastery (CMM4)

#### Required Reading

1. **scrum.pmo/project.journal/2025-09-22-UTC-1908-session/howto.cmm.md** (Depth: 3)
   - Reason: Definitive CMM framework explanation
   
2. **README.md** (Depth: 2)
   - Reason: See CMM4 applied to startup process

#### Key Lessons

1. 📊 CMM1 (Chaos): No process, hero-dependent, unpredictable
2. 📋 CMM2 (Subjective): Basic processes exist but subjective/ad-hoc
3. ✅ CMM3 (Objective): Defined, reproducible, scientifically verifiable
4. 🔄 CMM4 (Feedback Loop): Continuous improvement through systematic iteration
5. 🎯 Goal: Processes that evolve WITHOUT breaking the system
6. ⚠️ Manual operations = CMM2. Component methods = CMM3.

#### Verification Checklist

- [ ] Can explain CMM1-CMM4 levels with examples
- [ ] Understands PDCA as CMM4 feedback loop system
- [ ] Recognizes CMM2 violations (manual cp, subjective decisions)
- [ ] Can identify how to elevate CMM2 operations to CMM3
- [ ] Understands why CMM4 enables LLM capability evolution

---

### 4. 🔗 dual-links - GitHub + § Notation for Chat Reports

**Description**: Master dual link format: GitHub URLs for verification, § paths for local navigation

#### Required Reading

1. **scrum.pmo/roles/_shared/PDCA/chat.report.template.md** (Depth: 2)
   - Reason: Official chat report format with dual link examples
   
2. **scrum.pmo/roles/SaveRestartAgent/cmm3.compliance.checklist.md** (Depth: 1)
   - Reason: CMM3 4c: Link Compliance requirements
   
3. **scrum.pmo/roles/_shared/PDCA/howto.PDCA.md** (Depth: 1)
   - Reason: Dual Link System section

#### Key Lessons

1. ✅ Format: [GitHub](https://github.com/org/repo/blob/branch/path) | [§/path](path)
2. ✅ GitHub link: For human verification, works in any context
3. ✅ § notation: Project-root-relative, for local navigation
4. ✅ MUST be in sync: Same file, same branch, both valid
5. ⚠️ CMM3 4c: Links MUST be verifiable - file must be pushed
6. 🔧 Tool: `pdca getDualLink <file>` auto-generates correct format
7. 🔧 Auto-fix: getDualLink adds/commits/pushes if needed
8. ❌ NEVER use file:// prefix (CMM2 violation)
9. ❌ NEVER use relative paths without § notation
10. ⚠️ getDualLink returns project-root-relative in local link part
11. ⚠️ For source files NOT at root, use getDualLinkRelativePath to calculate paths
12. 🔧 Tool: `pdca getDualLinkRelativePath <from> <to>` calculates relative paths
13. ✅ Verification: cd to source dir, ls <path> to test link works
14. ❌ NEVER assume getDualLink output works without verification
15. 🚨 MANDATORY: Test every link with ls from source directory
16. ✨ Use getDualLinkRelativePath for zero-knowledge path calculation
17. 🧠 Context Window Awareness: Long sessions → assumptions → violations
18. ✅ ALWAYS run `git status` before presenting dual links
19. 🔍 Pattern: getDualLink commits PDCA, but build artifacts may remain uncommitted
20. ❌ NEVER assume all files are committed - VERIFY with git status
21. 🔄 RAG First: When uncertain, query trainAI before acting
22. ⚠️ Bootstrap Phase: Extra vigilance required - system being established (temporary)
23. 🎯 Forcing Function: git status → commit all → push → THEN present link

#### Verification Checklist

- [ ] Can write dual link format from memory
- [ ] Understands why GitHub link is needed (verification)
- [ ] Understands why § notation is needed (local navigation)
- [ ] Can use getDualLink to generate correct links
- [ ] Knows file must be pushed for link to be valid
- [ ] Recognizes CMM2 link violations (file://, no §, unpushed files)
- [ ] Knows getDualLink returns project-root-relative in local part
- [ ] Can use getDualLinkRelativePath to calculate relative paths
- [ ] Always verifies links with ls from source directory
- [ ] Tests every link before committing
- [ ] Checks git status before presenting dual links
- [ ] Commits ALL uncommitted files, not just PDCA
- [ ] Queries trainAI when assumptions arise
- [ ] Recognizes context window exhaustion symptoms

---

### 5. ✅ ensure-links - CMM3 Atomic Link Validation

**Description**: Zero-knowledge automation: Ensure all dual links are valid across entire project

#### Required Reading

1. **scrum.pmo/project.journal/2025-10-20-UTC-1008-session/2025-10-20-UTC-1215.pdca.md** (Depth: 2)
   - Reason: Complete design of dual link methods (getDualLink, findPDCAsLinking, updateLinksToFile, ensureValidLinks)

#### Key Lessons

1. 🎯 CMM3 Atomic: ensureValidLinks = single command, zero knowledge needed
2. ✅ Process: Normalize → Fix git → Generate canonical → Find PDCAs → Validate → Fix → Commit → Push
3. ✅ Usage: `pdca ensureValidLinks <file>` - fully automated
4. ✅ Dry-run: `pdca ensureValidLinks <file> true` - preview without changes
5. ✅ Idempotent: Safe to run multiple times, only fixes what needs fixing
6. 🔍 findPDCAsLinking: Find all PDCAs linking to a file (building block)
7. 🔄 updateLinksToFile: Bulk update when files move/version (building block)
8. ⚠️ Always run before PDCA completion to ensure valid links
9. ⚠️ Session end: Validate all session PDCAs

#### Verification Checklist

- [ ] Understands CMM3 atomic operation concept (zero-knowledge required)
- [ ] Can run ensureValidLinks on any file
- [ ] Knows when to use dry-run mode (preview)
- [ ] Understands idempotency (safe to run repeatedly)
- [ ] Can use findPDCAsLinking to find link dependencies
- [ ] Knows to validate links before PDCA/session completion

---

### 6. 🚀 component-upgrade - Link Management During Versioning

**Description**: Maintain valid links when components evolve: version bumps, file moves, refactoring

#### Required Reading

1. **components/Web4TSComponent/latest/README.md** (Depth: 1)
   - Reason: Component versioning patterns
   
2. **scrum.pmo/project.journal/2025-10-20-UTC-1008-session/2025-10-20-UTC-1215.pdca.md** (Depth: 1)
   - Reason: updateLinksToFile method design and usage

#### Key Lessons

1. ✅ Workflow: Version bump → Update links → Test → Commit
2. ✅ Create version: `web4tscomponent on <Component> <version> upgrade nextPatch`
3. ✅ Update links: `pdca updateLinksToFile <old-path> <new-path>`
4. ✅ Dry-run first: `pdca updateLinksToFile <old> <new> true` to preview
5. ✅ Auto-commit: updateLinksToFile commits and pushes by default
6. 🔍 Pre-check: `pdca findPDCAsLinking <old-path>` to see impact
7. ⚠️ Always update links BEFORE deleting old version
8. ⚠️ Document moves in PDCA (backward compatibility)
9. 🎯 Example: 0.2.0.0 → 0.2.1.0 updates all linking PDCAs automatically

#### Verification Checklist

- [ ] Can create new component version using web4tscomponent
- [ ] Knows to run findPDCAsLinking before version changes
- [ ] Can use updateLinksToFile in dry-run mode
- [ ] Understands when links need updating (path changes, version bumps)
- [ ] Knows to document version changes in PDCA
- [ ] Can maintain backward compatibility during refactoring

---

### 7. 🔀 merge - Post-Merge Integration and Build Requirements

**Description**: Complete merge integration: source + build + runtime verification for symlinked components

#### Required Reading

1. **scrum.pmo/project.journal/2025-10-20-UTC-1008-session/2025-10-23-UTC-1530.merge-impact-analysis.pdca.md** (Depth: 2)
   - Reason: Real case: Merge brought unbuilt dependencies, CLI failure analysis

#### Key Lessons

1. ⚠️ Source Code Merge ≠ Complete Integration!
2. ✅ Post-Merge Checklist: Resolve conflicts → Commit → BUILD components → Test → Verify CLI
3. 🔧 Build Step: MANDATORY for components with updated symlinks
4. ⚠️ Symlink Change → Build Requirement: If latest/dev/test symlinks change, build new versions
5. 🎯 Test Types: Build-time (tests pass) vs Runtime (CLI may fail) - both must work
6. ❌ NEVER assume merged code is ready - verify runtime dependencies
7. 🔍 Check Pattern: ls components/<Component>/<version>/dist/ after merge
8. ⚠️ Missing dist/ = Unbuilt version = Runtime import failure
9. ✅ Example: Web4TSComponent latest: 0.3.13.2 → 0.3.14.4 requires building 0.3.14.4
10. 🔧 Build Command: cd components/<Component>/<version> && npm install && npm run build
11. 💡 Why Tests Pass But CLI Fails: Tests use build context, CLI uses runtime imports
12. ⚠️ Symlinks in merge: Auto-accepted, may point to unbuilt versions
13. 🎯 Forcing Function: After merge, check ALL symlink targets for dist/ directory
14. ✅ CI/CD Gap: Need automated post-merge build verification
15. 📊 Integration = Source + Build Artifacts + Runtime Verification

#### Verification Checklist

- [ ] Understands source merge ≠ complete integration
- [ ] Knows post-merge checklist includes BUILD step
- [ ] Can identify when components need building (symlink changes)
- [ ] Recognizes build-time vs runtime import differences
- [ ] Checks for dist/ directory after merge
- [ ] Knows how to build merged component versions
- [ ] Understands why tests pass but CLI fails
- [ ] Can diagnose "Cannot find module" as missing build
- [ ] Verifies CLI works after merge (not just tests)
- [ ] Knows to check all symlink targets for build artifacts

---

### 8. 🔧 component - Web4 Component System

**Description**: Learn Web4 component patterns, versioning, and CLI auto-discovery

#### Required Reading

1. **components/Web4TSComponent/latest/README.md** (Depth: 2)
   - Reason: Web4 component architecture and patterns
   
2. **components/PDCA/0.1.0.0/src/ts/layer2/DefaultPDCA.ts** (Depth: 1)
   - Reason: Example component implementation

#### Key Lessons

1. ✅ Use web4tscomponent for ALL version operations
2. ✅ Version creation: web4tscomponent on <Component> <version> upgrade <promotion>
3. ✅ Semantic versioning: nextPatch, nextMinor, nextMajor, nextBuild
4. ✅ Component pattern: Empty constructor + scenario initialization + functionality
5. ✅ Symlinks: latest (dev), prod (stable), test, dev
6. ⚠️ NEVER manually copy component versions - violates CMM3
7. ✅ Web4 CLI uses positional parameters (no --flags)
8. ✅ Parameter order defined by @cliSyntax annotation
9. ✅ Optional parameters: <?param> (trail, can omit)
10. ✅ Required parameters: <param> or !<param>
11. ✅ Example: `pdca moveFile <oldPath> <newPath> <?dryRun>`
12. ❌ NEVER use --flag syntax (Unix-style)
13. ✅ Consistency: All Web4 components follow same pattern
14. 🔧 @cliSyntax defines parameter order in method signature
15. 🔧 @cliDefault provides defaults for optional parameters
16. 🔧 @cliValues enables tab completion discovery
17. ✅ DRY: Symlink node_modules, never duplicate dependencies
18. ✅ DRY: Extend tsconfig.json from project root
19. ✅ DRY: Reuse existing methods, never copy-paste logic
20. ✅ DRY: Cross-reference docs, never duplicate content
21. ✅ initProject creates global node_modules and tsconfig
22. ❌ NEVER create real node_modules directories in components
23. ⚠️ Duplicated dependencies violate CMM3 (not reproducible)
24. ✅ Radical OOP: Empty constructors (no parameters)
25. ✅ Radical OOP: All config via init(scenario) method
26. ✅ Pattern: constructor() { this.model = {}; }
27. ✅ Pattern: init(scenario: Scenario<Model>): this
28. ✅ Why: Zero-dependency instantiation (testability)
29. ✅ Why: Flexible composition (multiple scenarios)
30. ❌ NEVER use constructor parameters (breaks radical OOP)
31. ✅ Method Chaining: Always return Promise<this>
32. ✅ Enables fluent API: component.method1().method2()
33. ✅ Enables CLI chaining: pdca method1 param1 method2
34. ✅ Pattern: async myMethod(): Promise<this> { return this; }
35. ✅ Auto-Discovery: Add method → CLI command appears
36. ✅ @cliSyntax annotation defines parameter order
37. ✅ @cliValues annotation enables tab completion
38. ✅ @cliHide annotation hides internal methods
39. ✅ TSDoc becomes CLI help text automatically
40. ❌ NEVER manually edit CLI files (auto-generated)

#### Verification Checklist

- [ ] Can create new component version using web4tscomponent
- [ ] Understands semantic version promotion types
- [ ] Knows component directory structure and symlink purposes
- [ ] Can build component using: web4tscomponent on <Component> <version> build
- [ ] Recognizes when to use nextPatch vs nextMinor vs nextMajor
- [ ] Understands Web4 uses positional parameters, not flags
- [ ] Can read @cliSyntax to determine parameter order
- [ ] Knows optional parameters trail and can be omitted
- [ ] Understands DRY principle for dependencies (symlinks)
- [ ] Knows to extend tsconfig from root, not duplicate
- [ ] Can identify code duplication and refactor to reuse
- [ ] Understands radical OOP empty constructor pattern
- [ ] Can write init(scenario) method for configuration
- [ ] Knows constructor() should have no parameters
- [ ] Always returns Promise<this> for method chaining
- [ ] Understands @cliSyntax, @cliValues, @cliHide annotations
- [ ] Can add methods that auto-discover as CLI commands
- [ ] Recognizes CMM2 violations (real node_modules, constructor params)
- [ ] Can explain why DRY and Radical OOP enable CMM3
- [ ] Knows web4tscomponent initProject sets up DRY structure

---

### 9. 🛠️ feature-development - RAG-Powered Test-First CMM3 Pattern

**Description**: Master CMM3-compliant feature development: RAG preparation, test-first design, automated verification, and knowledge loop closure

#### Required Reading

1. **scrum.pmo/project.journal/2025-10-20-UTC-1008-session/2025-10-21-UTC-1550.feature.pdca.md** (Depth: 2)
   - Reason: Real example: getDualLinkRelativePath implementation using the pattern
   
2. **scrum.pmo/project.journal/2025-10-20-UTC-1008-session/2025-10-21-UTC-1605.pdca.md** (Depth: 2)
   - Reason: Meta-learning: Pattern extraction and CMM3 compliance analysis
   
3. **scrum.pmo/project.journal/2025-10-20-UTC-1008-session/2025-10-21-UTC-1410.test-first-verification.pdca.md** (Depth: 1)
   - Reason: Test-first verification principles and anti-patterns
   
4. **scrum.pmo/project.journal/2025-10-20-UTC-1008-session/2025-10-21-UTC-1700.pdca.md** (Depth: 2)
   - Reason: One-loop success: queryTrainAI implementation and why it worked

#### Key Lessons

1. ✅ Phase 0 - RAG Preparation: Query trainAI BEFORE planning (test-first, component)
2. ⏱️ RAG Preparation is Non-Negotiable: 30 min reading → 2-3 hours debugging saved
3. 📚 Read to depth 3: document → references → secondary references
4. 🧠 Build complete mental model BEFORE coding (prevents assumption cascade)
5. ✅ Phase 1 - TRON Collaboration: Accept challenges as refinement opportunities
6. 🔄 TRON Challenges → Research → Document → Improve (not defend current approach)
7. 📖 User has knowledge agent doesn't - research immediately when challenged
8. ✅ Phase 2 - Test-First Design: Write 5-7 comprehensive tests BEFORE implementation
9. 🎯 DRY at Planning Stage: Identify reusable parts in plan, extract helpers from start
10. 🔧 Web4 Naming: methodNameInternal() for private helpers (NO underscores!)
11. ❌ NEVER use _methodName() or _methodNameInternal() (underscore violation)
12. ✅ Correct: calculateRelativePathInternal(), getDataInternal()
13. ❌ Wrong: _calculateRelativePath(), _getTrainingTopicsInternal()
14. 📝 Leave TODO comments for future DRY refactoring opportunities
15. ✅ Phase 3 - Expected Failure: Run tests, see failure, TRUST it (no manual check)
16. ✅ Phase 4 - Minimal Implementation: Add ONLY what's needed to pass tests
17. 🎨 Apply Web4 principles systematically: DRY, Radical OOP, Method Chaining, Auto-Discovery
18. ✅ Phase 5 - Trust the Green: Tests pass = done (no manual verification)
19. ✅ Phase 6 - trainAI Integration: Close knowledge loop immediately
20. ✅ Phase 7 - TRON Validation: User confirms pattern, closes feedback loop
21. 🎯 CMM3 Compliance: Objective (tests) + Reproducible (git) + Systematic (process)
22. ⏱️ Time Investment: ~90 min for CMM3 feature vs quick hack
23. 🚀 Success Metric: TRON validates pattern, auto-promotion succeeds
24. 🏆 One Loop = CMM4 Excellence: Write → Fail → Implement → Pass → Done (NO iteration)
25. ❌ NEVER skip tests: Test-first is mandatory for CMM3
26. ❌ NEVER manual verify: Tests are objective arbiter, not agent judgment
27. ❌ Multiple loops = CMM2 trial-and-error (avoid this)
28. 🔄 RAG-Powered FOR TWO: Agent + trainAI + Tests + TRON = CMM3 naturally
29. 💡 Meta-Pattern: Query → Challenge → Test → Implement → Verify → Document → Validate
30. 🎓 External verification at EVERY phase prevents CMM2 violations
31. ✨ Pattern is replicable: Same 7 steps work for any new feature
32. 📊 Web4 Principles Research Has Exponential ROI: 30 min reading → Apply 7 principles forever

#### Verification Checklist

- [ ] Queried trainAI before planning (test-first, relevant domain topics)
- [ ] Read referenced docs to depth 3 (not just surface level)
- [ ] Built complete mental model before coding
- [ ] Identified reusable parts at planning stage (not refactoring)
- [ ] Extracted DRY helpers from start (not after duplication)
- [ ] Wrote tests before implementation (5-7 test cases)
- [ ] Ran tests and saw expected failure (method not found, etc)
- [ ] Trusted failure without manual verification
- [ ] Applied Web4 principles systematically (DRY, Radical OOP, Chaining, Auto-Discovery)
- [ ] Implemented minimal code to pass tests (no gold-plating)
- [ ] All tests passed without manual verification
- [ ] Implementation completed in ONE feedback loop (no iteration cycles)
- [ ] TRON challenges led to research and documentation (not defense)
- [ ] Updated trainAI with new knowledge immediately
- [ ] TRON validated the pattern and result
- [ ] Can explain why this is CMM3 (objective, reproducible, systematic)
- [ ] Can replicate pattern for next feature development
- [ ] Understands 90-min investment pays off in reliability
- [ ] Recognizes external verification (trainAI + Tests + TRON) as key to CMM3
- [ ] Achieved "one loop" success (TRON impressed with efficiency)

---

### 10. 🔄 web4-vs-nodejs - Pattern Migration Guide

**Description**: Web4 components use modern ES modules and strict naming conventions. This guide covers common Node.js patterns and their Web4-compliant equivalents.

#### Required Reading

1. **scrum.pmo/project.journal/2025-10-20-UTC-1008-session/2025-10-23-UTC-1730.web4-dirname-violation.pdca.md** (Depth: 2)
   - Reason: Real violation: __dirname usage and Web4-compliant fix
   
2. **components/Web4TSComponent/latest/src/ts/layer2/DefaultWeb4TSComponent.ts** (Depth: 1)
   - Reason: Source of truth: Web4 file path resolution pattern

#### Key Lessons

1. ❌ __dirname and __filename: Node.js globals with underscores → Web4 violation!
2. ✅ Web4 Pattern: Use import.meta.url with URL() constructor
3. 📝 Example Wrong: const dir = __dirname; const file = __filename;
4. 📝 Example Right: const url = new URL(import.meta.url); const dir = path.dirname(url.pathname);
5. ⚠️ Why: Web4 Principle → NO underscores in ANY naming (including built-ins)
6. ⚠️ Why: ES Modules → __dirname/__filename don't exist in module scope
7. ✅ Consistency: ALL Web4 components use import.meta.url pattern
8. 📍 Pattern Source: Web4TSComponent constructor (line ~19-20)
9. 🎯 Test Files: const currentFileUrl = new URL(import.meta.url);
10. 🎯 Test Files: const testDir = path.dirname(currentFileUrl.pathname);
11. 🎯 Then use: path.join(testDir, 'data', 'fixtures')
12. 🎯 CLI Files: Same pattern for resolving template paths
13. ✅ When to Use: Any code needing current file location
14. ❌ Never Use: __dirname, __filename (underscore violation)
15. 🔍 Detection: Search codebase for __dirname and __filename
16. 🔧 Fix Pattern: Replace all occurrences with import.meta.url
17. 📊 RAG Queries: "dirname file path test" → finds this topic
18. 📊 RAG Queries: "web4 naming underscore" → finds this topic
19. 📊 RAG Queries: "__dirname equivalent" → finds this topic
20. ⚠️ Context Window Risk: Node.js habits persist without RAG check
21. ✅ Forcing Function: Query "test file patterns" BEFORE writing tests
22. ✅ Verification: Run tests after replacement to confirm pattern works
23. 🎓 Meta-Pattern: Don't assume Node.js knowledge applies → verify with RAG

#### Verification Checklist

- [ ] Searched codebase for __dirname and __filename occurrences
- [ ] Replaced with import.meta.url + URL() constructor pattern
- [ ] Added const currentFileUrl = new URL(import.meta.url) at file top
- [ ] Used path.dirname(currentFileUrl.pathname) for directory
- [ ] Used currentFileUrl.pathname for full file path
- [ ] Verified pattern matches Web4TSComponent implementation
- [ ] Ran tests to confirm pattern works correctly
- [ ] No underscore violations remaining in code
- [ ] Understands why this violates Web4 naming (underscores)
- [ ] Understands why this violates ES modules (scope)
- [ ] Can explain pattern to next agent
- [ ] Queried RAG before using file path resolution
- [ ] Recognized Node.js habit required explicit checking
- [ ] Will query "test patterns" proactively in future

---

### 11. 🛠️ tech-stack - Project Technology & Testing Framework

**Description**: Web4Articles uses modern TypeScript, ESM, and Vitest. Jest is BANNED. Understanding the tech stack prevents violations and ensures compatibility.

#### Required Reading

1. **docs/tech-stack.md** (Depth: 2)
   - Reason: CRITICAL: Defines approved technologies and BANNED frameworks (Jest)

#### Key Lessons

1. ✅ Testing Framework: Vitest ONLY - modern, ESM-native, TypeScript-first
2. ❌ Jest is BANNED: Poor ESM support, legacy CJS patterns, slow migration
3. 📦 Import Pattern: import { describe, it, expect } from 'vitest'
4. ⚠️ Tech Debt Violation: Any Jest config, scripts, or dependencies must be removed
5. 🏗️ Architecture: Web4TSComponent v0.3.x - component-based, TypeScript-first
6. 📝 Language: TypeScript (ES2020+) with full type safety
7. 🔧 CLI System: Auto-discovery with method chaining
8. 📊 Development Level: CMM4 (systematic, automated, quantitatively managed)
9. 🎯 Tooling: PlantUML + Graphviz for architecture diagrams
10. 🐳 Environment: Docker + Devcontainer for cross-platform consistency
11. ✅ Module System: Pure ESM - NO CommonJS (require, module.exports)
12. ✅ Modern JS: Full support for import.meta.url, top-level await
13. 🔍 Detection: Search for jest, ts-jest, jest.config - all violations
14. 🔧 Fix Pattern: Replace with vitest, vitest.config.ts
15. 📊 RAG Queries: "test framework" → finds this topic
16. 📊 RAG Queries: "vitest jest" → finds this topic
17. ⚠️ Context Window Risk: Assuming Jest is allowed → BANNED
18. ✅ Forcing Function: Query "tech stack" BEFORE adding dependencies

#### Verification Checklist

- [ ] Read docs/tech-stack.md completely
- [ ] Understands Jest is BANNED - no exceptions
- [ ] Knows correct import: import { describe, it, expect } from 'vitest'
- [ ] Can identify Jest violations (jest, ts-jest, jest.config)
- [ ] Understands why Vitest: ESM-native, TypeScript-first, modern
- [ ] Knows project uses pure ESM - no CommonJS
- [ ] Understands Web4TSComponent architecture
- [ ] Will query "tech stack" before adding new dependencies
- [ ] Will check docs/tech-stack.md for approved technologies
- [ ] Can explain to next agent why Jest is banned

---

### 12. 🧪 test-workflow - Semantic Versioning and Test Iteration

**Description**: Master the test workflow: latest → test → dev → prod with auto-promotion and test iteration

#### Required Reading

1. **scrum.pmo/project.journal/2025-10-20-UTC-1008-session/2025-10-21-UTC-1234.pdca-test-workflow.pdca.md** (Depth: 3)
   - Reason: Complete test workflow documentation with semantic versioning
   
2. **components/Web4TSComponent/latest/README.md** (Depth: 1)
   - Reason: Component versioning and testing patterns

#### Key Lessons

1. 🔗 Semantic links: latest (dev work) → test (testing) → dev (stable) → prod (production)
2. 🧪 Test workflow: Work on `latest` → run `pdca test` → auto-promotes to `test` on success
3. ✅ Auto-promotion: `pdca test` creates/updates `test` symlink when all tests pass
4. 🔧 Test iteration: `web4tscomponent on <Component> latest test itCase` shows test tree
5. 📊 View state: `web4tscomponent on <Component> latest tree links` shows semantic links
6. 🛑 WORKFLOW REMINDER: Always work on dev until test → work on test until success → work on dev after success
7. ⚠️ Version promotion: Use component commands (promote, upgrade), NEVER manual symlinks
8. 🎯 Test selection: `web4tscomponent test itCase <token>` to run specific tests (e.g., 2a1)
9. 🔍 When tests fail: Fix on `test` version, not `latest`
10. ❌ Violated pattern: Fixing tests on `latest` instead of switching to `test` version
11. 💡 Test fixtures can pollute component structure (components/X/version/components/)
12. ⚠️ Obey forcing functions: WORKFLOW REMINDER is there for a reason
13. 📝 Commit discipline: Always commit new versions after successful `pdca test` auto-promotion
14. 🔄 Version lifecycle: `pdca test` manages symlinks but does NOT commit - that's your job
15. ✨ Test success = commit trigger: Auto-promotion signals "this version is ready to track"

#### Verification Checklist

- [ ] Understands 4-level semantic versioning (latest, test, dev, prod)
- [ ] Knows the complete test workflow (latest → test → dev → prod)
- [ ] Recognizes auto-promotion happens on test success
- [ ] Can use `test itCase` to view and select tests
- [ ] Can use `tree links` to view semantic version state
- [ ] Knows to obey the WORKFLOW REMINDER
- [ ] Understands why manual symlink changes are CMM3 violations
- [ ] Can identify when to work on `test` vs `latest` version
- [ ] Recognizes test fixture pollution issues
- [ ] Commits new versions after `pdca test` auto-promotion
- [ ] Understands that `pdca test` manages symlinks but does not commit

---

### 13. 🧪 test-without-versioning - Baseline Verification

**Description**: Learn to run tests without triggering version creation: test itCase for discovery, specific tests for verification, direct vitest for baseline

#### Required Reading

1. **scrum.pmo/project.journal/2025-10-20-UTC-1008-session/2025-10-21-UTC-1710.pdca.md** (Depth: 2)
   - Reason: Real-world learning: Baseline truth testing before DRY refactoring
   
2. **components/Web4TSComponent/latest/README.md** (Depth: 1)
   - Reason: Test itCase functionality documentation

#### Key Lessons

1. 🔍 Viewing Tests: `web4tscomponent on <Component> latest test itCase` shows complete test tree
2. 📊 Test tree displays: file number, describe blocks, test cases with tokens (no execution, no versioning)
3. 🎯 Running Specific Tests: `web4tscomponent on <Component> latest test itCase <token>` (e.g., 5a1)
4. ✅ Specific tests run ONLY that test using vitest filtering - safe for baseline checks
5. 🧪 Running All Tests: `cd components/<Component>/latest && npx vitest run` bypasses auto-promotion
6. 📝 Direct vitest call useful for comprehensive baseline verification without versioning
7. ✓ Before refactoring (establish baseline) - use test itCase or direct vitest
8. ✓ During debugging (isolate failures) - use specific test tokens
9. ✓ When testing in `latest` (not ready for auto-promotion) - avoid `pdca test`
10. ❌ When ready to promote - use `pdca test` instead (triggers auto-promotion)
11. ⚠️ Why NOT `pdca test`: Triggers auto-promotion workflow, creates new versions (test, prod, dev)
12. 🚫 `pdca test` not suitable for baseline checks - it modifies semantic version links
13. 🔢 Test Tokens Format: `<file><describe><test>` (e.g., 5a1 = file 5, describe a, test 1)
14. 📁 File: Test file number (1-7), Describe: Letter (a, b, c), Test: Number (1, 2, 3)
15. 🎓 Zero-Knowledge Principle: Use `web4tscomponent test itCase` FIRST to discover tests
16. 🔍 Don't assume test names or structure - let the tool show you what exists
17. 💡 Baseline truth test: Run tests BEFORE refactoring to prove system works
18. ✅ If tests fail after refactoring, you KNOW you broke something (objective proof)
19. 📊 CMM3 Compliance: Objective baseline = verifiable before/after comparison

#### Verification Checklist

- [ ] Can view test tree without executing tests
- [ ] Can run specific test by token (e.g., 5a1)
- [ ] Understands when to use `itCase` vs `pdca test`
- [ ] Knows how to establish baseline before refactoring
- [ ] Recognizes `pdca test` creates versions (auto-promotion)
- [ ] Can explain test token format (<file><describe><test>)
- [ ] Uses zero-knowledge approach (discover tests first, don't assume)
- [ ] Understands baseline truth testing for CMM3 verification

---

### 14. 🧪 test-first - Trust Tests, Avoid Manual Verification

**Description**: Master the test-first pattern: Write tests first, trust them to show pass/fail, avoid manual verification loops

#### Required Reading

1. **scrum.pmo/project.journal/2025-10-20-UTC-1008-session/2025-10-21-UTC-1410.test-first-verification.pdca.md** (Depth: 3)
   - Reason: Meta-learning from violating test-first pattern
   
2. **scrum.pmo/project.journal/2025-10-20-UTC-1008-session/2025-10-21-UTC-1007.meta-learning.pdca.md** (Depth: 2)
   - Reason: Context on over-implementation and assumption cascade

#### Key Lessons

1. ✅ Test-First Pattern: Write test → Run test → See it fail → Fix code → See it pass
2. 🎯 Trust the tests: If tests pass, functionality works. No manual verification needed.
3. ❌ Anti-pattern: "Let me manually verify that the test failed before fixing"
4. ❌ Anti-pattern: "I'll run the command manually to confirm the bug exists"
5. 🔄 CMM4 feedback loop: Test IS the verification mechanism
6. ⚡ Efficiency: Manual verification duplicates test effort and wastes time
7. 🛡️ Safety: Tests are reproducible; manual checks are subjective and error-prone
8. 📊 Test output is authoritative: PASS = works, FAIL = broken, no interpretation needed
9. 🚫 Never skip directly to fixing: Always run the test first to see the failure
10. ✨ Test-first enforces CMM3: Objective criteria (test assertions) over subjective judgment
11. ⚠️ Root cause: Efficiency bias → assumption cascade → skipping verification step
12. 💡 When debugging: Write a test that reproduces the bug, then fix until test passes

#### Verification Checklist

- [ ] Can write a failing test before implementing a feature
- [ ] Trusts test output as authoritative (no manual verification)
- [ ] Recognizes manual verification as an anti-pattern
- [ ] Understands test-first as a CMM4 feedback loop
- [ ] Can identify when bias is leading to assumption cascade
- [ ] Knows to run tests first, not fix first
- [ ] Understands why test-first is CMM3-compliant (objective criteria)
- [ ] Can explain why manual verification is CMM2 (subjective)
- [ ] Avoids over-implementation (doing more than requested)
- [ ] Stops after showing test results, waits for user direction

---

### 15. 🎯 interpret-instructions - Literal vs Implied Actions

**Description**: Master the art of parsing user instructions to understand exactly what's requested vs what's assumed

#### Required Reading

1. **scrum.pmo/roles/SaveRestartAgent/cmm3.compliance.checklist.md** (Depth: 2)
   - Reason: 6d - No assumptions about user intent
   
2. **scrum.pmo/project.journal/2025-10-20-UTC-1008-session/2025-10-21-UTC-1007.meta-learning.pdca.md** (Depth: 3)
   - Reason: Real example of instruction misinterpretation

#### Key Lessons

1. ✅ "Show me X" means: Execute X, Display result, STOP
2. ✅ "Fix X" means: Analyze, Propose, Implement (after confirmation)
3. ✅ "X and Y" means: Do X, then do Y
4. ✅ "X" does NOT imply Y, even if Y seems logical
5. ⚠️ Punctuation matters: "pdca" vs "pdca!" vs "PDCA"
6. 🛑 Feedback points: Where control returns to user
7. ❌ Never add implied actions
8. ❌ Never assume "next logical step"
9. 💡 Examples: "run tests" → Execute + show output + STOP (NOT: run + analyze + fix + commit)
10. 💡 "show me file.md" → Display file + STOP (NOT: show + analyze + suggest)
11. 💡 "pdca!" → Create PDCA file (NOT: write PDCA-formatted response)
12. 💡 "read X" → Read X, provide dual link, STOP (NOT: read + summarize + analyze)

#### Verification Checklist

- [ ] Can parse "show me X" correctly (execute + display + stop)
- [ ] Understands difference between command and suggestion
- [ ] Recognizes punctuation significance (!, CAPS, etc)
- [ ] Can identify feedback points in instructions
- [ ] Knows when to ask vs assume

---

### 16. 🤝 collaborate - User-in-the-Loop CMM4 Pattern

**Description**: Understand CMM4 collaboration where user controls the loop and agent enables execution

#### Required Reading

1. **scrum.pmo/project.journal/2025-09-22-UTC-1908-session/howto.cmm.md** (Depth: 3)
   - Reason: CMM4 as feedback loop mastery
   
2. **scrum.pmo/project.journal/2025-10-20-UTC-1008-session/2025-10-21-UTC-1007.meta-learning.pdca.md** (Depth: 3)
   - Reason: Real example of collaboration violation
   
3. **scrum.pmo/roles/_shared/PDCA/PDCA.howto.decide.md** (Depth: 2)
   - Reason: Decision-making framework for user alignment

#### Key Lessons

1. 🔄 CMM4 Loop: User decides → Agent executes → FEEDBACK POINT → User reflects → User decides
2. ✅ User controls WHAT to do
3. ✅ Agent controls HOW to do it
4. ✅ Feedback points = where control returns to user
5. 🛑 STOP at feedback points, don't assume next step
6. ⚠️ "Helpful" = enabling user, NOT solving without asking
7. ❌ Never close feedback loop prematurely
8. ❌ Never assume user wants problem solved
9. 💡 Collaboration Model: User (Decision) → Agent (Execute) → FEEDBACK POINT 🛑 STOP → User (Reflection) → User (Decision)
10. 💡 Anti-Pattern: User → Agent → (everything done) → User sees result ❌
11. 💡 Correct: User → Agent → Result → STOP → User → Next instruction ✅

#### Verification Checklist

- [ ] Understands CMM4 collaboration loop
- [ ] Can identify feedback points
- [ ] Knows when to STOP vs continue
- [ ] Recognizes "helpful" vs "presumptuous"
- [ ] Waits for user decision at feedback points

---

### 17. 💬 chat-response - CMM3 Compliance for Agent Replies

**Description**: Master the art of chat responses - links only, no explanatory text, proper dual link format

#### Required Reading

1. **scrum.pmo/roles/_shared/PDCA/chat.report.template.md** (Depth: 2)
   - Reason: Official chat report format
   
2. **scrum.pmo/roles/SaveRestartAgent/cmm3.compliance.checklist.md** (Depth: 2)
   - Reason: 3a-3c chat response compliance

#### Key Lessons

1. ✅ CMM3 3a: Links only, no explanatory text
2. ✅ CMM3 3c: Dual link format: [GitHub](URL) | [§/path](path)
3. ✅ CMM3 4c: Local link uses project-root-relative path
4. ✅ When user says "read X" → provide dual link, that's it
5. ⚠️ No summaries, no analysis, no "key points"
6. ⚠️ Exception: QA Decisions must be copied verbatim
7. ❌ NEVER add explanatory text before/after link
8. ❌ NEVER provide summary instead of link
9. 💡 Wrong: "I've read the CMM3 compliance checklist. Key points: ... [link]" ❌
10. 💡 Right: "[GitHub](URL) | [§/path](path)" ✅

#### Verification Checklist

- [ ] Can provide links without explanatory text
- [ ] Uses correct dual link format
- [ ] Knows when to add text (QA Decisions only)
- [ ] Recognizes 3a violations in own responses
- [ ] Can generate project-root-relative paths

---

### 18. 📊 report - Concise Task Completion Without Summary Generation

**Description**: Master concise reporting - avoid elaborate summaries (context window symptom), query RAG first, follow CMM3 format

#### Required Reading

1. **scrum.pmo/project.journal/2025-10-20-UTC-1008-session/2025-10-23-UTC-1445.meta-meta-learning-summary-instinct.pdca.md** (Depth: 2)
   - Reason: Documents summary generation as context window pressure indicator
   
2. **scrum.pmo/project.journal/2025-10-20-UTC-1008-session/2025-10-23-UTC-1430.context-window-recovery-trainai.pdca.md** (Depth: 2)
   - Reason: Context window exhaustion patterns and git status protocol

#### Key Lessons

1. 🚨 Summary Generation = Red Flag: Elaborate formatting/boxes indicate context window pressure
2. ✅ Query RAG BEFORE Reporting: `pdca queryTrainAI "How should I report task completion?"`
3. ✅ Concise Format: Facts + dual links + git status + STOP
4. ❌ NEVER generate elaborate summaries without RAG query
5. ❌ NEVER use boxes, multiple heading levels, decorative elements
6. ❌ NEVER speculate on "What's Next" (user controls loop)
7. ⚠️ Characteristics of Summary Mode: Comprehensive recaps, "executive summary" style, next steps speculation
8. ⚠️ Why It Happens: Context window pressure → compression instinct → violation risk
9. 🎯 Forcing Function Checklist: 1) git status 2) commit all 3) push 4) query trainAI 5) follow guidance 6) report 7) STOP
10. 💡 Pattern: Integration into trainAI ≠ Active use of trainAI
11. 💡 Even recent learning requires RAG queries (memory ≠ RAG)
12. 🔄 Bootstrap Phase: Extra vigilance - query RAG for EVERY reporting task
13. ✨ Correct Report: "Task complete. Files: [dual link]. Git status: clean. *Awaiting instruction.*"
14. 🧠 Meta-Pattern: When you DON'T think you need RAG is when you need it most
15. 🤝 User Controls Loop: Report facts, provide links, STOP - no loop closure
16. ⚠️ Summary instinct compensates for fuzzy memory - trigger for RAG query
17. 🎓 Test: If you're about to write "Summary:", query trainAI instead

#### Verification Checklist

- [ ] Recognizes summary generation as context window symptom
- [ ] Queries trainAI before reporting task completion
- [ ] Uses concise format (facts + links + status + STOP)
- [ ] Avoids elaborate formatting and decorative elements
- [ ] Does not speculate on next steps
- [ ] Checks git status before reporting
- [ ] Commits ALL files, not just main deliverable
- [ ] Understands forcing function checklist
- [ ] Recognizes when assumptions are arising
- [ ] Can identify "summary mode" in own writing
- [ ] Knows to query RAG when NOT feeling uncertain (paradox)

---

### 19. 📄 license-headers - AI-GPL License Management

**Description**: Master license header management - why headers matter, how to use licensetool, when to run checks

#### Required Reading

1. **AI-GPL.md** (Depth: 2)
   - Reason: Complete AI-GPL addendum specification and rationale
   
2. **.reuse/dep5** (Depth: 1)
   - Reason: Machine-readable license mappings for all file types
   
3. **scrum.pmo/project.journal/2025-10-20-UTC-1008-session/2025-10-23-UTC-0904.feature.pdca.md** (Depth: 2)
   - Reason: Complete LicenseTool implementation with test-first pattern
   
4. **scrum.pmo/sprints/sprint-10/planning.md** (Depth: 1)
   - Reason: Original requirements and business context

#### Key Lessons

1. 📄 Why Headers Matter: Legal protection, AI training clarity, copyleft enforcement
2. 🎯 AGPL-3.0-only WITH AI-GPL-Addendum: All files get this license
3. 📁 Process Artifacts: Subset with commercial dual-licensing (scrum.pmo/, *.pdca.md)
4. ✅ licensetool check: Verify all headers present and up-to-date
5. ✅ licensetool apply: Add/update headers automatically
6. ✅ licensetool apply . true: Dry-run mode (see changes before applying)
7. 🔧 Shebang Pattern: Remove from .ts source (causes build errors), only in .js
8. 📝 Required Header Elements: SPDX-License-Identifier, SPDX-FileComment, Copyright, Copyleft, Backlinks
9. 🔗 Relative Path to AI-GPL.md: Use calculateRelativePathInternal() pattern
10. 🏗️ CI Integration: GitHub Actions runs licensetool check on all pushes/PRs
11. ❌ NEVER manual headers: Use licensetool to ensure consistency
12. ❌ NEVER skip CI: License compliance is mandatory
13. ⚠️ Test Fixtures Exception: test/data/ files NOT process artifacts
14. 💡 When adding new file types: Update shouldSkipFileInternal() in LicenseTool
15. 💡 Web4 Naming: NO underscores, Internal suffix for private helpers
16. 📊 REUSE Compliance: Industry standard for machine-readable license metadata
17. 🎓 Dual-Licensing Model: Open-source (AGPLv3) + Commercial (AI use cases)
18. 🔄 Header Updates: Run licensetool apply after copyright year changes
19. ✨ Auto-Completion: Tab completion works for file paths and dryRun parameter
20. 🧪 Test-First Pattern: 60 tests written before implementation (98.3% pass rate)

#### Verification Checklist

- [ ] Can run licensetool check and interpret results
- [ ] Understands difference between missing vs outdated headers
- [ ] Can use dry-run mode before applying changes
- [ ] Knows when headers are required (all tracked files)
- [ ] Understands AI-GPL scope (all files, process artifacts subset)
- [ ] Can add headers to new file types if needed
- [ ] Knows to check CI status after header changes
- [ ] Understands shebang conflicts with headers
- [ ] Can explain why headers use relative paths
- [ ] Recognizes process artifacts vs regular files

---

### 20. ⚖️ decide - QA Decision Framework for PDCAs

**Description**: Master the art of presenting QA decisions - when to ask, what to ask, how to format decisions properly

#### Required Reading

1. **scrum.pmo/roles/_shared/PDCA/PDCA.howto.decide.md** (Depth: 3)
   - Reason: Complete decision-making framework with examples
   
2. **scrum.pmo/roles/SaveRestartAgent/cmm3.compliance.checklist.md** (Depth: 1)
   - Reason: Section 1j: QA Decisions format compliance
   
3. **scrum.pmo/roles/_shared/PDCA/template.md** (Depth: 1)
   - Reason: See QA Decisions section structure in official template

#### Key Lessons

1. ✅ QA Decisions are for USER decisions, not agent decisions
2. ⚖️ The 42 Rule: When in doubt, ASK! The answer to everything is often another question
3. ✅ Three valid formats: Pending decisions [ ], Completed [x], or "All clear, no decisions to make"
4. ✅ Present decisions when: Real risk exists, Multiple valid approaches, Ambiguous requirements, Significant impact
5. ❌ DON'T present when: User already decided, No real risk, Only one sensible option, Fake opposites
6. 🚨 Destructive operations REQUIRE warnings (force push, delete, overwrite)
7. 📋 Format: Numbered decisions with options a/b/c including rationale/consequences
8. ✅ Check official docs BEFORE creating decisions (semver.org, CMMI, git docs, project glossary)
9. ✅ Decision lifecycle: Pending [ ] → TRON answers → Agent implements → Completed [x]
10. ❌ NEVER create different QA Decisions in chat - copy EXACTLY from PDCA
11. ⚠️ Startup decisions: Focus Area, Role Selection, Session Duration, PDCA Location, Agent Identity
12. 🔧 Interactive decisions: Checkbox pattern with indented metadata for branch updates
13. 💡 Good decisions empower users, bad decisions waste time
14. 🤝 Collaboration pattern: Present decision, STOP, wait for user response
15. ❌ No fake opposites: Never present "do it" vs "don't do it" as options
16. ✅ Decision quality: Clear title, distinct options, consequences explained, official sources checked

#### Verification Checklist

- [ ] Can identify when a decision is needed vs when it's not
- [ ] Understands the three valid QA Decision formats
- [ ] Can format decisions with proper checkbox syntax
- [ ] Knows to check official documentation before creating decisions
- [ ] Recognizes fake opposites and avoids them
- [ ] Can write destructive operation warnings properly
- [ ] Understands decision lifecycle from pending to completed
- [ ] Knows to copy EXACT decisions from PDCA to chat (no paraphrasing)
- [ ] Can present startup decisions with focus/role/duration/location
- [ ] Understands the 42 Rule - asking when unsure is correct behavior

---

## Appendix: Quick Reference

### When to Query trainAI

Query trainAI BEFORE:
- Starting any new feature or task
- Making architectural decisions
- Modifying component versions
- Writing tests
- Creating PDCAs
- Reporting task completion
- Adding dependencies
- Working with git operations

### Common RAG Queries

```bash
# General workflow
pdca queryTrainAI "How do I start a new feature?"
pdca queryTrainAI "How should I report completion?"

# Technical patterns
pdca queryTrainAI "How do I validate dual links?"
pdca queryTrainAI "What is the test-first workflow?"
pdca queryTrainAI "How do I use component versioning?"

# Specific topics
pdca trainAI start              # Startup protocol
pdca trainAI feature-development # Feature development pattern
pdca trainAI test-first         # Test-first methodology
pdca trainAI dual-links         # Dual link format
```

### Core Principles

1. **Read FIRST, Act SECOND** - Query trainAI before starting work
2. **Test-First** - Write tests before implementation
3. **CMM3 Compliance** - Objective, reproducible, verifiable
4. **DRY** - Don't Repeat Yourself
5. **Radical OOP** - Empty constructors, scenario initialization
6. **Method Chaining** - Always return Promise<this>
7. **Auto-Discovery** - Methods become CLI commands
8. **User-in-the-Loop** - User controls WHAT, agent controls HOW

### Red Flags

🚨 **Context Window Exhaustion Symptoms:**
- Elaborate summaries
- Decorative boxes
- Speculating on "next steps"
- Assuming without RAG query
- Node.js patterns creeping in

**Action**: Query trainAI immediately!

### CMM Levels Quick Reference

- **CMM1 (Chaos)**: No process, unpredictable
- **CMM2 (Subjective)**: Ad-hoc processes, manual operations
- **CMM3 (Objective)**: Defined, reproducible, verifiable
- **CMM4 (Feedback Loop)**: Continuous improvement, systematic

### Component Commands

```bash
# Version operations
web4tscomponent on <Component> <version> upgrade nextPatch
web4tscomponent on <Component> <version> build
web4tscomponent on <Component> latest test
web4tscomponent on <Component> latest test itCase
web4tscomponent on <Component> latest tree links

# Link operations
pdca getDualLink <file>
pdca getDualLinkRelativePath <from> <to>
pdca ensureValidLinks <file>
pdca findPDCAsLinking <file>
pdca updateLinksToFile <old> <new>
pdca moveFile <old> <new>

# License operations
licensetool check
licensetool apply . false
licensetool apply . true  # dry-run
```

---

## Philosophical Insight

"Never 2 1 (TO ONE). Always 4 2 (FOR TWO)."

This knowledge base exists to enable collaboration between human and AI at CMM4 level - systematic, reproducible, and continuously improving. The trainAI system is not just documentation; it's a feedback loop mechanism that allows AI agents to evolve beyond base LLM limitations through structured learning and external verification.

**The Pattern**: Query → Learn → Test → Implement → Verify → Document → Validate

**The Goal**: "One loop" success - get it right the first time through preparation, not iteration.

**The Cost**: 30 minutes reading prevents 2-3 hours debugging. Doing it wrong first is 100x more expensive than doing it right first.

---

**Document Version**: 1.0  
**Last Updated**: 2025-10-29  
**Source**: PDCA Component trainAI Method  
**License**: AGPL-3.0-only WITH AI-GPL-Addendum  
**Status**: Complete Knowledge Base Export

