# def mk_adjacency_list(n, edge_list):
#     adj_list = [set() for i in range(n)]
#     for (i,j) in edge_list:
#         adj_list[i].add(j)
#         adj_list[j].add(i)
#     return adj_list

# # Test Partition
# def test_cut(n, adj_list, cut):
#     num_edges_crossing_cut = [0]*n
#     for (i, neighbors) in enumerate(adj_list):
#         num_edges_crossing_cut[i] = sum([cut[i] != cut[j] for j in neighbors])
#         if 2 * num_edges_crossing_cut[i] < len(neighbors):
#             assert f'Test Failed: In your cut, vertex {i} has {len(neighbors)} edges incident on it but only {num_edges_crossing_cut[i]} edges cross the cut'
#     return 


# def find_balanced_cut(n, adj_list):
#     assert n >= 1
#     assert len(adj_list) == n

#     # Check that the adjacency list makes sense and represents a directed graph
#     for (i, neighbors) in enumerate(adj_list):
#         assert all(0 <= j < n for j in neighbors)
#         assert i not in neighbors  # no self-loops allowed
#         for j in neighbors: 
#             assert i in adj_list[j]

#     # Initialize the cut: first half in S1 (True), second half in S2 (False)
#     cut = [True if i < n / 2 else False for i in range(n)]

#     while True:
#         idx = find_imbalanced_node(adj_list, cut)
#         if idx is False:
#             break
#         else:
#             cut[idx] = not cut[idx]

#     return cut

# def find_imbalanced_node(adj_list, cut):
#     for i in range(len(adj_list)):
#         same_set_edges = sum(1 for j in adj_list[i] if cut[i] == cut[j])
#         if same_set_edges > len(adj_list[i]) // 2:
#             return i
#     return False


# n = 5
# edge_list =  [(0,1),(0,2),(0,3),(0,4), (1,2),(1,3),(2,4),(3,4)]
# adj_list = mk_adjacency_list(n, edge_list)

# print(find_balanced_cut(n, adj_list))

from math import sqrt

def euclidean_distance(a, b):
    (xa, ya) = a
    (xb, yb) = b
    return sqrt( (xb - xa)**2 + (yb - ya)**2)


# Function find_farthest_point_from_current_centers
# returns a pair (j, rj) where 
# - 0 <= j < len(coords) is the index of the farthest point P_j
# - rj is the distance of the point P_j from its nearest center
def find_farthest_point_from_current_centers(coords, center_indices):
    n = len(coords)
    assert all( 0 <= j < n for j in center_indices)
    rj_values = [ (min([euclidean_distance(xi, coords[j]) for j in center_indices]), i) for (i, xi) in enumerate(coords)]
    (rj, j) = max(rj_values)
    return (j, rj)

## Implement a function greedy_k_centers that given a list of coordinates `coords`, returns center_list, R
##   - centers_list is a list of indices [j1,..., jk]. Note that coords[j1], ..., coords[jk] will yield coordinates of the actual centetr.
##   - R is the radius resulting from the choice of the k centers
## Please use the implementation of find_farthest_point_from_current_centers above.
def greedy_k_centers(coords, k, debug=True): ## Please print messages from this function only if debug flag is True
    centers = [0] # Add the very first point 
    if debug:
        print(f'Initial center: {coords[0]}')
    # your code here
    for i in range(1, k):
        (farthestIdx, distance) = find_farthest_point_from_current_centers(coords[1::], centers)
        if farthestIdx not in centers:
            centers.append(farthestIdx)
    (farthestIdx, distance) = find_farthest_point_from_current_centers(coords[1::], centers)
    return (centers, farthestIdx)
    raise NotImplementedError

coords = [(1,2), (3,5), (4,7), (8, 14), (9,3), (7,7), (6,5), (4, 6), (5,2), (1,8)]
(center_indices, R) = greedy_k_centers(coords, 2)
print(center_indices, R)
