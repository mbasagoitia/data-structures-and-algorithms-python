# from pulp import *
# from math import sqrt

# # Helper function to calculate Euclidean distance
# def calculate_distance(a, b):
#     (xa, ya) = a
#     (xb, yb) = b
#     return sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

# def compute_optimal_prices(source_coords, source_weights, dest_coords, dest_weights):
#     n = len(source_coords)
#     m = len(dest_coords)
    
#     lpModel = LpProblem("Optimal_Pricing", LpMaximize)
    
#     p = LpVariable.dicts("p", range(n), None)
#     p_prime = LpVariable.dicts("p_prime", range(m), None)
    
#     D = {}
#     for i in range(n):
#         for j in range(m):
#             D[i, j] = calculate_distance(source_coords[i], dest_coords[j])
    
#     lpModel += lpSum([p_prime[j] * dest_weights[j] for j in range(m)]) - lpSum([p[i] * source_weights[i] for i in range(n)])
    
#     for i in range(n):
#         for j in range(m):
#             lpModel += p_prime[j] - p[i] <= D[i, j]

#     lpModel.solve()
    
#     source_prices = [p[i].varValue for i in range(n)]
#     target_prices = [p_prime[j].varValue for j in range(m)]
    
#     return source_prices, target_prices

# source_coords = [ (1,5), (4,1), (5,5) ]
# source_weights = [9, 4, 5]
# dest_coords = [ (2,2), (6,6) ]
# dest_weights = [9, 9]
# n = 3
# m = 2
# (source_prices, dest_prices) = compute_optimal_prices(source_coords, source_weights, dest_coords, dest_weights)
# profit = sum([pi*wi for (pi, wi) in zip(dest_prices, dest_weights)]) - sum([pj*wj for (pj, wj) in zip(source_prices, source_weights)])
# assert(abs(profit - 52.22) <= 1E-01), f'Error: Expected profit is {52.22} obtained: {profit}'
# print('Test Passed: 7 points')

from pulp import LpVariable, LpProblem, LpMaximize, lpSum, LpStatus, value

# Number of variables
n = 2
# Number of inequalities
m = 6

# A list of list of coefficients of the LHS of inequalities
c_matrix = [
    [1, -1],
    [1, 2],
    [-1, 0],
    [1, 0],
    [-1, 0],
    [1, 0]
]

# d_values: a list of RHS coefficients
d_list = [-5, 3, -4, -2, -3, -1]

# Bounds: a list of pairs for each variable
bounds = [(-10, 10), (-10, 10)]

# Define the decision variables for x and binary w
decision_vars_x = [LpVariable(f'x{k}', lowBound=bounds[k][0], upBound=bounds[k][1]) for k in range(n)]
decision_vars_w = [LpVariable(f'w{l}', 0, 1, cat="Binary") for l in range(m)]

# Create the maximization problem
max_problem = LpProblem("max_problem", LpMaximize)

# Maximize the sum of the binary variables (i.e., the number of constraints satisfied)
max_problem += lpSum(decision_vars_w)

# Calculate big M values
M = [0] * m
for i in range(m):
    maximum_val = 0
    for j in range(n):
        if c_matrix[i][j] >= 0:
            maximum_val += c_matrix[i][j] * bounds[j][1]
        else:
            maximum_val += c_matrix[i][j] * bounds[j][0]
    M[i] = maximum_val

# Add constraints to the problem with "big M" approach
for i in range(m):
    max_problem += (lpSum(c_matrix[i][j] * decision_vars_x[j] for j in range(n))) <= (d_list[i] + M[i] * (1 - decision_vars_w[i]))
    # Print each constraint for debugging
    print(f"Constraint {i}: {lpSum(c_matrix[i][j] * decision_vars_x[j] for j in range(n))} <= {d_list[i]} + {M[i]} * (1 - {decision_vars_w[i]})")

# Add bounds for x variables explicitly
for i in range(n):
    max_problem += decision_vars_x[i] >= bounds[i][0], f"x{i}_lower_bound"
    max_problem += decision_vars_x[i] <= bounds[i][1], f"x{i}_upper_bound"

# Now solve the problem
max_problem.solve()

# Output the results
print("Status:", LpStatus[max_problem.status])
print("Decision variables x:", [value(v) for v in decision_vars_x])
print("Binary variables w (constraints satisfied):", [value(v) for v in decision_vars_w])
print("Objective value (max number of constraints satisfied):", value(max_problem.objective))
