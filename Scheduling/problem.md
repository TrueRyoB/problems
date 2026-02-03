# Scheduling
You have a class pool of $N$ lectures.

Lecture $i$ offers $M_i$ sessions, where session $j$ is held from $t_{i, j, 1}$ to $t_{i, j, 2}$. 

You need to choose exactly one session for enrollment for each lecture.

Determine if it's possible to take all lectures without any time duplications.

## Constraints
- $1 \leq N \leq 18$
- $1 \leq M_i \leq 10$
- $0 \leq t_{i, j, 1} \lt t_{i, j, 2} \leq 10^{10}$
