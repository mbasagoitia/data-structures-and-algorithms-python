# NP-Complete Problem Examples

## SAT Variants

- 2-CNF-SAT, where every clause has two literals, can be solved in polynomial (O(n^2)) time, unlike 3-CNF-SAT.

- If you have greater than 3 CNF-SAT, it can be reduced to 3-CNF-SAT, so their time complexity is the same.

- Horn-SAT: Special form of SAT where in each clause, all but one of the literals is negated. If all clauses are Horn clauses, the problem can be solved in polynomial time. Led to development of logic programming.

- K-Max-SAT: Instead of satisfying all clauses, satisfy at least k out of the m clauses
    - K-Max-SAT is NP-Complete because 3-CNF-SAT can be reduced to it.

## Graph Problems

- K-Clique Problem: Find a subset of k nodes where each node is connected to every other node. NP-Complete because 3-SAT can be reduced to it.

- Vertex Cover: A subset of vertices such that for every edge in the graph, at least one of the endpoints of the edges is in that subset of vertices. Every edge "touches" one of the vertices. We often want to find the smallest such subset, or vertex cover.
    - Decision version: K-Vertex-Cover: is there a vertex-cover with k or fewer vertices in the graph? K-Vertex-Cover can be verified with a certificate in polynomial time, so it is in NP.

- K-Vertex-Cover is also NP-Complete because there is a reduction from K-clique to it.

### Reducing K-clique to K-vertex Cover

Idea: Consider the complement graph of the original graph (a graph containing only the edges NOT present in the original graph). If there is a k-clique in the original graph, then there is a n - k vertex cover (where n is the number of nodes) in the complement and vice versa.

## 0-1 Integer Linear Programming

The goal is to maximize an objective function subject to some linear inequalities, with the constraint that the decision variables can only be 0 or 1.

Decision version: Is there a feasible solution whose objective value is >= some limit k?

This problem is NP-Complete because 3-CNF can be reduced to it.

## Knapsack Problem

We found a pseudopolynomial algorithm to handle the decision version of the knapsack problem. It is also NP-complete.

## Travelling Salesperson

Given a graph with edge weights, is there a way to visit all vertices and return to the starting point such that the sum of edge weights is <= some budget?

This problem is also NP-Complete.