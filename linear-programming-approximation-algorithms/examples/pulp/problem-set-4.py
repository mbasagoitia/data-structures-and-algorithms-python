from pulp import *
def k_tsp_mtz_encoding(n, k, cost_matrix):
    # check inputs are OK
    assert 1 <= k < n
    assert len(cost_matrix) == n, f'Cost matrix is not {n}x{n}'
    assert all(len(cj) == n for cj in cost_matrix), f'Cost matrix is not {n}x{n}'
    prob = LpProblem('kTSP', LpMinimize)
    # finish your implementation here
    # your code must return a list of k-lists [ [0, i1, ..., il], [0, j1,...,jl],...] wherein 
    # the ith entry in our list of lists represents the 
    # tour undertaken by the ith salesperson
    # your code here

    binary_vars = [[[LpVariable(f'x_{k_idx}_{i}_{j}', cat='Binary') if i != j else None
                     for j in range(n)] for i in range(n)] for k_idx in range(k)]
    
    time_stamps = [[LpVariable(f't_{k_idx}_{i}', lowBound=0, cat='Continuous') for i in range(n)] for k_idx in range(k)]

    objective_function = lpSum([binary_vars[k_idx][i][j] * cost_matrix[i][j]
                                for k_idx in range(k)
                                for i in range(n)
                                for j in range(n)
                                if i != j])
    prob += objective_function

    for j in range(1, n):
        prob += lpSum([binary_vars[k_idx][i][j] for k_idx in range(k) for i in range(n) if i != j]) == 1

    for k_idx in range(k):
        prob += lpSum([binary_vars[k_idx][0][j] for j in range(1, n)]) == 1
        prob += lpSum([binary_vars[k_idx][j][0] for j in range(1, n)]) == 1
    
    for k_idx in range(k):
        for i in range(1, n): 
            prob += lpSum([binary_vars[k_idx][i][j] for j in range(n) if i != j]) == lpSum([binary_vars[k_idx][j][i] for j in range(n) if i != j]) 

    for k_idx in range(k):
        for i in range(1, n):
            for j in range(1, n):
                if i != j:
                    xkij = binary_vars[k_idx][i][j]
                    ti = time_stamps[k_idx][i]
                    tj = time_stamps[k_idx][j]
                    prob += tj >= ti + 1 - (n + 1) * (1 - xkij)

    status = prob.solve(PULP_CBC_CMD(msg=True))

    if status != LpStatusOptimal:
        return f'Unexpected non-optimal status: {LpStatus[status]}'

    tours = [[] for _ in range(k)]
    visited_nodes = set()

    for k_idx in range(k):
        tour = [0]
        visited_nodes.add(0)
        current_node = 0

        while len(tour) < n and len(visited_nodes) < n:
            sols = [j for j in range(n) if binary_vars[k_idx][current_node][j] is not None and binary_vars[k_idx][current_node][j].varValue >= 0.999]
            if len(sols) == 0:
                break
            next_node = sols[0]

            if next_node in visited_nodes:
                break

            tour.append(next_node)
            visited_nodes.add(next_node)
            current_node = next_node

        tours[k_idx] = tour

    return tours


def calculate_tour_cost(tour, cost_matrix):
    tour_cost = 0
    for i in range(len(tour) - 1):
        if cost_matrix[tour[i]][tour[i + 1]] is not None:
            tour_cost += cost_matrix[tour[i]][tour[i + 1]]
    # Also add the return to depot cost
    if cost_matrix[tour[-1]][0] is not None:
        tour_cost += cost_matrix[tour[-1]][0]
    return tour_cost

    raise NotImplementedError

cost_matrix=[ [None,3,4,3,5],
             [1, None, 2,4, 1],
             [2, 1, None, 5, 4],
             [1, 1, 5, None, 4],
             [2, 1, 3, 5, None] ]
n=5
k=2

print(k_tsp_mtz_encoding(n, k, cost_matrix))