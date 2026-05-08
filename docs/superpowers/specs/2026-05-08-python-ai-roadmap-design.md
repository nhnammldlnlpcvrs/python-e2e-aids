# Python AI/DS Learning Roadmap — Repository Design

**Date:** 2026-05-08
**Status:** Approved

## Overview

Personal learning repository structured across 6 progressive stages, from Python beginner to AI/Data Science expert. All content in English for portability and community sharing.

## Repository Structure

```
python-e2e-aids/
├── .github/workflows/             # CI (lint, test on push)
├── 01-python-core/
│   ├── theory/                    # Markdown topic notes
│   ├── code/                      # Runnable .py examples
│   └── projects/                  # 2+ mini-projects
├── 02-dsa/
│   ├── theory/
│   ├── code/
│   └── projects/
├── 03-oop-design-patterns/
│   ├── theory/
│   ├── code/
│   └── projects/
├── 04-ai-dl-libraries/
│   ├── numpy/
│   ├── pandas/
│   ├── matplotlib/
│   ├── scikit-learn/
│   ├── pytorch/
│   └── projects/
├── 05-domain-specialization/
│   ├── nlp/
│   │   ├── theory/
│   │   ├── code/
│   │   └── projects/
│   └── cv/
│       ├── theory/
│       ├── code/
│       └── projects/
├── 06-data-science/
│   ├── statistics/
│   ├── sql/
│   ├── eda/
│   ├── visualization/
│   └── projects/
├── math-engineering/              # Shared LaTeX math reference
├── resources/                     # Curated links, books
├── projects-showcase/             # Cross-stage portfolio projects
├── README.md
└── .gitignore
```

## Stage Specifications

### Stage 1 — Python Core
- **Theory:** Types, functions, iterators/generators, decorators, context managers, OOP basics, threading, asyncio, packaging
- **Math:** Set builder notation, Amdahl's Law
- **Projects:** CLI File Organizer, Async News Aggregator
- **Key resources:** Fluent Python (Ramalho), Python Docs, CS50P

### Stage 2 — DSA
- **Theory:** Arrays, linked lists, stacks/queues, hash tables, trees, graphs, DP, greedy, backtracking
- **Big-O analysis for every implementation**
- **Math:** Recurrence relations, Master Theorem, load factor
- **Projects:** Pathfinding Visualizer, LRU Cache + TTL Cache

### Stage 3 — OOP & Design Patterns
- **Theory:** Encapsulation, inheritance (MRO/C3), polymorphism (ABC/Protocol), SOLID
- **Patterns:** Singleton, Factory, Builder, Adapter, Decorator, Facade, Observer, Strategy, Command
- **Projects:** Plugin-based Task Runner, E-commerce Order System

### Stage 4 — AI & DL Libraries
- **NumPy:** Broadcasting, vectorization, einsum, linalg, SVD
- **Pandas:** groupby, merge, pivot_table, rolling, apply
- **Matplotlib:** pyplot, subplots, FuncAnimation
- **Scikit-learn:** Pipelines, CV, metrics, preprocessing
- **PyTorch:** Tensors, autograd, nn.Module, DataLoader
- **Key math:** Matrix multiply, chain rule backprop, gradient descent, F1 score, ROC-AUC
- **Projects:** ML Pipeline Titanic, Neural Network NumPy vs PyTorch

### Stage 5 — Domain Specialization
- **NLP:** TF-IDF, Word2Vec, RNN/LSTM, Transformer attention, BERT/GPT fine-tuning, RAG
- **CV:** Convolution, CNN (ResNet), Object Detection (YOLO), Segmentation (U-Net), GANs
- **Key math:** Cosine similarity, skip-gram loss, attention formula, IoU, GAN minmax objective
- **Projects:** Sentiment Analysis BERT, QA Bot RAG, Image Classifier Transfer Learning, Neural Style Transfer

### Stage 6 — Data Science
- **Statistics:** Descriptive stats, normal distribution, hypothesis testing, correlation, regression
- **SQL:** Joins, window functions, CTEs, aggregation
- **EDA best practices**
- **Key math:** Normal PDF, p-value definition, Pearson r, R-squared, Bayes theorem
- **Projects:** End-to-End Sales Dashboard, A/B Testing Simulation

## Shared Math Reference (`math-engineering/`)
- Linear Algebra: Ax=b, eigen decomp, SVD, PCA derivation
- Calculus: Chain rule, gradient descent, partial derivatives
- Probability & Statistics: Bayes theorem, MLE, distributions
- Information Theory: Entropy, cross-entropy, KL divergence

## Design Decisions
- **Language:** English for all code, comments, and documentation
- **Structure:** Stage-based folders (01-06) for linear progression
- **Math:** Dedicated `math-engineering/` with LaTeX math blocks
- **Portfolio:** `projects-showcase/` for larger cross-stage projects
- **Minimal CI:** Basic linting only, no heavy testing initially
