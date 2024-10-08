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

# factory_problem = LpProblem("factory_problem", LpMinimize)
# n = 3
# m = 3
# cost = [
#   [4, 6, 9],
#   [5, 7, 3],
#   [8, 4, 7]
# ]

# capacity = [100, 150, 200]
# demand = [80, 120, 150]

# decision_vars = [[LpVariable(f'x{i}{j}', 0) for j in range (m)] for i in range (n)]

# factory_problem += lpSum(decision_vars[i][j] * cost[i][j] for j in range(m) for i in range(n))

# for i in range(n):
#     factory_problem += lpSum(decision_vars[i][j] for j in range(m)) <= capacity[i]

# for j in range(m):
#     factory_problem += lpSum(decision_vars[i][j] for i in range(n)) == demand[j]

# factory_problem.solve()
# print(constants.LpStatus[factory_problem.status])
# print([[j.varValue for j in i] for i in decision_vars])
# print(factory_problem.objective.value())

# quiz_problem = LpProblem("quiz_problem", LpMaximize)

# decision_vars = [LpVariable(f'x{x}', lowBound=-15, upBound=15) for x in range (5)]

# quiz_problem += 2*decision_vars[0] - 3*decision_vars[1] + decision_vars[2]
# quiz_problem += decision_vars[0] - decision_vars[1] + decision_vars[2] <= 5
# quiz_problem += decision_vars[0] - decision_vars[1] + 4*decision_vars[2] <= 7
# quiz_problem += decision_vars[0] + 2*decision_vars[1] - decision_vars[2] + decision_vars[3] <= 14
# quiz_problem += decision_vars[2] - decision_vars[3] + decision_vars[4] <= 7

# quiz_problem.solve()
# print(quiz_problem.objective.value())

# quiz_problem2 = LpProblem("quiz_problem", LpMinimize)

# decision_vars = [LpVariable(f'x{x}', lowBound=-1, upBound=1, cat="Integer") for x in range (3)]

# quiz_problem2 += 2*decision_vars[0] - 3*decision_vars[1] + decision_vars[2]

# quiz_problem2 += decision_vars[0] - decision_vars[1] >= 0.5
# quiz_problem2 += decision_vars[0] - decision_vars[1] <= 0.75
# quiz_problem2 += decision_vars[1] - decision_vars[2] <= 1.25
# quiz_problem2 += decision_vars[1] - decision_vars[2] >= 0.95

# quiz_problem2.solve()
# print(constants.LpStatus[quiz_problem2.status])
# print([v.varValue for v in decision_vars])
# print(quiz_problem2.objective.value())

# resource_problem = LpProblem("resource_problem", LpMaximize)

# a = LpVariable("a", 0)
# b = LpVariable("b", 0)

# resource_problem += 40*a + 30*b

# resource_problem += 2*a + 3*b <= 100
# resource_problem += 3*a + 2*b <= 200

# resource_problem.solve()

# print(constants.LpStatus[resource_problem.status])
# print(a.varValue, b.varValue)
# print(resource_problem.objective.value())

# diet_problem = LpProblem("diet_problem", LpMinimize)

# x = LpVariable("x", 0)
# y = LpVariable("y", 0)

# diet_problem += 2*x + 3*y

# diet_problem += 3*x + 2*y >= 12
# diet_problem += x + 2*y >= 8

# diet_problem.solve()

# print(constants.LpStatus[diet_problem.status])
# print(x.varValue, y.varValue)
# print(diet_problem.objective.value())

# factory_problem = LpProblem("factory_problem", LpMinimize)
# xa1 = LpVariable("xa1", 0)
# xb1 = LpVariable("xb1", 0)
# xa2 = LpVariable("xa2", 0)
# xb2 = LpVariable("xb2", 0)

# factory_problem += 4*xa1 + 6*xa2 + 3*xb1 + 5*xb2

# factory_problem += xa1 + xa2 <= 100

# factory_problem += xb1 + xb2 <= 150

# factory_problem += xa1 + xb1 >= 130

# factory_problem += xa2 + xb2 >= 120

# factory_problem.solve()

# print(constants.LpStatus[factory_problem.status])
# print(xa1.varValue, xa2.varValue, xb1.varValue, xb2.varValue)
# print(factory_problem.objective.value())

# factory_problem = LpProblem("factory problem", LpMaximize)

# a = LpVariable("a", 0, cat="Integer")
# b = LpVariable("b", 0, cat="Integer")

# factory_problem += 50*a + 40*b

# factory_problem += a >= 50
# factory_problem += b >= 40
# factory_problem += 2*a + 3*b <= 300

# factory_problem.solve()

# print(constants.LpStatus[factory_problem.status])
# print(a.varValue, b.varValue)
# print(factory_problem.objective.value())

# investment_problem = LpProblem("investment", LpMaximize)

# decision_vars = [LpVariable(f'x{i}', cat="Binary") for i in range(1, 5)]
# print(decision_vars)

# investment_problem += 40000*decision_vars[0] + 50000*decision_vars[1] + 70000*decision_vars[2] + 25000*decision_vars[3]

# investment_problem += lpSum(decision_vars) <= 3
# investment_problem += 150000*decision_vars[0] + 200000*decision_vars[1] + 300000*decision_vars[2] + 100000*decision_vars[3] <= 500000

# investment_problem += decision_vars[0] <= decision_vars[1]
# investment_problem += decision_vars[2] + decision_vars[3] <= 1

# investment_problem.solve()

# print(constants.LpStatus[investment_problem.status])
# print([v.varValue for v in decision_vars])
# print(investment_problem.objective.value())

# product_problem = LpProblem("product_problem", LpMaximize)

# xm = LpVariable("xm", cat="Binary")
# xl = LpVariable("xl", cat="Binary")
# ym = LpVariable("ym", cat="Binary")
# yl = LpVariable("yl", cat="Binary")
# zm = LpVariable("zm", cat="Binary")
# zl = LpVariable("zl", cat="Binary")

# product_problem += 100000*xm + 70000*xl + 120*800*ym + 120*500*yl + 150*600*zm + 150*400*zl
# product_problem += 500000*xm + 300000*ym + 400000*zm + 200000*xl + 150000*yl + 250000*zl <= 1200000

# product_problem += xm + ym + zm <= 2
# product_problem += xl + yl + zl <= 2
# product_problem += xm + xl <= 1
# product_problem += ym + yl <= 1
# product_problem += zm + zl <= 1

# product_problem.solve()
# print(constants.LpStatus[product_problem.status])
# print(xm.varValue, xl.varValue, ym.varValue, yl.varValue, zm.varValue, zl.varValue)
# print(product_problem.objective.value())

# Vertex cover

# vertices = [1, 2, 3, 4, 5, 6, 7, 8]
# edge_list = [(1, 2), (1, 3), (1, 4), (2, 5), (3, 5), (4, 5), (5, 6), (5, 7), (5, 8)]

# vertex_cover = LpProblem("vertex_cover", LpMinimize)

# decision_vars = [LpVariable(f'x{i}', cat="Binary") for i in range(len(vertices))]

# vertex_cover += lpSum(decision_vars)

# for (i, j) in edge_list:
#     vertex_cover += decision_vars[i - 1] + decision_vars[j - 1] >= 1


# vertex_cover.solve()

# sols = []
# for i in range(len(decision_vars)):
#     if decision_vars[i].varValue == 1.0:
#         sols.append(i + 1)

# print(constants.LpStatus[vertex_cover.status])
# print("Vertices in cover:", sols, vertex_cover.objective.value())

# 0/1 Knapsack

weights = [1, 2, 3, 4]
values = [1, 6, 10, 12]

W = 5

knapsack = LpProblem("knapsack", LpMaximize)

decision_vars = [LpVariable(f'x_{i}', cat="Binary") for i in range(len(weights))]

knapsack += lpSum(decision_vars[i] * values[i] for i in range(len(values)))

knapsack += lpSum(decision_vars[i] * weights[i] for i in range(len(weights))) <= W

# Finish and extract solution