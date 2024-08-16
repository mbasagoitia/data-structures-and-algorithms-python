# What is Linear Programming?

Class of optimization problems where you are maximizing or minimizing some objective function (cost, revenue, profit, etc.)

Subject to some constraints

Example:

x1 + x2 - x3, where each is a real value number representing our decision variables

Maybe x1 is sugar, x2 is milk, and x3 is water--we need to maximize how "good" our drink is going to be based on these variables.

However, if we were to maximize this function, wouldn't we just say x1 and x2 are inifinity and x3 is negative infinity? No, because of constraints.

## Constraints

x1 <= 1
x2 <= 1
x3 <= 1
x1, x2, x3 >= 0

If you think about our example above, obviously we would choose x1 = 1, x2 = 1, and x3 = 0 to maximize our function given these constraints.

Another example: maximize the following:

x1 - 2x2 + x3

Subject to these constraints: 
- x1 - x2 + x3 <= 4
- x1 + x2 - x3 <= 7
- x1 - x2 <= 8
- x1 <= 12
- x2 <= 14
- x3 <= 22
- x1, x2, x3 >= 0

We need to find the set of values that BOTH maximizes the given function and satisfies all constraints.

## Why is it Called Linear?

The objective function must be linear (cannot include multiplication of terms, squares, sine, etc.). You can multiply terms by constants. Constraints must be linear inequalities.

Another example:

maximize C1x1 + C2x2 + .... Cnxn

Constraints:
- a11x1 + a12x2 ... a1nxn >= b1
.
.
.
- am1x1 + am2x2 .... amnxn <= bm

where aij are all constants, bi are all constants

You can negate the objective function signs and constraint inequalities to get the opposite effect--minimizing the function instead of maximizing.

Generally, you don't have strict inequalities < > as constraints in linear programs.
