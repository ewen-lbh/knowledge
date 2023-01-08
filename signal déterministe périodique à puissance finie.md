## Définition

Un [[signal]] [[signal déterministe]] [[périodique]] à [[énergie d'un signal|puissance]] [[fini|finie]].

## Puissance

Soit $x$ un signal déterministe périodique à puissance finie de [[période]] $T$

$$
P(x) = \frac{1}{T} \int^{-T/2}_{T/2} |x|^2
$$

## [[produit scalaire|Produit scalaire]]

$$
\langle x, y \rangle = \frac{1}{T} \int^{-T/2}_{T/2} x y^\ast
$$

## [[densité spectrale d'énergie|densité spectrale de puissance]]

Soit $x(t) = \displaystyle\sum_{k\in \mathbb{Z}} c_k \exp(j2\pi k f_0 t)$
Alors:
$$
s_x(f) = \sum_{k\in \mathbb{Z}} |c_k|^2 \delta(f - kf_0)
$$