from pulp import *

def encode_and_solve_three_coloring(n, edge_list):
    assert n >= 1, 'Graph must have at least one vertex'
    assert all( 0 <= i and i < n and 0 <= j and j < n and i != j for (i,j) in edge_list ), 'Edge list is not well formed'
    prob = LpProblem('Three Color', LpMinimize)
    #1. Formulate the decision variables
    decision_vars = [f'x_{i+1}{color}' for i in range(n) for color in ['R', 'G', 'B']]
    #2. Add the constraints for each vertex and edge in the graph.
    # The way you're accessing variables here isn't going to work
    for i in range(n):
        prob += f'x_{i+1}R' + f'x_{i+1}G' + f'x{i+1}B' == 1
    for (i, j) in edge_list:
        prob += f'x_{i + 1}R' + f'x_{j + 1}R' <= 1
        prob += f'x_{i + 1}G' + f'x_{j + 1}G' <= 1
        prob += f'x_{i + 1}B' + f'x_{j + 1}B' <= 1
    #3. Solve and interpret the status of the solution.
    prob.solve()
    #4. Return the result in the required form to pass the tests below.
    print(constants.LpStatus[prob.status])
    print([v.varValue for v in decision_vars])
    # your code here
    raise NotImplementedError

n = 5
edge_list = [(1,2), (1, 3), (1,4), (2, 4), (3,4)]
encode_and_solve_three_coloring(n, edge_list)