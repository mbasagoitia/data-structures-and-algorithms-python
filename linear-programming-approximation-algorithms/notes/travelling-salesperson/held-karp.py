# Recurrence for TSP
# min(minCostPath(S, e) + Ce1) for all S, e where Ce1 is the cost of going from endpoint e back to vertex 1
# Of course, starting vertex is not included in that subset, and for each iteration of the loop, e is not included in S

# Recurrence for minCostPath
# minCostPath(S, e) = min(Cse + minCostPath(S - s, s)) for all s in S

def minCostPath(S, e):
    dp = {(i, j): }