# Bowling
- path ( $L<=10^{10}$ , $W<=50$) and the end grid( $R=W$ )
- grid represented as string of two chars (# or .)
- you are given $N \leq 10^5$ tuples, consisting of a shooting angle, an acceleration rotation, and an initial pos ($0 \leq x_i \leq W, y_i=0$)
- you may only shot for $T<N$ attempts. return the max number of scores (= pins hit by at least one)
- assume no friction occurs
