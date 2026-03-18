## Vessel

There are $N$ vessels with maximum capacities $C_i$ for vessel $i$. Initially, all vessels are empty.

Let $v_i$ denote the current volume of water in cup $i$. At any step, you may perform one of the following:

1.  **Fill:** For any $i \in \{1, \dots, N\}$, set $v_i = C_i$.
2.  **Drink:** For any $i \in \{1, \dots, N\}$, set $v_i = \max(0, v_i - X)$.
3.  **Pour:** For any pair $(i, j)$ where $i \neq j$, transfer $\Delta = \min(v_i, C_j - v_j)$ from cup $i$ to cup $j$. 

Determine if it is possible to reach a target state $A = (A_1, A_2, \dots, A_N)$.

### Mathematical Constraints
- $1 \leq N \leq 10^4$
- $1 \leq C_i\leq 10^5$
- $1 \leq X \leq 10^5$
- $0 \leq A_i \leq C_i$
