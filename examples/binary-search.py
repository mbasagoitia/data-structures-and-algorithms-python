# Binary search

# Iterative solution

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while (left <= right):
        midIndex = ((left + right) // 2)

        if target == arr[midIndex]:
            return midIndex
        elif target < arr[midIndex]:
            right = midIndex - 1
        elif target > arr[midIndex]:
            left = midIndex + 1
            
    return -1

# Recursive solution

def binary_search_recursive(arr, target, left, right):

    if left <= right:
        midIndex = ((left + right) // 2)
        if target == arr[midIndex]:
            return midIndex
        elif target < arr[midIndex]:
            return binary_search_recursive(arr, target, left, midIndex - 1)
        else:
            return binary_search_recursive(arr, target, midIndex + 1, right)
    else:
        return -1


    
