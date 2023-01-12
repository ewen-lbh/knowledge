# Stabilité asymptotique
#automatique 

Propriété d'un [[point d'équilibre]], un point $x_e$ il est dit *asymptotiquement stable* si 

- il est [[stabilité d'un point|stable]]
- $\forall \varepsilon > 0, \exists \delta > 0, \|x_{0}- x_{e}\| < \delta \text{ et } t>0 \implies \| \phi(t, x_{0})- x_{e}\|< \varepsilon$

## Caractérisation par les [[valeur propre|valeurs propres]]

On a, pour le [[système différentiel]] $\begin{cases}\dot x = Ax \\ x(0) = x_0\end{cases}$ :
$$
\begin{align}
x_e \text{ asym. stable} &\iff \operatorname{Re} \operatorname{Sp} A < 0 \\
				&\iff \forall \lambda \in \operatorname{Sp} A \cap i\mathbb{R}, \operatorname{mult}_{\chi_A}(\lambda) = \operatorname{dim} E_\lambda(A)
\end{align}
$$

## Caractérisation par la [[trace]] et le [[déterminant]] de la [[matrice]] d'un système différentiel **[[linéaire]]**

Pour le système différentiel
$$
\begin{cases} \dot X(t) &= A X(t) \\ X(0) &= X_0 \end{cases}
$$

On a $$
\text{stabilité asymptotique} \iff \begin{cases} \operatorname{det} A &> 0 \\ \operatorname{tr} A &< 0 \end{cases}
$$
