# All Pairs Shortest Path Problems and Floyd-Warshall Algorithm

Rather than having a single source, we find the shortest path between any two nodes in the graph.

In a graph of n nodes, there are n^2 possible pairs.

Output:

- Distance (D) Matrix: Represent the shortest path distances as a matrix
- Next (N) Matrix: represents the next node (node after i) in the shortest path from nodes i to j

Given both of these matrices, you can retrieve the shortest path betwen any two nodes.

If the graph has all non-negative weight edges, we can run Dijkstra's algorithm from every source node and record the relevant information in the two matrices. Time complexity: V * (V + E * log(V)) (between n^2 log(n) and n^3 log(n))

If the graph does not have all non-negative weight edges, then we run Bellman-Ford algorithm for every vertex. Time complexity: between O(n^3) and O(n^4)

## Floyd-Warshall Algorithm

- Dynamic programming memoization algorithm

Consider if the path through each node k is shorter than the direct edge between i and j.

D(k)[i, j] = min(D(k-1)(i, j), D(k-1)(i, k) + D(k-1)(k, j))

- Initialize D(0) -> adjacency matrix with edge weights; infinity if i != j and !(i, j) no edge from i to j and 0 if i = j

for k = 1 to n:
    for i = 1 to n:
        for j = 1 to n:
            D(k)(i, j) = min(D(k-1)(i, j), D(k-1)(i, k) + D(k-1)(k, j))
return D(n)[i, j]

### How to Retrieve the Shortest Path

Update the Path Matrix: Whenever you update the distance in the Floyd-Warshall algorithm, update the next matrix accordingly. If distance[i][j] is updated using an intermediate node k, set next[i][j] = next[i][k].

N(k)(i, j) = N(k-1)(i, j) if A is smaller; N(k-1)(i, k) if B is smaller

Time Complexity of Floyd-Warshall: three nested for loops, so O(n^3)

### Pseudocode for Shortest Path Retrieval

def get_path(start, end, next):
    if next[start][end] == null:
        return "No path"
    path = []
    current = start
    while current != end:
        path.append(current)
        current = next[current][end]
    path.append(end)
    return path