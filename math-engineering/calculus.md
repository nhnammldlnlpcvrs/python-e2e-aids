# Calculus for Machine Learning

## 1. Derivatives

### Definition

$$f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}$$

### Common Derivatives

| Function | Derivative |
|----------|-----------|
| $x^n$ | $n x^{n-1}$ |
| $e^x$ | $e^x$ |
| $\ln(x)$ | $\frac{1}{x}$ |
| $\sin(x)$ | $\cos(x)$ |
| $\cos(x)$ | $-\sin(x)$ |
| $\tanh(x)$ | $1 - \tanh^2(x)$ |
| $\sigma(x) = \frac{1}{1+e^{-x}}$ | $\sigma(x)(1 - \sigma(x))$ |
| $\text{ReLU}(x) = \max(0, x)$ | $\mathbb{1}[x > 0]$ |

### Chain Rule

$$(f \circ g)'(x) = f'(g(x)) \cdot g'(x)$$

---

## 2. Partial Derivatives & Gradient

For $f: \mathbb{R}^n \to \mathbb{R}$:

$$\nabla f(\mathbf{x}) = \left[ \frac{\partial f}{\partial x_1}, \frac{\partial f}{\partial x_2}, ..., \frac{\partial f}{\partial x_n} \right]^T$$

### Gradient Descent

$$w_{t+1} = w_t - \eta \nabla L(w_t)$$

Where $\eta$ is the learning rate.

### Stochastic Gradient Descent (SGD)

$$w_{t+1} = w_t - \eta \nabla L_i(w_t)$$

Where $i$ is a random (or mini-batch) sample.

### SGD with Momentum

$$v_{t+1} = \beta v_t + \nabla L(w_t)$$
$$w_{t+1} = w_t - \eta v_{t+1}$$

### Adam Optimizer

$$m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t \quad \text{(first moment)}$$
$$v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2 \quad \text{(second moment)}$$
$$\hat{m}_t = \frac{m_t}{1 - \beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1 - \beta_2^t}$$
$$w_{t+1} = w_t - \eta \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}$$

---

## 3. Jacobian & Hessian

### Jacobian Matrix

For $f: \mathbb{R}^n \to \mathbb{R}^m$:

$$J_f = \begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n} \\
\vdots & \ddots & \vdots \\
\frac{\partial f_m}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_n}
\end{bmatrix}$$

### Hessian Matrix

For $f: \mathbb{R}^n \to \mathbb{R}$:

$$H_f = \begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \cdots & \frac{\partial^2 f}{\partial x_n^2}
\end{bmatrix}$$

The Hessian is symmetric: $H_{ij} = H_{ji}$.

---

## 4. Backpropagation (Neural Networks)

For a 3-layer MLP:

$$\hat{y} = \sigma(W_3 \cdot \sigma(W_2 \cdot \sigma(W_1 x + b_1) + b_2) + b_3)$$

### Forward Pass

$$z_1 = W_1 x + b_1, \quad a_1 = \sigma(z_1)$$
$$z_2 = W_2 a_1 + b_2, \quad a_2 = \sigma(z_2)$$
$$z_3 = W_3 a_2 + b_3, \quad \hat{y} = \sigma(z_3)$$
$$L = \text{Loss}(\hat{y}, y)$$

### Backward Pass (Chain Rule)

$$\frac{\partial L}{\partial z_3} = \frac{\partial L}{\partial \hat{y}} \cdot \sigma'(z_3)$$

$$\frac{\partial L}{\partial W_3} = \frac{\partial L}{\partial z_3} \cdot a_2^T$$

$$\frac{\partial L}{\partial z_2} = W_3^T \frac{\partial L}{\partial z_3} \cdot \sigma'(z_2)$$

$$\frac{\partial L}{\partial W_2} = \frac{\partial L}{\partial z_2} \cdot a_1^T$$

$$\frac{\partial L}{\partial z_1} = W_2^T \frac{\partial L}{\partial z_2} \cdot \sigma'(z_1)$$

$$\frac{\partial L}{\partial W_1} = \frac{\partial L}{\partial z_1} \cdot x^T$$

### General Pattern

For a linear layer $z = Wx + b$:

$$\frac{\partial L}{\partial W} = \frac{\partial L}{\partial z} \cdot x^T$$
$$\frac{\partial L}{\partial x} = W^T \cdot \frac{\partial L}{\partial z}$$

---

## 5. Convergence of Gradient Descent

### Convex Functions

A function $f$ is convex if for all $x, y$ and $\lambda \in [0,1]$:

$$f(\lambda x + (1-\lambda) y) \leq \lambda f(x) + (1-\lambda) f(y)$$

### L-smoothness

$$|f'(x) - f'(y)| \leq L |x - y|$$

For L-smooth convex functions, GD with $\eta = 1/L$ converges:

$$f(x_t) - f(x^*) \leq \frac{L\|x_0 - x^*\|^2}{2t}$$

### μ-Strong Convexity

$$f(y) \geq f(x) + f'(x)(y-x) + \frac{\mu}{2}\|y-x\|^2$$

For μ-strongly convex, L-smooth functions, GD with $\eta = 1/L$:

$$\|x_t - x^*\| \leq \left(\frac{L-\mu}{L+\mu}\right)^t \|x_0 - x^*\|$$

---

## 6. Taylor Series Approximation

$$f(x) \approx f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + ...$$

**First-order (linear):** $f(x) \approx f(a) + f'(a)(x-a)$

**Second-order (quadratic):** $f(x) \approx f(a) + f'(a)(x-a) + \frac{1}{2}f''(a)(x-a)^2$

---

## 7. Softmax Derivative

Softmax: $s_i = \frac{e^{z_i}}{\sum_j e^{z_j}}$

$$\frac{\partial s_i}{\partial z_j} = \begin{cases}
s_i (1 - s_j) & \text{if } i = j \\
-s_i s_j & \text{if } i \neq j
\end{cases}$$

Combined with cross-entropy loss $L = -\sum_k y_k \log s_k$:

$$\frac{\partial L}{\partial z_i} = s_i - y_i$$

This elegant result is why softmax + cross-entropy is universal in classification.
