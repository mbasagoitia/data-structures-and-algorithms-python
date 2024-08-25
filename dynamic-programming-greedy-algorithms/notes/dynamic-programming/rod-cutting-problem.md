# Introduction to Dynamic Programming and Rod-Cutting Problem

Dynamic programming is used for solving optimization problems. DP represents a time-memory tradeoff, as you must use extra memory to store the values you compute. Two components make a problem a good candidate for DP: optimal substructure and overlapping subproblems.

Two types of dynamic programming:

- *Top-down/memoization*: write the procedure in a recursive manner, but save computed values in an array or hash table to avoid recomputing them later--look up values as needed rather than recomputing

- *Botton-up/tabulation*: solve smaller prerequisite subproblems first, storing each solution, then build up larger subproblems from the solutions to smaller problems that you already have

## Rod-Cutting Problem

Say you are a company that sells steel rods, and you would like to maximize your profit by cutting the rods into varying lengths and selling the pieces for a set price per length.

We need to determine the optimal choice for cutting the rods and the profit you will get from that solution.

## Main Ideas of Dynamic Programming

In problems such as the rod-cutting problem, we have a sequence of decisions to make.

Once you commit to the first cut, you are back to the original problem, but with different data (if you made a cut of 3m out of your 10m rod, now you have a 7m rod instead of 10m).

Now, what is the best decision for a rod of 7m? We can determine this recursively.

**Optimal Substructure** Property

1. The decisions we need to make are sequential.
2. If I commit to one decision at the current stage, then the remaining leftover problem is an instance of the original problem.
3. The final solution involves solving step 2 optimally and combining with original decision.

Many times, if your problem has the optimal substructure property, it can be solved with dynamic programming.

## Back to Rod-Cutting Problem

Given a rod of length L and a price table with lengths l1 .... ln and prices p1 .... pn, what is the maximum revenue possible and how do I obtain it?

Steps:

1. Identify optimal substructure
    - You could commit to n different decisions for the first cut, which would leave you with the profit pn for whatever n length you chose plus a rod of length L - ln. That means you need to find the answer for the subproblem (the new rod of length L - ln).
2. Write down a recurrence for the optimal value.
    - maxRevenue(L) where L is the length of the original rod
    - if L == 0, maxRevenue(L) = 0
    - If L < 0, maxRevenue(L) = -inf (not allowed in this problem)
    - The best option and our recurrence would be *the maximum of the following:* maxRevenue(L - l1) + p1, maxRevenue(L - l2) + p2 ... maxRevenue(L - ln) + pn, and 0. Why 0? 0 would be a decision to waste the entire rod (no revenue). Whichever of these options provides the best answer will be the best answer for the original problem.
3. Memoize the problem using arrays or hashtables--cache the results of overlapping subproblems.

One solution would be to loop through the values in the table and keep track of a currentMax value, comparing it against the maximum solution for each rod length (maxRevenue(L - ln)) and updating as necessary, then returning currentMax. Your base cases would be where L == 0 or L < 0.

This would be a very slow implementation (exponential, 2^n)! **It will also calculate the same subproblem many times,** which leads to lots of repeated work. Can we speed it up?

## Memoization Approach

Instead of calling the recursion each time, look up the value to see if it has been stored in the table. If it hasn't, store the solution.

## How to Retain the Solution

Compute the solution for each subproblem and store in your table T so that T[0] = 0, T[1] = 0, etc.

Have another table S store the decision at each step that gives you the best (local/immediate/current) solution. At T[0], decision S[0] is nil (no cuts, no decision); at T[3] S[3] = 3 (the best local solution was to cut a rod of size 3). Once both tables are filled out, look up S[n](in our case, S[10]). This would represent making the best decision, say, of cutting a piece of length 4. That leaves us with a rod of length 6. Now look up 6 in the S table and get the best decision from length 6, which is 3. Now we are left with a rod of length 3...do the same thing and look up the best solution for a rod of length 3. This is how you recover the solution.

So, once you are done, just traverse the S array.