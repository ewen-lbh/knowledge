#signal 

## Énoncé

Soit $(X_1, X_2) \sim \mathcal{N}_2(m, \sigma^2)$ avec $m \neq 0$ et $g: \mathbb{R} \to \mathbb{R}$

$$
	\frac{\partial E(g(X_1) g(X_2))}{\partial E(X_1 X_2)} = E\left( \frac{\partial g(X_1)}{\partial X_1} \cdot \frac{\partial g(X_2)}{X_2}  \right)
$$

## Application au [[quadrateur]]

On a $y = x^2$.

On veut une expression de $R_y$ en fonction de $R_x$.

$$
\begin{align*}
\frac{\partial R_y}{\partial R_x}(\tau)  &= \frac{\partial \langle y, y(\cdot -\tau) \rangle }{\partial \langle x, x(\cdot -\tau) \rangle} \\
&= \frac{\partial E(x^2(t) x^2(t-\tau))}{\partial E(x(t) x(t-\tau))} \\
&= \frac{\partial E(g(x_1(t)) g(x_2(t)) )}{\partial E(x_1(t) x_2(t))} \quad \text{avec}\ x_1 = x,\ x_2 = x(\cdot - \tau) \text{ et } g = \operatorname{id}^2 \\
&= E\left( \frac{\partial x^2}{\partial x} \cdot \frac{\partial x(\cdot - \tau)^2}{\partial x(\cdot - \tau)} \right) \quad \text{d'après le théorème de Price} \\
&= E(4x(t)x(t-\tau)) \\
&= 4 E(x(t) x(t-\tau)) \\
&= 4 \langle x, x(\cdot - \tau) \rangle \\
&= 4 R_x(\tau)
\end{align*}
$$

On intègre:

$$
\begin{align*}
R_y(\tau) &= 2R_x(\tau)^2 + \text{const}
\end{align*}
$$

Pour trouver $\text{const}$, on évalue en $\tau = 0$:

$$
\begin{align*}
R_y(0) &= \langle y, y \rangle \\
&= E(yy^\ast) \\
&= E(|y|^2) \\
&= E(|x^2|^2) \\
&= E(x^4) \\
&= (3 \times 1) \sigma^4 \quad \text{moments d'une loi Gaussienne centrée} \\
&= 4\sigma^4 \\
\text{or} \quad R_y(0) &= 2R_x^2(0) + \text{const} \\
\text{donc} \quad \text{const} &= 4\sigma^4 - 2(R_x(0))^2 \\
&= 4\sigma^4 - 2E(|x|^2) \\
&= 4\sigma^4 - \sigma^2 \quad \text{si $|x| = x$ i.e. $x\geq 0$}
\end{align*}
$$

On peut aussi s'en tenir à $\text{const} = R^2_x(0)$


