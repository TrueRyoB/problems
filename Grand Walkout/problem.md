## the Grand Walkout

You have just finished watching a movie in a theater represented by an $H \times W$ grid. You are currently at position $(r, c)$. 

Your goal is to exit the theater by reaching any coordinate that lies outside the grid boundaries. 

The theater contains three types of cells:
* `.` (**Walkway**): Always passable.
* `I` (**Standing**): Occupied, but the person is standing. You **can** pass through.
* `A` (**Sitting**): Occupied, and the person is sitting. You **cannot** pass through.

You can perform two types of actions:

1. **Move**: Move to an adjacent cell (up, down, left, or right) if the target cell is not in state `A`. This action has a cost of $0$.
2. **Toggle**: Choose a cell $(i_0, j_0)$ that is **4-adjacent** to your current position. Perform a toggle on the **cross** centered at $(i_0, j_0)$. This action has a cost of $1$.

**The Toggle Operation:**
A "cross" consists of the center cell $(i_0, j_0)$ and its four immediate neighbors: $(i_0-1, j_0), (i_0+1, j_0), (i_0, j_0-1),$ and $(i_0, j_0+1)$. For every cell in this cross:
* If the cell is `I`, it becomes `A`.
* If the cell is `A`, it becomes `I`.
* If the cell is `.`, it remains unchanged.

All changes made by a Toggle persist as you continue to move through the theater.


Find the **minimum number of Toggles** required to reach any position outside the grid. If it is impossible to leave the theater, output `-1`.

### Constraints
* $1 \le H, W \le 1000$
* $1 \le r \le H$
* $1 \le c \le W$
* The starting cell $(r, c)$ is guaranteed to be passable (`.` or `I`).
* The theater may contain any number of `I`, `A`, or `.` cells.
