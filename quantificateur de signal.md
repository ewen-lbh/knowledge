Une [[transformation non-linéaire d'un signal]] avec 
$$
y(t) = i(t) \Delta q_{i(t)}
$$

Avec:

- $i(t)$ l'indice de l'échantillon le plus proche temporellement de $t$
- $\Delta q_{i(t)}$ tel que $$
	x(t) \in x_{i(t)} + \frac{1}{2} \left[ -\Delta q_{i(t)}, +\Delta q_{i(t)} \right]
$$
## Quantification uniforme
Quand $\Delta q_{i(t)}$ ne dépend pas de $t$ (donc ni de $i$):

$$
\Delta q_{i(t)} = \Delta q =  \frac{2 \max x}{2^\text{bits}}
$$
## Erreur de quantification
On suppose que l'erreur $\varepsilon$ suit $\mathcal{U}([ -\Delta q, +\Delta q ]/2)$.

### SNR

$$
\begin{align*}
\operatorname{SNR}_{\text{dB}} &= 10 \log \frac{\sigma_x^2}{\sigma_\varepsilon^2} \\
&= 10 \log \frac{(\max x)^2 /2}{(\Delta q)^2 / 12} \\
&= 10 \log \left(  \frac{(\max x)^2}{2} \cdot \frac{12 \cdot 2^{\text{2bits}}}{4 (\max x)^2} \right) \\
&= 10 \log \left( \frac{12}{8}  2^{2\text{bits}} \right ) \\
&= 10 \log \frac{8}{12} + 10 \log 2^{2 \text{bits}} \\
&\stackrel{\text{approx?}}{=} 1.76 + 6\text{bits}
\end{align*}
$$

