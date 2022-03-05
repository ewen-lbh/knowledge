# Tri par sélection
Algorithme de [[tri]]

## Principe
- On sélectionne l'élément le plus petit et on le [[permutation|permute]] avec le premier élément de la [[liste]].
- On effectue le même procédé sur la [[sous-liste]] ne contenant pas le premier élément, jusqu'à avoir à traiter la sous-liste de longueur 1, où l'on renvoie simplement la liste (qui est triée par définition).

## Implémentation
En Python

```python
def argmin(data):
	i_min = 0
	for i in range(1, len(data)):
		if data[i] < data[i_min]:
			i_min = i
	return i_min

def selection_sort(data):
	if len(data) <= 1: return data

	i_min = argmin(data)
	data[0], data[i_min] = data[i_min], data[0]
	selection_sort(data[1:])

	return data
```