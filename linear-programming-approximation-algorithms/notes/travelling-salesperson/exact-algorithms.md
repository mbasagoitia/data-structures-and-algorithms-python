# Exact Algorithms for TSP

## Held-Karp Algorithm

Dynamic programming algorithm for symmetric TSP (Cij = Cji) that outperforms the brute force algorithm, but is still exponential time.

We will visualize our decisions/recurrence as going from an arbitrary starting node and choosing an ending node which loops back to the start. Then we have the "box" of all the remaining nodes which we are trying to find a path through.

MinCostPath(S, e) -> Find the minimum cost of a subset of vertices ending at vertex e visiting each node exactly once. e is not in the subset S. Remember to add the cost of the edge from the ending vertex to the starting vertex.

In what order do we visit the vertices in S?

Example:

minCostTSPTour(5) = min(minCostPath({2, 3, 4}, 5) + C5,1, minCostPath({2, 3, 5}, 4) + C4, 1, etc.)
- This can be written as a loop through different values of e

The above is trying to find the minimum of different calculation of minCostPath for different ending vertices. It considers the cost of different subsets in the graph and adds the edge from the ending vertex to the starting vertex.

Solving the minCostPath problem leads you to the answer for the TSP.

### Solving minCostPath

minCostPath(S, e) where S is a subset of vertices and e is an endpoint not in the set, nor is the starting point

Goal: Find a path that traverses every vertex in the subset exactly once and ends at e (don't worry about the edge from e to start)

Start by committing to a last node s in the subset S; commit to cost of s -> e

Recurrence is Cse + minCostPath(S - s, s) <- Remove s from the subset and find the new minCostPath ending at s, adding the cost from s to e. Find the minimum of all choices of s in the set S.

### Memoization

Each entry in the table will be labeled by a subset S and an endpoint e, (S, e) which gives you the minCostPath for that subset and endpoint. The table will be built for smaller subsets first, then larger subsets.

Base cases:

- The subset contains 1 vertex: mcp({i}, e) -> mcp = ci1 + cie (only one way to traverse; cost of start to i + i to e)
- The subset is empty: mcp({}, e) = c1e (cost from start to end)

To construct the TSP tour, record the vertetx at each step that gives you the minimum cost path.

### Time Complexity

n^2 * 2^n

## Integer Linear Programming Solution to TSP

We will work again with symmetric TSPs here.

Decision variables:

- xi->j for every pair of vertices where i is visited before j, binary variable 0 or 1 (TSP either went from i to j or did not)
- ti: timestamp for when you visited node i

Constraints:

- 1 <= ti <= n
- xi->j + ti <= j if j != 1
- For every vertex i, the summation over all possible values j of xi->j = 1 (we can only take one outgoing path from our vertex i)
- For every vertex i, the summation of all possible values k of xk->i = 1 (we can take only one incoming path to each vertex i)
- If xi->j = 1, ti + 1 <= tj HOWEVER we can't actually do this logic in ILP, so do the following:
    - "Big M trick:" ti + xi->j <= tj + (n - 1)(1 - xi->j)
    - This establishes that no cycles/revisiting of nodes occurs (subtours)

Objective function: Minimize the summation of Cij * xi->j for all decision variables xi ->j where Cij is the cost of going from i to j

In the worst case, this approach is slower than Held-Karp, but may work faster in practice

## Subtours and Subtour Elimination Formulation

In this formulation, we will regard xi->j and xj->i as the same

- Sum of all edges either leaving or entering i = 2 (one leaving, one entering; # of tour edges incident on a vertex)
Subtour elimination constraints:
- For every S which is a potential subtour of 1 ... n, the summation of all edges where i belongs to S and j does not belong to S (potential edges in the tour), the number of edges must be >= 2

This approach doesn't use timestamp decision variables, but adds 2^n constraints.

To avoid adding all these constraints up front, run the algorithm and if you encounter a subtour, add the subtour elimination constraint for that subset and solve again, repeating if necessary.