# Glass Cannon
You are a game technical designer working on balance adjustments for League of Legends.
Your task is to configure a new buff, Glass Cannon, so that the affected champions collectively achieve an average win rate close to 50%, while minimizing the standard deviation from 50% across those champions.

You are given stats for $N$ champions.
Each champion $i$ has the following base attributes:
- $AD_i$: Attack Damage
- $AS_i$: Attack Speed
- $AR_i$: Armor
- $H_i$: Maximum Health

## Combat Model
- Combat is 1v1 and deterministic.
- Attacks are discrete.
- A champion performs basic attacks at fixed intervals determined by AS.
- Each basic attack deals damage computed as:

$$
\mathrm{Damage}(i,j) = \max(1, \lfloor \frac{AD_i}{2} - \frac{AR_j}{4} \rfloor)
$$

Champions attack until one of their health reaches zero.

Win rate between the two is calculated as follows.

$$
\mathrm{Result}(i,j)=
\begin{cases}
1   & \text{if } i \text{ defeats } j, \\
0   & \text{if } j \text{ defeats } i, \\
0.5 & \text{if both } i \text{ and } j \text{ are buffed}.
\end{cases}
$$

## Buff definition
Out of the $N$ champions, exactly $T$ champions receive the buff.
The Glass Cannon buff applies the following multiplicative stat changes:
- $H'=(1-h)H$
- $AD'=(1+a)AD$
- $AS'=(1+s)AS$
where $0 \lt h, a, s$ are global constants shared by all buffed champions.

## Evaluation matric
Each champion players a deterministic 1v1 match against every other champion.

Let $W_i$ denote the resulting win rate of buffed champion $i$.

The objective is to minimize the standard deviation from the target win rate of 50% as follows:

$$
\min_{a, s, h} \frac{1}{T} \sqrt{\sum_{i}^{N} (W_i-0.5)^2}
$$

## Task
Determine one possible combination of positive floating numbers $(a, s, h)$ that satisfies the Glass Cannon fantasy while keeping the balance impact close to neutral.

## Constraints
- $2 \leq N \leq 10^5$
- $1 \leq H_i, AD_i, AR_i\leq 10^{10}$
- $0 \lt AS_i \leq 5.0$
- $1 \leq T \lt N$
- $1 \leq t_i \leq N$
- Every input is integer but $AS_i$
