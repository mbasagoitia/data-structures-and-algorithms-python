# Maximum Subarray Problem Using Divide and Conquer

Given an array A with size n, find the maximum possible value of the difference between two indices i and j, where 1 <= i <= j <= n

## Brute Force Approach

max = 0
for i up to n - 1
    for j from i + 1 up to n
        max = max(max A[j] - A[i])
return max

This approach uses two nested for loops, which has O(n^2) time complexity. We can do better!

## Divide and Conquer Approach

- Divide array into two halves (A[1] to A[n/2] and A[n/2 + 1] to A[n])
- Recursively determine the max subarray of the left side, right side, and max subarray that crosses the midpoint
- In the third case, you compare the minimum element from the left subarray with the maximum element from the right subarray
- The best solution is the maximum difference from each of the three cases

## Pseudocode for Max Subarray

def max_subarray(A, l, u)
    # base cases
    # subarray only has one element
    if u == l
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
    x1 = min_element(A, l, m)
    y1 = max_element(A, m + 1, u)

    return max(m1, m2, y1 - x1)

def min_element(A, l, u):
    min_elt = infinity
    for i from l to u:
        min_elt = min(min_elt, A[i])
    return min_elt

Basically same logic for max_element

## Time Complexity

Base case:

- T(n) = O(1) if n <= 2 (trivial)
Recursive calls:

- Calculating midpoint = O(1)
- Each recursive call = T(n/2) (runs on half of the input size)
- Computing max/min elements; entire array in worst case = O(n)
- Computing max of the three numbers = O(1)

Adding these up we get 2*T(n/2) + 2*O(n) + 3*O(1) or

2T(n/2) + O(n)

Simplifies to O(n log(n))