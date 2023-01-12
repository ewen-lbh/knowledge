## Définition

Un [[signal]] non-[[signal déterministe|déterministe]] [[stationnarité|stationnaire]]. Il est défini par une [[variable aléatoire]] au lieu d'une fonction du temps.

- La [[espérance|moyenne]] ne dépend pas de $t$
- Le [[moment d'ordre 2]] $E(t\mapsto x(t) x^\ast(t-\tau))$ ne dépend pas de $t$

## [[produit scalaire]]

$$
\langle x, y \rangle = E(xy^\ast)
$$
## [[énergie d'un signal|puissance]] moyenne

$$
P(x) = E(|x|^2)
$$
## [[densité spectrale d'énergie|densité spectrale de puissance]]

**Si $X = \mathcal{F}[x]$ existe**:

$$
s_x(f) = \lim_{T\to \infty} \frac{1}{T} E\left( \left| \int^{-T/2}_{T/2} X(f) e^{-j2\pi ft} \mathrm{d}t \right|^2 \right)
$$


## Espérance d'un signal [[filtre|filtré]]

$$
E(H \cdot X) = H(0) \cdot E(X)
$$
 