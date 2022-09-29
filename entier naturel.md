# Entier naturel
#modélisation 

## Construction de Peano

On a besoin de:

- $\operatorname{entier}(x)$ ($x \in \mathbb{N}$)
- $\operatorname{zero}(x)$ ($x = 0$)
- $\operatorname{succ}(x, y)$ ($y = x+1$)
- $\operatorname{égalité}(x, y)$ ($x=y$)
- $\operatorname{somme}(x, y, z)$ ($x+y=z$)

### $\operatorname{un}$

$$
\forall x, \operatorname{un}(x) \iff ( \operatorname{entier}(x) \land \exists y, \operatorname{entier}(x) \land \operatorname{zero}(y) \land \operatorname{succ}(y, x) )
$$
### $\operatorname{deux}$

Comme $\operatorname{un}$ mais on met $\operatorname{un}$ au lieu de $\operatorname{zero}$.

### $\operatorname{égalité}$

$$
	\begin{align*}
\forall x, \forall y, \operatorname{entier}(x) \land \operatorname{entier}(y) \implies &( \operatorname{égalité}(x, y) \iff ( \\
& [\operatorname{zero}(x) \iff \operatorname{zero}(y)] \land {} \\
& [\lnot \operatorname{zero}(x) \land \lnot \operatorname{zero}(y) \implies (\\
&\exists x' \exists y', \operatorname{entier}(x') \land \operatorname{entier}(y') \land \operatorname{succ}(x, x') \land \operatorname{succ}(y, y') \land \operatorname{égalité}(x', y'))]\\
) )
\end{align*}
$$

### $\operatorname{somme}$

On pose

- $0+m = m$
- $\operatorname{succ}(n) + m = \operatorname{succ}(n+m)$