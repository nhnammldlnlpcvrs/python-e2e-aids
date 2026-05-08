# Information Theory for Machine Learning

## 1. Entropy (Shannon Entropy)

Measures the average information content (uncertainty) of a random variable:

$$H(X) = -\sum_{x} p(x) \log_2 p(x) \quad \text{(bits)}$$

$$H(X) = -\sum_{x} p(x) \ln p(x) \quad \text{(nats)}$$

### Properties

- $0 \leq H(X) \leq \log n$ where $n$ = number of outcomes
- $H(X) = 0$ if deterministic (one outcome has probability 1)
- $H(X) = \log n$ for uniform distribution (maximum uncertainty)

### Binary Entropy

$$H_2(p) = -p \log_2 p - (1-p) \log_2(1-p)$$

Maximum at $p=0.5$: $H_2(0.5) = 1$ bit.

---

## 2. Joint & Conditional Entropy

### Joint Entropy

$$H(X, Y) = -\sum_{x,y} p(x,y) \log p(x,y)$$

### Conditional Entropy

$$H(Y \mid X) = -\sum_{x} p(x) \sum_{y} p(y \mid x) \log p(y \mid x)$$

$$H(Y \mid X) = H(X, Y) - H(X)$$

### Chain Rule

$$H(X_1, X_2, ..., X_n) = \sum_{i=1}^{n} H(X_i \mid X_1, ..., X_{i-1})$$

---

## 3. Mutual Information

Measures how much information one variable provides about another:

$$I(X; Y) = H(X) - H(X \mid Y) = H(Y) - H(Y \mid X)$$

$$I(X; Y) = \sum_{x,y} p(x,y) \log \frac{p(x,y)}{p(x)p(y)}$$

### Properties

- Symmetric: $I(X; Y) = I(Y; X)$
- Non-negative: $I(X; Y) \geq 0$
- $I(X; Y) = 0$ iff $X$ and $Y$ are independent

---

## 4. KL Divergence (Relative Entropy)

Measures how one probability distribution differs from another:

$$D_{KL}(P \parallel Q) = \sum_x P(x) \log \frac{P(x)}{Q(x)}$$

### Properties

- **Not symmetric:** $D_{KL}(P \parallel Q) \neq D_{KL}(Q \parallel P)$
- **Non-negative:** $D_{KL}(P \parallel Q) \geq 0$ (Gibbs' inequality)
- $D_{KL}(P \parallel Q) = 0$ iff $P = Q$ almost everywhere

### Forward vs Reverse KL

| Direction | Behavior | Use Case |
|-----------|----------|----------|
| $D_{KL}(P \parallel Q)$ | **Mean-seeking** — Q covers all modes of P | MLE training |
| $D_{KL}(Q \parallel P)$ | **Mode-seeking** — Q focuses on one mode | Variational inference |

---

## 5. Cross-Entropy

$$H(P, Q) = -\sum_x P(x) \log Q(x) = H(P) + D_{KL}(P \parallel Q)$$

For a classification problem, $P$ is the true distribution (one-hot label), $Q$ is the predicted distribution:

$$\mathcal{L}_{\text{CE}} = -\sum_{c=1}^{C} y_c \log(\hat{y}_c)$$

For binary classification (logistic loss):

$$\mathcal{L}_{\text{BCE}} = -[y \log \hat{y} + (1-y) \log(1-\hat{y})]$$

---

## 6. Perplexity

Common metric in NLP (language modeling):

$$\text{PPL} = 2^{H(P, Q)} = 2^{-\frac{1}{N}\sum_i \log_2 p(w_i \mid w_{<i})}$$

Lower perplexity = better model. A perplexity of 1 means perfect prediction.

---

## 7. Data Processing Inequality

If $X \to Y \to Z$ forms a Markov chain:

$$I(X; Z) \leq I(X; Y)$$

Processing data can only destroy information, never create it.

---

## 8. Information Bottleneck

Find a compressed representation $T$ of $X$ that preserves information about $Y$:

$$\min_{P(T \mid X)} I(X; T) - \beta \cdot I(T; Y)$$

Where $\beta$ controls the compression-relevance tradeoff.

### Connection to Deep Learning

The layers of a neural network can be viewed as successive information bottlenecks, with the penultimate layer compressing input into a representation that preserves label-relevant information.

---

## 9. Fano's Inequality

Lower bound on error probability from conditional entropy:

$$P(\hat{X} \neq X) \geq \frac{H(X \mid Y) - 1}{\log |\mathcal{X}|}$$

---

## Python Snippets

```python
import numpy as np

def entropy(p):
    """Compute entropy in nats. p should sum to 1."""
    p = np.asarray(p)
    p = p[p > 0]  # 0 log 0 = 0
    return -np.sum(p * np.log(p))

def kl_divergence(p, q):
    """KL(P || Q)"""
    p, q = np.asarray(p), np.asarray(q)
    mask = (p > 0) & (q > 0)
    return np.sum(p[mask] * np.log(p[mask] / q[mask]))

def cross_entropy(y_true, y_pred):
    """Cross-entropy loss"""
    y_pred = np.clip(y_pred, 1e-15, 1 - 1e-15)
    return -np.sum(y_true * np.log(y_pred))
```
