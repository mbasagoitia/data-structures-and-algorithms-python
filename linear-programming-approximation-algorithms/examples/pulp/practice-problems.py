# Problem 1

# Maximize Z = 3x + 2y

# Subject to:

# x + y <= 4
# x <= 2
# y <= 3
# x,y >= 0

from pulp import *

# math_problem = LpProblem("math_problem", LpMaximize)

# x = LpVariable("x", 0)
# y = LpVariable("y", 0)

# decision_vars = [x, y]

# math_problem += 3*x + 2*y

# math_problem += x + y <= 4
# math_problem += x <= 2
# math_problem += y <= 3

# math_problem.solve()

# print(constants.LpStatus[math_problem.status])

# results = [v.varValue for v in decision_vars]

# print(results)
# print(math_problem.objective.value())

# Problem 2

# You have two products (A and B) and want to maximize profit.
# The profit for product A is $30 per unit, and for product B is $40 per unit.
# You have 100 hours of labor and 80 units of material available.
# It takes 5 hours and 3 units of material to make one unit of A,
# and 6 hours and 4 units of material to make one unit of B.

# profit_problem = LpProblem("profit_problem", LpMaximize)

# a = LpVariable("A", 0, cat="Integer")
# b = LpVariable("B", 0, cat="Integer")

# profit_problem += 30*a + 40*b

# profit_problem += 5*a + 6*b <= 100
# profit_problem += 3*a + 4*b <= 80

# profit_problem.solve()
# print(constants.LpStatus[profit_problem.status])
# print(a.varValue, b.varValue)
# print(profit_problem.objective.value())

# Problem #3

# A dietitian is designing a meal plan that consists of two food items: Food A and Food B.
# The dietitian wants to meet specific nutritional requirements using these foods.
# Each food item provides a certain amount of calories, protein, and fat per serving.
# The goal is to minimize the cost while meeting the nutritional requirements.

# At least 600 calories.
# At least 50 grams of protein.
# No more than 40 grams of fat.

diet_problem = LpProblem("diet_problem", LpMinimize)

a = LpVariable("food_a", 0)
b = LpVariable("food_b", 0)

diet_problem += 0.5*a + 0.3*b

diet_problem += 400*a + 200*b >= 600
diet_problem += 30*a + 10*b >= 50
diet_problem += 20*a + 5*b <= 40

diet_problem.solve()
print(constants.LpStatus[diet_problem.status])
print(a.varValue, b.varValue)
print(diet_problem.objective.value())

# Problem 4

# A company needs to allocate resources to different projects.
# Each project requires a certain amount of resources and provides a profit.
# The company has a limited amount of total resources available.
# Your task is to maximize the total profit by deciding how much of each project to undertake.

# The company has n projects.
# Each project i requires r[i] units of resources and provides a profit of p[i].

# Total resources available: R
# Objective: Maximize the total profit:

# You will be provided with the following inputs:

# An integer n representing the number of projects.
# A list of integers r representing the resource requirements for each project.
# A list of integers p representing the profit for each project.
# An integer R representing the total resources available.