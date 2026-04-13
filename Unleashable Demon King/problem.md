## Unleashable Demon King

In the grand finals of a legendary tournament, Faker and Takahashi are facing off in a unique jungle challenge on Summoner's Rift.

There are $N$ monster camps in the jungle. The $i$-th camp initially contains $A_i$ small monsters. The players have agreed to a specialized "Leash" duel to test their last-hit skills.

Faker and Takahashi take turns clearing monsters. On each turn, a player must select one non-empty camp. Let $M$ be the number of monsters currently remaining in that camp; the player must remove $x$ monsters such that $1 \leq x \leq \max(1, \lfloor \frac{M}{2} \rfloor)$.

However, there is a catch: the player forced to take the very last monster in the entire jungle suffers a "Cursed Last Hit." This massive debuff acts as a permanent hex, rendering the champion powerless and making them **lose the game**.

Faker goes first. Assuming both players play perfectly, determine if Faker can secure the win.

### Output
For each test case, output "Faker" if the first player wins, or "Takahashi" if the second player wins.

### Constraints

* $1 \leq T \leq 10^4$
* $1 \leq N \leq 10^4$
* $1 \leq A_i \leq 100$
* The sum of $N$ over all test cases does not exceed $10^4$.
* The total sum of all $A_i$ across all test cases does not exceed $10^6$.
