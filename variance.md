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
