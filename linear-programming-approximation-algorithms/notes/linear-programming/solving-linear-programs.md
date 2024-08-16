# Solving Linear Programs

## Problems

Infeasible constraints: The constraints themselves are not possible to satisfy all at once

Unbounded problem: There is no limit to how much we can optimize the solution

If solutions are feasible and bounded, then we can find an optimal solution

## Parts of a Linear Program

- Decision variables (real numbers); think Alice, Bob, and Charlie x1 ... xn
- Linear objective function that we try to maximize/minimize
- Constraints: all linear inequalities

You could give these three components to an LP solver which will give you one of three answers:
- Infeasible
- Unbounded
- Optimal solution for decision variables x1* ... xn* that maximizes the objective function