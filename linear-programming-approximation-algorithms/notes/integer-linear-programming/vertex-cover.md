# Vertex Cover as ILP

Description:

The Vertex Cover problem involves selecting a subset of vertices in an undirected graph such that every edge in the graph is connected to at least one of the selected vertices. The challenge is to find the smallest such subset, which is a difficult problem to solve efficiently due to its NP-complete nature.

Consider the following graph:
- Vertices V = {1, 2, 3, 4}
- Edges E = {(1, 2), (2, 3), (3, 4)}

A vertex cover could be C = {2, 3} because these vertices cover all edges in the graph, and is also the smallest subset (minimum vertex cover).

## Formulating Vertex Cover as an ILP Problem

Decision variables:
- x1 ... xn (number of vertices) where xi = 0 if vi is not in the cover, 1 if it is

Objective: minimize x1 + x2 ... + xn

Constraints:
- xu + xv >=1 (at least one of the two endpoints u or v for each edge is in the cover)
- Do this for every edge

