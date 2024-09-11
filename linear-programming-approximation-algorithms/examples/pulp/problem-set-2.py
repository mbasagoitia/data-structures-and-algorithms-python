from pulp import *

def encode_and_solve_three_coloring(n, edge_list):
    assert n >= 1, 'Graph must have at least one vertex'
    assert all( 0 <= i and i < n and 0 <= j and j < n and i != j for (i,j) in edge_list ), 'Edge list is not well formed'
    prob = LpProblem('Three Color', LpMinimize)
    #1. Formulate the decision variables
    decision_vars = {(i+1, color): LpVariable(f'x_{i+1}{color}', 0, 1, cat="Binary") for i in range(n) for color in ['R', 'G', 'B']}
    #2. Add the constraints for each vertex and edge in the graph.
    print(decision_vars)
    for i in range(1, n + 1):
        prob += decision_vars[(i, 'R')] + decision_vars[(i, 'G')] + decision_vars[(i, 'B')] == 1
    for (i, j) in edge_list:
        prob += decision_vars[(i + 1, 'R')] + decision_vars[(j + 1, 'R')] <= 1
        prob += decision_vars[(i + 1, 'G')] + decision_vars[(j + 1, 'G')] <= 1
        prob += decision_vars[(i + 1, 'B')] + decision_vars[(j + 1, 'B')] <= 1
    #3. Solve and interpret the status of the solution.
    prob.solve()
    #4. Return the result in the required form to pass the tests below.
    if LpStatus[prob.status] != 'Optimal':
        return False, []
    
    color_assignment = []
    for i in range(1, n + 1):
        if decision_vars[(i, 'R')].varValue == 1:
            color_assignment.append('r')
        elif decision_vars[(i, 'G')].varValue == 1:
            color_assignment.append('g')
        elif decision_vars[(i, 'B')].varValue == 1:
            color_assignment.append('b')

    return (True, color_assignment)
    # # your code here
    raise NotImplementedError

n = 5
edge_list = [(1,2), (1, 3), (1,4), (2, 4), (3,4)]
encode_and_solve_three_coloring(n, edge_list)

# Write a function solve_warehouse_location(location_coords, R) wherein location_coords is a list of coordinates  [(𝑥0,𝑦0),…,(𝑥𝑛−1,𝑦𝑛−1)]
#   and  𝑅>0
#   is the distance limit. For your convenience, the euclidean_distance between two points is implemented. Setup and solve the ILP using PULP.

# Your code should return a list of indices  [𝑖1,𝑖2,...,𝑖𝑘]
#   which are the optimal locations for the warehouses to be located minimizing the number of warehouses and ensuring that every point is within distance  𝑑
#   of a warehouse.

# Objective: min: sum(w0 ... wn-1)

# Constraints:
# D[j] is the set of all points i where d_i_j <= R
# for all j: sum(D[j]) >= 1

from math import sqrt 

def euclidean_distance(location_coords, i, j):
    assert 0 <= i and i < len(location_coords)
    assert 0 <= j and j < len(location_coords)
    if i == j: 
        return 0.0
    (xi, yi) = location_coords[i] # unpack coordinate
    (xj, yj) = location_coords[j]
    return sqrt( (xj - xi)**2 + (yj - yi)**2 )

    
def solve_warehouse_location(location_coords, R):
    assert R > 0.0, 'radius must be positive'
    n = len(location_coords)
    prob = LpProblem('Warehouselocation', LpMinimize)
    #1. Formulate the decision variables
    decision_vars = [LpVariable(f'w_{i}', 0, 1, cat="Binary") for i in range (n-1)]
    prob += lpSum(decision_vars)
    #2. Add the constraints for each vertex and edge in the graph.
    # I can use the function above... need to interpret how it works
    distances = {(i, j): sqrt((x*i - x*j)**2 + (y*i - y*j)**2) for x, y in range(n) for (i, j) in location_coords}
    print(distances)
    D = []
    for (i, j) in distances:
        if 
    #3. Solve and interpret the status of the solution.
    #4. Return the result in the required form to pass the tests below.
    # your code here
    raise NotImplementedError