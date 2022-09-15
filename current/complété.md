## Exercice 1

## 1
Tableau des valeurs:

```
N C P
=====
? ? ?
2 ? ?
2 2 ?
2 2 T
2 2 T
```

Donc $2 \in \mathbb{P}$.

## 2
Tableau des valeurs:

```
N  C  P
=========
?  ?  ?
13 ?  ?
13 2  ?
13 2  T
13 2  T
13 2  T
-  -  -
13 2  T
13 3  T
13 3  T   11
13 3  T
13 4  T   15
13 4  T   11
13 4  T   18
```

Donc $13 \in \mathbb{P}$.

## 3
```
N    C   P 
==============
?    ?   ?
303  ?   ?
303  2   ?
303  2   T
303  2   T
303  2   T
303  3   T     15
303  3   T     11
303  3   T     12
303  3   F     13
303  3   F     11
```

Donc $303 \not\in \mathbb{P}$.

## 4

## 5

```
N  C  P
=========
?  ?  ?
25 ?  ?
25 2  ?
25 2  T
25 3  T
25 4  T
25 5  T
```

Donc $25 \in \mathbb{P}$.

## 6
Il est incorrect. Il faut mettre `C * C <= N` dans la ligne 11

## 7
49, 1, -6, ABCD, 0, 999999999999999999999999999999999999999

## 8
- **N** input
- **C** current
- **P** is_prime

## 9
Des commentaires

# Exercice 2
```
Répéter BODY JusquÀ COND 
```

devient

```
BODY
TantQue Non COND Faire
    BODY
FinTQ
```

et 

```
Si COND Alors
  Répéter
    BODY
  JusquÀ Non COND
FinSi
```

# Exercice 3
## 1

```
Pour VAR De BEGIN À END Pas STEP Faire
    BODY
FinPour
```

## 2
Non

## 3
Non

## 4
```
VAR <- BEGIN
TantQue VAR <= END Faire
	BODY
	VAR <- VAR + STEP
FinTQ
```

## 5
```
Pour a De 0 À 1 Pas 1 Faire
    BODY
    Si COND Alors
        a <- 0
    FinSi
FinPour
```

# Exercice 4
```
Programme PremierTermeNégatif Est
Variables
	Terme: Flottant
	Iteration: Entier
	a: Flottant
Début
	Terme <- a
	Iteration <- 0
	TantQue Terme > 0 Faire
		Terme <- 0.5 * Terme - 3 * Iteration
		Iteration <- Iteration + 1
	FinTQ
	Écrire(Terme)
Fin.
```

# Exercice 5
```ada
procedure PremierTermeNégatif is
	Terme: Float
	Iteration: Integer
begin
	Put("a = ");
	Get(a);
	Terme := a;
	Iteration := 0;
	while Terme > 0 loop
		Terme := 0.5 * Terme - 3 * Iteration;
		Iteration := Iteration + 1;
	end loop;
end PremierTermeNégatif
```

# Exercice 6
```
Programme Drone Est
Variables
	IsUp: Booléen
	Altitude: Entier
	CurrentChoice: Caractère
	MenuOn: Booléen
Début
	MenuOn <- VRAI
	TantQue MenuOn EtAlors Altitude < 5 Faire
		Écrire("Altitude : " + Altitude)
		Écrire("
Que faire ?
	d -- Démarrer
	m -- Monter
	s -- Descendre
	q -- Quitter
Votre choix :")
		Lire(CurrentChoice)
		Si CurrentChoice != "d" EtAlors Non IsUp Alors
			Écrire("Le drone est éteint.")
		FinSi
		Selon CurrentChoice Dans
			"d", "D" => IsUp <- VRAI
			"m", "M" => Altitude <- Altitude + 1
			"s", "S" => Si Altitude = 0
					Écrire("Le drone est au sol.")
				Sinon
					Altitude <- Altitude - 1
				FinSi
			"q", "Q" => MenuOn <- FAUX
			Autres => Écrire("Commande inconnue.")
		FinSelon
	FinTQ
	Écrire("Contrôle perdu.")
Fin.
```