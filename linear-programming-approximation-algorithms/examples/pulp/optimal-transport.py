from pulp import *
from math import sqrt
def calculate_distance(a, b):
    (xa, ya) = a
    (xb, yb) = b
    return sqrt( (xa- xb)**2 + (ya - yb)**2)
    
def get_objective(var_values, source_coords, dest_coords):
    # A useful function for our test cases: please do not modify
    # It should help you in your code however to see how we calculate the objective function
    obj = sum([ var_values[i][j] * calculate_distance(source_coords[i], dest_coords[j])  for i in range(n) for j in range(m)  ])
    return obj 

def calculate_optimal_transport_plan(source_coords, source_weights, dest_coords, dest_weights):
    n = len(source_coords)
    assert (n== len(source_weights))
    m = len(dest_coords)
    assert (m == len(dest_weights))
    assert( sum(source_weights) == sum(dest_weights)) #
    # Set up a formulation of the optimization problem
    #1. Create the LP model
    lpModel = LpProblem('Optimal Transport', LpMinimize)
    #2. Create a list of decision variables : x_{i,j} for i in range(n) and for j in range(m)
    decision_vars = [[LpVariable(f'x_{i}_{j}', 0) for j in range(m)] for i in range(n)]
    #3. Add the objective function. You can use the function calculate distance to help you 
    lpModel += lpSum([decision_vars[i][j] * calculate_distance(source_coords[i], dest_coords[j]) for i in range(n) for j in range(m)])
    #4. Add the constraints.
    for i in range(n):
        lpModel += lpSum([decision_vars[i][j] for j in range(m)]) == source_weights[i]

    for j in range(m):
        lpModel += lpSum([decision_vars[i][j] for i in range(n)]) == dest_weights[j]
    #5. Solve and extract the solution/return it back in the required form to pass test cases
    # your code here
    lpModel.solve()

    sol = [[decision_vars[i][j].varValue for j in range(m)] for i in range(n)]
    return sol
    raise NotImplementedError