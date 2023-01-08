## Définition

On a $h$ la [[réponse impulsionnelle]] d'un [[filtre]] et $x$ un [[signal]] bruité, i.e. tel que:
$$
x = s + n
$$avec 
- $s$ un [[signal déterministe à énergie finie]]
- $n$ un [[signal aléatoire stationnaire]] avec $E(n) = 0$

$$
\operatorname{SNR}[h, s, n] = \frac{h \ast s}{E(h \ast n)}
$$
## Caractérisations

On a également

$$
\begin{align*}
h\ast s &= | \mathcal{F}^{-1}(S \cdot H)|^2 \\
(h\ast s)(t)&= \int_\mathbb{R} H(f) S(f) e^{j2\pi f t} \mathrm{d}f
\end{align*}
$$
et 
$$
\begin{align*}
E(h\ast n) &= \int_\mathbb{R} |H|^2 \cdot s_n \quad \text{par Wiener-Lee} \\
&= R_{h\ast n}(0) \\
&= P(h\ast n )
\end{align*}
$$

