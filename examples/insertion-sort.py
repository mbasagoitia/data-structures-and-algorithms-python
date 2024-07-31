# Insertion sort implementation

def insertion_sort(arr):
    # Looping through the second element (the first is already considered the "sorted half" of the array) to the end
    for i in range(1, len(arr)):
        # Points to the second element, will initially compare against first element
        j = i
        # If current element is larger than the preceding element but greater than 0
        while arr[j - 1] > arr[j] and j > 0:
            # Swap the two elements
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            # Continue left through the list
            j -= 1

# Without comments

def insertion_sort(arr):

    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1