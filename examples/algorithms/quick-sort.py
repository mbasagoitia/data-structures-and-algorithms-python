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

# In-place

def quick_sort(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    if start < end:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, start, end)
        # Recursively sort elements before and after partition
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)

def partition(arr, start, end):
    pivot = arr[end]

    i = start - 1  # Index of smaller element

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Swap arr[i+1] and arr[end] (the pivot)
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1



