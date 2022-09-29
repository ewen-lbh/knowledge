# Stabilité asymptotique
#automatique 

Propriété d'un [[point d'équilibre]], un point $x_e$ il est dit *asymptotiquement stable* si 

- il est [[stabilité d'un point|stable]]
- $\forall \varepsilon > 0, \exists \delta > 0, \|x_{0}- x_{e}\| < \delta \text{ et } t>0 \implies \| \phi(t, x_{0})- x_{e}\|< \varepsilon$

## Caractérisation par les [[valeur propre|valeurs propres]]

On a, pour le système différentiel $\begin{cases}\dot x = Ax \\ x(0) = x_0\end{cases}$ :
$$
x_e \text{ asymptotiquement stable} \iff \operatorname{Re} \operatorname{Sp} A < 0
$$