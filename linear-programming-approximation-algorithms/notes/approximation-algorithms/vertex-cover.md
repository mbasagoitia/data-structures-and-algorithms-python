# Approximation Algorithms for Vertex Cover

## Greedy Approach: Greedy on Vertex with Highest Degree

- Choose the node with the highest degree (number of edges leaving the node) and add it to the vertex cover.
- Delete that node and all outgoing edges
- Repeat until no edges are left

You can do this efficiently by maintaining a priority queue to find node with highest degree.

However, this doesn't work well compared to the optimum, especially as the size of the graph grows. It is always some n log n factor away from the optimum.

## Maximal Matching

Here we will look at another greedy approach, which is no worse than twice the size of the vertex cover of the optimal solution.

- Arbitrarily choose some edge and add both of its endpoints (vertices) to the vertex cover
- Delete all edges that are incident on those two vertices
- Repeat until no edges are left