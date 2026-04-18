# Mitsudesu

There is an $H$ x $W$ grid, where cell $(i, j)$ has value $A_{i, j}$.

At time step $t=0$, exactly $M$ cells are infected. Each of the location is provided as $y_i, x_i$.

At each step, any infected cells simultaneously spread infection to all of its adjacent cells. 

You are given $Q$ queries. For each query, solve the sum of the values of infected cells at $t=B_i + 0.5$.


## Constraints
- $1 \leq W, H \leq 1000$
- $0 \leq A_{i,j} \leq 10^9$
- $1 \leq M \leq WH$
- $1 \leq y_i \leq H$
- $1 \leq x_i \leq W$
- $1 \leq Q \leq 10^5$
- $0 \leq B_i \leq 10^{18}$
