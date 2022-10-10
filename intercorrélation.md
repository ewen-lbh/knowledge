# Intercorrélation

Pour deux [[signaux à énergie finie]] $x$ et $y$:

$$
R_{xy}(\tau) = \int_\mathbb{R} x(t) \bar y(t-\tau) \mathrm{d}
t = \left\langle x(t), y(t-\tau)\right\rangle$$

On fait un produit scalaire entre $x$ et tout les décalés de $y$ dans une fenêtre pour voir leur similitude

## Propriétés

- $R_x = x \ast \hat x$ avec $\hat x(t) = \bar x(-t)$ TODO c'est un tshetch pas un circonflexe
- $\mathcal{F}[R_x(\tau)] = |\mathcal{F}[x]|^2$ (c'est la [[densité spectrale d'énergie]])
