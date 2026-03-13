## Hacked!

Your operating system has been hacked! A virus has taken exclusive control of your $N$ available CPU threads.

The virus is running $M$ periodic processes, where process $i$ requires $W_i$ amount of computation time with the deadline $D_i$ per cycle.

All processes are initiated simultaneously at $t = 0$. Assuming that the virus uses an optimal, preemptive scheduling strategy, determine the earliest time mod $998244353$ at which the system will crash due to a process missing its deadline. If the system can run indefinitely, return -1 instead.

### Constraints
- $1 \leq N \lt M \leq 10^5$
- $1 \leq W_i \lt D_i \leq 10^5$
