def max_crossing_sum(arr, left, mid, right):
    # Include elements on the left of mid
    sum_left = float('-inf')
    current_sum = 0
    for i in range(mid, left - 1, -1):
        current_sum += arr[i]
        if current_sum > sum_left:
            sum_left = current_sum

    # Include elements on the right of mid
    sum_right = float('-inf')
    current_sum = 0
    for i in range(mid + 1, right + 1):
        current_sum += arr[i]
        if current_sum > sum_right:
            sum_right = current_sum

    # Return sum of elements on left and right of mid
    return sum_left + sum_right

def max_subarray_sum(arr, left, right):
    # Base case: only one element
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    # Find the maximum sum in the left, right, and crossing subarrays
    left_max = max_subarray_sum(arr, left, mid)
    right_max = max_subarray_sum(arr, mid + 1, right)
    cross_max = max_crossing_sum(arr, left, mid, right)

    # Return the maximum of the three
    return max(left_max, right_max, cross_max)

# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
max_sum = max_subarray_sum(arr, 0, n - 1)
print("Maximum subarray sum is:", max_sum)
