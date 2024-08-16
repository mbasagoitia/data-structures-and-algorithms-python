# Dijkstra's Algorithm

Algorithm for finding the single-source shortest path for graphs with non-negative edge weights. You can have cycles.

This is a natural way for graphs to exist in the world; distance, time, queue size, etc. which can only be non-negative values.

This is a greedy algorithm and shares many commonalities with Prim's Algorithm.

Uses similar edge-relaxing technique that the Bellman-Ford algorithm uses, but each edge is relaxed exactly once.

Basic idea:

- Compute a clever ordering of edges
- Relax each edge in this order exactly once

## Steps

1. At every step, choose a previously unvisited node whose d value (path cost) is smallest
2. Relax all outgoing edges of v (update d and parent)
3. Mark v as visited
4. Repeat until all nodes are visited

Your output table will have columns node, d (cost), pi (parent), visited

What data structure can we use to find the node whose d value is the smallest at every step?

A min-heap! With d values as keys.

# Pseudocode for Dijkstra's Algorithm with a Min-Heap

# V: set of vertices
# E: set of edges

# Initialize table
for each vertex v in V:
    if v is the source:
        v.d = 0                # Distance to source is 0
        v.pi = nil             # Predecessor is undefined
    else:
        v.d = infinity         # Distance to source is infinity
        v.pi = nil             # Predecessor is undefined

# Construct a min-heap
vertices_array = [v1, ..., vn]
heapify(vertices_array)        # Heapify based on v.d as the key

while vertices_array is not empty:
    u = extract_min(vertices_array)  # Extract vertex with minimum distance
    for each outgoing_edge (u, v) in adjacency_list[u]:  # For each neighbor v of u
        if u.d + w(u, v) < v.d:       # Relaxation step
            v.d = u.d + w(u, v)       # Update the shortest path estimate
            v.pi = u                  # Update the predecessor
            bubble_up(vertices_array, v) # Update the heap to reflect changes

# Definitions:
# - u.d represents the shortest distance estimate from the source to u.
# - w(u, v) is the weight of the edge from u to v.
# - v.pi is the predecessor of v in the shortest path.


## Time Complexity

O((m + n)log(n))

Much faster than Bellman-Ford!