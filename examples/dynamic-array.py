class DynamicArray:
    
    def __init__(self, initial_size=16, initial_fill=0, debug=False):
        self.allocated_size = initial_size
        self.size = 0
        self.array = [initial_fill] * initial_size
        self.debug = debug
    
    # Allows direct access with d[idx]
    def __getitem__(self, idx):
        assert idx >= 0 and idx < self.size
        return self.array[idx]
    
    # Allows writing with d[idx] = val
    def __setitem__(self, idx, val):
        assert idx >= 0 and idx < self.size
        self.array[idx] = val
    
    def append(self, x):
        # Check if there's enough allocated size
        if self.size >= self.allocated_size:
            if self.debug:
                print(f'Ran out of memory: old allocated size: {self.allocated_size}, new allocated size is {2*self.allocated_size}')
            # Double the size of the array
            self.allocated_size = 2 * self.allocated_size
            old_array = self.array
            new_array = allocateMemory(self.allocated_size)
            copyInto(old_array, new_array)
            self.array = new_array
        # Append the element to the end
        self.array[self.size] = x
        self.size += 1

# Example usage

l = DynamicArray(initial_size=1, initial_fill=0, debug=True)
for j in range(1000):
    l.append(j)
print(f'l[5] = {l[5]}')
l[0] = 30
print(f'l[0] = {l[0]}')
