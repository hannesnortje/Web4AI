# Web4AI Training Pipeline

LLM Training Pipeline with Three-Tier RAG System for Web4 Architecture patterns and practices.

## Overview

This project implements a balanced LoRA training strategy for fine-tuning large language models on Web4 architectural patterns, PDCA cycles, and TypeScript component development patterns.

## Components

- **RAG System**: Three-tier retrieval system (ChromaDB + Redis + SQLite)
- **Training Pipeline**: Automated sample generation and model fine-tuning
- **Evaluation**: Comprehensive test harnesses for quality validation

## Project Structure

- `scripts/` - Python scripts for indexing, training, evaluation
- `data/` - Generated JSONL training files
- `config/` - Configuration files (training params, RAG settings)
- `outputs/` - LoRA adapters, GGUF models, eval reports
- `eval/` - Evaluation test harnesses
- `logs/` - Log files for debugging
- `Implementation/` - Implementation guides and roadmaps

## Setup

```bash
# Install dependencies
poetry install

# Activate virtual environment
poetry shell
```

## Phases

1. **Phase 1**: Setup & RAG Bootstrap
2. **Phase 2**: Sample Generation
3. **Phase 3**: LoRA Training
4. **Phase 4**: GGUF Export & Ollama Integration
5. **Phase 5**: Evening Loop & Continuous Improvement

## Requirements

- Python 3.11+
- 32GB RAM (for local training)
- Redis server
- Ollama (for production deployment)

## License

Proprietary - Cerulean Circle

