from pulp import *

def formulate_lp_problem(m, n, list_c, list_a, list_b):
    assert n > 0
    assert m > 0
    assert len(list_c) == n
    assert len(list_a) == len(list_b) and len(list_b) == m
    assert all(len(l) == n for l in list_a)
    lpModel = LpProblem('LPProblem', LpMaximize)
    ## 1. Create all the decision variables and store all the decision variables in a list
    decision_vars = [ LpVariable(f'x{i}', None, None) for i in range(n) ] 
    ## 2. Create the objective function 
    obj_func = 0
    for i in range(n):
        obj_func += list_c[i] * decision_vars[i]
        
    lpModel += obj_func
    ## 3. Create all the constraints
    # your code here
    for i in range (m):
        constraint = 0
        for j in range (n):
            constraint += list_a[i][j] * decision_vars[j]
        constraint = constraint <= list_b[i]
        print (constraint)
        lpModel += (constraint)

    lpModel.solve()
    print('Status is :', LpStatus[lpModel.status])
        
    isFeasible = lpModel.status != constants.LpStatusInfeasible
    isBounded = lpModel.status != constants.LpStatusUnbounded
    
    if lpModel.status == constants.LpStatusOptimal:
        return (isFeasible, isBounded, [x.varValue for x in decision_vars])
    else:
        return (isFeasible, isBounded, [])
    raise NotImplementedError
    
    
m = 5
n = 4 
list_c = [-1, 2, 1, 1]
list_a = [ [ 1, 0, -1, 2], [2, -1, 0, 1], [1, 1, 1, 1], [1, -1, 1, 1], [0, -1, 0, 1]]
list_b = [3, 4, 5, 2.5, 3]
(is_feas, is_bnded, sols) = formulate_lp_problem(m, n, list_c, list_a, list_b)
assert is_feas, "The LP should be feasible. But your code returns a status of infeasible."
assert not is_bnded, "The LP should be unbounded but your code returns a status of bounded."
print('Passed: 3 points')