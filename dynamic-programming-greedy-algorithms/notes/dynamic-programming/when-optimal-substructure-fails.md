# When Optimal Substructure Fails

When a problem does not have optimal substrucure, dynamic programming will not give you the best solution.

## Examples

Take the knapsack problem again, except value V is the sum of the items chosen if the number of items chosen is less than 10, but if there are more, the value is Vij * 0.1 (only gets 1/10 the value if too many items are stolen).

At any step of the problem, it's possible that 10 items have already been stolen, and solving each subproblem optimally will not necessarily give the optimal solution to the original problem.