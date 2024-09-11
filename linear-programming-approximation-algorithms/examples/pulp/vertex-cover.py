from pulp import *

edge_list = [(1, 2), (1, 3), (1, 4), (2, 3), (3, 4), (2, 6), (3, 6), (3, 5), (4, 5), (6, 5), (4, 7), (5, 7), (6, 7)]

def compute_optimal_vertex_cover(n, edge_list):
    prob = LpProblem('vert_cover', LpMinimize)
    dvars = [LpVariable(f'w_{i}', cat='Binary') for i in range(1, n+1)]
    prob += lpSum(dvars)
    for (i, j) in edge_list:
        assert 1 <= i <= n 
        assert 1 <= j <= n
        prob += dvars[i-1] + dvars[j-1] >= 1
    stat = prob.solve()
    assert stat == LpStatusOptimal, 'Problem does not have optimal status -- something went wrong -- this should not happen for this problem'
    vert_cover = [i+1 for i in range(n) if dvars[i].varValue > 0 ]
    return len(vert_cover)

def compute_lp_relaxation_vertex_cover(n, edge_list):
    prob = LpProblem('vert_cover', LpMinimize)
    dvars = [LpVariable(f'z_{i}', lowBound=0.0, upBound=1.0, cat='Continuous') for i in range(1, n+1)]
    prob += lpSum(dvars)
    for (i, j) in edge_list:
        assert 1 <= i <= n 
        assert 1 <= j <= n
        prob += dvars[i-1] + dvars[j-1] >= 1
    stat = prob.solve()
    assert stat == LpStatusOptimal, 'Problem does not have optimal status -- something went wrong -- this should not happen for this problem'
    vert_cover = [x.varValue for x in dvars]
    return sum(vert_cover)

# print(compute_optimal_vertex_cover(len(edge_list), edge_list))
print(compute_lp_relaxation_vertex_cover(len(edge_list), edge_list))

