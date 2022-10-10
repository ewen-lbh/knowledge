# Produit de convolution
Opérateur défini par

$$
f \ast g = \int_{-\infty}^{+\infty} g(t-\tau) f(\tau) \mathrm{d}\tau
$$

## Propriétés

- Avec la [[transformée de Fourrier]]: 
	- $\mathcal{F}[f \ast g] = \mathcal{F}[f]\cdot \mathcal{F}[g]$
	- $\mathcal{F}[f\cdot g] = \mathcal{F}[f] \ast \mathcal{F}[g]$



- $\mathcal{F}[\text{carré}] = \text{sinc}$

## Avec l'[[impulsion de Dirac]]
- **localisation** $x(t)\delta(t-t_0) = x(t_0)\delta(t-t_0)$
- [[produit de convolution]] $x(t)\ast \delta(t-t_0) = x(t-t_0)$
	- $x(t_0) = \int_\mathbb{R} x(t) \delta(t-t_0) \mathrm{d}t$

