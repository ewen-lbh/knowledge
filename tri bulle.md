# Tri bulle
[[algorithme]] de [[tri]]

## Principe
- On [[comparaison|compare]] chaque élément au suivant et on les [[permutation|permute]] si besoin. 
- On arrête le processus quand on a fait un passage de [[liste]] entier sans effectuer aucune permutation (car la liste était donc triée).

## Implémentation
En Python, version [[tri en place|en place]]

```python
def bubble_sort(data):
	is_sorted = False
	while not is_sorted:
		is_sorted = True
		for i in range(len(data)):
			if data[i] > data[i+1]:
				data[i], data[i+1] = data[i+1], data[i]
				is_sorted = False
	return data
```
