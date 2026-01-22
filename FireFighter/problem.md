# Fire Fighter
Kyoto is modeled as a rectangular grid of housings with witdth $W$ and height $H$.

Each housing corresponds to one cell $(i,j)$ and has its value $A_{i,j}$.

At time step $t=0$, exactly $N$ distinct housings in Kyoto are on fire.

---

Time proceeds in discrete steps. At each step:
- Any housing that is on fire spreads fire to all adjacent housings (Manhattan distance exactly 1) that are in the normal state.
- Fire spreading happens simultaneously for all burning housings

---

Each housing is always in exactly one of the following states:
- Normal: neither burning nor seized
- Burning
- Seized: Fire is suppressed; fire neither spreads from nor enters this housing

--- 

When a housing enters the Fire state, the city permanently loses its full value $A_{i,j}$. If the same housing catches fire again later, no additional cost is incurred.

You are a magical fire fighter and pay perform the following operation at any time step:
- You may select one connected component of housings currently on fire.
- All housings in the selected component immediately enters the Seized state.
- Let $M$ be the number of housings in that component.
- A seized component of size $M$ required $\lceil \log_4 M \rceil$ discrete time steps to be completely removed.
- During these steps, the housings remain Seized.
- After the removal time finishes, all housings in the component return to the Normal state.

You may freeze only one component at a time.

--- 
Determine the minimum possible total value lost by the city through optimal use of your magical seize oeprations.

## Constraints
- $1 \leq W, H \leq 10^3$
- $0 \leq A_{i,j} \leq 10^9$
- $1 \leq N \leq WH$
