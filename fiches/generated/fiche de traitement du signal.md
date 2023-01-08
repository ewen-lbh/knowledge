# fiche de traitement du signal

## transformée de Fourrier

On prend $p \in \mathcal{L}^2$ (ou $p \in \mathcal{L}^1$, c'est _plus simple_)
Formule directe
$$
\mathcal{F}[p](f) := \int_\mathbb{R} e^{-j2\pi f t} p(t) \mathrm{d}t
$$
[[transformée de Fourrier inverse|Formule inverse]]
$$
\mathcal{F^{-1}}[P](t) := \int_\mathbb{R} e^{j2\pi f t} P(f) \mathrm{d}f
$$

[3b1b](https://youtube.com/watch?v=spUNpyF58BY)


### [[dérivée|Dérivation]]

$$
 \mathcal{F}[x^{(n)}](f) = (j2\pi f)^n \mathcal{F}[x](f)
$$

### Propriétés
$\mathcal{F}$ est

- linéaire
- conserve la parité
- **transformation** $\mathcal{F}[x(t-t_0)](f) = e^{-2\pi j f t_0} X(f)$
- **modulation** $\mathcal{F}[x(t)e^{j2\pi f_0 t}] = X(f-f_0)$
- **similitude** $\mathcal{F}[x(at)](f) = \frac{1}{|a|} X(\frac{f}{a})$

en gros translation en temps $\iff$ multiplication par exp(...) en fréquence


### Transformées usuelles

| Temporel | Fréquentiel |
| ------------ | ------------------------------- |
| $x^\ast$ | $X^\ast \circ (-\operatorname{id})$
|$x \circ (a \operatorname{id} + b)$ | $\frac{1}{|a|} X(\frac{a}{f}) e^{j2\pi \frac{b}{a} f}$ |




## transformée de Fourrier inverse

#signal

Avec $X$ dans $L^1$ ou $L^2$

$$
\int_\mathbb{R} e^{j2\pi ft} X(f) \mathrm{d}f
$$

## produit de convolution

#signal
Opérateur défini par

$$
f \ast g = \int_{-\infty}^{+\infty} g(t-\tau) f(\tau) \mathrm{d}\tau
$$

### Propriétés

- Avec la [[transformée de Fourrier]]: 
	- $\mathcal{F}[f \ast g] = \mathcal{F}[f]\cdot \mathcal{F}[g]$
	- $\mathcal{F}[f\cdot g] = \mathcal{F}[f] \ast \mathcal{F}[g]$

- $\mathcal{F}[\text{carré}] = \text{sinc}$

- [[égalité de Parseval]]

### Avec l'[[impulsion de Dirac]]
- **localisation** $x(t)\delta(t-t_0) = x(t_0)\delta(t-t_0)$
- produit de convolution $x(t)\ast \delta(t-t_0) = x(t-t_0)$
- $x(t_0) = \int_\mathbb{R} x(t) \delta(t-t_0) \mathrm{d}t$


### Convolution par la [[réponse impulsionnelle]] d'un [[filtre]]

#### Propriétés

Soit $h$ la réponse impulsionnelle d'un filtre. L'opération $T = x \mapsto x \ast h$ est:

- Linéaire
- Invariante dans le temps $$\forall t_0, t \in \mathbb{R}, T[x](t) = T[x](t-t_0)$$
- Stable (BIBO)
   Si $x$ est borné alors $T[x]$ est borné, ou de manière équivalente (CNS) $$\int_\mathbb{R} |h| < \infty$$
- Le spectre du signal est "limité"



## impulsion de Dirac

#signal 

$\delta$ tel que

- $\int_{-\infty}^0 \delta = 0$
- $\int_{0}^{+\infty} \delta = 1$

### [[transformée de Fourrier]]

- $\mathcal{F}(\delta) = 1$
- $\mathcal{F}(1) = \delta$
- $\mathcal{F}(\delta(t-t_0)) = \operatorname{exp}(-j2 \pi ft_0)$ (et pareil dans l'autre sens)

### Propriétés

- [[série de Fourier]]: $$
\sum_{n\in \mathbb{Z}} c_n e^{+j2\pi n f_0 t} = \sum_{n\in \mathbb{Z}} c_n \delta(f-nf_0)
$$



## signal déterministe à énergie finie

#signal 

### Définition

Un [[signal]] [[signal déterministe|déterministe]] à [[énergie d'un signal|énergie]] [[fini|finie]]

### Énergie

$$
E(x) = \int_\mathbb{R} | x |^2 = \int_\mathbb{R} |\mathcal{F}[X]|^2 
$$

### Produit scalaire

$$
\langle x, y \rangle = \int_\mathbb{R} x y^\ast
$$

### [[densité spectrale d'énergie]]

$$
s_x(f) = |\mathcal{F}[x](f)|^2
$$



## signal déterministe périodique à puissance finie

### Définition

Un [[signal]] [[signal déterministe]] [[périodique]] à [[énergie d'un signal|puissance]] [[fini|finie]].

### Puissance

Soit $x$ un signal déterministe périodique à puissance finie de [[période]] $T$

$$
P(x) = \frac{1}{T} \int^{-T/2}_{T/2} |x|^2
$$

### [[produit scalaire|Produit scalaire]]

$$
\langle x, y \rangle = \frac{1}{T} \int^{-T/2}_{T/2} x y^\ast
$$

### [[densité spectrale d'énergie|densité spectrale de puissance]]

Soit $x(t) = \displaystyle\sum_{k\in \mathbb{Z}} c_k \exp(j2\pi k f_0 t)$
Alors:
$$
s_x(f) = \sum_{k\in \mathbb{Z}} |c_k|^2 \delta(f - kf_0)
$$

## signal déterministe non périodique à puissance finie

### Définition

Un [[signal]] [[signal déterministe|déterministe]] non-[[périodique]] à [[énergie d'un signal|puissance]] [[fini|finie]]

### Puissance

$$
P(x) = \lim_{T\to \infty} \frac{1}{T} \int^{-T/2}_{T/2} |x|^2
$$

### [[produit scalaire|Produit scalaire]]

$$
\langle x, y\rangle = \lim_{T\to \infty} \frac{1}{T} \int^{-T/2}_{T/2} xy^\ast
$$

### [[densité spectrale d'énergie|densité spectrale de puissance]]

$$
s_x(f) = \lim_{T\to \infty} \frac{1}{T} \left| \int^{-T/2}_{T/2} x(t) e^{-j2\pi ft} \mathrm{d}t \right|^2
$$

## signal aléatoire stationnaire

### Définition

Un [[signal]] non-[[signal déterministe|déterministe]] [[stationnarité|stationnaire]]. Il est défini par une [[variable aléatoire]] au lieu d'une fonction du temps.

- La [[espérance|moyenne]] ne dépend pas de $t$
- Le [[moment d'ordre 2]] $E(t\mapsto x(t) x^\ast(t-\tau))$ ne dépend pas de $t$

### [[produit scalaire]]

$$
\langle x, y \rangle = E(xy^\ast)
$$
### [[énergie d'un signal|puissance]] moyenne

$$
P(x) = E(|x|^2)
$$
### [[densité spectrale d'énergie|densité spectrale de puissance]]

**Si $X = \mathcal{F}[x]$ existe**:

$$
s_x(f) = \lim_{T\to \infty} \frac{1}{T} E\left( \left| \int^{-T/2}_{T/2} X(f) e^{-j2\pi ft} \mathrm{d}t \right|^2 \right)
$$


### Espérance d'un signal [[filtre|filtré]]

$$
E(H \cdot X) = H(0) \cdot E(X)
$$
 

## densité spectrale d'énergie

Pour n'importe quel [[signal]], c'est la [[transformée de Fourrier]] de l'[[autocorrélation]]:
$$
s_x = \mathcal{F}[R_x]
$$

Il y a aussi une caractérisation qui diffère selon la [[classes de signaux|classe du signal]].

### Propriétés

- **positive** $s_x \geq 0$
- **réelle** $s_x \in \mathbb{R}^\mathbb{R}$
- **parité** si $x$ réel, $s_x$ [[parité d'une fonction|paire]]

### Lien avec l'[[énergie d'un signal]]

$$
\int_\mathbb{R} s_x = E(x)
$$

### Du signal [[filtre|filtré]]

Voir les [[relations de Wiener-Lee]]

### Lien avec les probabilités

S'apparente à la [[densité de probabilité]]: c'est la répartition de l'énergie en fonction des fréquences

## intercorrélation

Pour deux [[signal|signaux]] $x$ et $y$ de même [[classes de signaux|classe]]

$$
R_{xy}(\tau) = \left\langle x, y(\cdot-\tau)\right\rangle$$
Avec $\langle \cdot, \cdot\cdot \rangle$ dépendant de la classe des signaux

### Du signal [[filtre|filtré]]

Voir les [[relations de Wiener-Lee]]

## autocorrélation

Cas particulier de l'[[intercorrélation]]

$$
R_x(\tau) = R_{xx}(\tau)
$$

### Du signal [[filtre|filtré]]

Voir les [[relations de Wiener-Lee]]

### Symétrie Hermitienne

$$
R_x^\ast(-\tau) = R_x(\tau)
$$

### Valeur maximale

$$
|R_x(\tau)| \leq R_x(0)
$$

### Distance entre $x(t)$ et $x(t-\tau)$

$$
d(x(t), x(t-\tau)) = \sqrt{ 2\Big[R_x(0) - R_x(\tau)\Big] }
$$

### Décomposition de Lebesgue

On peut quasiment tout le temps décomposer l'autocorrélation en une somme d'une fonction $\xrightarrow[\tau \to \infty]{} 0$ et d'une somme de fonctions [[périodique|périodiques]]

## signal bruit

### Bruit blanc

[[signal aléatoire stationnaire]] tel que 
$$
\begin{cases}
R_x &= \frac{N_0}{2} \delta \\
s_x &= \frac{N_0}{2}
\end{cases}
$$

### Bruit gaussien

## réalisabilité d'un filtre

### Définition

#### Domaine temporel

Un filtre de [[réponse impulsionnelle]] $h$ est dit _réalisable_ si et seulement si:

1. $h$ est réelle
2. $h \in L^1$ (stabilité)
3. $h$ est [[réponse impulsionnelle causale|causale]]

#### Domaine fréquentiel

1. $H$ vérifie la [[symétrie Hermitienne]]
2. ne peut se traduire
3. $H = -jH \ast \frac{1}{\pi \operatorname{id}}$

## relation de filtrage linéaire

#signal 

#### [[signal déterministe]]

$$
Y = X \cdot H
$$
#### [[signal aléatoire stationnaire]]: isométrie fondamentale

TODO diapo 36 c'est quoi $\stackrel{I}{\leftrightarrow}$ ?

## relations de Wiener-Lee

#signal 

On pose $x$ un [[signal]] et $h$ la [[réponse impulsionnelle]] d'un [[filtre]].

### Sur la [[densité spectrale d'énergie]]

$$
s_{x * h} = |H|^2 \cdot s_x
$$
### Sur l'[[intercorrélation]]

$$
R_{x\ast h,\ x} = R_x \ast h
$$
### Sur l'[[autocorrélation]]

$$
R_{x\ast h}(\tau) = R_x(\tau) \ast h(\tau) \ast h^\ast(-\tau)
$$


## quantificateur de signal

Une [[transformation non-linéaire d'un signal]] avec 
$$
y(t) = i(t) \Delta q_{i(t)}
$$

Avec:

- $i(t)$ l'indice de l'échantillon le plus proche temporellement de $t$
- $\Delta q_{i(t)}$ tel que $$
	x(t) \in x_{i(t)} + \frac{1}{2} \left[ -\Delta q_{i(t)}, +\Delta q_{i(t)} \right]
$$
### Quantification uniforme
Quand $\Delta q_{i(t)}$ ne dépend pas de $t$ (donc ni de $i$):

$$
\Delta q_{i(t)} = \Delta q =  \frac{2 \max x}{2^\text{bits}}
$$
### Erreur de quantification
On suppose que l'erreur $\varepsilon$ suit $\mathcal{U}([ -\Delta q, +\Delta q ]/2)$.

#### SNR

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



## transformation non-linéaire d'un signal

Sorte de "filtre" mais sans [[relation de filtrage linéaire]], la sortie l'image d'une [[fonction]] quelconque de l'entrée:

$$
y = g(x)
$$

### Exemples

- [[quadrateur]]
- [[quantificateur de signal]]

## théorème de Price

#signal 

### Énoncé

Soit $(X_1, X_2) \sim \mathcal{N}_2(m, \sigma^2)$ avec $m \neq 0$ et $g: \mathbb{R} \to \mathbb{R}$

$$
	\frac{\partial E(g(X_1) g(X_2))}{\partial E(X_1 X_2)} = E\left( \frac{\partial g(X_1)}{\partial X_1} \cdot \frac{\partial g(X_2)}{X_2}  \right)
$$

### Application au [[quadrateur]]

On a $y = x^2$.

On veut une expression de $R_y$ en fonction de $R_x$.

$$
\begin{align*}
\frac{\partial R_y}{\partial R_x}(\tau)  &= \frac{\partial \langle y, y(\cdot -\tau) \rangle }{\partial \langle x, x(\cdot -\tau) \rangle} \\
&= \frac{\partial E(x^2(t) x^2(t-\tau))}{\partial E(x(t) x(t-\tau))} \\
&= \frac{\partial E(g(x_1(t)) g(x_2(t)) )}{\partial E(x_1(t) x_2(t))} \quad \text{avec}\ x_1 = x,\ x_2 = x(\cdot - \tau) \text{ et } g = \operatorname{id}^2 \\
&= E\left( \frac{\partial x^2}{\partial x} \cdot \frac{\partial x(\cdot - \tau)^2}{\partial x(\cdot - \tau)} \right) \quad \text{d'après le théorème de Price} \\
&= E(4x(t)x(t-\tau)) \\
&= 4 E(x(t) x(t-\tau)) \\
&= 4 \langle x, x(\cdot - \tau) \rangle \\
&= 4 R_x(\tau)
\end{align*}
$$

On intègre:

$$
\begin{align*}
R_y(\tau) &= 2R_x(\tau)^2 + \text{const}
\end{align*}
$$

Pour trouver $\text{const}$, on évalue en $\tau = 0$:

$$
\begin{align*}
R_y(0) &= \langle y, y \rangle \\
&= E(yy^\ast) \\
&= E(|y|^2) \\
&= E(|x^2|^2) \\
&= E(x^4) \\
&= (3 \times 1) \sigma^4 \quad \text{moments d'une loi Gaussienne centrée} \\
&= 4\sigma^4 \\
\text{or} \quad R_y(0) &= 2R_x^2(0) + \text{const} \\
\text{donc} \quad \text{const} &= 4\sigma^4 - 2(R_x(0))^2 \\
&= 4\sigma^4 - 2E(|x|^2) \\
&= 4\sigma^4 - \sigma^2 \quad \text{si $|x| = x$ i.e. $x\geq 0$}
\end{align*}
$$

On peut aussi s'en tenir à $\text{const} = R^2_x(0)$




