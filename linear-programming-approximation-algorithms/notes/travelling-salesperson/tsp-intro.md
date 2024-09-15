# Introduction to Travelling Salesperson Problem

Given a weighted, undirected (or in some cases directed), complete (between any two nodes there is an edge) graph with n nodes, with each edge weight representing a cost, we would like to find the optimal tour of the graph. The tour starts at an arbitrary node and visits all vertices exactly once (cannot revisit previous vertices) and end at the starting point, while minimizing the cost of edges travelled.

For the TSP problem, you receive inputs n (number of vertices) and a matrix where i, j represents the edge cost of edge (i, j). Because the graph is undirected, C(i, j) = C(j, i).

Used in logistics problems, delivery, routing, manufacturing, etc.

## TSP is NP-Complete

We do not have any exact and sufficient solutions for TSP problems.

The exact solutions we know are brute force, dynamic programming, ILP which are not scalable.

We also have approximation algorithms and heuristics.

## NP-Hardness of TSP

Decision version:

Given a graph as above, is there a TSP tour of total cost <= some cost W?

We can verify that a tour given to you has edge weight less than W and that it is a TSP tour in linear time.

The reduction to TSP comes from the Hamiltonian cycle problem, which is itself reduced from the SAT problem.

## Reduction from HAM-Cycle to TSP

Given a graph that is not necessarily complete and has no edge weights/costs, assign a weight of 1 to each existing edge and fill in missing edges with a cost of 2. Remember that TSP requires a complete graph. 

Our goal is to find a TSP tour of this new graph with cost <= n. The only way to do this in the original graph is to only choose edges of cost 1. If you are able to achieve this, it means the original problem was a Hamiltonian cycle.

## TSPs are Hard to Approximate

Unless P = NP, there is no approximation algorithm for TSP that can guarantee a bound of some constant times the optimum solution. Finding such an algorithm is itself NP-hard.

Many practical instances of the TSP problem satisfy the metric property, in which distances/edge weights between nodes satisfy the triangle inequality--in other words, there will generally be edges A, B, and C, where:

A -> B + B -> C >= A -> C

Metric and Euclidean TSPs do in fact have approximation algorithms with 3/2 factor approximations or better. Only general TSPs where these properties don't hold have no polynomial time approximation algorithm.