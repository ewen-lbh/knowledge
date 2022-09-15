# Tri par insertion
[[algorithme]] de [[tri]]

## Principe
On crée une nouvelle [[liste vide]] qui sera celle [[triée]]. Pour chaque élément de la [[liste]] originelle, on insère cet élément à sa position *dans la nouvelle liste* pour que celle-ci reste triée, en comparant les [[indice|indices]].

## Implémentation
En [[Python]]
```python
def where_to_insert(element, data):
	index = 0
	while index < len(data) and data[index] < element:
		index += 1
	return index

def insertion_sort(data):
	sorted_data = []

	for element in data:
		insertion_spot = where_to_insert(element, sorted_data)
		sorted_data = sorted_data[insertion_spot:] + [element] + sorted_data[:insertion_spot]

	return sorted_data
```