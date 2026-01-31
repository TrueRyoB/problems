# Mermaid
There are $N$ buttons. Initially, $M$ buttons are enabled.

Pressing the button $i$ will enable $A_i$ buttons.

What is the minimum number of times you have to press buttons to enable the majority of buttons? If it's impossible, yield $-1$ instead.


## Constraints
- $1 \leq M \leq N \leq 10^5$
- $1 \leq m_i \leq N$
- $0 \leq A_i \leq N$
- $1 \leq a_{i,j} \leq N$
- $x \neq y \to a_{i, x} \neq a_{i, y}$
- $\sum A_i \leq 10^5$
