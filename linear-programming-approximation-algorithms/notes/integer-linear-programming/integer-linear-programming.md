# Integer Linear Programming

Modification of linear programming that is useful for solving combinatorial optimization problems such as:

- Vertex cover problem
- Travelling salesperson problem
- Satisfiability problem

Like a linear program, maximize/minimize a linear function of some decision variables subject to some linear constraints (inequalities). However, in an integer linear program, the decision variables are restricted to the set of integers (positive and negative whole numbers).

## Uses of Integer Linear Programs

- Knapsack Problem

You have a knapsack with a weight limit W and a set of items, each with a given value and weight. Select which items to include or exclude from the knapsack such that the total weight is less than the weight limit W, while maximizing the value of items in the knapsack.

This is an example of a combinatorial optimization problem.

## Knapsack Problem as an Integer Linear Programming Problem

Decision variables:

- xi ... xn, which is 0 if Ii (item i) is not picked, and 1 if Ii is picked <- indicator variable

Goal: maximize v1x1 + v2x2 ... + vnxn

v1x1 will be either 0 (if not picked) or the value of the item, v1, (if picked) since x1 is an indicator variable that acts as an on/off switch.

Where vn = value of the item n

Constraints:

- w1x1 + w2x2 ... wnxn <= W

Where w1 = weight of item 1 and W is the weight limit of the knapsack.

- 0 <= x1 <= 1, ... 0 <= xn <= 1
- x1 ... xn are integers (integrality constraint)

We have the integrality constraint because any value other than 0 or 1 has no meaning in this context--we half-picked the item? We picked half the item?

This kind of program may be known as a 0-1 program or binary program.

When considering the feasible region in an integer LP, the possible solutions exist as "dots" on the possible integer values inside of the feasible region, known as lattice points.

If you drop the integrality constraint on an integer LP, this is known as "LP relaxation."

The optimal solution of an ILP and an LP may be the same, or they may differ based upon the **integrality constraint.**

- Optimal solution of LP >= optimal solution of ILP (if we are maximizing; opposite if minimizing)
- If the optimal solution of the LP is integral, the optimal solution equals the optimal solution for the ILP

## Integrality Gap

How much larger can the optimal solution to the LP be than the solution to the ILP?

gap = optimum LP / optimum ILP (if maximizing, reversed if minimizing)

There is no limit/bound to how large the gap can be (think of the tall, skinny triangle example).