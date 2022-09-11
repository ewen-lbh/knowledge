# Tri pivot
[[algorithme]] de [[tri]]

Aussi appelé *Tri rapide* (*Quicksort* en anglais)

## Principe
- On choisit un élément de la [[liste]] appelé *pivot*.
- On sépare les éléments plus petits, plus grands ou égaux au pivot dans trois listes
- On trie (par [[récursion]]) les listes des éléments plus grands et des éléments plus petits que le pivot
- On [[concaténation|concatène]] les trois listes

## Implémentation
En Python

```python
def quicksort(data):
	if len(data) <= 1: return data

	pivot = data[0] # Could be chosen arbitrarily, as long as it's in data
	smaller, pivots, larger = [], [], []

	for element in data:
		(
		 larger  if element > pivot else
		 smaller if element < pivot else
		 pivots
		).append(element)

	return quicksort(smaller) + pivots + quicksort(greater)
```