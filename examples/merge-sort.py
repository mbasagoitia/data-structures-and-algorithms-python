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

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
