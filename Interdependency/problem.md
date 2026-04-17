## Interdependency

There is an array $A$ at length $N$, consisting of real numbers.

Solve the minimum number of operations to match it to an array $B$.

For each operation, choose integers $i$ and $j$, where $1 \leq i, j \leq N$ and $i \neq j$; then, set $A_i = A_j + d$ where $d \in {1, -1}$. 

If it is impossible, output $-1$ instead.

### Constraints
- $1 \leq N \leq 10^5$
- $|A_i|, |B_i| \leq 10^5$
- $|A|=|B|=N$
