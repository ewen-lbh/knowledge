# Déduction naturelle
## Introductions

### Implication $I_\to$

Prouver $\psi$ sous les hypothèses $\Gamma$ et $\phi$ implique de prouver $\phi \implies \psi$ sous l'hypothèse $\Gamma$
$$
\frac{\Gamma, \phi \vdash \psi}{\Gamma\vdash\phi\to\psi} I_\to
$$
### Négation $I_\lnot$

Prouver l'[[absurde]] $\bot$ sous les hypothèses $\Gamma$ et $\phi$ implique de prouver $\lnot\phi$ sous l'hypothèse $\Gamma$

$$
\frac{\Gamma, \phi \vdash \bot}{\Gamma\vdash\lnot\phi}
$$
## Éliminations
### Négation $E_\lnot$
$$
\frac{\Gamma\vdash\phi,\lnot\phi}{\Gamma\vdash\bot}
$$
### Conjonction $E_\land^D$, $E_\land^G$

$$
\begin{matrix}
\frac{\Gamma\vdash A\land B}{\Gamma\vdash A} & \frac{\Gamma\vdash A\land B}{\Gamma\vdash B}
\end{matrix}
$$
### Disjonction $E_\lor^D$, $E_\lor^G$

