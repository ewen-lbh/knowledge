# Liste
Objet

Définie par [[récurrence]] de la manière suivante:

- $[]$ est appelé la *liste vide*
- $[a_1]$ est une liste de longueur 1, et
	- $[a_1][0]$ vaut $a_1$.
- $[a_1, a_2]$ est une liste de longueur 2, et
	- $[a_1, a_2][0]$ vaut $a_1$
	- $[a_1, a_2][1]$ vaut $a_2$
- par récurrence, on a pour tout $n \in \mathbb{N}$:
	- $[a_1, \ldots, a_n]$ est une liste de longueur $n$, et
		- $\forall k \in \{0, \ldots, n-1\},\ [a_1, \ldots, a_n][k] := a_{k-1}$