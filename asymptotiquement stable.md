Qualité d'un [[point d'équilibre]].

## Cas d'une [[équation différentielle autonome]] et [[équation différentielle homogène|homogène]]

Pour $\dot x = Ax$, on a $0$ stable si et seulement si la [[partie réelle]] du [[spectre]] de $A$ est strictement négative:
$$
\operatorname{Re} \operatorname{Sp} A < 0
$$

ou si cette partiel réelle est négative et que, pour les [[valeur propre]] nulles, les [[multiplicité algébrique]] et [[multiplicité géométrique|géométriques]] sont égales:

$$
\begin{cases}
&\operatorname{Re} \operatorname{Sp} A &\le 0 \\
\forall \lambda \in \operatorname{Sp} A \cap i\mathbb{R}, &\operatorname{mult}_{\chi_A}(\lambda) &= \dim E_\lambda(A)
\end{cases}
$$


## Cas non linéaire
Pour $\dot x = f \circ x$, **si** la [[partie réelle]] du [[spectre]] de $f'(x_e)$ est strictement négative, **alors** $x_e$est asymptotiquement stable

$$
\operatorname{Re} \operatorname{Sp} f'(x_e) < 0
$$
