## String factory
A factory has $N$ characters of 'a', $M$ of 'b', and $L$ of 'c'.

Each individual character is distinct and has a unique value: $A_i$ for the $i$-th 'a',  $B_i$ for the $i$-th 'b', and $C_i$ for the $i$-th 'c'.

Strings are formed by appending characters one by one. A string is completed and shipped immediately as soon as its suffix matches any of the following conditions:

- The suffix is "ab"
- The suffix is "bc"
- The suffix is "ca"

After a string is shipped, you may choose to either start forming a new string or terminate the process. You do not need to use all available characters.

Find the sum of the total values of all possible combinations of shipped strings modulo $9982442353$.

Note: a "combination" is defined as a multiset of shipped strings. This means the internal order of characters within each string matters, but the order in which the strings themselves are shipped does not.

### Constraints
- $1 \leq N, M, L \leq 10^4$
- $1 \leq A_i, B_i, C_i \leq 10^4$
