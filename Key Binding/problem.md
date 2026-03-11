## Key Binding

You are tasked with reconstructing a target string $S$ of length $N$ using a collection of substrings $B = \{b_1, b_2, \dots, b_M\}$. 

You are also provided with a set of costs $C = \{c_1, c_2, \dots, c_M\}$.

The goal is to create a one-to-one mapping between the costs in $C$ and the substrings in $B$ such that the total cost to assemble the entire string $S$ is minimized. 

Additionally, transition cost $T_{i, j}$ incurs whenever substring $b_j$ is used immediately after substring $b_i$ in the reconstruction of $S$.

It is guaranteed that $S$ can be fully formed using elements from $B$.

Output the matching result. 

### Constraints
- $1 \leq N \leq 10^5$
- $|S| = N$
- $1 \leq M \leq 10^2$
- $1 \leq |b_i|$
- $\sum |b_i| \leq 10^5$
- $1 \leq c_j \leq 10^4$
- $1 \leq T_{i, j} \leq 10^4$
- $S$ and $b_i$ consists of printable ASCII characters found on a standard US keyboard
