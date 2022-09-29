# dérivée seconde au sens de Frechêt
#optimisation 

On a
$$
\forall h, k \in E, f''(x)(h, k) = (v \mapsto f'(v)\cdot h)'(x) \cdot k
$$

### Preuve

$g(x) = B \circ \psi (x)$




$f: \mathbb{R}^n \to \mathbb{R}$. 

$$
\begin{align}
f'(x)\cdot h = J_f(x)\times h &= \begin{pmatrix} \frac{\partial f}{\partial x_1}(x) & \ldots & \frac{\partial f}{\partial x_n}(x)\end{pmatrix} \begin{pmatrix} h_1 \\ \vdots \\ h_n \end{pmatrix} \\
&= \langle \nabla f(x), h \rangle
\end{align}
$$

$$
\nabla f : \mathbb{R}^n \to \mathbb{R}^n
$$

$$J_{\Delta f}(x) = \nabla^2 f(x)$$


$g: x \mapsto \nabla f(x) \mapsto \langle \nabla f(x), k \rangle = f'(x)\cdot k$

$g'(x)\cdot h = f''(x)(h, k)$

$\psi : y \mapsto \langle y, k\rangle$
$\psi'(y)\cdot \underbrace{\delta}_{J_{\Delta f}(x)\times h} = \langle \delta, k\rangle$

$$
\begin{align}
g'(x)\cdot h &= f''(x) \cdot (h, k) \\
&= \langle J_{\Delta f}(x)\times h, k \rangle \\
&= h {}^T J_{\Delta f}(x)\times k
\end{align}
$$

# À SAVOIR

$$
\begin{align}
f'(x)\cdot h &= J_f(x)\times h \\
&= \begin{pmatrix} \frac{\partial f_1(x)}{\partial x_1} & \ldots & \frac{\partial f_1(x)}{\partial x_n} \\
\vdots & & \vdots \\ 
\frac{\partial f_n(x)}{\partial x_1} & \ldots & \frac{\partial f_n(x)}{\partial x_n} \\
\end{pmatrix} \begin{pmatrix} h_1 \\ \vdots \\ h_n \end{pmatrix}
\end{align}
$$


Pour $f: \mathbb{R}^n \to \color{red}{\mathbb{R}}$, $J_f(x)$ a une seule ligne, et $\nabla f(x)$ c'est $J_f(x)$ mais mis en colonne.


### Exemple

$$
f: x = \begin{pmatrix} x_1 \\ \vdots \\ x_n\end{pmatrix} \mapsto \frac{1}{2} \| x \|^2 = \frac{1}{2} \sum_{i=1}^n x_i^2
$$

$$J_f(x) = x^{\top}$$
et
$$
\nabla f: \mathbb{R}^n \to \mathbb{R}^n
$$

#### Moindre carrés linéaire

$$
\begin{align}
\nabla f&: \mathbb{R}^n \to \mathbb{R}^n \\
\beta &\mapsto \nabla f(\beta) = (X^\top X)\beta - X^\top y = A \beta + b\\
\nabla^2 f(\beta) &= J_{\Delta f}(\beta) = A = X^\top X
\end{align}
$$

Il faut que $\nabla^2 f(x)$ soit symmétrique

### Résidu non linéaire

$$
\begin{align}
f(x) = \frac{1}{2} \sum_{i=1}^n r_i^2(x) = \frac{1}{2} \| r(x) \|^2
\end{align}
$$
On a 

$$\begin{align}
g &:= r(x) \mapsto \frac{1}{2} \| r(x) \| \\
f'(x)\cdot h &= g'(r(x))\cdot (r'(x)\cdot h) \\
g'(y)\cdot k &= J_g(y)\times k = \langle \nabla g(y), k \rangle \\
&= \langle y, k\rangle & \text{avec} \begin{cases} y = r(x) \\ k = J_f(x) \times h \end{cases} \\
f'(x)\cdot h &= \langle r(x), J_r(x)\times h \rangle \\
&= r(x)^\top \times J_r(x)\times h \\
&= J_f(x)\times h
\end{align} 
$$

Or 

$$
J_f(x) = r(x)^\top J_r(x)
$$

et

$$\begin{align}
\nabla f(x) &= J_r^\top(x) \times r(x) \\
J_r^\top(x) &= \begin{pmatrix}
| & | & | \\
\nabla r_1(x) & | & \nabla r_n(x) \\
| & | & | \\
\end{pmatrix}\\
\nabla f(x) &= \sum_{i=1}^m r_i(x)\nabla r_i(x) \\
\nabla^2 f(x) &= \sum_{i=1}^m r_i(x)\nabla r_i(x) + \sum_{i=1}^n \nabla r_i(x) \nabla^\top r_i(x)
\end{align}$$

On veut dériver $g: x \stackrel{g_1}{\mapsto} (r_i(x),  \nabla r_i(x)) \stackrel{g_2}{\mapsto} r_i(x) \nabla r_i(x)$.

- $g_1'(x)\cdot h = \left(\left\langle \nabla r_i(x), h \right\rangle, J_{\nabla r_i}(x)\cdot h\right)$
- $g_2 = (a, b) \mapsto ab$, donc $g_2'(a, b)\cdot (k_1, k_2)  = g_2(a, k_2) + g_2(k_1, b) = a k_2 + k_1 b$
- $g'(x)\cdot h = g'_2(g_1(x))\cdot (g'_1(x)\cdot h)$

