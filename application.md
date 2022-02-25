# Application
Objet $f$ encapsulant une expression contenant une variable non-définie $x$

## Notation
$$f := x \mapsto \text{expression}$$
## Spécification de la source et du but

$$
f := \begin{cases}
	\text{source} &\to \text{but} \\
	x &\mapsto \text{expression} \\
	\end{cases}
$$

## Évaluation
Opérateur $\cdot(\cdot \cdot)$ ayant pour valeur celle de l'$\text{expression}$ de $\cdot$ , avec la variable non-définie remplacée par $\cdot\cdot$.

### Exemple
$$(x \mapsto x^2)(2) = 2^2$$