# Introduction to Greedy Algorithms

Dynamic programming solutions can be very expensive space-wise, even when memoized.

Greedy algorithms are very fast algorithms to solve the same type of problems that we may solve using DP (maximize or minimize a value function with staged decisions and optimal substructure).

A greedy algorithm uses a **local criterion** or **greedy criterion** to make an immediate choice, then uses that same criterion to make the next choice, etc.

No future lookahead, just make the locally optimal choice.

Tradeoff for inexpensive operations is that you don't always get the optimal solution overall.

Greedy algorithms often work top to bottom--make a choice and then solve a subproblem.

## Rod-Cutting Problem Example

Say that we sorted our rod lengths by price per unit length (the most money for the shortest rod). We will choose the feasible length (less than the current total length of the remaining rod) that provides the greatest value per centimeter as our greedy criterion.

## Why Use Greedy Algorithms?

- They are fast
- Sometimes, they actually give you the best answer
