from pulp import *
from math import sqrt

# Helper function to calculate Euclidean distance
def calculate_distance(a, b):
    (xa, ya) = a
    (xb, yb) = b
    return sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

def compute_optimal_prices(source_coords, source_weights, dest_coords, dest_weights):
    n = len(source_coords)
    m = len(dest_coords)
    
    lpModel = LpProblem("Optimal_Pricing", LpMaximize)
    
    p = LpVariable.dicts("p", range(n), None)
    p_prime = LpVariable.dicts("p_prime", range(m), None)
    
    D = {}
    for i in range(n):
        for j in range(m):
            D[i, j] = calculate_distance(source_coords[i], dest_coords[j])
    
    lpModel += lpSum([p_prime[j] * dest_weights[j] for j in range(m)]) - lpSum([p[i] * source_weights[i] for i in range(n)])
    
    for i in range(n):
        for j in range(m):
            lpModel += p_prime[j] - p[i] <= D[i, j]

    lpModel.solve()
    
    source_prices = [p[i].varValue for i in range(n)]
    target_prices = [p_prime[j].varValue for j in range(m)]
    
    return source_prices, target_prices

source_coords = [ (1,5), (4,1), (5,5) ]
source_weights = [9, 4, 5]
dest_coords = [ (2,2), (6,6) ]
dest_weights = [9, 9]
n = 3
m = 2
(source_prices, dest_prices) = compute_optimal_prices(source_coords, source_weights, dest_coords, dest_weights)
profit = sum([pi*wi for (pi, wi) in zip(dest_prices, dest_weights)]) - sum([pj*wj for (pj, wj) in zip(source_prices, source_weights)])
assert(abs(profit - 52.22) <= 1E-01), f'Error: Expected profit is {52.22} obtained: {profit}'
print('Test Passed: 7 points')