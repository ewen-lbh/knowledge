#automatique #signal 

## Définition

[[transformée de Fourrier]] de la [[réponse impulsionnelle]]

$$
H = \mathcal{F}[h]
$$



## Forme de [[fraction rationnelle]]

Pour un [[filtre numérique]] exprimé par ces coefficients, on a $H \in \mathbb{Q}(\mathbb{R})$ car
$$
Y = H \cdot X
$$
avec $Y$ la sortie et $X$ l'entrée

## Décomposition

Si $h$ est une [[réponse impulsionnelle causale]], on a 
$$
H = H_r + jH_i
$$
avec 
$$ \begin{cases}
H_r &= H_i \ast \frac{1}{\pi \operatorname{id}} \\
 H_i &= - H_r \ast \frac{1}{\pi \operatorname{id}}
\end{cases} $$



