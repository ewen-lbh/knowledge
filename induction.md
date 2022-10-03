# Induction
#modélisation 

C'est pas les plaques de cuisson
Faraday on t'oublie  :'(

### Exemple: définition des listes

Soit $A$ un ensemble

On définit $\operatorname{liste} A$ par *induction*:
- $\operatorname{Nil} \in \operatorname{liste} A$
- $\forall h \in A, \forall t \in \operatorname{liste} A, \operatorname{Cons}(h, t) \in \operatorname{liste} A$

Les correspondances avec [[Python]] sont les suivantes:
|  | |
|--|--|
 |$\operatorname{Nil}$ |  `[]`|
|$\operatorname{Cons}(h, t)$ | `[h] + t`|

#### append
##### Définition
$$
\begin{align*}
&\forall l \in \operatorname{liste} A, \operatorname{append}(\operatorname{Nil}, l) = l \\
&\forall x \in A, \forall (y, z) \in (\operatorname{liste} A)^2, \operatorname{append}(\operatorname{Cons}(x, y), z) = \operatorname{Cons}(x, \operatorname{append}(y, z))
\end{align*}
$$
##### $\operatorname{append}(x, \operatorname{Nil})=x$

- $\operatorname{append}(\operatorname{Nil}, \operatorname{Nil}) = \operatorname{Nil}$
- $$
\begin{align*}
\forall h \in A, \forall t \in \operatorname{liste} A, \operatorname{append}(\operatorname{Cons}(h, t), \operatorname{Nil}) &= \operatorname{Cons}(h, \operatorname{append}(t, \operatorname{Nil}))\\
&= \operatorname{Cons}(h, t) \qquad \text{en supposant la propriété vraie sur $t$}
\end{align*}
$$

##### associativité de $\operatorname{append}$

- $\operatorname{append}(\operatorname{Nil}, \operatorname{append}(y, z)) = \operatorname{append}(y, z) = \operatorname{append}(\operatorname{append}(y, z), \operatorname{Nil})$
- $$\begin{align*}
\forall h \in A, \forall t \in \operatorname{liste} A, \\
\operatorname{append}(\operatorname{Cons}(h, t), \operatorname{append}(y, z)) &= \operatorname{Cons}(h, \operatorname{append}(t, \operatorname{append}(y, z))\\
&= \operatorname{Cons}(h, \operatorname{append}(\operatorname{append}(t, y), z))
\end{align*}$$

##### involutivité de $\operatorname{rev}$

- $\operatorname{rev}(\operatorname{rev}(\operatorname{Nil})) = \operatorname{rev}(\operatorname{Nil}) = \operatorname{Nil}$
- $$
\begin{align*}
\forall h \in A, \forall t \in \operatorname{liste} A, \operatorname{rev}(\operatorname{rev}(\operatorname{Cons}(h, t))) &= \operatorname{rev}( \operatorname{append}(\operatorname{Cons}(h, \operatorname{Nil})), \operatorname{rev}(t))\\
&= \operatorname{append}(\operatorname{rev(\operatorname{Cons}(h, \operatorname{Nil}))}, \operatorname{rev}(\operatorname{rev}(t)))\\
&= \operatorname{append}(\operatorname{append}(\operatorname{rev}(\operatorname{Nil}), \operatorname{Cons}(h, \operatorname{Nil})), t)\\
&= \operatorname{append}(\operatorname{append}(\operatorname{Nil}, \operatorname{Cons}(h, \operatorname{Nil})), t)\\
&= \operatorname{append}(\operatorname{Cons}(h, \operatorname{Nil}), t)\\
&= \operatorname{Cons}(h, \operatorname{append}(\operatorname{Nil}, t))\\
&= \operatorname{Cons}(h, t)
\end{align*}
$$

Avec le Lemme 
$$
\begin{align*}
\operatorname{rev}(\operatorname{append}(a, b)) = \operatorname{append}(\operatorname{rev}(b), \operatorname{rev}(a))
\end{align*}
$$

En effet,
$$\begin{align*}
\operatorname{rev}(\operatorname{append}(\operatorname{Cons}(h, t), b)) &= \operatorname{rev}(\operatorname{Cons}(h, \operatorname{append}(t, b)))\\
&= \operatorname{append}(\operatorname{rev}(\operatorname{append}(t, b)), \operatorname{Cons}(h, \operatorname{Nil}))\\
&= \operatorname{append}(\operatorname{append}(\operatorname{rev}(b), \operatorname{rev}(t)), \operatorname{Cons}(h, \operatorname{Nil}))\\
&= \operatorname{append}(\operatorname{rev}(b), \operatorname{append}(\operatorname{rev}(t), \operatorname{Cons}(h, \operatorname{Nil})))\\
&= \operatorname{append}(\operatorname{rev}(b), \operatorname{rev}(\operatorname{append}(\operatorname{rev}(\operatorname{Cons}(h, \operatorname{Nil})), \operatorname{rev}(\operatorname{rev}(t)))))\\
&= \operatorname{append}(\operatorname{rev}(b), \operatorname{rev}(\operatorname{append}(\operatorname{append}(\operatorname{rev}(\operatorname{Nil}), \operatorname{Cons}(h, \operatorname{Nil})), t)))\\
&= \operatorname{append}(\operatorname{rev}(b), \operatorname{rev}(\operatorname{append}( \operatorname{append}(\operatorname{Nil}, \operatorname{Cons}(h, \operatorname{Nil})), t )))\\
&= \operatorname{append}(\operatorname{rev}(b), \operatorname{rev}(\operatorname{append}(\operatorname{Cons}(h, \operatorname{Nil}), t)))\\
&= \operatorname{append}(\operatorname{rev}(b), \operatorname{rev}(\operatorname{Cons}(h, \operatorname{append}(\operatorname{Nil}, t))))\\
&= \operatorname{append}(\operatorname{rev}(b), \operatorname{rev}(\operatorname{Cons}(h, t)))
\end{align*}$$

