# Équation différentielle

## Solution complète avec exponentielle de matrice

Pour le système différentiel
$$
\begin{cases}
 \dot X (t) &= AX(t) + Bu(t) \\
X(0) &= X_0
\end{cases}
$$
La solution est
$$
X(t) = e^{tA} X(0) + \int_0^t e^{(t-s)A} B u(s) \mathrm{d}s
$$
