def quick_sort(arr):
    # Base case: arrays with 0 or 1 elements are already sorted
    if len(arr) <= 1:
        return arr
    # Choose a pivot element from the array (here, we take the last element)
    pivot = arr[-1]
    # Partition the array into three parts:
    # left: elements less than the pivot
    # middle: elements equal to the pivot
    # right: elements greater than the pivot
    left = [x for x in arr[:-1] if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr[:-1] if x > pivot]
    # Recursively apply quick_sort to the left and right parts, then combine
    return quick_sort(left) + middle + quick_sort(right)

# Without comments
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]

    left = [x for x in arr[:-1] if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

