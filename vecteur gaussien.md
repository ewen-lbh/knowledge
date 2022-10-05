# Vecteur gaussien
Généralisation d'une [[loi normale]] à plusieurs [[dimension|dimensions]].

$X = \begin{pmatrix}X_1 \\ \vdots \\ X_n \end{pmatrix} \sim \mathcal{N}_n(m, \Sigma)$ (avec $\Sigma$ une [[matrice]] [[symmétrique]] [[définie-positivité|définie-positive]]) ssi

$$
p(x) = \frac{1}{(2 \pi)^{\frac{n}{2}} \sqrt{\det \Sigma }} \exp \left( - \frac{1}{2}(x-m)^\top \Sigma^{-1}(x-m) \right)
$$
## Cas particulier où $\Sigma$ est [[diagonalisabilité|diagonalisable]]

On pose $\Sigma = \operatorname{diag}(\sigma_1^2, \ldots, \sigma_n^2)$

$$
\begin{align*}
p(x) = p(x_1, \ldots, x_n) &= \frac{1}{(2 \pi)^{\frac{n}{2}} \sqrt{\prod_{i=1}^n \sigma_i^2}} \exp \left( -\frac{1}{2} \begin{pmatrix}x_1 - m_1 & \cdots & x_n - m_n \end{pmatrix} \begin{pmatrix} 
\frac{1}{\sigma_1^2} \\ & \ddots \\ & & \frac{1}{\sigma_n^2} \end{pmatrix} \begin{pmatrix} x_1 - m_1 \\ \vdots \\ x_n - m_n \end{pmatrix}  \right)\\
&= \frac{1}{(2 \pi)^{\frac{n}{2}} \sqrt{\prod_{i=1}^n \sigma_i^2}} \exp \left( - \frac{1}{2}    \sum_{i=1}^n \left( \frac{x_i - m_i}{\sigma_i} \right)^2  \right)\\
&= \prod_{i=1}^n \frac{1}{\sqrt{2 \pi \sigma_i^2}} \exp \left( - \frac{1}{2} \frac{(x_i-m_i)^2}{\sigma_i^2} \right)\\
&= \prod_{i=1}^n p(\cdot, \ldots, x_i, \ldots, \cdot)
\end{align*}
$$

## Exercices

### Loi de $(X, Y)$ avec $p(x, y) \propto \exp\left(-x^2 - \frac{3}{2}y^2 - xy + 4x + 7y\right)$

1. Factoriser par $-\frac{1}{2}$ pour identifier
2. On développe l'expr d'une $\mathcal{N}_2$:
   $$
   \begin{align*}
p(x, y) &= \underbrace{\frac{1}{2 \pi \sqrt{\det \Sigma}}}_{K} \exp \left[ - \frac{1}{2} \left( \begin{pmatrix}x\\y\end{pmatrix} - \begin{pmatrix}m_1 \\ m_2\end{pmatrix} \right)^\top \begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{12} & \Sigma_{22} \end{pmatrix} \left(\begin{pmatrix}x\\y\end{pmatrix} - \begin{pmatrix}m_1 \\ m_2\end{pmatrix}\right)  \right]\\
&= K \exp \left[ - \frac{1}{2} \left( (x-m_1)^2\Sigma_{11} + 2(y-m_1)(x-m_2) \Sigma_{12} + (y-m_2)^2 \Sigma_{22} \right)  \right]\\
&= K \exp \left[ - \frac{1}{2} ( \Sigma_{11} x^2 + \Sigma_{22} y^2 + 2 \Sigma_{12} xy - (-2m_1 \Sigma_{11} - 2 m_2 \Sigma_{12}) x + (-2m_2 \Sigma_{22} - 2 m_1 \Sigma_{12})y + \underbrace{c}_\text{on le met dans $K$} )  \right]\\
\end{align*}
$$

On identifie:$$\begin{cases} \Sigma_{11} &= 2 \\ \Sigma_{22} &= 3 \\ \Sigma_{12} &= 1  \\
-8 &= 2 m_1 \Sigma_{11} - 2 m_2 \Sigma_{12}  \\
 -14 &= -2m_2 \Sigma_{22} - 2 m_1 \Sigma_{12} 
 \end{cases} \text{ie} \begin{cases}
 \Sigma_{11} &= 2  \\
\Sigma_{22} &= 3  \\
\Sigma_{12} &= 1 \\
m_1 &= 1  \\
m_2 &= 2
 \end{cases} $$
Ainsi $\Sigma = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$ et donc $\Sigma^{-1} =  \frac{1}{5} \begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}$ et donc

$$
(X, Y) \sim \mathcal{N}_2\left( \begin{pmatrix}1 \\ 2\end{pmatrix}, \begin{pmatrix}\frac{3}{5} & - \frac{1}{5} \\ - \frac{1}{3} & \frac{2}{5}\end{pmatrix} \right)
$$
(On vérif pas le coef de proportionnalité devant pour être sur que c'est une $\mathcal{N}_2$ mais c'est implicite, on diviserait $p(x, y)$ par ce qu'il faut pour que ça en devienne une)

## Cas [[bivarié]] ($n=2$)

On pose la [[fonction caractéristique]]

$$
\phi(u) = \exp \left(i(u_1 m_1 + u_2 m2) - \frac{1}{2} \Sigma_{11} u_1^2 - \frac{1}{2} \Sigma_{22} u_2^2 - \Sigma_{12} u_1 u_2\right) 
$$
- $\frac{\partial \phi(u)}{\partial u_1}|_{u=0} = im_1$
- $\frac{\partial \phi(u)}{\partial u_2}|_{u=0}= im_2$
- $\frac{\partial^2 \phi(u)}{\partial u_1 \partial u_2}|_{u=0} = -m_1 m_2 - \Sigma_{12}$

## Transformation [[affine]]

- $X \sim \mathcal{N}_n(m, \Sigma)$
- $Y = AX + b$, $A \in \mathcal{M}_{p,n }(\mathbb{R}), b \in \mathbb{R}^p$

$$
\begin{align*}
\theta_Y(v) &= E[\exp(v^\top Y)]\\
&= E[\exp(v^\top (AX+b))]\\
&= E[e^{v^\top AX} e^b]\\
&= e^{v^\top b} E[e^{(A^\top v)^\top X}]\\
&= e^{v^\top b} \theta_X(A^\top v)\\
&= e^{v^\top b} \exp\left((A^\top v)^\top m + \frac{1}{2} (A^\top v)^\top \Sigma A^\top v\right)\\
&= \exp\left(v^\top(Am + b) + \frac{1}{2} v^\top(A \Sigma A^\top )v\right)\\
\end{align*}
$$

Donc: 
$$
AX + b \sim \mathcal{N}_n(Am+b, A \Sigma A^\top)
$$

## [[Loi marginale]]

- $X = \begin{pmatrix}X' \\ X''\end{pmatrix} \sim \mathcal{N}_n(m, \Sigma)$
- $m = \begin{pmatrix}m' \\ m''\end{pmatrix}$
- $\Sigma= \begin{pmatrix} \Sigma' & M \\ M^\top & \Sigma'' \end{pmatrix}$

$$
\begin{align*}
X' &= \underbrace{\begin{pmatrix} I_p \sqcup 0_{n-p, p} \end{pmatrix}}_A \begin{pmatrix}X' \\ X''\end{pmatrix} + \underbrace{\begin{pmatrix}0 \\ 0\end{pmatrix}}_b
\end{align*}
$$

$$
A =  \begin{pmatrix} & & | & & \\ & I_p & | & 0_{n-p, p} & \\ & & |  \end{pmatrix} =  \underbrace{\begin{pmatrix} 
1 & 0 & \cdots & 0 & | & 0 & \cdots & 0  \\ 
0 & 1 & \cdots & 0 & | & 0 & \cdots & 0  \\ 
0 & 0 & \ddots & 0 & | & 0 & \cdots & 0  \\ 
0 & 0 & \cdots & 1 & | & 0 & \cdots & 0 \\
\end{pmatrix}}_{p \qquad \qquad \qquad n-p}
$$

Donc
$$
\begin{align*}
X' &\sim \mathcal{N}_n( Am+b, A \Sigma A^\top )\\
&\sim \mathcal{N}_n(  )
\end{align*}
$$


### [[Indépendance]]

$$X' \coprod X'' \iff M = 0$$

#### Preuve
$$\begin{align*}
X' \coprod X'' &\iff \phi_{X'}(u) \phi_{X''}(u); u = \begin{pmatrix}u' \\ u''\end{pmatrix} \\
&\iff \exp\left(iu^\top m' - \frac{1}{2} u'^\top \Sigma' u'\right)\exp \left(iu''^\top m'' - \frac{1}{2} u''^\top \Sigma'' u''\right)= \exp\left(iu^\top m - \frac{1}{2} u^\top \Sigma u\right)\\
&\iff u'^\top \Sigma' u' + u''^\top \Sigma'' u'' = u^\top \Sigma u\\
&\iff u'^\top M u'' + u''^\top M u' = 0 \\
&\iff u'^\top M u'' + (u''^\top M u')^\top = 0 \\
&\iff M = 0
\end{align*}$$


## Théorème de Cochran

- $X \sim \mathcal{N}_n(m, \sigma^2 I_n)$ ($m\in \mathbb{R}^n, \sigma^2 > 0$)
- $E_1 \stackrel{\bot}{\oplus} \cdots \stackrel{\bot}{\oplus} E_n = \mathbb{R}^n$
voir slides

## Statistiques des échantillons Gaussiens

voir slides
