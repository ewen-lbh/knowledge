# Espérance conditionnelle
#PROBA 
_pas aux partiels askip_
$$
E(\alpha(X, Y)) = E_X(E_Y(\alpha(X, Y)|X))
$$

## Exemple

Soit $Y_N = \sum_{i=1}^N X_i$ avec $X_i \sim \mathcal{B}(p)$ et $N \sim \mathcal{P}(\lambda)$

$$
\begin{align*}
E(Y_N) &= E\left(\sum_{i=1}^N X_i \right) \\
&= E_N\left(E_{Y_N}\left(\sum_{i=1}^N X_i \mid N\right)\right) \quad \text{avec $\alpha(N, X_1, \ldots, X_N) = \sum_{i=1}^N X_i$} \\
&= E_N(Np)\\
&= pE_N(N)\\
	&= p \lambda
\end{align*}
$$

