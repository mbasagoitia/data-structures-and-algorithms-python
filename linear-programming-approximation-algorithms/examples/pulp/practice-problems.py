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

# diet_problem = LpProblem("diet_problem", LpMinimize)

# a = LpVariable("food_a", 0)
# b = LpVariable("food_b", 0)

# diet_problem += 0.5*a + 0.3*b

# diet_problem += 400*a + 200*b >= 600
# diet_problem += 30*a + 10*b >= 50
# diet_problem += 20*a + 5*b <= 40

# diet_problem.solve()
# print(constants.LpStatus[diet_problem.status])
# print(a.varValue, b.varValue)
# print(diet_problem.objective.value())

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

# profit_problem = LpProblem("profit_problem", LpMaximize)
# n = 4
# p = [10, 15, 20, 25]
# r = [2, 3, 4, 5]
# R = 10
# decision_vars = [LpVariable(f'x{i + 1}', 0) for i in range(n)]
# profit_problem += lpSum(p[i]*decision_vars[i] for i in range(n))
# profit_problem += lpSum(r[i]*decision_vars[i] for i in range(n)) <= R

# profit_problem.solve()
# print(constants.LpStatus[profit_problem.status])
# print([v.varValue for v in decision_vars])
# print(profit_problem.objective.value())

# squares = [x**2 for x in range(1, 11)]
# print(squares)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# evens = [x for x in numbers if x % 2 == 0]
# print(evens)

# words = ['apple', 'banana', 'cherry', 'date']
# word_lengths = [len(word) for word in words]
# print(word_lengths)

# data = [1, 'hello', 3.5, 'world', True]
# strings_only = [var for var in data if isinstance(var, str)]
# print(strings_only)

# nested_list = [[1, 2], [3, 4], [5, 6]]
# flattened_list = [x for y in nested_list for x in y]
# print(flattened_list)

# fizz_buzz = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1, 16)]
# print(fizz_buzz)

# nested_list2 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# flattened_list2 = [x for y in nested_list2 for x in y if x % 2 == 0]
# print(flattened_list2)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# transposition = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# print(transposition)

# words = ['apple', 'banana', 'cherry', 'date']
# word_dict = {word:len(word) for word in words}

# print(word_dict)

# scores = {'Alice': 85, 'Bob': 92, 'Charlie': 87, 'David': 78}
# pass_fail = {key:("Pass" if scores[key] >= 80 else "Fail") for key in scores}
# print(pass_fail)

# Factory Problem

# A company has n factories producing goods and m warehouses that need to receive the goods.
# Each factory can produce a certain number of goods, and each warehouse has a certain demand that needs to be met.
# The transportation cost per unit of goods between each factory and warehouse is given by a matrix.

# Your task is to determine how much goods each factory should send to each warehouse to minimize the total
# transportation cost while meeting all the warehouse demands without exceeding the factory capacities.

# Details:

# Number of factories: n
# Number of warehouses: m
# Production capacity: capacity[i] for each factory i.
# Warehouse demand: demand[j] for each warehouse j.
# Transportation cost matrix: cost[i][j] represents the transportation cost from factory i to warehouse j.

factory_problem = LpProblem("factory_problem", LpMinimize)
n = 3
m = 3
cost = [
  [4, 6, 9],
  [5, 7, 3],
  [8, 4, 7]
]

capacity = [100, 150, 200]
demand = [80, 120, 150]

decision_vars = [[LpVariable(f'x{i}{j}', 0) for j in range (m)] for i in range (n)]

factory_problem += lpSum(decision_vars[i][j] * cost[i][j] for j in range(m) for i in range(n))

for i in range(n):
    factory_problem += lpSum(decision_vars[i][j] for j in range(m)) <= capacity[i]

for j in range(m):
    factory_problem += lpSum(decision_vars[i][j] for i in range(n)) == demand[j]

factory_problem.solve()
print(constants.LpStatus[factory_problem.status])
print([[j.varValue for j in i] for i in decision_vars])
print(factory_problem.objective.value())
