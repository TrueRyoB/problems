# Shark
This problem is interactive.

There are $N$ lagoons and $M$ channels, where $i$ interconnects the lagoons $u_i$ and $v_i$.

In the middle of summer, you are noticed that there is a shark in one of the lagoons. Your mission is to suppress the shark and promise the marinal safety.

For each opportunity, you can cast a spell $(k, d)$.
- both $k$ and $d$ must be nonnegative integers
- $k$ must be unselected and within the range $[1, N]$
- $k$-th lagoon is now suppressed
- it will let you know if a shark is present in any lagoons in a range $d$.

The shark chooses to move to another lagoon after the cast, if and and only if the current lagoon is not suppressed and there exists at least one adjacent lagoon not suppressed.

Locate the position of the shark and confirm that it's suppresed, before you run out of your spells.

## Constraints
- $3 \leq N \leq 10^5$
- $N-1 \leq M \leq \min(10^5, \frac{N(N-1)}{2})$
- $1 \leq u_i \lt v_i \leq N$
- $i \neq j \to (u_i, v_i) \neq (u_j, v_j)$
