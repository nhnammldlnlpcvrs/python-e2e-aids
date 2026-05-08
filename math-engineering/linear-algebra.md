# Linear Algebra for Machine Learning

## 1. Vectors

### Notation
A vector $\mathbf{v} \in \mathbb{R}^n$ is an ordered list of $n$ real numbers:

$$\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}$$

### Dot Product (Inner Product)

$$\mathbf{a} \cdot \mathbf{b} = \mathbf{a}^T \mathbf{b} = \sum_{i=1}^{n} a_i b_i = \|\mathbf{a}\| \|\mathbf{b}\| \cos \theta$$

### Vector Norms

**L1 (Manhattan):** $\|\mathbf{v}\|_1 = \sum_i |v_i|$

**L2 (Euclidean):** $\|\mathbf{v}\|_2 = \sqrt{\sum_i v_i^2}$

**Lp:** $\|\mathbf{v}\|_p = \left(\sum_i |v_i|^p\right)^{1/p}$

**L∞ (Max):** $\|\mathbf{v}\|_\infty = \max_i |v_i|$

---

## 2. Matrices

A matrix $A \in \mathbb{R}^{m \times n}$ has $m$ rows and $n$ columns.

### Matrix Multiplication

$$C = A \cdot B \quad \Rightarrow \quad C_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}$$

Where $A \in \mathbb{R}^{m \times n}$ and $B \in \mathbb{R}^{n \times p}$.

### Properties

- **Not commutative:** $AB \neq BA$ (in general)
- **Associative:** $(AB)C = A(BC)$
- **Distributive:** $A(B + C) = AB + AC$
- **Transpose:** $(AB)^T = B^T A^T$
- **Inverse:** $(AB)^{-1} = B^{-1} A^{-1}$ (if both invertible)

### Important Matrix Types

- **Symmetric:** $A = A^T$
- **Orthogonal:** $A^T = A^{-1}$, so $A^T A = I$
- **Diagonal:** $A_{ij} = 0$ for $i \neq j$
- **Positive Definite:** $\mathbf{x}^T A \mathbf{x} > 0$ for all $\mathbf{x} \neq 0$

---

## 3. Linear Systems

$$A\mathbf{x} = \mathbf{b}$$

Where $A \in \mathbb{R}^{m \times n}$, $\mathbf{x} \in \mathbb{R}^n$, $\mathbf{b} \in \mathbb{R}^m$.

### Solution Existence

- **Unique solution:** $A$ is square and invertible → $\mathbf{x} = A^{-1}\mathbf{b}$
- **No solution:** Overdetermined system → use least squares
- **Infinite solutions:** Underdetermined system → use min-norm solution

### Least Squares

$$\min_{\mathbf{x}} \|A\mathbf{x} - \mathbf{b}\|_2^2$$

$$\hat{\mathbf{x}} = (A^T A)^{-1} A^T \mathbf{b}$$

---

## 4. Eigenvalues & Eigenvectors

$$A\mathbf{v} = \lambda \mathbf{v}$$

Where $\mathbf{v} \neq 0$ is an eigenvector and $\lambda$ is its eigenvalue.

### Eigendecomposition

If $A$ is diagonalizable (has $n$ linearly independent eigenvectors):

$$A = V \Lambda V^{-1}$$

Where $V = [\mathbf{v}_1, ..., \mathbf{v}_n]$ and $\Lambda = \text{diag}(\lambda_1, ..., \lambda_n)$.

### Trace & Determinant

$$\text{tr}(A) = \sum_i A_{ii} = \sum_i \lambda_i$$

$$\det(A) = \prod_i \lambda_i$$

---

## 5. Singular Value Decomposition (SVD)

Every matrix $A \in \mathbb{R}^{m \times n}$ can be factored as:

$$A = U \Sigma V^T$$

- $U \in \mathbb{R}^{m \times m}$: left singular vectors (orthogonal)
- $\Sigma \in \mathbb{R}^{m \times n}$: diagonal matrix of singular values $\sigma_1 \geq \sigma_2 \geq ... \geq 0$
- $V \in \mathbb{R}^{n \times n}$: right singular vectors (orthogonal)

### Applications

- **PCA:** Principal components are columns of $V$ (or $U\Sigma$)
- **Pseudoinverse:** $A^+ = V \Sigma^+ U^T$
- **Low-rank approximation:** Truncated SVD
- **Matrix condition number:** $\kappa(A) = \sigma_{\max} / \sigma_{\min}$

---

## 6. PCA (Principal Component Analysis)

### Derivation

1. Center data: $\tilde{X} = X - \bar{\mathbf{x}}$
2. Compute covariance: $C = \frac{1}{n-1} \tilde{X}^T \tilde{X}$
3. Eigendecomposition: $C = V \Lambda V^T$
4. Select top $k$ eigenvectors → $V_k$
5. Project: $Z = \tilde{X} V_k$

### Variance Explained

$$\text{Variance Ratio}_k = \frac{\sum_{i=1}^k \lambda_i}{\sum_{i=1}^n \lambda_i}$$

---

## 7. Matrix Calculus (for Backpropagation)

### Gradient w.r.t. Vector

$$\nabla_{\mathbf{x}} f(\mathbf{x}) = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{bmatrix}$$

### Common Identities

$$\nabla_{\mathbf{x}} (\mathbf{a}^T \mathbf{x}) = \mathbf{a}$$

$$\nabla_{\mathbf{x}} (\mathbf{x}^T A \mathbf{x}) = (A + A^T)\mathbf{x}$$

$$\nabla_{\mathbf{x}} \|A\mathbf{x} - \mathbf{b}\|_2^2 = 2A^T(A\mathbf{x} - \mathbf{b})$$

$$\nabla_{\mathbf{X}} \log \det(\mathbf{X}) = (\mathbf{X}^{-1})^T$$

### Chain Rule for Matrices

$$\frac{\partial z}{\partial x_{ij}} = \sum_{k,l} \frac{\partial z}{\partial y_{kl}} \cdot \frac{\partial y_{kl}}{\partial x_{ij}}$$

---

## Python Implementation (NumPy)

```python
import numpy as np

# SVD
A = np.random.randn(5, 3)
U, S, Vt = np.linalg.svd(A, full_matrices=False)

# PCA
X_centered = X - X.mean(axis=0)
cov = X_centered.T @ X_centered / (len(X) - 1)
eigenvals, eigenvecs = np.linalg.eigh(cov)
top_k = eigenvecs[:, -k:]  # largest eigenvalues last
X_pca = X_centered @ top_k

# Gradient check
def gradient_check(f, grad_f, x, eps=1e-7):
    numerical = np.zeros_like(grad_f)
    for i in range(len(x)):
        x_plus = x.copy()
        x_plus[i] += eps
        numerical[i] = (f(x_plus) - f(x)) / eps
    return np.allclose(grad_f, numerical, atol=1e-5)
```
