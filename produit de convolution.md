#signal
Opérateur défini par

$$
f \ast g = \int_{-\infty}^{+\infty} g(t-\tau) f(\tau) \mathrm{d}\tau
$$

## Propriétés

- Avec la [[transformée de Fourrier]]: 
	- $\mathcal{F}[f \ast g] = \mathcal{F}[f]\cdot \mathcal{F}[g]$
	- $\mathcal{F}[f\cdot g] = \mathcal{F}[f] \ast \mathcal{F}[g]$

- $\mathcal{F}[\text{carré}] = \text{sinc}$

- [[égalité de Parseval]]

## Avec l'[[impulsion de Dirac]]
- **localisation** $x(t)\delta(t-t_0) = x(t_0)\delta(t-t_0)$
- produit de convolution $x(t)\ast \delta(t-t_0) = x(t-t_0)$
- $x(t_0) = \int_\mathbb{R} x(t) \delta(t-t_0) \mathrm{d}t$


## Convolution par la [[réponse impulsionnelle]] d'un [[filtre]]

### Propriétés

Soit $h$ la réponse impulsionnelle d'un filtre. L'opération $T = x \mapsto x \ast h$ est:

- Linéaire
- Invariante dans le temps $$\forall t_0, t \in \mathbb{R}, T[x](t) = T[x](t-t_0)$$
- Stable (BIBO)
   Si $x$ est borné alors $T[x]$ est borné, ou de manière équivalente (CNS) $$\int_\mathbb{R} |h| < \infty$$
- Le spectre du signal est "limité"

