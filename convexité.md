# Convexité
[[propriété]] d'une [[fonction]] ou d'un [[ensemble]].

## Pour un ensemble
$C \subset E$ est **convexe** si et seulement si:

$$
\forall (a, b) \in C^2,\ \forall t \in [0, 1],\ ta + (1-t)b \in C
$$

### Remarque
$ta+(1-t)b$ avec $t \in [0, 1]$ est une manière d'exprimer un point sur un segment quand $a$ et $b$ ne sont pas dans un [[ensemble ordonné]].

## Pour une fonction
On a $f$ **convexe** si et seulement si:

- $\operatorname{src} f$ est convexe))
- $\forall (a, b) \in (\operatorname{src} f)^2,\ \forall t \in [0, 1],\  f(ta+(1-t)b) \leq tf(a) + (1-t)f(b)$

On a alors la propriété suivante pour $\operatorname{src} f \subset \mathbb{R}$:

- Pour tout points $(a, b) \in (\operatorname{src} f)^2$: 
	$f([a, b])$ est en dessous de la corde $[f(a), f(b)]$

### Caractérisation par la [[dérivée]] seconde
Si $f'' \ge 0$, $f$ est convexe

### Caractérisation par la [[matrice hessienne]].

Si $\operatorname{tr} \nabla^2 f(x) \ge 0$, $f$ est convexe