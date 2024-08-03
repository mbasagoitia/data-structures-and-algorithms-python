# import heapq

# # Using the python built-in heap data structure
# arr = [4, 1, 7, 3, 8, 5]
# heapq.heapify(arr)  # Converts arr into a heap

# print(arr)  # Output will be a heap representation: [1, 3, 5, 7, 8, 4]

# # Insert a new element into the heap
# heapq.heappush(arr, 2)
# print(arr)  # Output: [1, 2, 5, 3, 8, 4, 7]

# # Extract the smallest element (min-heap)
# min_element = heapq.heappop(arr)
# print(min_element)  # Output: 1
# print(arr)  # Output: [2, 3, 5, 7, 8, 4]

# # Peek at the smallest element
# print(arr[0])  # Output: 2

# Implementing our own heap methods

class Heap:

    length = 0

    def __init__(self, arr):
        self.arr = arr
        self.length = len(arr)

    def insert(self, val):
        self.arr.append(val)
        self.length += 1
        self.bubble_up(self.arr, self.arr[len(self.arr) - 1])

    def delete(self, idx):
        self.arr.pop(idx)
        self.length -= 1
        self.arr[idx] = self.arr.pop()
        self.bubble_down(self.arr, idx)

    def heapify(self):
        for i in range(len(self.arr) - 1, -1, -1):
            # Potential issue here
            self.bubble_down(self, i)

    def get_min(self):
        print(self.arr[0])

    def bubble_up(self, idx):
        if idx <= 0:
            return
        parent_idx = (idx - 1) // 2
        if self.arr[idx] < self.arr[parent_idx]:
            self.arr[parent_idx], self.arr[idx] = self.arr[idx], self.arr[parent_idx]
            self.bubble_up(self, parent_idx)
            return

    def bubble_down(self, idx):
        left_child_idx = idx * 2 + 1
        right_child_idx = idx * 2 + 2
        if left_child_idx >= self.length:
            return
        if left_child_idx < self.length and right_child_idx >= self.length:
            self.arr[idx], self.arr[left_child_idx] = self.arr[left_child_idx], self.arr[idx]
            self.bubble_down(self, left_child_idx)
        else:
            if self.arr[left_child_idx] < self.arr[right_child_idx]:
                smallest = left_child_idx
            else:
                smallest = right_child_idx
            self.arr[idx], self.arr[smallest] = self.arr[smallest], self.arr[idx]
            self.bubble_down(self, smallest)

my_heap = Heap([9, 1, 4, 1, 2, 123, 12, 53])

print(my_heap.arr)
my_heap.heapify()
my_heap.get_min()
print(my_heap.arr)