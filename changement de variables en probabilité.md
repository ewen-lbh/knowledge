$$
\begin{align}
P[Y=l^2] &= P[(X-2)^2=l^2] \\
&= P[X-2=l \cup X-2=-l] \\
&= \begin{cases}
 P[X=2]  & \text{si } l = 0 \\
 P[X=l+2] + \underbrace{P[X\leq 1]}_\text{= 0} & \text{si } l \geq 3 \\
 P[X=1]+P[X=3] & \text{si } l = 1 \\
 P[X=0] + P[X=4] &\text{si } l = 2
\end{cases}
\end{align}
$$

## Changement de variable continue

Si $X$ v.a. continue à valeurs dans un ouvert $O_X \subset \mathbb{R}$ et $g: O_X \to O_Y$ ($O_Y$ ouvert également) bijective de réciproque continue,

$$
p_Y = p_X \circ g^{-1} \cdot \left| \frac{dx}{dy} \right|
$$

### Exemples
#### Avec la [[loi exponentielle]]
avec $X \sim \mathcal{E}(1)$  (donc $p = x\mapsto e^{-x}$, c'est la [[loi exponentielle]]) et $g = x \mapsto 1/x$:

- $g$ est bijective de $\mathbb{R}_+^\ast$ dans $\mathbb{R}_+^\ast$
- $dx/dy = -\frac{1}{y^2}$
- $$ p_Y(t) = \frac{p_X(g^{-1}(t))}{t^2} = \frac{e^{-\frac{1}{y}}}{y^2} $$
#### Avec la [[loi normale]]
On a $X\sim \mathcal{N}(m, \sigma^2)$ et $g = a\operatorname{id} + b$ avec $a \neq 0$.

- $g$ est bijective de $\mathbb{R}$ dans $\mathbb{R}$
- $dx/dy = 1/a$
- $$ \begin{align}
p_Y(t) &= p_X(g^{-1}(y)) |dx/dy| \\ &= \frac{1}{|a|\sqrt{2\pi\sigma^2}} \exp\left( -\frac{(\frac{y-b}{a}-m)^2}{2\sigma^2} \right) \\ &= \frac{1}{\sqrt{2\pi\sigma^2a^2}} \exp\left( -\frac{(\frac{y-b}{a}-m)^2}{2\sigma^2} \right) \\
&= \frac{1}{\sqrt{2\pi\sigma^2a^2}} \exp\left( - \frac{(y-(b+am))^2}{2a^2\sigma^2} \right)
\end{align}
$$
**Donc $Y \sim \mathcal{N}(am+b, (a\sigma)^2)$** (on retrouve les propriétés sur $V$ et $E$.)

### Preuve

On a $P(X\in[x, x+dx]) = P(Y\in[y, y+dy])$
$$
\begin{align}
P(X \in [x, x+dx]) &= \int_x^{x+dx} p_X \\
&= \int_{-\infty}^{x+dx} p_X - \int_{-\infty}^{x} p_X 
 \\
&= F(x+dx) - F(x)
\end{align} 

$$

Avec $F$ la [[fonction de répartition]]

Et
$$
\begin{align}
\frac{P(X\in[x,x+dx])}{dx} &= F'(x) = p_X(x)
\end{align}
$$

Donc

$$
p_X(x)dx = \pm p_Y(y)dy
$$
(on a un $-$ si $g$ est décroissante car $y+dy$ sera en dessous du $y$)

Enfin:

$$
p_Y = p_X \circ g^{-1} \cdot \left| \frac{dx}{dy} \right|
$$

## Cas de la bijectivité par morceaux

On ajoute la contribution de chaque bijection sur chaque morceau

### Exemple

$X \sim \mathcal{N}(0, 1)$ et $g = \operatorname{id}^2$.

- $g$ est bijective par morceaux: $g^{-1} = -\sqrt{}$ sur $\mathbb{R}^-$ et $\sqrt{}$ sur $\mathbb{R}^+$.
- 1<sup>re</sup> bijection sur $\mathbb{R}_-^\ast$.
	- $dx/dy = -\frac{1}{2\sqrt{y}}$
	- $q_1(y) = p_X(g^{-1}(y)) |dx/dy| = \frac{1}{\sqrt{2\pi}} \exp \left(- \frac{y^2}{2}  \right) \frac{1}{2\sqrt{y}} = \frac{1}{2\sqrt{2\pi y}}\exp \left( -\frac{y}{2}\right)$
- 2<sup>e</sup> bijection sur $\mathbb{R}_+^\ast$.
	- $dx/dy = \frac{1}{2\sqrt{y}}$
	- $q_2(y) = p_X(g^{-1}(y)) |dx/dy| = \frac{1}{\sqrt{2\pi}} \exp \left(- \frac{y^2}{2}  \right) \frac{1}{2\sqrt{y}} = \frac{1}{2\sqrt{2\pi y}}\exp \left( -\frac{y}{2}\right)$
- Somme des contributions: $p_Y = q_1 + q_2 = x\mapsto \frac{1}{\sqrt{2\pi y}}\exp\left( -\frac{y}{2} \right)$
(donc $Y \sim \chi^2_1$) ($\mathbb{TRIVIAL}$)