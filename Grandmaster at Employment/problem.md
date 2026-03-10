# Grandmaster at Employment

## Problem Description

This is an **online heuristic optimization problem** consisting of $Q$ independent test cases. Your goal is to maximize the **sum of the scores** across all queries.

### The Interview Process

For each query $i$, you are presented with a queue of $N_i$ applicants one by one.

* **Decision Window:** For each applicant, you must decide whether to hire or reject them. This decision must be made within $M_i$ "time units"—meaning you must decide on the $j$-th applicant before you are allowed to see the $(j + M_i + 1)$-th applicant.
* **Hiring Goal:** You must hire exactly $T_i$ applicants from the queue.
* **Competency Matrix:** Each applicant $j$ has a set of $W_i$ competency scores, denoted as $A_{i, j, k}$ for $k = 1, \dots, W_i$.

### Objective Function

The total value of a hired team for query $i$ is the **product of the sums** of their competencies across all $W_i$ aspects. If $S$ is the set of indices of the $T_i$ hired applicants, the score $V_i$ is:

$$V_i = \prod_{k=1}^{W_i} \left( \sum_{j \in S} A_{i, j, k} \right)$$

Your final performance is evaluated based on the **sum** of $V_i$ across all $Q$ queries.

## Constraints

* $1 \leq Q \leq 10^5$
* $1 \leq N_i$
* $2 \leq \sum_{i=1}^{Q} N_i \leq 10^5$
* $1 \leq T_i < N_i$
* $0 \leq M_i < N_i$ (Look-ahead/Decision delay constraint)
* $1 \leq W_i \leq 10$
* $1 \leq A_{i, j, k} \leq 100$
