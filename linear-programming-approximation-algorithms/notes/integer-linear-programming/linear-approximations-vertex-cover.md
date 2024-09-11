# Linear Approximations to Vertex Cover

Remember, the vertex cover problems aims to find the smallest subset of vertices in an undirected graph such that for every edge, at least one vertex is in the subset.

## ILP Formulation

- Decision variables w1 ... wn where wi is 0 or 1 (the vertex is either included in the cover or not; binary variables)
- Objective: minimize w1 + w2 ... + wn
- Subject to
    - For every edge (j, k) in the graph, wj + wk >= 1

## LP Relaxation

Drops the integrality constraint; w1 ... wn can be numbers between 0 and 1, and the solver will give you fractional answers. So, what is the difference between the optimal solution given to you by the LP solution and the ILP solution? Remember lattice points inside the feasible region representing valid ILP solutions.

How do we make sense of the optimal LP solution in the vertex cover problem?

## LP Plus Rounding

Round each decision variable to the nearest value (0 or 1), which gives us a vertex cover that is no worse than 2x larger than the optimum vertex cover.

Using LP plus rounding yields a valid vertex cover, but it may not be optimum.

LP-Rounding solution >= Optimum ILP solution and Optimum ILP solution > LP solution

The LP-Rounding solution <= 2 * optimum LP solution (fractional value)

This is because if wi has been rounded to 1, then zi was at least 0.5.

This is important because solving for the optimum ILP solution takes exponential time, whereas solving the LP relaxation and then rounding takes polynomial time and still gives a solution no larger than twice the optimal solution.

## Integrality Gap

In the vertex cover problem, the gap between the objective achieved by the best ILP solution and the objective achieved by the best LP relaxation is no worse than 2; bounded by 2.