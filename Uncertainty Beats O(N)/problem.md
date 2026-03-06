# Uncertainty Beats O(N)
You are given an unsorted array $A$ of size $N$. It is guaranteed that every element in $A$ is an integer in the range $[1, N]$. You have access to a geneative function that returns an index $i \in [0, N-1]$ sampled uniformly at random.

Your goal is to verify whether the minimum excluded value of the array is exactly $T$. You employ an optimized strategy to check this. Let $E$ be the expected number of random accesses reqired to confirm that $mex(A)=T$ with a confidence level of at least $P$.

Find $E$ mod $998244353$.

## Constraints
- $0 \leq N \leq 10^9$
- $0 \leq T \leq N$
- $0 \leq P \lt 998244353$
