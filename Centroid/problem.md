# Centroid
This problem is interactive.

You are given a number of nodes $N$ and their range for both x and y axis as $W$ and $H$.

Each node is located at an integer point.

Your assignment is to find a centroid in a blindfold. You have two query options.

1. ```guess x y```: queries the sum of the Euclidean distance in a floating number
2. ```submit x y```: ends the querying session

A centroid is a coordinate where the sum of the Euclidean distance to a certain set of nodes are minimum.

Your submission is judged AC iff the bias is within $10^{-6}$ for each x and y.

For both queries, it takes $O(\log N)$ to be computed.

## Constraint
- $1 \leq N \leq 10^5$
- $1 \leq W, H \leq 10^{12}$
- $0 \leq px_i \leq W$
- $0 \leq py_i \leq H$
- every input is integer
