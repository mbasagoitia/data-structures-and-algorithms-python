import heapq

# Create a heap from a list
arr = [4, 1, 7, 3, 8, 5]
heapq.heapify(arr)  # Converts arr into a heap

print(arr)  # Output will be a heap representation: [1, 3, 5, 7, 8, 4]

# Insert a new element into the heap
heapq.heappush(arr, 2)
print(arr)  # Output: [1, 2, 5, 3, 8, 4, 7]

# Extract the smallest element (min-heap)
min_element = heapq.heappop(arr)
print(min_element)  # Output: 1
print(arr)  # Output: [2, 3, 5, 7, 8, 4]

# Peek at the smallest element
print(arr[0])  # Output: 2
