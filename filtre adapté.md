## Définition

[[filtre]] avec la [[fonction de transfert]] minimisant le [[rapport signal sur bruit]]

## Majoration du SNR

$$
\operatorname{SNR}[h, n, s](t_0) \leq \underbrace{\int_\mathbb{R} b \cdot b^\ast}_{\operatorname{SNR}^\max(t_0)}
$$
## Expression

Le filtre est adapté ssi:

$$
H(f) = k \frac{S^\ast(f)}{s_n(f)} e^{-j2\pi f t_0}
$$

Avec 
$$
\begin{align*}
k &= \frac{a}{b} > 0 \\
a &= \sqrt{s_n} \cdot H \\
b(f) &= \frac{S^\ast}{\sqrt{s_n}}(f) \cdot e^{-j2\pi f t_0}
\end{align*}
$$

## Preuve

On se sert de l'[[intégalité de Cauchy-Schwartz]]: il faut préparer l'expression du numérateur du [[rapport signal sur bruit]] pour avoir le carré d'un module de produit scalaire:

$$
 \left| \int_\mathbb{R} H(f) S(f) e^{j2\pi ft_0} \right|^2 = \left| \int_\mathbb{R} a \cdot b^\ast \right|^2
$$

…tel que le dénominateur soit une norme dans le produit des deux normes:

$$
\int_\mathbb{R} s_n \cdot |H|^2 = \int_\mathbb{R} a \cdot a^\ast
$$

1. On prend
   -  $a = H$ 
    - $S \cdot \exp(\ldots) = b^\ast$ 
1. D'où 
   - $b = S^\ast \cdot \exp(- \ldots)$
2. Il faut $a a^\ast = |H|^2 s_n$, donc on modifie:
   - $a = \sqrt{s_n} H$
3. Mais il faut quand même $a b^\ast = \ldots$, donc on modifie $b$:
   - $b = \frac{1}{\sqrt{s_n}} S^\ast \exp(-\ldots)$

L'inégalité de Cauchy-Schwartz s'écrit:

$$
\begin{align*}
| \langle a, b \rangle | &\leq \| a \| \| b \|\\
\iff \left| \int_\mathbb{R} a \cdot b^\ast \right| &\leq \sqrt{\int_\mathbb{R} a a^\ast} \sqrt{\int_\mathbb{R} bb^\ast} \\
\iff \left| \int_\mathbb{R} a \cdot b^\ast \right|^2 &\leq \sqrt{\int_\mathbb{R} a a^\ast}^2 \sqrt{\int_\mathbb{R} bb^\ast}^2\\
\iff \underbrace{\frac{|\int_\mathbb{R} a b^\ast |^2}{|\int_\mathbb{R} aa^\ast|}}_{\operatorname{SNR(t_0)}} &\leq \int_\mathbb{R} bb^\ast
\end{align*}
$$
Pour le $H$ minisant le SNR, on se sert du cas d'égalité:

$$
\operatorname{SNR}(t_0) = \int_\mathbb{R} b b^\ast \iff a = k \cdot b \quad \text{avec} \  k > 0
$$

## Exemple: le bruit blanc

On a $x = s + n$ et $n$ un [[signal bruit]] blanc.

$$
\begin{align*}
\operatorname{SNR}^\max(t_0) &= \int_\mathbb{R} bb^\ast \\
&= \int_\mathbb{R} \sqrt{s_n}^{-1} (\sqrt{s_n}^{-1})^\ast \cdot e^{-j2 \pi ft_0} e^{j2 \pi f t_0} \cdot S S^\ast \\
&= \int_\mathbb{R} \frac{1}{s_n} \cdot 1 \cdot |S|^2 \\
&= \frac{1}{s_n} \int |S|^2 \\
&= \frac{2E}{N_0} \quad \text{car $s_n = \frac{N_0}{2}$}
\end{align*}
$$