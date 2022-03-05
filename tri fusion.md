# Tri fusion
Algorithme de [[tri]]

## Principe
- On divise la [[liste]] en deux [[sous-listes]] de [[longueur]] égales ou presque (en scindant à l'indice $\left\lfloor \frac{\operatorname{len} l}{2} \right\rfloor$) 
- Ensuite, on trie ces deux sous-listes (par un appel [[récursion|récursif]]), 
- Puis on les fusionne en  suivant l'algorithme suivant:
	- On crée un nombre appelé *marqueur* pour chaque liste que l'on initialise à 0 et une [[liste vide]], qui sera la liste fusionnée.
	- On choisiera successivement l'élément venant de la première sous-liste — c'est-à-dire celui de la première sous-liste à l'[[indice]] du marqueur de la première sous-liste — ou celui venant de la deuxième
	- Tant qu'il manque des éléments à la liste fusionnée (la [[longueur]] de cette liste n'est pas la [[addition|somme]] des longueurs des deux sous-listes:
		- Si les éléments sont tout les deux accessibles (chaque marqueur est strictement inférieur à la longueur de sa sous-liste)
			- On [[comparaison|compare]] les éléments venant des deux sous-listes et on ajoute le plus petit à la liste fusionnée
			- On [[incrémentation|incrémente]] le marqueur associé à la sous-liste dont on a ajouté l'élément
		- Sinon, au moins un des deux est accessible, on choisit celui-ci et on incrémente le marqueur associé

## Implémentation
En Python
```python
def merge(l1, l2):
	"""
	Merges two *sorted* list into a list equal to sorted(l1 + l2)
	"""

	mark_1, mark_2 = 0, 0
	merged = []

	# While the list is not complete
	while len(merged) < len(l1) + len(l2):
		# If both elements are accessible
		if mark_1 < len(l1) and mark_2 < len(l2):
			# Add the smallest, and update the corresponding mark.
			from_l1 = l1[mark_1]
			from_l2 = l2[mark_2]
			if from_l1 < from_l2:
				merged.append(from_l1)
				mark_1 += 1
			else:
				merged.append(from_l2)
				mark_2 += 1
		else:
			# Add the one that's accessible, and update the corresponding mark.
			if mark_1 < len(l1):
				merged.append(l1[mark_1])
				mark_1 += 1
			else:
				merged.append(l2[mark_2])
				mark_2 += 1

	return merged

def merge_sort(data):
	if len(data) <= 1: return data

	cut_at = int(len(data)/2)

	return merge(
		merge_sort(data[cut_at:]),
		merge_sort(data[:cut_at]),
	)
```

