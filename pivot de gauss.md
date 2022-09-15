# Pivot de Gauss
[[algorithme]] de résolution d'un [[système de Cramer]].

## Principe
L'algorithme se décompose en trois parties

### La descente
Permet de rendre la [[matrice]] [[triangulaire]] supérieure en annulant les [[coefficient|coefficients]] inférieurs à la [[diagonale]].

- Pour chaque [[colonne]] $j$ exceptée la dernière
	- On cherche le coefficient le [[maximum|plus grand]] en [[module]] dans ceux en dessous la diagonale (y compris celui de la diagonale). Ce coefficient est appelé *pivot*.
	- On permute la [[ligne]] contenant ce coefficient avec celle de la diagonale
	- On répercute les changement en [[permutation|permutant]] également les deux lignes sur le vecteur second membre
	- Pour chaque coefficient $a_{ij}$ en dessous de la diagonale (sauf celui sur la diagonale)
		- On [[soustraction|soustrait]] à la ligne $L_i$ un [[multiple]] de la ligne $L_j$ (qui contient donc le pivot) afin d'annuler cette ligne: $$L_i \leftarrow L_i - \frac{a_{ij}}{a_{jj}} L_j$$

		- On répercute les chagements en effectuant la même [[transvection]] sur le vecteur second membre: $$b_i \leftarrow b_i - \frac{a_{ij}}{a_{jj}} b_j$$
La matrice devient triangulaire supérieure.

### La remontée
Permet de rendre une matrice triangulaire supérieure diagonale en annulant les coefficients [[surdiagonal|surdiagonaux]]

- **En partant de la dernière colonne**, et jusqu'à la seconde (la première colonne n'a aucun coefficient [[surdiagonal]])
	- Inutile de chercher le pivot, il est déjà en $a_{jj}$ car la descente a été effectuée
	- On effectue les mêmes transvections que pour la descente mais sur les coefficients strictement surdiagonaux (on n'a d'ailleurs pas besoin de faire ces [[opérations élémentaires sur une matrice|opérations]] sur la matrice, mais seulement sur le vecteur second membre)

La matrice devient diagonale.

### La résolution du système diagonal
(Que l'on appelle aussi *système résolu* pour cette raison)
Le vecteur solution s'obtient à partir du vecteur second membre, en divisant chaque coefficient $b_k$ par $a_{kk}$.

### L'algorithme complet
Consiste à effectuer la descente, la remontée puis la résolution du système diagonal.


## Implémentation
En python

### La descente
```python
def triangularize(A, b):
	lines, columns = A.shape
	for j in range(1, columns - 1):
		
		# Find pivot's position within the column
		pivot_at = j
		for i in range(j, lines):
			if abs(A[pivot_at, j]) < abs(A[i, j]):
				pivot_at = i
		
		# Put pivot on the diagonal if it isn't already
		if pivot_at != j:
			A[[j, pivot_at]] = A[[pivot_at, j]]
			b[[j, pivot_at]] = b[[pivot_at, j]]

		# Cancel out every line below the diagonal
		for i in range(j+1, lines):
			A[i] -= A[i, j]/A[j, j] * A[j]
			b[i] -= A[i, j]/A[j, j] * b[j]
```

### La remontée
```python
def diagonalize_triangular(A, b):
	lines, columns = A.shape
	for j in range(columns - 1, 1, step=-1):
		for i in range(1, j):
			# No need to do it on A
			b[i] -= A[i, j]/A[j, j] * b[j]
```

### La résolution du système diagonal
```python
def solve_diagonal(A, b):
	_, columns = b.shape
	for k in range(columns):
		b[k] /= A[k, k]
```

### L'algorithme complet
```python
def gauss(A, b):
	# Prevent overwriting arguments
	U, v = A.copy(), b.copy()

	triangularize(U, v)
	diagonalize_triangular(U, v)
	solve_diagonal(U, v)
	return v
```

## Autres applications
### Inversion d'une matrice

On peut calculer l'[[inverse d'une matrice]] à l'aide de la fonction `lambda A: gauss(A, identity(A.shape[0])` où `identity` donne la [[matrice identité]] de l'ordre de l'argument.

Cette fonction provient du [[module Python|module]] [[numpy]]