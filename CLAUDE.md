# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

Personal learning repository structured across 6 progressive stages: Python beginner → AI/Data Science expert. This is a living portfolio — code, theory notes, math references, and projects all live here.

## Architecture

Each stage follows the same pattern:

```
0X-stage-name/
├── theory/       # Markdown notes — one file per topic
├── code/         # Runnable .py examples demonstrating concepts
└── projects/     # 2+ self-contained mini-projects per stage
```

Stages are ordered (01 → 06) and build on each other:
- **01-python-core** — idiomatic Python through asyncio
- **02-dsa** — every data structure/algorithm from scratch with Big-O
- **03-oop-design-patterns** — SOLID, GoF patterns in Python
- **04-ai-dl-libraries** — NumPy, Pandas, Matplotlib, Scikit-learn, PyTorch (sub-folders per library)
- **05-domain-specialization** — `nlp/` and `cv/` sub-trees, each with theory/code/projects
- **06-data-science** — statistics, SQL, EDA, visualization

Shared resources live at repo root:
- `math-engineering/` — linear algebra, calculus, probability/stats, information theory (LaTeX)
- `resources/` — curated books, courses (free/OSS prioritized)
- `projects-showcase/` — larger cross-stage portfolio projects

## Conventions

- **Language:** All code, comments, and documentation in English
- **Math:** LaTeX with `$$` delimiters in all markdown files
- **Linting:** `ruff check .` (see `.github/workflows/ci.yml`)
- **Python version:** 3.12 (CI target), 3.10+ minimum
- **No build system yet** — `requirements.txt` or `pyproject.toml` to be added per stage as needed
- **Data files excluded** — `.csv`, `.parquet`, `.pt`, `.h5` etc. in `.gitignore`; use `data/.gitkeep` for empty data dirs
