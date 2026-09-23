## Potential Enzyme

There is a hidden string of length $N$ consisting of at most $M$ distinct characters.

Your goal is to find the substring that maximizes its score based on its non-overlapping occurrences in the original string.

The score of a repeating substring is defined as:

$$\text{Score} = (c - 1) \times L^2$$

where $c$ is the number of maximum non-overlapping occurrences of the substring, and $L$ is its length.

Assuming all possible strings of length $N$ are equally likely, find the probability that the length of one of the maximum-scoring substrings is $k$, for each $k$ ($1 \leq k \leq N$).

Express your answer modulo $998244353$. Note that a single string may have multiple substrings that achieve the same maximum score.

### Constraints

* $1 \leq N \leq 1000$
* $M = 4$
