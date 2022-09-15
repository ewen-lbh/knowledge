# Tri par tiroirs
[[algorithme]] de [[tri]] d'éléments de [[ℕ]]

## Principe
- On crée un [[tableau]] $T$ associant un élément de la [[liste]] au nombre de fois où il apparaît dans celle-ci
- On parcours ce [[tableau]] $T$ en ajoutant à la [[liste]] triée (initialement [[liste vide|vide]]) $T[n]$ fois le nombre $n$

## Implémentation
### En [[OCaml]]

```ocaml
let rec max l = match l with
	| [a] -> a
	| h::t -> let m = max t in if h > m then h else m

let rec repeat times element = if times = 0 
	then [] 
	else element :: (repeat (times - 1) element)


let couting_sort l = 
	let greatest = max l in
	let counters = Array.make (greatest+1) 0 in
	
	let rec count todo = match todo with
	| [] -> ()
	| h::t -> begin
		counters.(h) <- counters.(h) + 1;
		count t;
	end in count l;
	
	let rec walk current sorted = if current > greatest 
		then sorted 
		else walk (current+1) (
			sorted @ (repeat (counters.(current)) current)
		)
	in walk 0 []
```