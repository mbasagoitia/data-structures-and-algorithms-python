def merge_sort(arr):
    # Base case: if the array has one or zero elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively split and sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge the sorted halves
    return merge(sorted_left, sorted_right)

def merge(left, right):
    # Initialize an empty result list and pointers for left and right arrays
    result = []
    i = 0
    j = 0

    # Merge the two lists until one is exhausted
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements in the left list
    while i < len(left):
        result.append(left[i])
        i += 1

    # Append any remaining elements in the right list
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# Without comments

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# Another implementation, modifies array in-place

def merge_sort(arr, left, right):
    # Base case: check if the subarray has 1 or 0 elements (already sorted, do nothing)
    if left >= right:
        return
    
    # Calculate the midpoint to split the array into two halves
    mid = (left + right) // 2
    
    # Recursively sort the left half
    merge_sort(arr, left, mid)
    
    # Recursively sort the right half
    merge_sort(arr, mid + 1, right)
    
    # Merge the sorted halves back into the original array
    merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    # Initialize pointers for traversing the left (i) and right (j) halves
    i = left
    j = mid + 1
    temp = []

    # Merge elements from the two halves into temp in sorted order
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    # Append any remaining elements from the left half
    while i <= mid:
        temp.append(arr[i])
        i += 1

    # Append any remaining elements from the right half
    while j <= right:
        temp.append(arr[j])
        j += 1

    # Copy the sorted elements from temp back to the original array, offset by left
    for k in range(len(temp)):
        arr[left + k] = temp[k]
