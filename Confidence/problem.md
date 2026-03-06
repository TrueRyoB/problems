# Confidence
You are given a dataset with $H$ rows and $W$ colmns, where each row corresponds to the same target.

Each entry $A_{i,j}$ denotes the confidence score for the $j$-th attribute.

Design an implementation and output the classification result.

## Constraints
- $1 \leq H \leq 10^5$
- $2 \leq W \leq 10$
- $0 \leq A_{i,j} \leq 1.0$
- $\forall i | \sum_{j} A_{i,j}=1$
