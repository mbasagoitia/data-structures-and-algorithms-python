# Bellman-Ford Algorithm for Shortest Paths

Given a directed graph with edge weights, determine single-source shortest paths from the given source.

This algorithm repeatedly performs the "edge relax" operation.

Output table: destinations, source, cost, pi (parent columns) for each node. Each node's initial cost is infinity and starting parent is nil.

## Relax Operation

Updates estimates of path cost by considering previous path cost plus edge weight, if that value is less than the estimate of the current node.

If d[u] + w(u, v) < d[v]
d[v] = d[u] + w(u, v)
pi[v] = u

Where d[u] = previous cost estimate
d[v] = current cost estimate
w(u, v) = edge weight between u and v
pi[v] = parent node of v (we go through u to reach v)

"Relaxes" along the edge (u, v)

If you have successfully found all shortest paths in the graph, d[u] + w(u, v) >= d[v] and no more relax operations can take place.

The shortest paths have all been found if the following are true:

- The cost of the path from the source to itself is 0
- No edge between any nodes u and v can be successfully relaxed; d[u] + w(u, v) >= d[v]

## Bellman-Ford Algorithm

- Initialize a table the same as before; three columns: destination, distanct/cost (intially infinity), parent(initially nil)

n = number of vertices

- Loop through the vertices; for i = i to n - 1 (if you have 4 vertices, iterate 3 times)
    - Inner loop: for each edge e in the graph, relax(e)
    - When performing the relax operation, we also update the parent to remember the edge along which we have achieved the latest and best estimate distance from the source.

- Work for negative weight cycles (not covered here; not allowed in shortest path algorithms)

## Time Complexity

Outer loop: n - 1
Inner loop: m
Relax: O(1) (simple comparison)

Total = O(v * E) = number of vertices * number of edges

## Properties of Bellman-Ford Algorithm

d*[v] = shortest path distance from source to vertex v

1. Monotone: at any point in the algorithm, d[v] >= d*[v] for any node v
2. If d[v] is not infinity, there exists a path from source to v whose path weight = d[v] (not necessarily the shortest path)
3. After i iterations of Bellman-Ford, d[v] must be <= shortest path of i edges or fewer

If a graph has no negative weight cycles, then any shortest path must have <= n - 1 edges

## Handling Negative Weight Cycles

1. Initialize output table
2. Looping from 1 through n - 1, for each edge, relax
3. Check if negative weight cycles exist AFTER these loops have finished
    - Check if any edge can lead to a further relaxation; if they can, then you have a negative weight cycle