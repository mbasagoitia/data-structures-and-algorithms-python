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