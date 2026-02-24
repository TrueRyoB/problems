# Walpurgis

There are $N^2$ students, each sitting in their chair forming a grid of $N$ x $N$.

Student $(i, j)$ and $(k, l)$ are connected online if and only if $G_{i,j}$ = $G_{k,l}$ 

Right after the exam commencement, it turned out that $M$ students allegedly stole a cheating sheet, provided only to you as a coordinate $(Ci_i, Cj_i)$ for violating student $i$. 

As a professor, your mission is to stop academic violation from propagating. You are somehow granted an ability to randomly spot a student with a cheating sheet uniformly at random among all remaining with a cheating sheet.

For each discrete time step, you can catch the student and every other member connected to them and kick them all out of the classroom. 

Driven by a panic, at the probability of P, a student hands out their cheating sheet to one of the surroundings randomly if at least one of the max of four are filled. 

Solve the probability in MOD 998244343 where there remains at least one student in the classroom post exam after the "clean up".

## Constraint
- $2 \leq N \leq 10$
- $1 \leq G_{i, j} \leq N^2$
- $1 \leq M \leq N^2$
- $1 \leq Ci_i, Cj_i \leq N$
- $0 \leq P \leq 998244342$
