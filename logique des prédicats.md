#modélisation

On ajoute à la [[logique propositionnelle]] des [[quantificateurs]] $\forall$ et $\exists$.

Attention, on ne peut pas [[type|typer]] les variables introduites par ces quantificateurs: à la limite, $\forall x \in E, \mathcal{P}(x)$ (resp. $\exists x \in E, \mathcal{P}(x)$) est une simple *notation* pour $\forall x, E(x) \implies \mathcal{P}(x)$ (resp. $\exists x, E(x) \land \mathcal{P}(x)$).

## Exemples

### Vrai ou faux?

- $G = \forall x, \exists y, p(x, y)$
	- Dans le domaine $\mathbb{N}$, avec $p(x, y) = x \ge y$
		- C'est vrai: si $x > 0$, alors on prend $y = x-1$. Sinon, on prend $y = x = 0$ et $0 \ge 0$ donc OK.
		- (ou alors on prend $y = 0$)
	- Dans le domaine $\mathbb{N}$ avec $p(x, y) = x > y$
		- C'est **faux**: si $x = 0$, il n'existe pas de $y$ strictement plus petit (car $-1 \not\in \mathbb{N}$)
	- Dans le domaine $\mathbb{Z}$ avec $p(x, y) = x > y$
		- C'est vrai: on prend  $y = x-1$. $(\mathbb{Z}, +, \times)$ est un anneau donc $x-1 \in \mathbb{Z}$.
	- Dans le domaine Humanité avec $p(x, y) = y \text{ est le père de } x$
		- "On en discute au foyer"

### Traduction

- Tous les hommes sont intelligents
  $\forall H, \operatorname{homme}(H) \implies \operatorname{intelligent}(H)$
- Pierre est intelligent
  $\operatorname{intelligent}(\text{Pierre})$
- Aucun homme n'est intelligent
  $\forall H, \operatorname{homme}(H) \implies \lnot \operatorname{intelligent}(H)$
- Seuls les hommes sont intelligents
  $\forall o, \operatorname{intelligent}(o) \implies \operatorname{homme}(o)$
- Tous les hommes sont soit beaux, soit intelligents
  $\forall H, \operatorname{homme}(H) \implies \operatorname{beau}(H)  \operatorname{xor} \operatorname{intelligent}(H)$ 
  (avec $\operatorname{xor} = (a, b) \mapsto (a \land \lnot b) \lor (\lnot a \land b)$)
- Certains hommes sont intelligents ou beaux
  $\exists H, \operatorname{homme}(H) \land(\operatorname{beau}(H) \lor \operatorname{intelligent}(H))$
- Une condition nécéssaire pour que $x$ soit premier est qu'il soit impair ou qu'il soit égal à 2
  $\forall x, \operatorname{\mathbb{Z}}(x) \implies \operatorname{premier}(x) \implies \lnot \operatorname{pair}(x) \lor \operatorname{=}(x, 2)$
- Il existe un homme qui aime les chiens
  $\exists H, \forall c, \operatorname{homme}(H) \land \operatorname{chien}(c) \implies \operatorname{aime}(H, c)$
- Personne ne connaît tout le monde
  $\forall h_1, \exists h_2, \operatorname{homme}(h_1) \land \operatorname{homme}(h_2) \implies \lnot\operatorname{connaît}(h_1, h_2)$
- Il y a une chanson qu'aucun enfant ne chante
  $\exists c,\operatorname{chanson}(c) \land (\forall e, \operatorname{enfant}(e) \implies \lnot\operatorname{chante}(c, e))$
- Tout le monde a un père. Le grand-père paternel est le père du père. Donc tout le monde a un grand père paternel
   $(\forall x, \operatorname{homme}(x) \implies \operatorname{père}(x)) \land \operatorname{=}( \operatorname{gpp}, \operatorname{père} \circ \operatorname{père}) \vdash \forall x,\operatorname{homme}(x) \implies \operatorname{gpp}(x)$
   $(\forall x, \operatorname{homme}(x) \implies (\exists y, \operatorname{homme}(y) \land \operatorname{père}(y, x)) \land (\forall y \forall z \forall t, \operatorname{père}(y, t) \land \operatorname{père}(z, y) \implies \operatorname{grand\_père}(z, t))) \implies \forall x, \operatorname{homme}(x) \implies (\exists y, \operatorname{homme}(y) \land \operatorname{grand\_père}(y, x))$