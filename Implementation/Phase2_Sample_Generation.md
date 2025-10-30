# Phase 2: Sample Generation - Implementation Roadmap

**Duration:** Flexible (1-2 weeks typical)  
**Goal:** Generate 37K training samples + 2K eval samples from RAG queries (~20M tokens total)

---

## Overview

Phase 2 generates all training data by intelligently querying the RAG system established in Phase 1. This is the core innovation: RAG serves as both the training data source AND the runtime reference library. All 37K samples are generated via semantic search, graph expansion, and temporal filtering to ensure consistency, traceability, and quality.

**Key Philosophy:** This document describes WHAT to implement, not HOW to code it. Each generation script is specified by its objectives, requirements, expected outputs, and validation criteria. Implementation details are left to the builder.

---

## Prerequisites

Before starting Phase 2, ensure Phase 1 is complete:

- [ ] Phase 1 completed successfully
- [ ] RAG system operational (ChromaDB + SQLite Graph + SQLite)
- [ ] 1,157 PDCAs indexed (~5,785 chunks)
- [ ] 5,372 TypeScript files indexed
- [ ] 12K tool examples indexed
- [ ] All validation tests passed

---

## Step 1: Core Sample Generation (25K samples)

**Estimated Time:** 3-5 days  
**Goal:** Generate style_core (12K), domain_patterns (8K), process_framework (5K)

### 1.1 Generate style_core.jsonl (12K samples)

**Objective:** Extract Web4 coding patterns from indexed TypeScript files via semantic queries.

**Script Location:** `scripts/generate_style_core.py`

**Requirements:**
- Query ChromaDB `components` collection for TypeScript files
- Generate 12K samples across 4 pattern categories
- Apply semantic search with pattern-specific queries
- Use layer filters where applicable
- Output samples in JSONL format with complete metadata

**Pattern Categories to Extract:**

**A. Empty Constructor Pattern (3,000 samples)**
- **Query:** "TypeScript class with empty constructor and init method"
- **Layer Filter:** None (all layers)
- **Key Features:** Classes with empty/minimal constructor, initialization logic in `init()` method
- **Purpose:** Teach separation of construction from initialization

**B. 5-Layer Architecture Pattern (3,000 samples)**
- **Query:** "layer2 implementation with layer3 interface and layer5 CLI"
- **Layer Filter:** layer2, layer3, layer5
- **Key Features:** Clear separation between layers, proper dependency flow
- **Purpose:** Teach Web4 architectural structure

**C. Radical OOP Pattern (3,000 samples)**
- **Query:** "deep encapsulation no public fields scenario based state management"
- **Layer Filter:** None (all layers)
- **Key Features:** Private fields, accessor methods, encapsulated state
- **Purpose:** Teach strict object-oriented principles

**D. Scenario-Based State Pattern (3,000 samples)**
- **Query:** "toScenario serialization immutable scenarios init method"
- **Layer Filter:** None (all layers)
- **Key Features:** `toScenario()` method, immutable state snapshots, scenario reconstruction
- **Purpose:** Teach Web4 state management approach

**Sample Generation Process:**
1. Initialize ChromaDB client and embedding model (sentence-transformers/all-MiniLM-L6-v2)
2. For each pattern category:
   - Generate query embedding from pattern query string
   - Query ChromaDB with semantic search (n_results = target_count)
   - Apply layer filter if specified
   - Extract document content and metadata from results
3. For each result, create training sample:
   - `instruction`: "Generate a TypeScript component following the [pattern name] pattern"
   - `input`: "Create a component with proper [pattern name] implementation"
   - `output`: Full TypeScript file content from ChromaDB
   - `metadata`: Include task_type, pattern_name, layer, source, sample_id
4. Write all samples to `data/style_core.jsonl` in JSONL format
5. Report generation statistics

**Expected Output:**
```
============================================================
Generating style_core.jsonl (12K samples)
============================================================

--- Pattern: empty_constructor (target: 3000) ---
  Generated 3000 samples

--- Pattern: 5_layer_architecture (target: 3000) ---
  Generated 3000 samples

--- Pattern: radical_oop (target: 3000) ---
  Generated 3000 samples

--- Pattern: scenario_state (target: 3000) ---
  Generated 3000 samples

✓ Saved 12000 samples to data/style_core.jsonl

============================================================
COMPLETE: 12000 style_core samples generated
============================================================
```

**Validation:**
- [ ] Script runs without errors
- [ ] `data/style_core.jsonl` created
- [ ] Exactly 12K samples generated
- [ ] All 4 patterns covered (3K each)
- [ ] Samples contain valid TypeScript code
- [ ] Metadata complete for all samples

---

### 1.2 Generate domain_patterns.jsonl (8K samples)

**Objective:** Extract distilled problem-solving patterns from historical PDCAs via semantic queries and graph expansion.

**Script Location:** `scripts/generate_domain_patterns.py`

**Requirements:**
- Query ChromaDB `pdca_historical` collection for PDCA chunks
- Generate 8K samples across 4 task type categories
- Apply pattern distillation to reduce token count (400-600 tokens vs 1200-1800 full PDCA)
- Optionally use SQLite Graph to expand context via breadcrumb chains
- Output samples in JSONL format with source tracking

**Task Type Categories to Extract:**

**A. Debugging Patterns (2,000 samples)**
- **Query:** "debugging methodology problem solution"
- **Key Features:** Problem identification, root cause analysis, solution steps, verification
- **Purpose:** Teach systematic debugging approaches

**B. Architectural Decision Patterns (2,000 samples)**
- **Query:** "architectural decision TRON format rationale"
- **Key Features:** Decision trigger, analysis, chosen approach, rationale, trade-offs
- **Purpose:** Teach architectural decision-making using TRON format

**C. Integration Patterns (2,000 samples)**
- **Query:** "integration patterns API communication"
- **Key Features:** Component integration, API design, communication patterns, error handling
- **Purpose:** Teach system integration approaches

**D. Collaboration Patterns (2,000 samples)**
- **Query:** "agent collaboration handoff patterns"
- **Key Features:** Multi-agent coordination, work handoffs, communication protocols
- **Purpose:** Teach effective collaboration in multi-agent environments

**Pattern Distillation Algorithm:**
- **Purpose:** Reduce full PDCA (1200-1800 tokens) to core pattern (400-600 tokens) - saves 60% tokens
- **Method:**
  1. Parse PDCA content by lines
  2. Identify key sections: Headers (##), Decisions, Solutions, Patterns
  3. Extract only lines containing key information
  4. Skip verbose descriptions and implementation details
  5. Limit to approximately 40 lines (~400-600 tokens)
  6. Preserve structure and context for learning

**Sample Generation Process:**
1. Initialize ChromaDB client and embedding model
2. For each task type category:
   - Generate query embedding from task type query string
   - Query ChromaDB `pdca_historical` for relevant chunks (n_results = target_count)
   - Extract document content and metadata
3. For each result:
   - Apply pattern distillation to reduce token count
   - Create training sample:
     - `instruction`: "Extract the key pattern from this [task type] PDCA"
     - `input`: First 500 characters of PDCA as context
     - `output`: Distilled pattern (400-600 tokens)
     - `metadata`: Include task_type, pdca_id, agent_name, source, sample_id
4. Write all samples to `data/domain_patterns.jsonl`
5. Report generation statistics

**Expected Output:**
```
============================================================
Generating domain_patterns.jsonl (8K samples)
============================================================

--- Task: debugging (target: 2000) ---
  Generated 2000 samples

--- Task: architectural_decision (target: 2000) ---
  Generated 2000 samples

--- Task: integration (target: 2000) ---
  Generated 2000 samples

--- Task: collaboration (target: 2000) ---
  Generated 2000 samples

✓ Saved 8000 samples to data/domain_patterns.jsonl

============================================================
COMPLETE: 8000 domain_patterns samples generated
============================================================
```

**Validation:**
- [ ] `data/domain_patterns.jsonl` created
- [ ] Exactly 8K samples generated
- [ ] All 4 task types covered (2K each)
- [ ] Patterns are distilled (400-600 tokens, not full 1200-1800 token PDCAs)
- [ ] Metadata includes pdca_id, agent_name, task_type
- [ ] Samples preserve key insights while reducing verbosity
---

### 1.3 Generate process_framework.jsonl (5K samples)

**Objective:** Teach PDCA structure, TRON format, CMM framework, and key behavioral lessons via template-based generation.

**Script Location:** `scripts/generate_process_framework.py`

**Requirements:**
- Generate 5K samples from hard-coded process framework templates
- No RAG queries needed - these are the "rules" to be taught
- Cover 5 template categories with specific counts per category
- Output samples in JSONL format with category metadata

**Framework Template Categories:**

**A. PDCA Structure Template (1,000 samples)**
- **Instruction:** "Generate a PDCA document following v3.2.4.2 template"
- **Template:** Complete PDCA structure with all required sections:
  - ## Objective: Clear goal statement
  - ## Plan: Analysis, Approach, TRON decision
  - ## Do: Implementation steps and code changes
  - ## Check: Verification and quality checks
  - ## Act: Lessons learned and next steps
  - Breadcrumb Links: PRECEDES and FOLLOWS
- **Purpose:** Teach standard PDCA document structure

**B. TRON Format Template (1,000 samples)**
- **Instruction:** "Format a decision using TRON structure"
- **Template:** TRON decision format:
  - **[T]rigger:** What prompted this decision?
  - **[R]esponse:** What action was taken?
  - **[O]utcome:** What was the result?
  - **[N]ext:** What are the next steps?
- **Purpose:** Teach structured decision documentation

**C. CMM Levels Template (500 samples)**
- **Instruction:** "Explain CMM compliance levels"
- **Template:** CMM framework explanation:
  - CMM1: Initial (ad-hoc, reactive)
  - CMM2: Managed (documented, some planning)
  - CMM3: Defined (standardized processes)
  - CMM4: Quantitatively Managed (measured, optimized)
  - Progression path: CMM2 → CMM3 via patterns
- **Purpose:** Teach CMM maturity model

**D. Dual Links Template (500 samples)**
- **Instruction:** "Create breadcrumb navigation with dual links"
- **Template:** Dual link pattern explanation:
  - Every PDCA must have PRECEDES and FOLLOWS links
  - Format: `[YYYYMMDD-HHMMSS-AgentName.RoleName.pdca.md]`
  - Purpose: Enable breadcrumb navigation through work history
- **Purpose:** Teach breadcrumb navigation pattern

**E. Key Lessons Template (2,000 samples)**
- **Instruction:** "Apply key behavioral lesson"
- **Template:** Lesson structure:
  - **Key Lesson:** [Lesson title]
  - **Context:** When does this apply?
  - **Principle:** Core principle
  - **Application:** How to apply
  - **Example:** Concrete example
- **Examples Include:**
  - Empty constructor pattern
  - Automate everything (no manual operations)
  - Test first, then code
  - Dual links always
  - 50+ additional key lessons from trainAI
- **Purpose:** Teach Web4 behavioral principles

**Sample Generation Process:**
1. Define framework templates with categories and counts
2. For each template category:
   - Generate specified number of samples (may include slight variations)
   - Create training sample:
     - `instruction`: Template-specific instruction
     - `input`: Empty (templates are self-contained)
     - `output`: Template content
     - `metadata`: Include task_type, category, source, sample_id
3. Write all samples to `data/process_framework.jsonl`
4. Report generation statistics

**Expected Output:**
```
============================================================
Generating process_framework.jsonl (5K samples)
============================================================

--- Category: pdca_structure (target: 1000) ---
  Generated 1000 samples

--- Category: tron_format (target: 1000) ---
  Generated 1000 samples

--- Category: cmm_levels (target: 500) ---
  Generated 500 samples

--- Category: dual_links (target: 500) ---
  Generated 500 samples

--- Category: key_lessons (target: 2000) ---
  Generated 2000 samples

✓ Saved 5000 samples to data/process_framework.jsonl

============================================================
COMPLETE: 5000 process_framework samples generated
============================================================
```

**Validation:**
- [ ] `data/process_framework.jsonl` created
- [ ] Exactly 5K samples generated
- [ ] All 5 categories covered with correct counts
- [ ] Templates include all required Web4 methodology elements
- [ ] Samples are self-contained (no external references needed)

---

**Step 1 Completion Checklist:**

- [ ] style_core.jsonl: 12K samples generated
- [ ] domain_patterns.jsonl: 8K samples generated
- [ ] process_framework.jsonl: 5K samples generated
- [ ] Total: 25K core samples
- [ ] All scripts run without errors
- [ ] All JSONL files created in `data/` directory

---

## Step 2: Specialized Samples (9K samples)

**Estimated Time:** 2-3 days  
**Goal:** Generate domain_representatives (3K), style_refactor (3K), guardrails (2K), tool_awareness (1K), reporting_protocol (3K)

### 2.1 Generate domain_representatives.jsonl (3K samples)

**Objective:** Select top 200-300 complete PDCAs with diverse temporal/agent/task coverage via quality scoring.

**Script Location:** `scripts/generate_domain_representatives.py`

**Requirements:**
- Query SQLite for top PDCAs by quality score
- Stratify sampling across time periods (Q1 2024 through Q1 2025)
- Ensure agent diversity and task diversity
- Retrieve full PDCA content from ChromaDB
- Generate variations to reach 3K target
- Output samples in JSONL format with quality metadata

**Quality Scoring Algorithm:**
- **Purpose:** Rank PDCAs by completeness and compliance
- **Scoring Factors:**
  - Base score: 50 points
  - CMM level: +10 points per level above CMM1 (max +30)
  - Completeness: +20 points for all sections present
  - Dual links: +10 points for valid PRECEDES and FOLLOWS
  - Maximum score: 100 points
- **Selection:** Top-ranked PDCAs per quarter ensure quality and diversity

**Temporal Stratification Strategy:**
- **Purpose:** Prevent recency bias, ensure historical patterns included
- **Quarters:**
  - Q1 2024: (2024-01-01 to 2024-03-31) → 600 samples
  - Q2 2024: (2024-04-01 to 2024-06-30) → 600 samples
  - Q3 2024: (2024-07-01 to 2024-09-30) → 600 samples
  - Q4 2024: (2024-10-01 to 2024-12-31) → 600 samples
  - Q1 2025: (2025-01-01 to 2025-03-31) → 600 samples
- **Total:** 3,000 samples evenly distributed

**Sample Generation Process:**
1. Initialize SQLite and ChromaDB clients
2. For each quarter:
   - Query SQLite for top PDCAs in date range (ORDER BY quality_score DESC)
   - Limit to top N PDCAs (approximately 200 total across quarters)
   - For each PDCA:
     - Retrieve all chunks from ChromaDB by pdca_id
     - Concatenate chunks to reconstruct full PDCA
     - Create training sample:
       - `instruction`: "Generate a complete PDCA document following Web4 methodology"
       - `input`: "Task: Create PDCA for [pdca_id]"
       - `output`: Full PDCA content (1200-1800 tokens)
       - `metadata`: Include pdca_id, agent_name, date, quarter, quality_score, source
3. Replicate samples to reach 3K target:
   - Create variations showing different aspects:
     - Prompt → PDCA structure
     - PDCA section → next section
     - Full PDCA generation
4. Write all samples (limit to exactly 3K) to `data/domain_representatives.jsonl`
5. Report generation statistics with quarter breakdown

**Expected Output:**
```
============================================================
Generating domain_representatives.jsonl (3K samples)
============================================================

--- Quarter: Q1_2024 ---
  Found 45 top PDCAs

--- Quarter: Q2_2024 ---
  Found 52 top PDCAs

--- Quarter: Q3_2024 ---
  Found 48 top PDCAs

--- Quarter: Q4_2024 ---
  Found 38 top PDCAs

--- Quarter: Q1_2025 ---
  Found 27 top PDCAs

--- Replicating to reach 3K target ---

✓ Saved 3000 samples to data/domain_representatives.jsonl

============================================================
COMPLETE: 3000 domain_representatives samples generated
============================================================
```

**Validation:**
- [ ] `data/domain_representatives.jsonl` created
- [ ] Exactly 3K samples generated
- [ ] Temporal diversity verified (stratified across 5 quarters)
- [ ] Agent diversity confirmed (multiple agents represented)
- [ ] Task diversity ensured (various task types)
- [ ] Quality scores documented in metadata
- [ ] Samples contain complete PDCAs (not fragments)

---

### 2.2 Generate style_refactor.jsonl (3K samples)

**Objective:** Show CMM2 → CMM3 transformations and code evolution patterns.

**Script Location:** `scripts/generate_style_refactor.py`

**Requirements:**
- Query ChromaDB for PDCAs tagged with "CMM2 to CMM3" transitions
- Extract before/after code pairs
- Focus on refactoring journeys and continuous improvement
- Generate 3K samples showing evolution patterns
- Output samples in JSONL format with transformation metadata

**Key Patterns to Extract:**
- Code refactoring from CMM2 (managed) to CMM3 (defined)
- Technical debt reduction examples
- Pattern application demonstrations
- Continuous improvement journeys
- Quality enhancement transformations

**Sample Structure:**
- `instruction`: "Show the refactoring from CMM2 to CMM3"
- `input`: Original CMM2 code or approach
- `output`: Improved CMM3 code with pattern application
- `metadata`: Include cmm_transition, pattern_applied, source

**Validation:**
- [ ] `data/style_refactor.jsonl` created
- [ ] 3K samples generated
- [ ] Before/after CMM transitions clearly shown
- [ ] Samples demonstrate improvement and learning

---

### 2.3 Generate guardrails.jsonl (2K samples)

**Objective:** Teach framework violations and compliance rules.

**Script Location:** `scripts/generate_guardrails.py`

**Requirements:**
- Extract violation examples from historical PDCAs
- Generate negative examples (what NOT to do)
- Cover key compliance rules
- Generate 2K samples with clear violation marking
- Output samples in JSONL format with violation type metadata

**Violation Categories:**
- **Jest Ban:** Use Vitest instead (framework compliance)
- **Manual Operations:** Automate everything (no manual steps)
- **Security Violations:** No hardcoded secrets, proper auth
- **Framework Violations:** Constructor logic, missing tests, etc.

**Sample Structure:**
- `instruction`: "Identify the violation in this code"
- `input`: Code or approach with violation
- `output`: Explanation of violation and correct approach
- `metadata`: Include violation_type, severity, is_negative_example

**Validation:**
- [ ] `data/guardrails.jsonl` created
- [ ] 2K samples generated
- [ ] Negative examples clearly marked
- [ ] All major violation types covered

---

### 2.4 Generate tool_awareness.jsonl (1K samples)

**Objective:** Teach generic tool-calling concepts (JSON structure, parameters) - IDE-agnostic.

**Script Location:** `scripts/generate_tool_awareness.py`

**Requirements:**
- Generate 1K samples teaching CONCEPT of tools
- Focus on JSON structure and parameter passing
- Keep completely IDE-agnostic (no Continue or Cursor specifics)
- Output samples in JSONL format

**Key Concepts to Teach:**
- Tools have names and take parameters
- Parameters are passed as JSON
- Tools return results
- Context awareness in tool usage
- Error handling for tool calls

**Sample Structure:**
- `instruction`: "Call a tool to perform [action]"
- `input`: Context describing what needs to be done
- `output`: Generic tool call structure (JSON format)
- `metadata`: Include concept_taught, is_generic_tool

**Important Note:** IDE-specific tool examples (12K Continue tools) stay in RAG, NOT trained here.

**Validation:**
- [ ] `data/tool_awareness.jsonl` created
- [ ] 1K samples generated
- [ ] Completely IDE-agnostic (no Continue/Cursor specifics)
- [ ] Teaches generic tool concepts effectively

---

### 2.5 Generate reporting_protocol.jsonl (3K samples)

**Objective:** Teach the structure and content of the Web4 reporting protocol.

**Script Location:** `scripts/generate_reporting_protocol.py`

**Requirements:**
- Generate 3K samples from a predefined reporting protocol template
- Cover all major sections: Introduction, Problem, Plan, Do, Check, Act, Lessons
- Ensure consistency in formatting and structure
- Output samples in JSONL format

**Template:**
```
{
  "instruction": "Generate a Web4 reporting protocol document",
  "input": "PDCA ID: [pdca_id], Agent: [agent_name], Date: [date]",
  "output": "Full Web4 reporting protocol document content",
  "metadata": {
    "pdca_id": "string",
    "agent_name": "string",
    "date": "string",
    "source": "string"
  }
}
```

**Validation:**
- [ ] `data/reporting_protocol.jsonl` created
- [ ] 3K samples generated
- [ ] All major sections present
- [ ] Consistent formatting
- [ ] No external references needed

---

**Step 2 Completion Checklist:**

- [ ] domain_representatives.jsonl: 3K samples generated
- [ ] style_refactor.jsonl: 3K samples generated
- [ ] guardrails.jsonl: 2K samples generated
- [ ] tool_awareness.jsonl: 1K samples generated
- [ ] reporting_protocol.jsonl: 3K samples generated
- [ ] Total: 12K specialized samples
- [ ] All scripts run without errors

---

## Step 3: Validation & QA (3K samples)

**Estimated Time:** 1-2 days  
**Goal:** Generate eval.jsonl (2K hold-out), validate all 37K training samples

### 3.1 Generate eval.jsonl (2K hold-out set)

**Objective:** Create stratified evaluation set that is NEVER trained, used for unbiased quality measurement.

**Script Location:** `scripts/generate_eval.py`

**Requirements:**
- Sample from all 8 training datasets
- Stratify sampling to represent all categories
- Mark samples as `never_train: true`
- Generate exactly 2K samples
- Output samples in JSONL format

**Stratified Distribution:**
- style_core.jsonl: 400 samples (20% of 2K)
- domain_patterns.jsonl: 300 samples (15% of 2K)
- process_framework.jsonl: 200 samples (10% of 2K)
- domain_representatives.jsonl: 150 samples (7.5% of 2K)
- style_refactor.jsonl: 150 samples (7.5% of 2K)
- guardrails.jsonl: 100 samples (5% of 2K)
- tool_awareness.jsonl: 50 samples (2.5% of 2K)
- reporting_protocol.jsonl: 200 samples (10% of 2K)
- **Total:** 1,550 samples (then expand to 2K with balanced additions)

**Sample Selection Process:**
1. Load each source JSONL file
2. Randomly sample specified count from each file
3. Mark all sampled items with eval metadata:
   - `is_eval`: true
   - `never_train`: true (critical flag)
4. Shuffle all samples together
5. Write exactly 2K samples to `data/eval.jsonl`
6. Display warning that these samples must NEVER be used for training

**Expected Output:**
```
============================================================
Generating eval.jsonl (2K hold-out samples)
============================================================

--- Sampling from style_core.jsonl: 400 samples ---
  Sampled 400 samples

--- Sampling from domain_patterns.jsonl: 300 samples ---
  Sampled 300 samples

[... additional categories ...]

✓ Saved 2000 eval samples to data/eval.jsonl
⚠️  IMPORTANT: These samples must NEVER be used for training!

============================================================
COMPLETE: 2000 eval samples generated
============================================================
```

**Validation:**
- [ ] `data/eval.jsonl` created
- [ ] Exactly 2K samples
- [ ] Stratified across all 7 categories
- [ ] All samples marked `never_train: true`
- [ ] Documented as hold-out set

---

### 3.2 Validate All 37K Training Samples + 2K Eval

**Objective:** Comprehensive validation of all generated samples before training.

**Script Location:** `scripts/validate_samples.py`

**Requirements:**
- Validate all 9 JSONL files (8 training + 1 eval)
- Check schema compliance for all samples
- Count tokens using Qwen tokenizer
- Verify sample counts match targets
- Report comprehensive statistics
- Fail loudly if any validation errors found

**Validation Checks:**

**A. File Existence and Count Validation**
- Verify all 8 expected files exist in `data/` directory
- Check each file has correct sample count:
  - style_core.jsonl: exactly 12,000
  - domain_patterns.jsonl: exactly 8,000
  - process_framework.jsonl: exactly 5,000
  - domain_representatives.jsonl: exactly 3,000
  - style_refactor.jsonl: exactly 3,000
  - guardrails.jsonl: exactly 2,000
  - tool_awareness.jsonl: exactly 1,000
  - reporting_protocol.jsonl: exactly 3,000
  - eval.jsonl: exactly 2,000
- **Total:** 37,000 training + 2,000 eval = 39,000 samples

**B. Schema Validation**
- **Required Top-Level Fields:**
  - `instruction` (string)
  - `input` (string)
  - `output` (string)
  - `metadata` (object)
- **Required Metadata Fields:**
  - `task_type` (string)
  - `sample_id` (string)
- Report any samples failing schema validation

**C. Token Distribution Validation**
- Initialize Qwen tokenizer: `Qwen/Qwen2.5-Coder-7B-Instruct`
- For each sample, count tokens in `instruction + input + output`
- Calculate per-file statistics:
  - Total tokens
  - Average tokens per sample
- Calculate overall statistics:
  - **Target Total:** ~20M tokens (acceptable range: 19M-21M)
  - **Target Average:** ~540 tokens/sample (acceptable range: 500-600)
- Report if outside acceptable ranges

**D. Quality Checks**
- Verify metadata completeness
- Check for duplicate sample_ids
- Validate source references
- Confirm diversity metrics where applicable

**Expected Output:**
```
============================================================
Validating All Samples
============================================================

--- Validating style_core.jsonl ---
  ✓ Count: 12000/12000
  ✓ Schema: All samples valid
  ✓ Tokens: 6,480,000 total, 540 avg/sample

--- Validating domain_patterns.jsonl ---
  ✓ Count: 8000/8000
  ✓ Schema: All samples valid
  ✓ Tokens: 4,320,000 total, 540 avg/sample

--- Validating process_framework.jsonl ---
  ✓ Count: 5000/5000
  ✓ Schema: All samples valid
  ✓ Tokens: 2,700,000 total, 540 avg/sample

--- Validating domain_representatives.jsonl ---
  ✓ Count: 3000/3000
  ✓ Schema: All samples valid
  ✓ Tokens: 1,620,000 total, 540 avg/sample

--- Validating style_refactor.jsonl ---
  ✓ Count: 3000/3000
  ✓ Schema: All samples valid
  ✓ Tokens: 1,620,000 total, 540 avg/sample

--- Validating guardrails.jsonl ---
  ✓ Count: 2000/2000
  ✓ Schema: All samples valid
  ✓ Tokens: 1,080,000 total, 540 avg/sample

--- Validating tool_awareness.jsonl ---
  ✓ Count: 1000/1000
  ✓ Schema: All samples valid
  ✓ Tokens: 540,000 total, 540 avg/sample

--- Validating reporting_protocol.jsonl ---
  ✓ Count: 3000/3000
  ✓ Schema: All samples valid
  ✓ Tokens: 1,620,000 total, 540 avg/sample

--- Validating eval.jsonl ---
  ✓ Count: 2000/2000
  ✓ Schema: All samples valid
  ✓ Tokens: 1,080,000 total, 540 avg/sample

============================================================
VALIDATION SUMMARY
============================================================
Total Samples: 39,000 (target: 39,000) ✓
Total Tokens: 19,440,000 (target: ~20M) ✓
Average Tokens/Sample: 498 (target: ~540) ✓

✅ ALL VALIDATIONS PASSED!
============================================================
```

**Validation:**
- [ ] All 8 files exist
- [ ] Correct sample counts (37K training + 2K eval = 39K total)
- [ ] Schema compliance 100%
- [ ] Total tokens ~20M (acceptable range: 19M-21M)
- [ ] Average tokens/sample ~540 (acceptable range: 500-600)
- [ ] No duplicate sample IDs
- [ ] Validation script exits with code 0 (success)

---

## Phase 2 Completion Checklist

### Core Samples (25K)
- [ ] style_core.jsonl: 12K samples ✓
- [ ] domain_patterns.jsonl: 8K samples ✓
- [ ] process_framework.jsonl: 5K samples ✓

### Specialized Samples (9K)
- [ ] domain_representatives.jsonl: 3K samples ✓
- [ ] style_refactor.jsonl: 3K samples ✓
- [ ] guardrails.jsonl: 2K samples ✓
- [ ] tool_awareness.jsonl: 1K samples ✓
- [ ] reporting_protocol.jsonl: 3K samples ✓

### Evaluation Set (3K total, 2K used)
- [ ] eval.jsonl: 2K hold-out samples ✓
- [ ] Marked as `never_train: true` ✓

### Validation
- [ ] Total: 37K training + 2K eval = 39K samples
- [ ] Total tokens: ~20M (19M-21M acceptable)
- [ ] Average tokens/sample: ~540 (500-600 acceptable)
- [ ] Schema compliance: 100%
- [ ] Diversity validated (temporal, agent, task)
- [ ] All JSONL files in `data/` directory
- [ ] Validation script passes all checks

---

## Success Criteria

**Phase 2 is complete when:**

✓ 37K training samples generated from RAG  
✓ 2K eval samples stratified (never trained)  
✓ Token count ~20M (avg 540/sample)  
✓ Quality validated (schema, diversity, scores)  
✓ All JSONL files ready for training

---

## Troubleshooting Guide

### Common Issues and Solutions

**Issue: Token Count Too High/Low**
- **Symptom:** Total tokens significantly off target (< 19M or > 21M)
- **Solutions:**
  - Adjust sample content length in generation scripts
  - Modify distillation rules to be more/less aggressive
  - Review pattern extraction to optimize verbosity

**Issue: Missing Samples in Category**
- **Symptom:** Some categories have fewer than expected samples
- **Solutions:**
  - Expand RAG queries with broader semantic search terms
  - Adjust metadata filters to be less restrictive
  - Generate variations of existing samples
  - Check RAG indexing for completeness

**Issue: Schema Validation Failures**
- **Symptom:** Samples missing required fields
- **Solutions:**
  - Review generation scripts to ensure all metadata populated
  - Add validation checks during generation (fail fast)
  - Fix template structure to include all required fields

**Issue: Low Diversity (Temporal/Agent/Task)**
- **Symptom:** Samples clustered in specific time periods, agents, or tasks
- **Solutions:**
  - Implement stratified sampling explicitly
  - Use SQLite temporal queries to enforce date distribution
  - Add diversity metrics to validation script
  - Manually review sample distribution

---

## Next Steps

Once Phase 2 is complete:

1. **Backup Generated Data** - Copy entire `data/` directory to safe location
2. **Review Sample Quality** - Manually spot-check 50-100 samples across categories
3. **Document Generation Stats** - Save validation output for reference
4. **Proceed to Phase 3** - LoRA training & deployment

**Estimated Time to Phase 3:** Immediately (if validation passes)

---

## Phase 2 Summary

**Deliverables:**
- ✓ 37K training samples (~20M tokens) generated from RAG
- ✓ 2K eval samples (hold-out set, never trained)
- ✓ All samples quality validated (schema, tokens, diversity)
- ✓ Diverse temporal/agent/task coverage ensured
- ✓ 8 JSONL files ready for training pipeline

**Scripts Created:**
- `scripts/generate_style_core.py` - TypeScript pattern extraction (12K)
- `scripts/generate_domain_patterns.py` - PDCA pattern distillation (8K)
- `scripts/generate_process_framework.py` - Framework templates (5K)
- `scripts/generate_domain_representatives.py` - Top PDCA selection (3K)
- `scripts/generate_style_refactor.py` - CMM2→CMM3 transformations (3K)
- `scripts/generate_guardrails.py` - Violation examples (2K)
- `scripts/generate_tool_awareness.py` - Generic tool concepts (1K)
- `scripts/generate_eval.py` - Hold-out set creation (2K)
- `scripts/validate_samples.py` - Comprehensive validation

**Data Files:**
- `data/style_core.jsonl` (12K samples)
- `data/domain_patterns.jsonl` (8K samples)
- `data/process_framework.jsonl` (5K samples)
- `data/domain_representatives.jsonl` (3K samples)
- `data/style_refactor.jsonl` (3K samples)
- `data/guardrails.jsonl` (2K samples)
- `data/tool_awareness.jsonl` (1K samples)
- `data/eval.jsonl` (2K samples - NEVER train)
- `data/reporting_protocol.jsonl` (3K samples)

**Duration:** Flexible (1-2 weeks typical)  
**Next Phase:** Phase 3 - Training & Deployment

---

*Document Version: 2.0*  
*Last Updated: 2025-10-29*  
*Part of: Web4 Balanced LoRA Training Strategy*
*Format: Implementation Roadmap (no embedded code)*

