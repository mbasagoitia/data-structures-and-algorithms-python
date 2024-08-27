# Knapsack Problem

Given a knapsack with weight capacity W and a set of items i1 ... ik of weights w and values v, maximize the value of the items placed in the knapsack, ensuring that their weights do not exceed the capacity of the knapsack.

For each item, there are two choices: take it or leave it. It is our goal to find the ideal subset of items. 

## Optimal Substructure

Sequence of decisions? Yes. For each item i, take it or leave it -- once we commit, the subproblem is the remaining items with the remaining weight capacity (either W or W - w1 depending on if we took the item or not).

## Recurrence

What sequence of decisions do I need to make to obtain the maximum value?

- j = items available for consideration
- W = maximum weight capacity

- maxValue(j, W) = 0 if W = 0 (base case; knapsack is full), -infinity if W < 0 (second base case), 0 if j = n + 1 and W > 0 (no items left), or...
- max(vj + maxValue(j + 1, W - wj), maxValue(j + 1, W))

- Explanation of recursive case: we take the maximum value of the two choices: we either took the item and then add its value (vj) and move onto the next item (j + 1) with the new weight capacity W - wj, or we did not take it and we simply move on to the next item (j + 1) without adding the value or updating the weight capacity.

## Memoize

Table with rows j = 1 ... j = n + 1 and columns 0 ... W0

- The first column and last row are all filled with 0 (base cases; W = 0 and j = n + 1)
- You are always looking at either one row below (same weight, next item), or one row below and one column over (different weight, next item)
- Fill in the table from left to right, bottom to top because each entry depends on data from below it and to its left

for j = n to 1
    for w = 1 to W0
        T[j, W] = max(T[j + 1, W], T[j + 1, W - wj] + vj)

return T[1, W0]

## Time Complexity

O(nW0)

It is pseudopolynomial; exponential in W0

## Recover the Optimal Solution

Use an S table to record the decision made at each step. Record either take or leave.

Traverse the table from j = 1 to j = n + 1 and determine the decision. If taken, go to the next item at the updated weight column. If left, go to the next item at the same weight and repeat.

This all assumes that item weights are whole numbers.