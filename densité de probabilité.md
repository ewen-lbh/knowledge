# Densité de probabilité
#PROBA

[[fonction]] permettant la mesure de la [[probabilité]] d'un [[événement]] de la forme $P(X\in\Delta)$, avec $X$ une [[variable aléatoire]] suivant une [[loi de probabilité]] continue et $\Delta \subset X(\Omega)$. Cette fonction doit satisfaire la [[condition de normalisation]]: $\int_{X(\Omega)} p = 1$.

## Pour un couple
On fait la double intégrale:

$$
p(x, y) = \iint_\mathbb{R} p(x, y)\mathrm{d}x\mathrm{d}y
$$

### Exemple
*Montrez que $p_a(x, y) = \begin{cases} 1-a(1-2x)(1-2y) & \text{si } (x, y) \in [0, 1] \times [0, 1] \\ 0 & \text{sinon} \end{cases}$ est une densité de probabilité*

$$
\begin{align}
\int_0^1\int_0^1 1-a(1-2x)(1-2y)\mathrm{d}x\mathrm{d}y &= \int_0^1 \left[ x-a(x-x^2)(1-2y) \right]_0^1 \mathrm{d}y \\
&= \int_0^1 1 \mathrm{d}y  \\
&= 1
\end{align}
$$

Donc $\iint_\mathbb{R} p_a(x, y) = 1$ pour tout $a$ donc ok.