# Approximation Algorithms for Maximum Satisfiability (MAX 3-SAT) Problem

Recall that you have n different boolean variables x1 ... xn which can either be True or False.

You have various clauses with a specified number of literals (in this case, 3 literals). The clauses are ANDs of ORs of literals that may be negated (NOT).

The goal is to find the truth assignment for n decision variables that satisfies the maximum number of m clauses. This problem is NP-complete. We can implement it as an integer linear program. Here, we will explore approximation algorithms.

## Approximation Algorithm: Greedy Approach

This approximation yields a solution of a factor no worse (smaller) than 7/8 of the optimum solution.

If you choose a truth assignment at random (probability 1/2 for T/F for each variable), the probability that any clause is satisfied is 7/8; therefore, the expected number of clauses satisfied is the summation of probability over all clauses, or 7/8*m.

We want to derandomize this process so that we can guarantee that at least 7/8 clauses are satisfied. To find a solution that is better than the average, plug in and calculate/simplify the problem for x1 ... xn = T or F at each step and choose whichever gives you a higher probability of being satisifed, and continue through the rest of the decision variables.