# Confidence
You have $H$ rows of data, where each row consists of $W$ columns holding floating numbers $A_{i,j}$.

Each floating number indicates a confidence level for the target object to be the attribute corresponding to the column index.

Construct your approach in categorizing the target and design an implementation that returns the classification result.

## Constraints
- $1 \leq H \leq 10^5$
- $2 \leq W \leq 10$
- $0 \leq A_{i,j} \leq 1.0$
- $\forall i | \sum_{j} A_{i,j}=1$
