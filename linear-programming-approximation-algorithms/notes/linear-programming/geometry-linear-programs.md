# Geometry of Linear Programs

Example:

Maximize x1 - 2x2

Constraints
- x1 >= 0
- x2 >= 0 

The two above constraints limit us to the first quadrant in a graph (both values 0 or positive)

- 3x1 + 2x2 <= 6
- 2x1 + 3x2 <= 6

The two above constraints would create a straight, sloped line when plotted on a graph

The region we are interested in, therefore, is the region below and to the left of the intersection of these two lines that still lies within quadrant 1. You can solve for the coordinates of the corner points; in this case, our corner points are (0, 0), (0, 2), (6/5, 6/5), and (2, 0)

These points form a quadrilateral, called a convex polyhedron, with each side corresponding to one of the constraints.
This is called the **feasible region** of the linear programming problem.

What is the optimal solution within the feasible region?
- We can plot the "levels" of the objective function, or a family of parallel lines that represent fixed values of the objective function. Think of "sweeping" in a certain direction to either increase or decrease this value. At some point, you reach the farthest point possible where you are still "touching" the feasible region. This point is the maximum (or minimum, depending on which direction you sweep).

- In this case, the point (2, 0) which is the bottom right point is the optimal solution to maximize the objective function and stay within the feasible region.
- x1* = 2, x2* = 0

What if we have more than two decision variables?

## Higher Dimensions

Suppose we have decision variables C1x1 ... Cnxn

- Our constraints will now form lines/regions that exist on a higher/hyper plane known as **convex polyhdedrons.**
- Our "levels" will not be straight lines, but planes or hyperplanes

## Convex Polyhedra Explained

A polyhedron is convex if for the straight line connecting any two points in the polyhedron, the straight line lies entirely inside the polyhedron.

The feasible region in any linear program forms a non-empty convex polyhedron.

## Unbounded Problem Example

Suppose we are maximizing x1 + x2

Constraints
- x1 >= 3
- x2 >= 5

Obvious problem here... just make them both infinity!

How does this look geometrically?

If you plot these two straight lines (x1 = 3 and x2 = 5) and consider the feasible region, there are no upper bounds on the top or right side. So, it forms an unbounded polygon. There is also no bound on the objective function.