# Probability & Statistics for Data Science

## 1. Probability Fundamentals

### Axioms

1. $0 \leq P(A) \leq 1$ for any event $A$
2. $P(\Omega) = 1$ where $\Omega$ is the sample space
3. $P(A \cup B) = P(A) + P(B)$ if $A \cap B = \emptyset$

### Conditional Probability

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

### Bayes' Theorem

$$P(H \mid E) = \frac{P(E \mid H) \cdot P(H)}{P(E)}$$

Where:
- $P(H)$ = prior probability
- $P(E \mid H)$ = likelihood
- $P(H \mid E)$ = posterior probability
- $P(E)$ = marginal likelihood (normalizing constant)

### Law of Total Probability

$$P(E) = \sum_i P(E \mid H_i) \cdot P(H_i)$$

---

## 2. Random Variables & Distributions

### Discrete Distributions

#### Bernoulli
$$P(X=k) = p^k(1-p)^{1-k}, \quad k \in \{0, 1\}$$
$$\mathbb{E}[X] = p, \quad \text{Var}(X) = p(1-p)$$

#### Binomial
$$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$$
$$\mathbb{E}[X] = np, \quad \text{Var}(X) = np(1-p)$$

#### Poisson
$$P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$$
$$\mathbb{E}[X] = \lambda, \quad \text{Var}(X) = \lambda$$

### Continuous Distributions

#### Normal (Gaussian)
$$f(x \mid \mu, \sigma^2) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$
$$\mathbb{E}[X] = \mu, \quad \text{Var}(X) = \sigma^2$$

**Standard Normal:** $\mu=0, \sigma=1$

**Z-score:** $z = \frac{x - \mu}{\sigma}$

#### Exponential
$$f(x \mid \lambda) = \lambda e^{-\lambda x}, \quad x \geq 0$$
$$\mathbb{E}[X] = \frac{1}{\lambda}, \quad \text{Var}(X) = \frac{1}{\lambda^2}$$

#### Uniform
$$f(x \mid a, b) = \frac{1}{b-a}, \quad a \leq x \leq b$$
$$\mathbb{E}[X] = \frac{a+b}{2}, \quad \text{Var}(X) = \frac{(b-a)^2}{12}$$

---

## 3. Expectation & Variance

### Expectation

$$\mathbb{E}[X] = \begin{cases}
\sum_x x \cdot p(x) & \text{discrete} \\
\int x \cdot f(x) \, dx & \text{continuous}
\end{cases}$$

### Variance

$$\text{Var}(X) = \mathbb{E}[(X - \mathbb{E}[X])^2] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$$

### Covariance

$$\text{Cov}(X, Y) = \mathbb{E}[(X - \mathbb{E}[X])(Y - \mathbb{E}[Y])]$$

### Correlation

$$\rho_{X,Y} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}$$

---

## 4. Law of Large Numbers & CLT

### Weak Law of Large Numbers

$$\lim_{n \to \infty} P(|\bar{X}_n - \mu| > \varepsilon) = 0$$

### Central Limit Theorem (CLT)

For i.i.d. random variables $X_1, ..., X_n$ with mean $\mu$ and variance $\sigma^2$:

$$\frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1)$$

Equivalently:

$$\bar{X}_n \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right) \quad \text{for large } n$$

---

## 5. Maximum Likelihood Estimation (MLE)

Given data $\{x_1, ..., x_n\}$ and model parameters $\theta$:

**Likelihood:** $L(\theta) = \prod_{i=1}^{n} P(x_i \mid \theta)$

**Log-likelihood:** $\ell(\theta) = \log L(\theta) = \sum_{i=1}^{n} \log P(x_i \mid \theta)$

**MLE:** $\hat{\theta}_{\text{MLE}} = \arg\max_\theta \ell(\theta)$

### Example: MLE for Normal Distribution

For $\mu$: $\hat{\mu} = \frac{1}{n}\sum_i x_i = \bar{x}$

For $\sigma^2$: $\hat{\sigma}^2 = \frac{1}{n}\sum_i (x_i - \bar{x})^2$

---

## 6. Hypothesis Testing

### Framework

- **$H_0$:** Null hypothesis (status quo)
- **$H_1$:** Alternative hypothesis
- **$\alpha$:** Significance level (probability of Type I error)
- **$\beta$:** Probability of Type II error
- **Power:** $1 - \beta$

| | $H_0$ True | $H_0$ False |
|---|---|---|
| **Reject $H_0$** | Type I Error ($\alpha$) | Correct (Power) |
| **Fail to Reject** | Correct | Type II Error ($\beta$) |

### p-value

$$p\text{-value} = P(\text{observing test statistic} \geq t_{\text{obs}} \mid H_0 \text{ is true})$$

If $p\text{-value} < \alpha$, reject $H_0$.

### Common Tests

| Test | Use Case | Test Statistic |
|------|----------|---------------|
| **Z-test** | Compare mean, σ known | $Z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}$ |
| **t-test** | Compare mean, σ unknown | $t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$ |
| **χ² test** | Independence/categorical | $\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$ |
| **ANOVA** | Compare 3+ group means | $F = \frac{MS_{\text{between}}}{MS_{\text{within}}}$ |

---

## 7. Regression

### Simple Linear Regression

$$y = \beta_0 + \beta_1 x + \varepsilon$$

**OLS Estimates:**

$$\hat{\beta}_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2} = r_{xy} \cdot \frac{s_y}{s_x}$$

$$\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$$

### R-squared

$$R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}} = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$$

### Adjusted R-squared

$$R^2_{\text{adj}} = 1 - \frac{(1-R^2)(n-1)}{n-k-1}$$

Where $k$ = number of predictors.

### Regularization

**Ridge (L2):** $\min_\beta \|y - X\beta\|_2^2 + \lambda \|\beta\|_2^2$

**Lasso (L1):** $\min_\beta \|y - X\beta\|_2^2 + \lambda \|\beta\|_1$

**Elastic Net:** $\min_\beta \|y - X\beta\|_2^2 + \lambda_1 \|\beta\|_1 + \lambda_2 \|\beta\|_2^2$

---

## 8. Confidence Intervals

### For Mean ($\sigma$ known)

$$\bar{x} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$$

### For Mean ($\sigma$ unknown)

$$\bar{x} \pm t_{\alpha/2, n-1} \cdot \frac{s}{\sqrt{n}}$$

### For Proportion

$$\hat{p} \pm z_{\alpha/2} \cdot \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$

### Bootstrap CI

Resample with replacement $B$ times, compute statistic each time, take $\alpha/2$ and $1-\alpha/2$ percentiles.
