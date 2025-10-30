# Phase 1: Setup & RAG Bootstrap - Implementation Roadmap

**Duration:** Flexible (1-2 weeks typical)  
**Goal:** Establish complete three-tier RAG system with all 907 PDCAs indexed and validated

---

## Overview

Phase 1 establishes the foundation for the entire training pipeline by creating a three-tier RAG system (ChromaDB + Redis Graph + SQLite) and indexing all source data. This phase is critical because RAG becomes the single source of truth for all subsequent training sample generation.

**Key Philosophy:** This document describes WHAT to implement, not HOW to code it. Each step outlines objectives, requirements, expected outcomes, and validation criteria. Implementation details are left to the builder.

---

## Prerequisites

Before starting Phase 1, ensure you have:

- [ ] **Hardware:** M1 Mac with 32GB RAM (or equivalent)
- [ ] **OS:** macOS, Linux, or Windows with WSL2
- [ ] **Access:** Web4Articles repository at `/Users/Shared/Workspaces/2cuGitHub/Web4Articles`
- [ ] **Account:** HuggingFace account (free tier sufficient, for base model download later)
- [ ] **Time:** 1-2 weeks allocated (full-time vs part-time)

---

## Step 1: Environment Setup

**Estimated Time:** 2-4 hours  
**Goal:** Install all required software and dependencies

### 1.1 Install Python 3.10+

**Objective:** Ensure Python 3.10 or higher is available for compatibility with latest ML libraries.

**Requirements:**
- Python 3.10 or higher required
- `python3` command accessible in PATH
- Support for virtual environments (`venv` module)

**Implementation Tasks:**
1. Check current Python version
2. If version is below 3.10, install appropriate version for your OS
3. Verify installation by checking version output

**Validation:**
- [ ] Python 3.10 or higher installed
- [ ] `python3 --version` shows correct version (3.10.x or higher)
- [ ] Can create virtual environments with `python3 -m venv`

---

### 1.2 Install Ollama

**Objective:** Install Ollama for model deployment and serving in production.

**Requirements:**
- Ollama CLI tool installed
- Ollama service can start and respond to commands
- Compatible with M1 Mac Metal acceleration

**Implementation Tasks:**
1. Download and install Ollama from official source (ollama.ai)
2. Verify installation with version check
3. Optionally start Ollama server to confirm it runs
4. Stop server if testing (will be used later in Phase 3-4)

**Validation:**
- [ ] Ollama installed successfully
- [ ] `ollama --version` shows version number
- [ ] Ollama server can start without errors

---

### 1.3 Install ChromaDB

**Objective:** Set up ChromaDB vector database for semantic search capabilities.

**Requirements:**
- ChromaDB version 0.4.18 installed in Python environment
- Able to import `chromadb` module without errors
- Python virtual environment activated

**Implementation Tasks:**
1. Create Python virtual environment in project directory
2. Activate virtual environment
3. Install ChromaDB via pip (version 0.4.18 specifically)
4. Install sentence-transformers for embedding generation (version 2.2.2)
5. Test import to verify installation

**Validation:**
- [ ] Virtual environment created and activated
- [ ] ChromaDB installed successfully
- [ ] Import test passes without errors
- [ ] sentence-transformers library available

---

### 1.4 Install Redis + RedisGraph

**Objective:** Set up Redis server with RedisGraph module for breadcrumb navigation graph database.

**Requirements:**
- Redis server running and accessible on localhost:6379
- RedisGraph module loaded (typically via Redis Stack)
- Python Redis clients installed (redis, redisgraph)

**Implementation Tasks:**
1. Install Redis server appropriate for your OS
2. Install Redis Stack (includes RedisGraph module)
3. Start Redis server and ensure it runs on system boot
4. Verify Redis responds to ping command
5. Install Python Redis clients in virtual environment
6. Test connection from Python

**Validation:**
- [ ] Redis server running (`redis-cli ping` returns PONG)
- [ ] RedisGraph module loaded (check with Redis Stack)
- [ ] Python Redis clients installed (redis==5.0.1, redisgraph==2.5.1)
- [ ] Can connect and execute basic graph commands from Python

---

### 1.5 Verify SQLite

**Objective:** Confirm SQLite is available for temporal query database.

**Requirements:**
- SQLite 3.x available (comes with Python standard library)
- Can import `sqlite3` module
- Can create and query databases

**Implementation Tasks:**
1. Verify SQLite is available via Python import
2. Check SQLite version (should be 3.x.x)
3. Optionally create test database to confirm functionality

**Validation:**
- [ ] SQLite available (should show version 3.x.x)
- [ ] Can import `sqlite3` module
- [ ] Can create and query test databases

---

### 1.6 Verify Web4Articles Repository Access

**Objective:** Confirm access to all source data files.

**Requirements:**
- Web4Articles repository accessible at specified path
- Exactly 907 PDCA files present (525 in project.journal, 382 elsewhere)
- Approximately 6,530 TypeScript files present

**Implementation Tasks:**
1. Navigate to repository location
2. Verify directory structure exists
3. Count PDCA files (should be 907 total)
4. Count TypeScript files (*.ts, *.tsx) across repository (should be ~6,530)
5. Verify read permissions on all files

**Validation:**
- [ ] Web4Articles repository accessible
- [ ] 907 PDCA files found (exact count)
- [ ] ~6,530 TypeScript files found (approximate)
- [ ] Can read sample files without permission errors

---

### 1.7 Set Up Project Structure

**Objective:** Create organized directory structure for all project artifacts.

**Requirements:**
- Standard project layout established
- Directories for scripts, data, config, outputs, evaluation, and logs
- Consistent with implementation guide expectations

**Implementation Tasks:**
1. Navigate to LLM_Training directory
2. Create the following directories:
   - `scripts/` - Python scripts for indexing, training, evaluation
   - `data/` - Generated JSONL training files
   - `config/` - Configuration files (training params, RAG settings)
   - `outputs/` - LoRA adapters, GGUF models, eval reports
   - `eval/` - Evaluation test harnesses
   - `logs/` - Log files for evening loop, debugging
3. Verify structure matches expected layout
4. Ensure directories are writable

**Expected Structure:**
```
LLM_Training/
├── scripts/          # Python scripts for indexing, training, evaluation
├── data/             # Generated JSONL training files
├── config/           # Configuration files (training params, RAG settings)
├── outputs/          # LoRA adapters, GGUF models, eval reports
├── eval/             # Evaluation test harnesses
├── logs/             # Log files for evening loop, debugging
├── Training/         # Existing: strategy docs, diagrams
├── RL/               # Existing: RL planning docs
└── Implementation/   # This guide
```

**Validation:**
- [ ] All directories created
- [ ] Directory structure matches expected layout
- [ ] Write permissions confirmed for all directories

---

### 1.8 Install Python Dependencies

**Objective:** Install all required Python libraries for ML training and RAG operations.

**Requirements:**
- All dependencies installed in virtual environment
- Specific versions maintained for reproducibility
- No version conflicts between packages

**Implementation Tasks:**
1. Create `requirements.txt` file with the following dependency categories:
   - **Core ML Libraries:** transformers (4.36.0), peft (0.7.1), torch (2.1.2), accelerate (0.25.0), bitsandbytes (0.41.3)
   - **Vector DB & Graph:** chromadb (0.4.18), sentence-transformers (2.2.2), redis (5.0.1), redisgraph (2.5.1)
   - **Data Processing:** datasets (2.15.0), jsonschema (4.20.0), tqdm (4.66.1)
   - **Utilities:** python-dotenv (1.0.0), pyyaml (6.0.1)

2. Install all dependencies via pip in activated virtual environment
3. Verify key imports work without errors
4. Check for any version conflicts or warnings

**Validation:**
- [ ] All packages installed without errors
- [ ] Import verification passes for key libraries (transformers, peft, torch, chromadb, redis, redisgraph)
- [ ] No version conflicts reported
- [ ] All specified versions match installed versions

---

## Step 2: RAG System Bootstrap

**Estimated Time:** 4-8 hours (mostly indexing time)  
**Goal:** Index all 907 PDCAs, 6,530 TypeScript files, 238 process docs, and 12K tool examples

### 2.1 Create Initial Indexing Script

**Objective:** Build a comprehensive indexing script that populates all three RAG tiers with source data.

**Script Location:** `scripts/initial_indexing.py`

**Requirements:**
- Index 534 PDCAs into all three tiers (ChromaDB, Redis Graph, SQLite)
- Apply PDCA-aware adaptive chunking (preserve section boundaries)
- Generate 768-dimensional embeddings using sentence-transformers
- Extract metadata (15+ fields) from PDCA filenames and content
- Index TypeScript files by layer and pattern
- Index tool examples with ecosystem metadata
- Handle errors gracefully, continue on individual file failures
- Provide progress tracking and summary statistics

**Core Functionality Needed:**

**A. PDCA-Aware Adaptive Chunking Function**
- **Purpose:** Split PDCAs into semantically complete chunks that preserve document structure
- **Input:** PDCA markdown content, PDCA ID
- **Output:** List of chunk dictionaries with content and metadata
- **Algorithm:**
  - Parse PDCA markdown using regex to identify section boundaries (## headers)
  - Create separate chunks for major sections: Objective, Plan, Do, Check, Act, Metadata
  - Each chunk should be 400-800 tokens (substantial enough for context)
  - Include chunk type (pdca_objective, pdca_plan, pdca_do, pdca_check, pdca_act, pdca_metadata)
  - Include chunk index (0-N for ordering)
  - Fallback: if parsing fails, return full PDCA as single chunk
- **Key Innovation:** Section-aware chunking prevents destructive fixed-size splitting

**B. PDCA Metadata Extraction Function**
- **Purpose:** Extract structured metadata from PDCA filename and content
- **Input:** PDCA file path
- **Output:** Dictionary with metadata fields
- **Filename Pattern:** `YYYYMMDD-HHMMSS-AgentName.RoleName.pdca.md`
- **Metadata to Extract:**
  - `agent_name` - extracted from filename before first dot
  - `agent_role` - extracted from filename after first dot
  - `date` - parsed from filename (YYYY-MM-DD format)
  - `timestamp` - Unix timestamp from date/time
  - `pdca_id` - filename stem (unique identifier)
- **Error Handling:** If filename doesn't match pattern, use defaults and file mtime

**C. PDCA Indexing Function**
- **Purpose:** Index all 534 PDCAs into three-tier RAG system
- **Steps:**
  1. Initialize ChromaDB collection `pdca_historical` (delete existing if present)
  2. Find all `*.pdca.md` files in Web4Articles (should be exactly 534)
  3. For each PDCA:
     - Read file content
     - Extract metadata from filename
     - Chunk content using PDCA-aware adaptive chunking
     - Generate embeddings for each chunk (768-dimensional vectors)
     - Add to ChromaDB with comprehensive metadata:
       - `chunk_type`, `chunk_index`, `pdca_id`
       - `agent_name`, `agent_role`, `date`, `timestamp`
       - `trained_in_adapter` (False initially)
       - `training_batch` (empty string initially)
       - `training_date` (empty string initially)
     - Insert record into SQLite `pdcas` table with temporal metadata
     - Create node in Redis Graph with PDCA properties
  4. Report total PDCAs indexed and total chunks created

**D. TypeScript File Indexing Function**
- **Purpose:** Index 3,477 TypeScript component files by layer and pattern
- **Steps:**
  1. Initialize ChromaDB collection `components` (delete existing if present)
  2. Find all `*.ts` and `*.tsx` files in Web4Articles
  3. For each TypeScript file:
     - Read file content
     - Detect layer from path (/layer2/, /layer3/, /layer5/)
     - Detect patterns from content:
       - `empty_constructor` - contains empty constructor() or minimal constructor
       - `scenario_state` - contains toScenario() method
       - `init_method` - contains init() method
     - Generate embedding from first 2K characters (for performance)
     - Add to ChromaDB with metadata:
       - `file_path` (full path)
       - `layer` (layer2, layer3, layer5, or unknown)
       - `patterns` (comma-separated list)
       - `file_type` (.ts or .tsx)
  4. Skip very small files (<100 chars)
  5. Report total TypeScript files indexed

**E. Tool Examples Indexing Function**
- **Purpose:** Index 12K IDE-specific tool examples for runtime injection
- **Steps:**
  1. Initialize ChromaDB collection `tool_examples` (delete existing if present)
  2. Read tool example files: `data/tool_core.jsonl` (10K), `data/tool_neg.jsonl` (2K)
  3. For each line in JSONL files:
     - Parse JSON to extract tool example
     - Generate embedding from instruction field
     - Add to ChromaDB with metadata:
       - `tool_name` (read_file, grep, run_terminal_command, etc.)
       - `tool_ecosystem` (continue, cursor, custom)
       - `usage_pattern` (simple, intermediate, complex, edge_case)
       - `is_negative` (true for tool_neg.jsonl examples)
  4. Skip if tool example files don't exist (optional data)
  5. Report total tool examples indexed

**F. SQLite Schema Creation**
- **Purpose:** Create temporal query database for fast date/agent lookups
- **Table:** `pdcas`
- **Schema:**
  - `id` TEXT PRIMARY KEY (pdca_id)
  - `agent_name` TEXT
  - `agent_role` TEXT
  - `date` TEXT (YYYY-MM-DD)
  - `timestamp` INTEGER (Unix timestamp)
  - `session_id` TEXT
  - `branch` TEXT
  - `sprint` TEXT
  - `cmm_level` INTEGER
  - `task_type` TEXT
  - `objective` TEXT
  - `quality_score` REAL
  - `verification_status` TEXT
  - `file_path` TEXT
- **Indexes:** Create indexes on date, timestamp, agent_name, cmm_level for fast queries

**G. Main Orchestration**
- **Purpose:** Coordinate all indexing operations
- **Flow:**
  1. Print banner and configuration
  2. Load embedding model (sentence-transformers/all-MiniLM-L6-v2)
  3. Initialize ChromaDB client (persistent storage at ./chroma_db)
  4. Initialize Redis Graph client (connect to localhost:6379, graph name: breadcrumb_graph)
  5. Initialize SQLite (database at ./pdca_timeline.db, create schema)
  6. Run PDCA indexing (returns total chunks)
  7. Run TypeScript indexing (returns total files)
  8. Run tool examples indexing (returns total examples)
  9. Print summary statistics
  10. Close database connections

**Expected Output:**
```
============================================================
Web4 RAG System - Initial Indexing
============================================================
Loading embedding model...
Initializing ChromaDB...
Connecting to Redis Graph...
Initializing SQLite...

=== Indexing PDCAs ===
Found 534 PDCA files
Indexing PDCAs: 100%|████████| 534/534 [01:23<00:00]
✓ Indexed 534 PDCAs into 2,670 chunks

=== Indexing TypeScript Files ===
Found 3,477 TypeScript files
Indexing TypeScript: 100%|████████| 3477/3477 [12:45<00:00]
✓ Indexed 3,477 TypeScript files

=== Indexing Tool Examples ===
Indexing tool_core.jsonl: 100%|████████| 10000/10000 [08:20<00:00]
Indexing tool_neg.jsonl: 100%|████████| 2000/2000 [01:40<00:00]
✓ Indexed 12,000 tool examples

============================================================
INDEXING COMPLETE!
============================================================
✓ PDCAs: 2,670 chunks from 534 files
✓ TypeScript: 3,477 files
✓ Tools: 12,000 examples

ChromaDB: ./chroma_db
SQLite: ./pdca_timeline.db
Redis Graph: breadcrumb_graph
============================================================
```

**Implementation Notes:**
- Use `tqdm` for progress bars
- Handle encoding errors gracefully (try UTF-8, fallback to latin-1)
- Log errors to console but continue processing
- Commit SQLite transactions periodically (every 100 PDCAs)
- Batch ChromaDB inserts for better performance
- Total runtime: 4-8 hours depending on hardware

**Validation After Running:**
- [ ] Script runs without fatal errors
- [ ] Approximately 2,670 PDCA chunks indexed (may vary ±10%)
- [ ] 3,477 TypeScript files indexed (exact count)
- [ ] 12K tool examples indexed (if files exist)
- [ ] ChromaDB directory created at `./chroma_db`
- [ ] SQLite database file created at `./pdca_timeline.db`
- [ ] Redis Graph contains nodes (verify with Redis CLI)
---

### 2.2 Verify Three-Tier Indexing

**Objective:** Create a test script to validate that all three RAG tiers are functioning correctly.

**Script Location:** `scripts/test_rag_queries.py`

**Requirements:**
- Test semantic search on ChromaDB
- Test graph traversal on Redis Graph
- Test temporal queries on SQLite
- Validate metadata completeness
- All tests must pass before proceeding to Phase 2

**Core Test Functions Needed:**

**A. Test Semantic Search (ChromaDB)**
- **Purpose:** Verify vector search returns relevant results
- **Test Cases:**
  1. Query: "debugging component initialization issues"
  2. Retrieve top 5 results from `pdca_historical` collection
  3. Verify results are relevant (contain debugging-related content)
  4. Verify results include metadata (pdca_id, agent_name, date, chunk_type)
- **Success Criteria:** At least 5 results returned, all contain relevant keywords

**B. Test Graph Traversal (Redis Graph)**
- **Purpose:** Verify breadcrumb navigation via PRECEDES edges
- **Test Cases:**
  1. Query Redis Graph for all PDCA nodes (MATCH (p:PDCA) RETURN p.id LIMIT 5)
  2. Verify at least 5 nodes returned
  3. Display node properties (pdca_id, agent, date)
- **Success Criteria:** Nodes accessible, properties populated
- **Note:** PRECEDES edges will be added later in Phase 4 evening loop

**C. Test Temporal Queries (SQLite)**
- **Purpose:** Verify fast date/agent filtering
- **Test Cases:**
  1. Query PDCAs from 2024 onwards (WHERE date >= '2024-01-01')
  2. Query PDCAs by agent (GROUP BY agent_name, COUNT)
  3. Verify results include expected fields (pdca_id, agent_name, date)
  4. Measure query speed (should be <100ms)
- **Success Criteria:** Temporal queries return results quickly with correct data

**D. Test Metadata Completeness**
- **Purpose:** Ensure all required metadata fields are populated
- **Test Cases:**
  1. Retrieve sample chunks from `pdca_historical` collection (limit 10)
  2. Check each chunk has all required fields:
     - `chunk_type`, `chunk_index`, `pdca_id`
     - `agent_name`, `agent_role`, `date`, `timestamp`
     - `trained_in_adapter`, `training_batch`, `training_date`
  3. Display sample metadata for inspection
- **Success Criteria:** All fields present in all sampled chunks

**Expected Output:**
```
============================================================
RAG System Validation Tests
============================================================

=== Testing Semantic Search (ChromaDB) ===
Query: debugging component initialization issues
Found 5 results:
  1. 20241015-102030-BuilderAgent.ComponentDevelopment_chunk_2: debugging init() ...
  2. 20241018-143015-TesterAgent.QualityAssurance_chunk_1: component initialization ...
  (showing abbreviated results)
✓ Semantic search working

=== Testing Graph Traversal (Redis Graph) ===
Found 5 PDCA nodes:
  - 20241027-090000-SaveRestartAgent.ProcessOrchestration
  - 20241026-153000-BuilderAgent.ComponentDevelopment
  (showing sample nodes)
✓ Graph traversal working

=== Testing Temporal Queries (SQLite) ===
Found 450 PDCAs from 2024:
  - 2024-10-27: 20241027-090000-SaveRestartAgent by SaveRestartAgent
  (showing sample results)

PDCAs by agent:
  - SaveRestartAgent: 125
  - BuilderAgent: 98
  - TesterAgent: 87
  (showing counts)
✓ Temporal queries working

=== Testing Metadata Completeness ===
✓ All 8 required metadata fields present

Sample metadata:
  - chunk_type: pdca_plan
  - chunk_index: 1
  - pdca_id: 20241027-090000-SaveRestartAgent.ProcessOrchestration
  - agent_name: SaveRestartAgent
  - agent_role: ProcessOrchestration
  - date: 2024-10-27
  - timestamp: 1730023200
  - trained_in_adapter: False

============================================================
ALL TESTS PASSED! ✓
============================================================
```

**Validation:**
- [ ] Semantic search returns relevant results
- [ ] Graph traversal finds PDCA nodes
- [ ] Temporal queries work correctly
- [ ] All metadata fields populated
- [ ] All tests pass

---

## Step 3: Data Quality Validation

**Estimated Time:** 2-4 hours  
**Goal:** Ensure RAG system is production-ready for sample generation

### 3.1 Create Test Harness Baseline

**Objective:** Establish baseline metrics from untrained base model for future comparison.

**Script Location:** `eval/baseline_test.py`

**Requirements:**
- Create baseline metrics JSON file
- Document all metric categories (pattern compliance, PDCA template, tool success, etc.)
- Set initial values to 0.0 (will measure trained model improvements in Phase 3)

**Baseline Metrics to Document:**
- `pattern_compliance` - Percentage of generated code following Web4 patterns (0.0 baseline)
- `pdca_template` - Percentage of generated PDCAs with correct structure (0.0 baseline)
- `tron_format` - Percentage of decisions following TRON format (0.0 baseline)
- `empty_constructor` - Percentage of classes with empty constructor pattern (0.0 baseline)
- `tool_success` - Percentage of tool calls executed successfully (0.0 baseline)
- `refusal_f1` - F1 score for appropriate refusals of unsafe requests (0.0 baseline)

**Output:** `outputs/baseline_metrics.json`

**Expected Content:**
```json
{
  "date": "2025-10-29T10:00:00",
  "model": "untrained_base",
  "metrics": {
    "pattern_compliance": 0.0,
    "pdca_template": 0.0,
    "tron_format": 0.0,
    "empty_constructor": 0.0,
    "tool_success": 0.0,
    "refusal_f1": 0.0
  },
  "notes": "Baseline established. Will measure trained model improvements in Phase 3."
}
```

**Validation:**
- [ ] `outputs/baseline_metrics.json` created
- [ ] Baseline documented for future comparison

---

### 3.2 Test RAG Query Performance

**Objective:** Verify query latency meets performance targets (<1 second).

**Requirements:**
- Test semantic query latency on ChromaDB
- Measure embedding generation time
- Measure similarity search time
- Ensure total latency under 1000ms

**Test Procedure:**
1. Load embedding model (sentence-transformers/all-MiniLM-L6-v2)
2. Connect to ChromaDB `pdca_historical` collection
3. Generate query embedding for test query: "show me component lifecycle management patterns"
4. Measure time to query collection (n_results=5)
5. Calculate total latency in milliseconds
6. Verify latency < 1000ms

**Expected Output:**
```
Semantic Query Latency: 480ms
✓ Query performance acceptable
```

**Validation:**
- [ ] Query latency under 1 second
- [ ] Results returned successfully
- [ ] Latency consistently acceptable across multiple queries

---

## Phase 1 Completion Checklist

Before proceeding to Phase 2, verify all items:

### Environment
- [ ] Python 3.10+ installed and verified
- [ ] Ollama installed (`ollama --version`)
- [ ] ChromaDB installed and tested
- [ ] Redis server running (`redis-cli ping`)
- [ ] RedisGraph module loaded
- [ ] SQLite available
- [ ] All Python dependencies installed

### Data Indexing
- [ ] 534 PDCAs indexed (verify count in ChromaDB)
- [ ] ~2,670 PDCA chunks created
- [ ] 3,477 TypeScript files indexed
- [ ] 238 process docs indexed (if applicable)
- [ ] 12K tool examples indexed (if files exist)
- [ ] ChromaDB collections created: `pdca_historical`, `components`, `tool_examples`
- [ ] Redis Graph contains PDCA nodes
- [ ] SQLite database populated

### Validation
- [ ] Semantic search returns relevant results (under 1 second)
- [ ] Graph traversal works (PDCA nodes accessible)
- [ ] Temporal queries work (date/agent filtering)
- [ ] Metadata completeness verified (15+ fields)
- [ ] Test harness baseline established
- [ ] Query performance acceptable (<1000ms)

### Documentation
- [ ] All scripts documented and executable
- [ ] Log files reviewed (no critical errors)
- [ ] Validation tests passed

---

## Success Criteria

**Phase 1 is complete when:**

✓ RAG system operational with 3 tiers (ChromaDB, Redis Graph, SQLite)  
✓ All 534 PDCAs queryable via semantic/graph/temporal methods  
✓ Test queries return relevant results under 1 second  
✓ Metadata complete (15+ fields per chunk)  
✓ Environment ready for Phase 2 sample generation

---

## Troubleshooting Guide

### Common Issues and Solutions

**Issue: Redis Connection Error**
- **Symptom:** `Could not connect to Redis at localhost:6379`
- **Solution:** Start Redis service for your OS (see section 1.4 for commands)
- **Verification:** Run `redis-cli ping` should return PONG

**Issue: ChromaDB Import Error**
- **Symptom:** `No module named 'chromadb'`
- **Solution:** Ensure virtual environment is activated and reinstall ChromaDB
- **Verification:** Python import test should pass

**Issue: Embedding Model Download Failure**
- **Symptom:** `Error downloading model: sentence-transformers/all-MiniLM-L6-v2`
- **Solution:** Check internet connection, retry download, or download manually
- **Verification:** Model should cache in `~/.cache/huggingface/`

**Issue: Out of Memory During Indexing**
- **Symptom:** `MemoryError: Unable to allocate array`
- **Solutions:**
  - Process files in smaller batches
  - Reduce embedding batch size
  - Close other applications
  - Consider upgrading RAM if consistently hitting limits

**Issue: PDCA Count Mismatch**
- **Symptom:** Found fewer than 534 PDCAs
- **Solution:** Verify Web4Articles repository path is correct
- **Verification:** Use find command to count `*.pdca.md` files

---

## Next Steps

Once Phase 1 is complete:

1. **Review Phase 1 Deliverables** - Ensure all checklist items completed
2. **Commit Indexing Scripts** - Save scripts to version control
3. **Backup RAG Databases** - Create backup of ChromaDB, Redis data, SQLite
4. **Proceed to Phase 2** - Begin sample generation from RAG

**Estimated Time to Phase 2:** Immediately (if Phase 1 validation passes)

---

## Phase 1 Summary

**Deliverables:**
- ✓ Complete three-tier RAG system (ChromaDB + Redis Graph + SQLite)
- ✓ 534 PDCAs indexed (~2,670 chunks)
- ✓ 3,477 TypeScript files indexed
- ✓ 12K tool examples indexed
- ✓ All queries validated and performant (<1 second)
- ✓ Baseline metrics established

**Scripts Created:**
- `scripts/initial_indexing.py` - Indexes all source data into RAG
- `scripts/test_rag_queries.py` - Validates three-tier functionality
- `eval/baseline_test.py` - Establishes baseline metrics

**Databases Created:**
- `./chroma_db/` - ChromaDB persistent storage
- `./pdca_timeline.db` - SQLite temporal database
- Redis Graph: `breadcrumb_graph` - In-memory graph database

**Duration:** Flexible (1-2 weeks typical)  
**Next Phase:** Phase 2 - Sample Generation

---

*Document Version: 2.0*  
*Last Updated: 2025-10-29*  
*Part of: Web4 Balanced LoRA Training Strategy*
*Format: Implementation Roadmap (no embedded code)*
