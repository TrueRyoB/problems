## Apparel Revolving

There are $T$ test cases for the following problem settings.

You have two closets, $A$ and $B$, which operate like queues. Initially, Closet $A$ contains $N$ items and Closet $B$ contains $M$ items in order. 

The $i$-th item in Closet $A$ has a value of $A_i$, and the $i$-th item in Closet $B$ has a value of $B_i$. 

Two items are considered identical if and only if their values are equal.

Each morning, you take the item at the front of both closets to wear as an outfit. At the end of the day, you push each item back to the end of its respective closet.

You can perform the following operation any number of times, possibly zero:
- Choose one of the closets. If it contains at least $2$ items, discard the item at the front of that closet.

Your goal is to maximize the number of days until you wear the same combination of item values again. 

Find the minimum number of items you need to discard to achieve it. 

### Constraints
- $1 \le T \le 10^5$
- $1 \le N, M \le 10^5$
- $1 \le A_i, B_i \le 10^6$
- The sum of $N$ and $M$ over all test cases does not exceed $10^6$.
