## Jurassic World
On your way home, you figure out that there are $N$ dinosaurs behind you. Dinosaur $i$ is currently at position $P_i$ relative to you.

Let $x$ be the current position of a dinosaur; at each step, it independently chooses an integer $y$ uniformly at random such that $0 \leq t \leq x$, and moves to position $y$.

If multiple dinosaurs teleport to the same position simultaneously, they fist fight until only one remains, and the others are eliminated.

The dinosaurs repeat this process for exactly $M$ steps before your ally arrives.
If any dinosaur reaches position $0$ at or before the end of the $M$-th step, you are caught.

Solve the probability that you survive.

### Constraints
- $1 \leq N \leq 10^5$
- $1 \leq P_i \leq 10^9$
- All $P_i$ are distinct
- $1 \leq M \leq 10^4$
