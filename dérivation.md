# Dérivation
Opérateur du [[type]] $(E \to F) \to E \to F$ agissant sur les fonctions [[dérivable|dérivables]] associant a une [[fonction]] $f$ la fonction donnant pour tout [[antécédent]] $a$ la [[limite]] du [[taux d'accroissement]] de $f$ en $a$.

$$
\cdot' := a \mapsto \lim_{t \to 0} \tau(a, \cdot)(a + t)
$$
## Exemple
$$
\begin{align}
(x\mapsto x^2)' &= a \mapsto \lim_{t\to 0} \tau(a, (x\mapsto x^2))(a + t) \\
&= a \mapsto \lim_{t \to 0} \frac{(a+t)^2 - a^2}{a + t - a} \\
&= a \mapsto \lim_{t \to 0} \frac{a^2 + 2at + t^2 - a^2}{t} \\
&= a \mapsto \lim_{t \to 0} 2a + t \\
&= a \mapsto 2a \\
\end{align}
$$


