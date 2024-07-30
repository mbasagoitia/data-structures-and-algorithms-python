def merge_sort(arr):
    # Base case for recursion. Array is sorted if it is of length 1
    if len(arr) > 1:
        # Slice of original array from beginning to midpoint (exclusive)
        left_arr = arr[:len(arr)//2]
        # Slice of original array from midpoint (inclusive) to end
        right_arr = arr[len(arr)//2:]

        # Recursive call to merge sort
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Merging subarrays by comparing leftmost elements of each array

        # Current index of left array
        i = 0
        # Current index of right array
        j = 0
        # Current index of merged array
        k = 0

        # Loop runs until it has evaluated every number in each array
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # If there are still elements left in the left subarray
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        # If there are still elements left in the right subarray (must be larger than what's already in merged array)
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

# Without comments

def merge_sort(arr):

    if len(arr) > 1:

        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
