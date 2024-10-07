# Recurrence for TSP
# min(minCostPath(S, e) + Ce1) for all S, e where Ce1 is the cost of going from endpoint e back to vertex 1
# Of course, starting vertex is not included in that subset, and for each iteration of the loop, e is not included in S

# Recurrence for minCostPath
# minCostPath(S, e) = min(Cse + minCostPath(S - s, s)) for all s in S

def memoize_min_cost_path(n, cost_matrix, debug=False):
    ## Maintaining a memo table and iterating through all sets of size $k$ systematically is  very tricky.
    ## We will just use inbuilt python data structures for this task.
    tbl = [] # Our table is simply a list of dictionaries. Each dictionary in our list is a memo table for sets of a fixed size $j$
    sol_tbl = [] # corresponding to tbl, we will hold the minimizing entry in sol_tbl to be able to recover the solution
    # tbl[i] is a dictionary that will hold all sets $S$ of size $i$ and end points e.
    # Also note that while we presented our algorithm to start from index 1, we will 
    # start our code from index 0. Therefore, vertex 0 is the starting point.
    assert len(cost_matrix) == n, f'Cost matrix is not {n}x{n}'
    assert all(len(cj) == n for cj in cost_matrix), f'Cost matrix is not {n}x{n}'
    # start by seeding the dictionary with S = emptyset
    mcp0 = {}
    sol0 = {}
    for e in range(1, n):
        S = frozenset() # frozenset in Python is an immutable set that can be hashed
        mcp0[(S, e)] = cost_matrix[0][e] # this is the base case when S = \emptyset as explained in notes above.
        sol0[(S, e)] = 0 # the previous vertex is just the start vertex 0
    tbl.append(mcp0) # add the "cost-to-go" dictionary to table
    sol_tbl.append(sol0) # add the solution dictionary to the solution table.
    ## now build up for set sizes from 1 to n-1. Set size 0 is already built and added to list at start.
    for size in range(1, n-1):
        mcp_prev = tbl[-1] # fetch the table for sets of size $n-1$.
        mcp = {} # initialize the current table
        sol = {} # initialize the current solution table
        # run through all sets of cardinality size-1
        for ((S, s), v) in mcp_prev.items():  
            assert len(S) == size-1, 'invariant failed -- the algorithm has been implemented wrong if this assertion fails'
            S_new = S.union(frozenset({s})) # make S_new = S Union {s}
            for e in range(1, n): # run through all possible end points 
                if e in S_new: # skip all end points already in the set S_new
                    continue
                new_path_cost = v + cost_matrix[s][e] # compute path cost using recursion
                old_path_cost = mcp.get((S_new, e)) # if the entry has already been added to the dictionary look it up
                old_sol = sol.get((S_new, e))
                if old_path_cost == None or old_path_cost > new_path_cost:  # if entry is not already in dictionary or tthe current solution is better than previous, replace
                    mcp[(S_new, e)] = new_path_cost
                    sol[(S_new, e)] = s
        tbl.append(mcp) # mcp is the memo table for sets of cardinality equal to the loop index size
        sol_tbl.append(sol) # sol_tbl is to be appended as well.
        if debug: # print stuff for our debugging
            print(f'Sets of size {size}')
            for ((S,e), v) in mcp.items():
                print(f'\t {S}, {e} --> {v}')
    ## Now compute best TSP tour and recover solution.
    mcp = tbl[-1] # pick up last entry 
    sol = sol_tbl[-1] 
    
    min_cost_tour = float('inf')
    end_pt = None
    # Now find the best TSP tour by using the equation that relates minCostPath to minTSPTour
    for e in range(1, n): # run through all end points
        S = frozenset({i for i in range(1, n) if i != e}) # create set S of all vertices other than e
        assert (S,e) in sol  
        v = mcp[(S,e)] # look up minCostPath(S,e)
        if v + cost_matrix[e][0] < min_cost_tour: # add the cost of retutrning from end point e to 0 to v
            min_cost_tour =  v + cost_matrix[e][0] # is it better than previous solution, if so replace.
            end_pt = e
    if debug:
        print(f'Minimum cost TSP tour: {min_cost_tour}')
        print(f'Last vertex visited before cycling back: {e}')
    # end_pt is the last vertex before cycling back to vertex 0.
    # Let's recover the tour now in the reverse order
    tour = [end_pt]
    S = frozenset({j for j in range(1, n) if j != end_pt}) # this is the set of nodes to visit
    for i in range(n-2, 0, -1):
        assert len(S) == i, f'{len(S)}, {i}'
        sol = sol_tbl[i]
        e = tour[-1]
        assert (S, e) in sol, f'Entry {(S,e)} missing from solution table: {sol}'
        new_end_pt = sol[(S,e)]
        if debug:
            print(f'Recovering solution: looking up sol[{(S, e)}] -> new end point: {new_end_pt}')
        assert new_end_pt in S
        tour.append(new_end_pt) # add new end point to the tour but remember to reverse the whole list at the end or else tour will be in reverse order 
        S = frozenset({j for j in S if j != new_end_pt}) # remove new_end_pt from the set S
        assert len(S) == i-1, f'{len(S)}, {i-1}'
    tour.append(0)
    tour.reverse() # reverse the tour since we have been appending to the end
    if debug:
        print(f'Tour:{tour}, cost: {min_cost_tour}')
    return tour, min_cost_tour