Pour $f$ une [[fonction]] réelle telle que $f(\mathbb{R}^-) = \{0\}$.

$$
\mathcal{L}(f) : \begin{cases}
\mathbb{C} &\to \mathbb{C} \\
p &\mapsto \int_0^{+\infty} f(t)e^{-pt} \mathrm{d}t
\end{cases}
$$
## Opérations usuelles

### [[dérivée]]

Multiplier par $p$ et soustraire $f(0^+)$

### [[intégrale]]

Diviser par $p$

### [[limite]] en $+\infty$

$$
\lim_{0+} \circ \mathcal{L} \circ \cdot' = \lim_{+\infty} \circ \operatorname{id}
$$

### [[produit de convolution]]

$$
\mathcal{L} \circ \ast = \times \circ \mathcal{L}
$$