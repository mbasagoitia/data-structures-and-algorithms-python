# Fully Polynomial Time Approximation Schemes

Approximation schemes that can get us arbitrarily close to a factor of 1 approximation in polynomial time. Consider a constant e; you can get to a factor of O(n^2 * 1/e) for example, or some other polynomial bound, but never a perfect answer (e cannot be zero).

These are very rare, but one exists for the knapsack problem.

Closely related to dynamic programming and we will be modifying a DP solution.

Given a list of items with weights and values, and a weight limit W, find a subset of items that maximizes the value of total items taken while respecting the weight limit.

The traditional DP solution is a pseudopolynomial time algorithm.

# Polynomial Time Approximation Scheme for Knapsack Problem

Recurrence:

W(i,v): What is the smallest total weight needed from a1 ... ai such that total value = v?

If we can calculate the above, we can use that calculation to compute the original problem by choosing the largest value for which the total weight comes in under the budget W. Instead of focusing on weight, we focus on value.

Base cases:

- W(0, v) = 0 if v is 0; infinity otherwise
- W(1, v) = w1 if v = v1; 0 if v is 0; infinity otherwise

W(i + 1, v) = min(W(i, v), wi + 1 + W(i, v-vi+1)) either choosing the i + 1th item or not

This is still exponential with a complexity of O(n^2 * Vmax)... what do we need to do?

Choose a scaling factor k and divide all values by k and round down to get a new set of values v1 ... vi

k = (e * vmax)/n

By scaling down and truncating the values rather than the weight, we still guarantee a solution that stays under the weight budget, but has faster time complexity by a factor of k, O(n^2 * Vmax/k).

Each new vi' is now floor(vi/k), so the following is true: vi/k >= vi' >= vi/k - 1

v(S) >= (1-e)*OPT in O(n^3 * 1/e) time