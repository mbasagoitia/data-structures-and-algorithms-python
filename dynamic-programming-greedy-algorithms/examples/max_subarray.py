def max_subarray(A, l, u):
    # base cases
    # subarray only has one element
    if u == l:
        return 0
    # subarray has two elements
    elif u == l + 1:
        return max(A[u] - A[l], 0)

    # calculate midpoint
    m = (l + u) // 2
    # Find maximum from the left and right half recursively
    m1 = max_subarray(A, l, m)
    m2 = max_subarray(A, m + 1, u)
    # find maximum from portion that crosses the midpoint
    y1 = max_element(A, m + 1, u)
    x1 = min_element(A, l, m)

    return max(m1, m2, y1 - x1)

def min_element(A, l, u):
    min_elt = float('inf')
    for i in range(l, u + 1):
        min_elt = min(min_elt, A[i])
    return min_elt

def max_element(A, l, u):
    max_elt = float('-inf')
    for i in range(l, u + 1):
        max_elt = max(max_elt, A[i])
    return max_elt

# Without comments

def max_subarray(A, l, u):
    if u == l:
        return 0
    elif u == l + 1:
        return max(A[u] - A[l], 0)

    m = (l + u) // 2
    m1 = max_subarray(A, l, m)
    m2 = max_subarray(A, m + 1, u)

    y1 = max_element(A, m + 1, u)
    x1 = min_element(A, l, m)

    return max(m1, m2, y1 - x1)

def min_element(A, l, u):
    min_elt = float('inf')
    for i in range(l, u + 1):
        min_elt = min(min_elt, A[i])
    return min_elt

def max_element(A, l, u):
    max_elt = float('-inf')
    for i in range(l, u + 1):
        max_elt = max(max_elt, A[i])
    return max_elt

