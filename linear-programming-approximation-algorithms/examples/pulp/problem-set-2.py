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