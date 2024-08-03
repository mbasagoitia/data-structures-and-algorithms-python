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

    heapified = False

    def __init__(self, arr):
        self.arr = arr

    def insert(self, val):
        self.arr.append(val)
        self.bubble_up(self.arr, len(self.arr) - 1)

    def delete(self, idx):
        if len(self.arr) > 1:
            # Replace the element to be deleted with the last element
            self.arr[idx] = self.arr.pop()
            # Restore the heap property by bubbling down the replaced element
            self.bubble_down(self.arr, idx, len(self.arr) - 1)
        else:
            # If only one element was in the heap, just remove it
            self.arr.pop()

    def heapify(self):
        for i in range((len(self.arr) // 2) - 1, -1, -1):
            self.bubble_down(self.arr, i, len(self.arr) - 1)
        self.heapified = True

    def get_min(self):
        if self.heapified:
            print(self.arr[0])
        else:
            self.heapify()
            print(self.arr[0])

    def bubble_up(self, heap, idx):
        if idx <= 0:
            return
        parent_idx = (idx - 1) // 2
        if heap[idx] < heap[parent_idx]:
            heap[parent_idx], heap[idx] = heap[idx], heap[parent_idx]
            self.bubble_up(heap, parent_idx)
            return

    def bubble_down(self, heap, idx, end):
        left_child_idx = idx * 2 + 1
        right_child_idx = idx * 2 + 2
        # If no left child, there is no right child
        if left_child_idx > end:
            return
        # If the left child is present but the right is not
        if left_child_idx <= end and right_child_idx > end:
            # If the node is in the incorrect place relative to its left child
            if heap[idx] > heap[left_child_idx]:
                heap[idx], heap[left_child_idx] = heap[left_child_idx], heap[idx]
                self.bubble_down(heap, left_child_idx, end)
        # If both children are present
        elif left_child_idx <= end and right_child_idx <= end:
            # If the node is in the incorrect place relative to either child
            if heap[idx] > heap[left_child_idx] or heap[idx] > heap[right_child_idx]:
                if heap[left_child_idx] < heap[right_child_idx]:
                    smallest = left_child_idx
                else:
                    smallest = right_child_idx
                heap[idx], heap[smallest] = heap[smallest], heap[idx]
                self.bubble_down(heap, smallest, end)

    def heapsort(self):
        self.heapify()
        end = len(self.arr) - 1
        while end > 0:
            # Swap the root (minimum element) with the last element in the current heap
            self.arr[0], self.arr[end] = self.arr[end], self.arr[0]
            # Reduce the size of the heap by one
            end -= 1
            # Bubble down the new root element to restore the heap property
            self.bubble_down(self.arr, 0, end)



my_heap = Heap([1, 3, 2, 4])
my_heap.heapify()
print("heapified", my_heap.arr)
my_heap.heapsort()
print("sorted", my_heap.arr)
