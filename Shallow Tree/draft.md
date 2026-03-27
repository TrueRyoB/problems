## Shallow Tree
You are tasked to design a decision tree for $H$ items grouped into $M$ categories.

The trait of item $i$ is represented as a binary sequence $b_i$ at length $W$ and the label $a_i$.

### possible operations

- all-or
- all-and
- all-xor

- objective: minimize the sum of computational effort for every case


### Constraints
- $1 \leq H \leq 10^3$
- $1 \leq M \leq H$
- $1 \leq W \leq 10^3$
- $b_i = {0, 1}^W$
