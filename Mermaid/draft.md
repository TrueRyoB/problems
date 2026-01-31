# Mermaid
There are $N$ buttons. Initially, the button $B$ is enabled.

Pressing the button $i$ will enable $A_i$ buttons.

What is the minimum number of times you have to press buttons to enable $K$ buttons? If it's impossible, yield $-1$ instead.


## Constraints
- $2 \leq N \leq 10^5$
- $1 \leq B \leq N$
- $0 \leq A_i \leq N$
- $1 \leq a_{i,j} \leq N$
- $x \neq y \to a_{i, x} \neq a_{i, y}$
- $\sum A_i \leq 10^5$
- $M \lt K \leq N$
