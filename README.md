# Python → AI/Data Science: Complete Learning Roadmap

A structured, code-heavy repository to go from Python beginner to AI/Data Science expert.

## Quick Start

```bash
git clone https://github.com/<your-username>/python-e2e-aids.git
cd python-e2e-aids
python -m venv .venv && source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Repository Structure

```
python-e2e-aids/
├── 01-python-core/                  # Python from basics to async
│   ├── theory/                      # Markdown notes per topic
│   ├── code/                        # Runnable .py examples
│   └── projects/                    # Mini-projects for portfolio
├── 02-dsa/                          # Data Structures & Algorithms
├── 03-oop-design-patterns/          # OOP, SOLID, Design Patterns
├── 04-ai-dl-libraries/              # NumPy, Pandas, Matplotlib, Sklearn, PyTorch
│   ├── numpy/  ├── pandas/  ├── matplotlib/
│   ├── scikit-learn/  ├── pytorch/  └── projects/
├── 05-domain-specialization/
│   ├── nlp/                         # NLP: TF-IDF → Transformers → LLMs
│   └── cv/                          # CV: CNNs → Object Detection → GANs
├── 06-data-science/                 # Stats, SQL, EDA, Visualization
├── math-engineering/                # Shared math reference (LaTeX)
├── resources/                       # Curated books, courses, papers
└── projects-showcase/               # Cross-stage portfolio projects
```

---

## Stage 1: Python Core

> **Goal:** Write idiomatic, performant Python. Understand everything from generators to asyncio.

### Must-Know Topics

| # | Topic | Sub-topics |
|---|-------|------------|
| 1.1 | **Foundations** | Types, mutability, `==` vs `is`, string interning, `sys.getsizeof` |
| 1.2 | **Control Flow** | Structural pattern matching (3.10+), `match`/`case`, `for`/`else` |
| 1.3 | **Functions** | `*args`/`**kwargs`, `functools.partial`, closures, `nonlocal`, `lambda` |
| 1.4 | **Iterables** | Iterator protocol, generators, `yield from`, `itertools`, comprehensions |
| 1.5 | **Decorators** | `@wraps`, decorator factories, class decorators, `@dataclass` |
| 1.6 | **Context Managers** | `__enter__`/`__exit__`, `contextlib.contextmanager`, `ExitStack` |
| 1.7 | **Error Handling** | Exception hierarchy, custom exceptions, `traceback`, `logging` |
| 1.8 | **Concurrency** | `threading`, `multiprocessing`, `concurrent.futures`, GIL, Amdahl's Law |
| 1.9 | **Asyncio** | `async`/`await`, event loop, `asyncio.gather`, `aiohttp`, `asyncio.Queue` |
| 1.10 | **Tooling** | `pyproject.toml`, `uv`/`poetry`, `pytest`, `ruff`, `mypy` |

### Key Math

$$\text{Amdahl's Law: } S = \frac{1}{(1-p) + \frac{p}{n}}$$

Where $S$ = speedup, $p$ = parallelizable fraction, $n$ = number of processors.

### Mini-Projects

1. **CLI File Organizer** — `argparse` + `pathlib` + `shutil` file sorter by extension/date with decorator-based logging
2. **Async News Aggregator** — concurrent RSS fetcher using `aiohttp` + `asyncio`, export to JSON/CSV

### Resources

- [Fluent Python (2nd Ed.)](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) — Luciano Ramalho
- [Python Official Docs](https://docs.python.org/3/) — the best reference
- [CS50P (Harvard)](https://cs50.harvard.edu/python/) — free, excellent intro
- [Real Python](https://realpython.com/) — deep dives

---

## Stage 2: Data Structures & Algorithms

> **Goal:** Implement every data structure and algorithm from scratch in Python. Analyze Big-O rigorously.

### Must-Know Topics

| # | Topic | Key Structures |
|---|-------|---------------|
| 2.1 | **Big-O Analysis** | $O(1)$, $O(\log n)$, $O(n)$, $O(n \log n)$, $O(n^2)$, $O(2^n)$. Time vs Space |
| 2.2 | **Arrays & Strings** | Dynamic arrays, amortized analysis, two-pointer, sliding window, KMP |
| 2.3 | **Linked Lists** | Singly, doubly, circular, Floyd's cycle detection |
| 2.4 | **Stacks & Queues** | Array-based, linked-based, monotonic stack, deque, priority queue |
| 2.5 | **Hash Tables** | Hash functions, collision resolution (chaining, open addressing), load factor $\alpha = n/m$ |
| 2.6 | **Trees** | BST, AVL (rotations), Red-Black, Trie, Segment Tree, Fenwick Tree |
| 2.7 | **Heaps** | Binary heap, heapify $O(n)$, heap sort, `heapq` |
| 2.8 | **Graphs** | Adjacency list/matrix, BFS, DFS, topological sort, Dijkstra, Bellman-Ford, A\*, MST (Kruskal, Prim) |
| 2.9 | **Dynamic Programming** | Memoization vs tabulation, 0/1 knapsack, LCS, LIS, edit distance, matrix chain |
| 2.10 | **Greedy & Backtracking** | Activity selection, N-Queens, Sudoku solver, subset sum |

### Key Math

**Master Theorem** for divide-and-conquer recurrences:

$$T(n) = aT\left(\frac{n}{b}\right) + f(n) \quad \text{where } a \geq 1, b > 1$$

**DP state transition (Edit Distance):**

$$dp[i][j] = \min\begin{cases} dp[i-1][j] + 1 & \text{(delete)} \\ dp[i][j-1] + 1 & \text{(insert)} \\ dp[i-1][j-1] + [s_i \neq t_j] & \text{(replace)} \end{cases}$$

### Mini-Projects

1. **Pathfinding Visualizer** — BFS / DFS / Dijkstra / A\* animated with `matplotlib.animation`
2. **LRU + TTL Cache** — hash map + doubly-linked list, decorator interface, thread-safe variant

### Resources

- [Problem Solving with Algorithms (Python)](https://runestone.academy/ns/books/published/pythonds/index.html) — free interactive book
- [Competitive Programming 3](https://cpbook.net/) — Halim & Halim
- [MIT 6.006](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — OCW
- [LeetCode Explore](https://leetcode.com/explore/) — structured problem sets

---

## Stage 3: OOP & Design Patterns

> **Goal:** Design extensible, testable, maintainable Python systems using OOP principles and GoF patterns.

### Must-Know Topics

| # | Topic | Python Specifics |
|---|-------|-----------------|
| 3.1 | **Encapsulation** | `_protected`, `__name_mangling`, `@property`, `__slots__`, descriptor protocol |
| 3.2 | **Inheritance** | `super()`, MRO (C3 linearization), `issubclass()`, `isinstance()`, mixins |
| 3.3 | **Polymorphism** | Duck typing, ABC (`@abstractmethod`), `Protocol` (structural subtyping), `@override` |
| 3.4 | **SOLID** | S: Single Responsibility, O: Open/Closed, L: Liskov, I: Interface Segregation, D: Dependency Inversion |
| 3.5 | **Creational Patterns** | Singleton (Borg), Factory Method, Abstract Factory, Builder, Prototype |
| 3.6 | **Structural Patterns** | Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy |
| 3.7 | **Behavioral Patterns** | Chain of Responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor |
| 3.8 | **Modern Python OOP** | `dataclasses`, `NamedTuple`, `Enum`, `Literal`, `TypeVar`, `Generic`, `Protocol` |

### Mini-Projects

1. **Plugin-based Task Runner** — `abc.ABC` base + `importlib` dynamic loading + `pydantic` config validation
2. **E-commerce Order System** — Strategy for discounts, Observer for events, Factory for payment gateways

### Resources

- [Architecture Patterns with Python](https://www.cosmicpython.com/) — free online book (DDD + patterns)
- [Refactoring.Guru](https://refactoring.guru/design-patterns) — design patterns with Python examples
- [ArjanCodes (YouTube)](https://www.youtube.com/@ArjanCodes) — practical Python design patterns
- [Python Design Patterns (GitHub)](https://github.com/faif/python-patterns) — opensource collection

---

## Stage 4: AI & Deep Learning Libraries

> **Goal:** Master the Python data science stack. Implement ML numerically, then with frameworks.

### NumPy

| Topic | Key Operations |
|-------|---------------|
| Array creation, indexing, slicing | `np.array`, fancy indexing, boolean masks |
| Broadcasting & vectorization | Avoid Python loops, understand broadcasting rules |
| Universal functions (ufuncs) | `np.vectorize`, `np.apply_along_axis` |
| Linear algebra | `np.linalg`, `@`, `np.einsum`, SVD |
| Random sampling | `np.random.Generator`, distributions |

**Key Math:**

$$C_{ij} = \sum_{k=1}^{n} A_{ik} \cdot B_{kj}$$

$$\text{SVD: } A_{m \times n} = U_{m \times m} \Sigma_{m \times n} V^T_{n \times n}$$

### Pandas

| Topic | Key Operations |
|-------|---------------|
| Series & DataFrame | Creation, multi-level indexing, `.loc`/`.iloc` |
| Data cleaning | `dropna`, `fillna`, `replace`, `astype`, `pd.to_datetime` |
| Transformations | `groupby`, `pivot_table`, `melt`, `stack`/`unstack`, `merge`/`join` |
| Window functions | `rolling`, `expanding`, `ewm` |
| Performance | `eval`, `query`, Categorical dtype, chunked reading |

### Matplotlib

| Topic | Notes |
|-------|-------|
| `pyplot` interface | Figures, axes, subplots, saving |
| Plot types | Line, scatter, bar, histogram, boxplot, heatmap, contour |
| Customization | `rcParams`, annotations, legends, colormaps, LaTeX rendering |
| Animation | `FuncAnimation`, saving to GIF/MP4 |

### Scikit-learn

| Topic | Key Concepts |
|-------|-------------|
| Preprocessing | `StandardScaler`, `OneHotEncoder`, `Pipeline`, `ColumnTransformer` |
| Supervised learning | Linear/Logistic Regression, SVM, Random Forest, XGBoost |
| Unsupervised | K-Means, DBSCAN, PCA, t-SNE |
| Model evaluation | Cross-validation, GridSearchCV, confusion matrix, ROC-AUC, F1 |
| Metrics | `classification_report`, `r2_score`, `mean_squared_error` |

**Key Math:**

$$\text{F1} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$$

$$\text{ROC-AUC} = \int_0^1 \text{TPR}(FPR^{-1}(x)) \, dx$$

### PyTorch

| Topic | Key Concepts |
|-------|-------------|
| Tensors | Creation, device (CPU/GPU), dtype, operations, gradient tracking |
| Autograd | `requires_grad`, `backward()`, gradient accumulation |
| `nn.Module` | `forward()`, `parameters()`, `state_dict`, `train()`/`eval()` |
| Layers | `nn.Linear`, `nn.Conv2d`, `nn.LSTM`, `nn.BatchNorm`, Activation functions |
| Training loop | `DataLoader`, `Dataset`, optimizer (`Adam`, `SGD`), `lr_scheduler` |
| Loss functions | `CrossEntropyLoss`, `MSELoss`, `BCEWithLogitsLoss` |

**Key Math — Backpropagation (chain rule):**

$$\frac{\partial L}{\partial w_{ij}} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial a_j} \cdot \frac{\partial a_j}{\partial z_j} \cdot \frac{\partial z_j}{\partial w_{ij}}$$

**Gradient Descent:**

$$w_{t+1} = w_t - \eta \nabla_w L(w_t)$$

### Mini-Projects

1. **ML Pipeline (Titanic)** — EDA → Feature Engineering → Model Selection → Hyperparameter Tuning → Submissions
2. **Neural Network from NumPy vs PyTorch** — 2-layer MLP on MNIST, same architecture, compare gradients and speed

### Resources

- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) — Jake VanderPlas (free)
- [Dive into Deep Learning (d2l.ai)](https://d2l.ai/) — interactive, PyTorch/TF/JAX
- [fast.ai](https://www.fast.ai/) — practical DL, top-down approach
- [Full Stack Deep Learning](https://fullstackdeeplearning.com/) — production ML
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html) — comprehensive

---

## Stage 5: Domain Specialization

### 5A — Natural Language Processing (NLP)

| # | Topic | Key Concepts |
|---|-------|-------------|
| 5.1 | **Text Processing** | Tokenization (word, subword, BPE), stemming, lemmatization, regex, Unicode |
| 5.2 | **Vector Space Models** | BoW, TF-IDF, cosine similarity, n-grams |
| 5.3 | **Word Embeddings** | Word2Vec (CBOW, Skip-gram), GloVe, FastText, co-occurrence matrix factorization |
| 5.4 | **Sequence Models** | RNN, LSTM (forget/input/output gates), GRU, bidirectional, stacked |
| 5.5 | **Attention & Transformers** | Scaled dot-product attention, multi-head, positional encoding, encoder-decoder |
| 5.6 | **Pretrained Language Models** | BERT (MLM + NSP), GPT (autoregressive), T5 (text-to-text) |
| 5.7 | **Fine-tuning & PEFT** | LoRA, QLoRA, prompt tuning, RLHF |
| 5.8 | **LLM Applications** | RAG (retrieval-augmented generation), agents, tool use, LangChain |

**Key Math:**

$$\text{TF-IDF}(t,d) = \text{tf}(t,d) \times \log\frac{N}{\text{df}(t)}$$

$$\text{Cosine Similarity: } \cos(\theta) = \frac{A \cdot B}{\|A\| \|B\|} = \frac{\sum A_i B_i}{\sqrt{\sum A_i^2} \sqrt{\sum B_i^2}}$$

$$\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

$$\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1, ..., \text{head}_h)W^O$$

$$\text{where head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$

**LSTM Gates:**

$$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f) \quad \text{(forget)}$$
$$i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i) \quad \text{(input)}$$
$$o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o) \quad \text{(output)}$$
$$\tilde{C}_t = \tanh(W_C \cdot [h_{t-1}, x_t] + b_C)$$
$$C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$$
$$h_t = o_t \odot \tanh(C_t)$$

**Cross-Entropy Loss:**

$$\mathcal{L} = -\sum_{c=1}^{C} y_c \log(\hat{y}_c)$$

### 5B — Computer Vision (CV)

| # | Topic | Key Concepts |
|---|-------|-------------|
| 5.9 | **Image Fundamentals** | Pixels, channels, histograms, color spaces (RGB, HSV, LAB) |
| 5.10 | **Filtering** | Convolution, Sobel, Canny, Gaussian blur, morphological ops |
| 5.11 | **CNN Architectures** | AlexNet → VGG → Inception → ResNet (skip connections) → EfficientNet |
| 5.12 | **Object Detection** | R-CNN family, YOLO (grid + anchors), SSD, NMS |
| 5.13 | **Segmentation** | Semantic (U-Net, DeepLab), Instance (Mask R-CNN) |
| 5.14 | **Generative Models** | Autoencoder, VAE, GAN, Diffusion models (DDPM), Stable Diffusion |
| 5.15 | **Vision Transformers** | ViT, patch embedding, self-attention for images |

**Key Math:**

**2D Convolution:**

$$(I * K)_{i,j} = \sum_{m=0}^{k_h-1} \sum_{n=0}^{k_w-1} I_{i+m,\, j+n} \cdot K_{m,n}$$

**Output dimensions after convolution:**

$$H_{out} = \left\lfloor \frac{H_{in} + 2P - F}{S} \right\rfloor + 1$$

**IoU (Intersection over Union):**

$$\text{IoU} = \frac{\text{Area of Overlap}}{\text{Area of Union}} = \frac{|A \cap B|}{|A \cup B|}$$

**Dice Loss (Segmentation):**

$$\mathcal{L}_{\text{Dice}} = 1 - \frac{2 \sum_i p_i g_i}{\sum_i p_i + \sum_i g_i}$$

**GAN Objective:**

$$\min_G \max_D V(D,G) = \mathbb{E}_{x \sim p_{data}}[\log D(x)] + \mathbb{E}_{z \sim p_z}[\log(1 - D(G(z)))]$$

### NLP Projects

1. **Sentiment Analysis with BERT** — fine-tune `bert-base-uncased` on IMDb reviews, deploy with FastAPI
2. **RAG Question-Answering Bot** — LangChain + ChromaDB + OpenAI/HuggingFace embedding, chat interface

### CV Projects

1. **Image Classifier with Transfer Learning** — fine-tune ResNet50 on custom dataset (CIFAR-100 or custom)
2. **Neural Style Transfer** — VGG19 feature extraction, content loss + style loss (Gram matrix)

### Resources

- [Speech & Language Processing (Jurafsky & Martin)](https://web.stanford.edu/~jurafsky/slp3/) — free online
- [HuggingFace NLP Course](https://huggingface.co/learn/nlp-course) — free, practical
- [CS224n (Stanford NLP)](https://web.stanford.edu/class/cs224n/) — lectures + assignments
- [CS231n (Stanford CV)](https://cs231n.github.io/) — notes + assignments
- [d2l.ai NLP Chapter](https://d2l.ai/chapter_natural-language-processing-pretraining/index.html)
- [d2l.ai CV Chapter](https://d2l.ai/chapter_convolutional-modern/index.html)
- [Papers with Code](https://paperswithcode.com/) — SOTA + implementations

---

## Stage 6: Data Science & Analysis

> **Goal:** Derive insights from data end-to-end — SQL → Python → Statistics → Dashboard.

### Must-Know Topics

| # | Topic | Key Concepts |
|---|-------|-------------|
| 6.1 | **Descriptive Statistics** | Mean, median, mode, variance, std, skewness, kurtosis, IQR |
| 6.2 | **Probability Distributions** | Bernoulli, Binomial, Poisson, Normal, Exponential, Gamma, Beta |
| 6.3 | **Inferential Statistics** | Sampling distributions, CLT, confidence intervals, bootstrap |
| 6.4 | **Hypothesis Testing** | Null/alternative, Type I/II error, p-value, t-test, $\chi^2$ test, ANOVA, Mann-Whitney U |
| 6.5 | **Correlation & Regression** | Pearson $r$, Spearman $\rho$, linear regression, $R^2$, adjusted $R^2$, regularization (Ridge, Lasso) |
| 6.6 | **Bayesian Statistics** | Bayes theorem, prior/likelihood/posterior, MCMC, PyMC |
| 6.7 | **SQL for Analytics** | `JOIN` (inner, left, right, full, cross, self), window functions (`ROW_NUMBER`, `RANK`, `LAG`/`LEAD`), CTEs, `GROUP BY` + `HAVING`, subqueries |
| 6.8 | **EDA Framework** | Univariate/bivariate/multivariate analysis, missing data patterns, outlier detection (Z-score, IQR, isolation forest) |
| 6.9 | **Visualization** | Seaborn, Plotly, Streamlit/Dash for dashboards |
| 6.10 | **A/B Testing** | Sample size calculation, randomization, t-test/z-test for proportions, effect size (Cohen's d), MDE |

### Key Math

**Normal Distribution PDF:**

$$\mathcal{N}(x \mid \mu, \sigma^2) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)$$

**Central Limit Theorem:**

$$\bar{X}_n \xrightarrow{d} \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right) \quad \text{as } n \to \infty$$

**Pearson Correlation Coefficient:**

$$r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2} \sqrt{\sum_{i=1}^{n}(y_i - \bar{y})^2}}$$

**Coefficient of Determination ($R^2$):**

$$R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}} = 1 - \frac{\sum_i (y_i - \hat{y}_i)^2}{\sum_i (y_i - \bar{y})^2}$$

**Bayes' Theorem:**

$$P(H \mid E) = \frac{P(E \mid H) \cdot P(H)}{P(E)}$$

**p-value:**

$$p\text{-value} = P(\text{test statistic} \geq t_{\text{obs}} \mid H_0 \text{ is true})$$

### Mini-Projects

1. **End-to-End Sales Analysis** — SQL (PostgreSQL) → Pandas EDA → Statistical testing → Streamlit dashboard with KPIs
2. **A/B Testing Simulation** — design experiment, calculate sample size with power analysis, run A/A validation, analyze with bootstrap CIs

### Resources

- [Introduction to Statistical Learning (ISLR)](https://www.statlearning.com/) — free PDF, Python edition available
- [OpenIntro Statistics](https://www.openintro.org/book/os/) — free, comprehensive
- [Kaggle Learn](https://www.kaggle.com/learn) — free micro-courses (Pandas, SQL, Data Viz, ML)
- [Mode Analytics SQL Tutorial](https://mode.com/sql-tutorial/) — practical SQL for analytics
- [DataCamp](https://www.datacamp.com/) — interactive (some free)

---

## Shared Math Reference (`math-engineering/`)

Essential math across all stages, written in LaTeX-friendly Markdown:

| File | Contents |
|------|----------|
| `linear-algebra.md` | Vectors, matrices, dot product, $Ax = b$, eigenvalues/eigenvectors, SVD, PCA derivation, matrix calculus |
| `calculus.md` | Derivatives, partial derivatives, chain rule, gradient, Jacobian, Hessian, gradient descent convergence |
| `probability-statistics.md` | Random variables, Bayes theorem, MLE, MAP, KL divergence, distributions catalog |
| `information-theory.md` | Entropy, cross-entropy, mutual information, perplexity, information bottleneck |

---

## Portfolio Projects (`projects-showcase/`)

Cross-stage projects that combine multiple skills:

| Project | Stages Used | Key Skills |
|---------|-------------|------------|
| **ML Model API** — FastAPI serving a trained model with Docker | 1, 4, 6 | async Python, sklearn, API design, Docker |
| **Chat with Your PDF** — RAG pipeline with local LLM | 1, 4, 5 | asyncio, PyTorch, embeddings, vector DB, Streamlit |
| **Kaggle Competition Pipeline** | 4, 6 | EDA, feature engineering, model tuning, ensembling |
| **Real-time Object Detection App** | 4, 5 | PyTorch, OpenCV, FastAPI, WebSockets |

---

## Progress Tracking

Track progress by checking off completed topics:

```markdown
- [ ] Stage 1: Python Core
- [ ] Stage 2: DSA
- [ ] Stage 3: OOP & Design Patterns
- [ ] Stage 4: AI & DL Libraries
- [ ] Stage 5: Domain Specialization (NLP / CV)
- [ ] Stage 6: Data Science & Analysis
```

---

## Setup & Usage

```bash
# Clone
git clone https://github.com/<your-username>/python-e2e-aids.git
cd python-e2e-aids

# Virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

# Install dependencies (create stage-specific requirements-*.txt)
pip install -r requirements.txt

# Run tests
pytest

# Lint
ruff check .
```

---

> **Philosophy:** Theory → Code → Math → Project. Every concept must pass through all four before moving on.
