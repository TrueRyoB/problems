# Compression
You are given a text $S$ at size $N$.

Your boss has given you $M$ transition functions, where function $i$ maps a substring of $b_i$ to an informational cost of $c_i$.

It is guaranteed that it is possible to construct the given text from domains of a set of transition functions provided.

Solve the minimum cost to achieve a full text conversion.

## Constraints
- $|S| = N$
- $1 \leq N \leq 10^5$
- $S$ consists of general characters
- $b_i$ consists of general characters
- $\sum |b_i| \leq 10^5$
- $1 \leq c_i \leq 10^5$
