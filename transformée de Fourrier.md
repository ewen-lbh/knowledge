On prend $p \in \mathcal{L}^2$ (ou $p \in \mathcal{L}^1$, c'est _plus simple_)
Formule directe
$$
\mathcal{F}[p](f) := \int_\mathbb{R} e^{-j2\pi f t} p(t) \mathrm{d}t
$$
[[transformée de Fourrier inverse|Formule inverse]]
$$
\mathcal{F^{-1}}[P](t) := \int_\mathbb{R} e^{j2\pi f t} P(f) \mathrm{d}f
$$
[3b1b](https://youtube.com/watch?v=spUNpyF58BY)


## [[dérivée|Dérivation]]

$$
 \mathcal{F}[x^{(n)}](f) = (j2\pi f)^n \mathcal{F}[x](f)
$$

## Propriétés
$\mathcal{F}$ est

- linéaire
- conserve la parité
- **transformation** $\mathcal{F}[x(t-t_0)](f) = e^{-2\pi j f t_0} X(f)$
- **modulation** $\mathcal{F}[x(t)e^{j2\pi f_0 t}] = X(f-f_0)$
- **similitude** $\mathcal{F}[x(at)](f) = \frac{1}{|a|} X(\frac{f}{a})$

en gros translation en temps $\iff$ multiplication par exp(...) en fréquence


## Transformées usuelles

| Temporel | Fréquentiel |
| ------------ | ------------------------------- |
| $x^\ast$ | $X^\ast \circ (-\operatorname{id})$
|$x \circ (a \operatorname{id} + b)$ | $\frac{1}{|a|} X(\frac{a}{f}) e^{j2\pi \frac{b}{a} f}$ |


