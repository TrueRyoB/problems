# Scheduler
There is a pool of $N$ lectures. 

Lecture $i$ offers $M_i$ sessions, where session $j$ is held during the time range $[t_{i,j,1}, t_{i,j,2})$ and has $P_{i,j}$ available seats.

To enroll in a lecture, you must register for exactly one of its sessions. 

You are given $Q$ queries.

Each query provides: 

- the number of lectures to enroll in $C_q$
- a set of lecture indices $L_q$
- a minimum required time padding $D_q$

A selection is valid if, after sorting the chosen sessions by start time, every pair of consecutive sessions $(a,b)$ satisfies the following.

$$
t_{end}(a)+D_q \leq t_{start}(b)
$$

For each query: 

1. Output the available number of valid session combinations whose sessions all have at least one remaining seat.
2. If it's at least one, choose the lexicographically smallest combination of session indices with respect to lecture index order, and consume one seat from each selected session.

Seats are depleted cumulatively across queries.

## Constraints
- $1 \leq N \leq 1000$
- $1 \leq M_i \leq 10$
- $0 \leq t_{i,j,1} \lt t_{i,j,2} \leq 10^{10}$
- $1 \leq P_{i,j} \leq 100$
- $1 \leq Q \leq 10$
- $1 \leq C_q \leq 18$
- $l \in L_q | 1 \leq l \leq N$
- $1 \leq D_q \leq 10^{10}$
