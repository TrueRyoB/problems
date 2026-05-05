## Enka

$N$ people are lined up in a circle. Person $i$ is next to person $(i+N-1) \mod N$ and $(i+1) \mod N$.

Each participant has a nonnegative integer.

Each of them reports the absolute difference of integers of their subsequent two people to be $A_i$.

You are given $Q$ queries.

For each query, solve the number of possible combinations of participants to their number modulo $998244353$, when person $x$ has integer $B_x$.


### Constarints

- $3 \leq N \leq 10^5$
- $0 \leq A_i \leq 10^5$
- $1 \leq Q \leq 10^5$
- $0 \leq x \leq N-1$
- $1 \leq B_x \leq 10^5$
