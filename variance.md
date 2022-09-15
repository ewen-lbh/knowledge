# Variance
[[application]] associant une [[variable aléatoire]] X à une mesure de l'éparpillement des valeurs qu'elle prend. Définie comme l'[[espérance]] du [[carré]] de la [[différence]] entre X et son [[espérance]].

$$
V := X \mapsto E((X - E(X))^2)
$$

## Théorème de König-Huygens

$$
V(X) = E(X^2) - E(X)^2
$$

---

$$
\begin{align}

V(X) &= E((X - E(X))^2) \\
     &= E(X^2 - 2XE(X) + E(X)^2) \\
     &= E(X^2) - 2E(X)E(X) + E(X)^2 &\text{par linéarité de $E$}\\
     &= E(X^2) - E(X)^2
\end{align}$$
## Propriétés
### Variance d'une [[combinaison linéaire]]

$$
\begin{align}
V(aX+b) &= E((aX+b - aE(X)-b)^2) \\
&= a^2 E(X^2-2XE(X) + E(X)) \\
&= a^2 V(X)
\end{align}
$$