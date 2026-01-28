# Tree Top Bop
As the protagonist of a popular platformer game, you earn gold by crushing enemies.

### Player rules
- The maximum distance you can travel in a single jump is $D$.
- Crushing an enemy resets the travel distance counter to $0$.
- Crushing from an enemy at $x_i$ to another at $x_j$, both the gold gain and the increase in the distance traveled are equal to $|x_j - x_i|$.

### Enemy rules
- There are $N$ enemies, each located at position $x_i$ on a one-dimensional line.
- Each enemy can be crushed at most $t_i$ times.

Determine the maximum total gold gain in a single attempt.

- $1 \leq D \leq 10^{10}$
- $1 \leq N \leq 10^5$
- $1 \leq x_i \leq 10^{10}$
- $i \lt j \to x_i \lt x_j$
- $1 \leq t_i \leq 10^{10}$
