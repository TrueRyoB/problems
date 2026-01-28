# Walkout
You just watched a movie in a seating area of $H \times W$ at $(i, j)$.
The theater consists of three types of seating:
- ".": empty seating
- "I": occupied by the standing
- "A": occupied by the sitting

You can pass through any seating if not in the state "A". 

- a query triggers a toggle to all occupied seating on a cross at an arbitrary center next to your current position
- return the minimum query req to walk out

## Constraints
- $1 \leq H, W \leq 10^3$
- $1 \leq i \leq H$
- $1 \leq j \leq W$
- $S_{i, j} \in {".", "I", "A"}$
