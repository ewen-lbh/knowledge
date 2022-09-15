# Recherche dichotomique d'une racine
Méthode numérique pour la recherche d'une [[racine]] d'une [[fonction]]

## Principe
On cherche une racine d'une fonction $f$ dans un [[segment]] donné $[a, b]$.
- On pose $x = \frac{b-a}{2}$.
- Tant que $|f(x)|$ est supérieure à un [[seuil d'erreur]] donné:
	- On pose $x = \frac{b-a}{2}$
	- Si $f(a)$ est du même signe que $f(x)$, alors la racine ne se trouve pas dans le segment $[a, x]$. 
		- On réduit donc l'intervalle de recherche à $[x, b]$ en posant $a = x$
	- Sinon, réciproquement:
		- On réduit l'intervalle de recherche à $[a, x]$ en posant $b = x$

## Implémentation
En [[Python]]
