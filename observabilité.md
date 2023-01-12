#automatique 

Un système  $\begin{cases} \dot x &= Ax + Bu \\ y &= Cx + Du \end{cases}$ est *observable* si et seulement si l'état initial est calculable avec $u([0, \tau])$ et $y([0, \tau])$.

## Critère d'observabilité de Kalman

On a un système observable ssi 

$$
\operatorname{ker} \begin{pmatrix}
C \\ CA \\ \vdots \\ CA^{n-1}
\end{pmatrix} = \set{0}
$$
