# Approximation Algorithms for TSP

## Metric TSP and Shortcutting

Recall that general TSPs cannot be approximated to any constant factor. 

However, a TSP may be metric if the following properties are satisfied for all nodes:

- Cij >= 0
- Cij = Cji
- Cik <= Cij + Cjk (direct path must be less than going through another vertex)

Metric TSPs are also NP-complete, but the constant factor approximation becomes easier.

## Shortcutting

Starting with a minimum-spanning tree (MST) of the graph, we can start to construct a TSP tour.

We start at a node 1 (arbitrarily) in the MST and traverse the MST, adding nodes to our TSP tour. When the end is reached, backtrack (skipping already visited nodes) until you reach a node you haven't visited. Move your pointer to this node; this creates a shortcut edge. The cost of this TSP tour is >= the cost of the MST, but bounded by a factor of 2 of the size of the optimal tour (and MST).

## Eulerian Tours

An Eulerian tour traverses every edge in an undirected graph exactly once and comes back to the starting point (unlike a Hamiltonian cycle which traverses every vertex).

For a graph to have an Eulerian tour, every vertex must have an even number of edges incident on it.

There is a polynomial time algorithm that can construct an Eulerian tour from a graph.

## Christofides Algorithm

Approximation algorithm for TSPs that gives a factor 3/2 approximation

- Start with a TSP instance and construct a minimum spanning tree (MST), assuming an arbitrary node is the root
- Instead of a DFS as above, perform an Eulerian tour of the TSP tree
    - However, this isn't currently possible because the leaf nodes have an odd number of edges incident on them (1)
    - Remember that an Eulerian tour requires only an even number of edges connected to each node
    - We will add some edges from the original graph back to the tree to satisfy this property
- Construct a subgraph from only the nodes that have an odd number of edges and find a matching for each set of 2 vertices; ideally, a minimum-weight matching for which there is an algorithm
    - There is always an even number of odd-edge nodes, so a valid matching will always exist
- Add these edges to the MST--double edges may arise, which is ok
- Now, each node has an even number of edges incident on it
- Perform an Eulerian tour of the graph
- Shortcut the Eulerian tour to remove nodes that have been previously visited; this gives you a TSP tour

The weight of this tour is <= 3/2 the optimal tour

