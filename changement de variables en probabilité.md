# Changement de variables
**En probabilités**

## Exemple

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

## Changement de variable continue dans $\mathbb{R}$

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

## Changement de variables continues dans $\mathbb{R}^2$

### Pour $g$ bijective

On a 

$$
p_{U, V}(u, v) = p_{X, Y}(g^{-1}(u, v)) |\operatorname{det} J|
$$

#### Exemples

- $X, Y\sim \mathcal{U}(0, 1)$
- $\begin{cases}U &= X+Y \\ V &= X \end{cases}$
1. $g = (x, y) \mapsto (x+y, x)$ est bijectif, de réciproque $g^{-1} = (u, v) \mapsto (u-v, u)$
2. *Calcul de la [[jacobienne]]*: $$
\begin{align*}
J &= \begin{pmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \ldots \end{pmatrix} \\
&= \begin{pmatrix}0 & 1\\
1  & -1\end{pmatrix}
\end{align*}
$$

3. Calcul de $p_{U, V}$

$$
\begin{align*}
p_{U, V}(u, v) &= p_{X, Y}(g^{-1}(u, v)) |\operatorname{det} J| \\
&= 1 \cdot |-1| \\
&= 1
\end{align*}
$$

4. Domaine de définition

$$
\begin{align*}
\begin{cases} 
0 < x < 1 \\
0 < y < 1
\end{cases} &\iff \begin{cases} 0 < v < 1  \\
0 < u-v < 1 \end{cases} \\
&\iff \begin{cases} 0 < v < 1 \\ v < u < v+1 \end{cases}
\end{align*}
$$

- $X, Y \sim \mathcal{N}(0, 1)$
- Loi de $(R, \Theta)$ avec $X = R \cos \Theta$ et $Y = R \sin \Theta$ ?

1. Un ptit dessin

![[Pasted image 20220928145549.png]]

2. On a une jijection de $\mathbb{R}^2 \setminus 0_{x^+} \to ]0, +\infty[ \times ]0, 2 \pi[$
Avec $0_{x^+} = [0, +\infty[ \times \mathbb{R}$.

3. La jacobienne

$$
\begin{align*}
J &= \begin{pmatrix} \frac{\partial x}{\partial r} & \frac{\partial x}{\partial \theta} \\ \frac{\partial y}{\partial r} & \frac{\partial y}{\partial \theta} \end{pmatrix}\\
&= \begin{pmatrix}\cos \theta & -r\sin \theta \\ \sin \theta & r\cos \theta \end{pmatrix}
\end{align*}
$$

4. Densité

- $$
\begin{align*}
p_{X, Y}(x, y) &= p(x, \cdot) \cdot p(\cdot, y) \\
	&= \frac{1}{\sqrt{2 \pi}} e^{-\frac{x^2}{2}} \frac{1}{\sqrt{2 \pi}} e^{-\frac{y^2}{2}}\\
	&= \frac{1}{\sqrt{2 \pi}} e^{- \frac{1}{2}(x^2 + y^2)}\\
\end{align*}
$$
- $$
\begin{align*}
p_{R, \Theta}(r, \theta) &= p_{X, Y}(g^{-1}(r, \theta)) |\operatorname{det} J| \\
&= p_{X, Y}(r \cos \theta, r \sin \theta) | \cos \theta \cdot r \cos \theta - \sin \theta \cdot (-r \sin \theta) |\\
&= \frac{1}{2 \pi} e^{- \frac{1}{2} r^2 (\cos^2 \theta + \sin^2 \theta)} |r \cos^2 \theta + r \sin^2 \theta |\\
		&= \frac{1}{2 \pi} e^{- \frac{1}{2}r^2} r
\end{align*}
$$

4. Domaine de définition: $]0, +\infty[ \times ]0, 2 \pi[$

²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²ooooooooooooooooooooooooooooooooooo²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²h²²²²²²²²²²²²²²²²²²²²²h²hh²hhhhh

## Changement continu de $\mathbb{R}^2$ dans $\mathbb{R}$

- $X, Y \sim \mathcal{U}(0, 1)$
- Loi de $U = X+Y$ ?

1. Changement de variable $\begin{pmatrix}X\\ Y\end{pmatrix} \mapsto \begin{pmatrix} U = X+Y \\ V =X \end{pmatrix}$
D'après l'exemple précédent, la densité est  $q = \mathbf{1}_{\mathcal{D}}$ 
![[Pasted image 20220928151804.png]]

On veut la loi marginale de $U$ : $q(u, \cdot) = \int_\mathbb{R} q(u, v) \mathrm{d}v$

Si $u < 0$ ou $u > 2$, $q(u, \cdot) = 0$.

Sinon, si $u \in ]0, 1[$:

$$
\begin{align*}
q(u, \cdot) &= \int_0^u 1 \mathrm{d}v \\
&= u
\end{align*}
$$

Si $u \in [1, 2[$

$$
\begin{align*}
q(u, \cdot) &= \int_{u-1}^1 1 \mathrm{d}v \\
&= 1 - (u-1)\\
&= 2-u
\end{align*}
$$


Et la [[fonction de répartition]]:

![[Pasted image 20220928153638.png]]

$$
\begin{align*}
F(u) &= P(U<u) \\
&=P(X+Y<u) \\
&= \begin{cases}
0 &\text{si $u \le 0$}\\
\frac{u^2}{2} &\text{si $u \in ]0, 1[$}\\
\frac{u^2}{2} - 2 \frac{(u-1)^2}{2} = \dots = - \frac{u^2}{2} + 2u - 1 &\text{si $u \in [1, 2[$}\\
1 &\text{sinon}
\end{cases}
\end{align*}
$$

- $X \sim \mathcal{N}(m_1, \sigma_1^2)$
- $Y \sim \mathcal{N}(m_2, \sigma_2^2)$
- Loi de $U = X+Y$

La [[fonction caractéristique]] de la [[somme]] est
$$
\begin{align*}
\phi_U(t) &= E[e^{itu}]\\
&= E[e^{itX}] E[e^{itY}] \\
&= \phi_X(t) \phi_Y(t)\\
	&= \operatorname{exp}\left(im_1 t - \frac{\sigma_1^2}{2} t^2\right)\cdot\operatorname{exp}(im_2 t - \frac{\sigma_2^2}{2} t^2)\\
&= \operatorname{exp}(i(m_1 + m_2)t - \frac{\sigma_1^2 + \sigma_2^2}{2} t^2)\\
	\text{donc}\quad U &\sim \mathcal{N}(m_1 + m_2, \sigma_1^2 + \sigma_2^2)
\end{align*}
$$

