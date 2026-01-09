# Circles
There is a canvas of size $2^K$ x $2^K$.

$N$ circles are drawn on the canvas. Each circle has its radius $r_i$. At time $t=0$, the center of the $i$-th circle is located at ($y_i$, $x_i$).

Initially, at each discrete time step, the $i$-th circles moves by ($dy_i$, $dx_i$). However, its velocity is updated by a $90$-degree rotation upon a collision to at least one other circle.

You are given $T$ queries. For each query, determine the number of unordered pair of intersected circles seen on the canvas.

## Constraints
- $1 \leq K \lt 32$
- $2 \leq N \leq 10^5$
- $1 \lt r_i \leq 2^{K-1}$
- $0 \leq y_i, x_i \lt 2^K$
- $|dy_i|, |dx_i| \leq 10$
- $1 \leq T \leq 10$
- $1 \leq t_i \leq 10^{100}$
- All inputs are integers.
