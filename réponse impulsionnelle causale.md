## Définition

Un [[réponse impulsionnelle]] $h$ est dite _causale_ si et seulement si:

$$
h(\mathbb{R}_-^\ast) = \set{0}
$$

## Interprétation

Cela signifie que le filtre ne dépend que des sorties antérieures, puisqu'il n'y a rien en sortie avant le temps initial ($t=0$).

## Rendre une réponse causale

On peut rendre n'importe quelle réponse causale en introduisant un retard, afin d'accumuler les sorties nécéssaires:

$$
\hat{h} = t \mapsto h(\tau - t)
$$

avec le retard $\tau$ égal (ou supérieur, mais pas trop d'intérêt) à:

$$
\operatorname{argmin} \set{h(t) > 0, t \in \mathbb{R}}
$$
