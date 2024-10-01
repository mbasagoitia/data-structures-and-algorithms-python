def fib(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def steps(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# print(steps(9))

# Recurrence: grid[m][n] = grid[m, n] + min(mcp(m + 1, n), mcp(m, n + 1))

grid = [[1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]]

def min_cost_path(grid):
    m = len(grid)
    n = len(grid[0])

    dp = [[0 for _ in range(n)] for _ in range(m)]

    dp[m-1][n-1] = grid[m-1][n-1]

    for i in range(n-2, -1, -1):
        dp[m-1][i] = grid[m-1][i] + dp[m-1][i+1]

    for j in range(m-2, -1, -1):
        dp[j][n-1] = grid[j][n-1] + dp[j+1][n-1]

    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])

    # Recover the solution
    sol = []

    a = 0
    b = 0

    while(a < m - 1 or b < n - 1):
        if a == m - 1:
            sol.append("Right")
            b += 1
        elif b == n - 1:
            sol.append("Down")
            a += 1
        else:
            if dp[a][b + 1] < dp[a + 1][b]:
                sol.append("Right")
                b += 1
            else:
                sol.append("Down")
                a += 1

    return (dp[0][0], sol)



# print(min_cost_path(grid))

T = 2534
coins = [1, 2, 5, 10, 250]

def coin_change(T, coins):
    dp = [float("inf")] * (T + 1)
    S = [None] * (T + 1)
    S[0] = 0
    dp[0] = 0

    for i in range(1, T + 1):
        local_min = float("inf")
        coin_used = None
        for coin in coins:
            if i - coin >= 0:
                if 1 + dp[i - coin] < local_min:
                    local_min = 1 + dp[i - coin]
                    coin_used = coin
        dp[i] = local_min
        S[i] = coin_used

    # print(dp)
    # print(S)

    target = T
    sol = []

    while target > 0:
        sol.append(S[target])
        target -= S[target]

    return dp[T] if dp[T] != float("inf") else -1, sol


# print(coin_change(T, coins))

# Recurrence: dp[i] = max(1,1+dp[j]) for all j>i where nums[j]>nums[i]

nums = [10, 9, 2, 5, 3, 7, 101, 18]

def lis(nums):
    dp = [1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        max_value = 0
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                if dp[j] > max_value:
                    max_value = dp[j]
        dp[i] = max_value + 1

    print(dp)

    return max(dp)

# print(lis(nums))

# def lcs(s1, s2):
#     # See problem statement

arr = [1, 2, 3, 4, 5, 6, 7]
target = 5

def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)

# print(binary_search(arr, target, 0, len(arr) - 1))

arr = [2, 4, 1, 7, 5]

def find_min_max(arr, left, right):
    # Base case: If the array contains only one element
    if left == right:
        return arr[left], arr[left]

    # Base case: If the array contains two elements
    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]

    # Divide the array into two halves
    mid = (left + right) // 2
    min1, max1 = find_min_max(arr, left, mid)
    min2, max2 = find_min_max(arr, mid + 1, right)

    # Combine the results from both halves
    overall_min = min(min1, min2)
    overall_max = max(max1, max2)

    return overall_min, overall_max

# Example usage:
# arr = [2, 4, 1, 7, 5]
min_value, max_value = find_min_max(arr, 0, len(arr) - 1)
print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")

def find_sum(arr, left, right):
    if left == right:
        return arr[left]
    if right == left + 1:
        return arr[left] + arr[right]
    mid = (left + right) // 2

    return find_sum(arr, left, mid) + find_sum(arr, mid + 1, right)

# print(find_sum([1, 2, 3, 4, 5], 0, len(arr) - 1))

def get_count(arr, left, right):
    if left == right:
        return 1
    mid = (left + right) // 2

    return get_count(arr, left, mid) + get_count(arr, mid + 1, right)

# print(get_count(arr, 0, len(arr) - 1))

def reverse_arr(arr, left, right):
    if left >= right:
        return arr
    arr[left], arr[right] = arr[right], arr[left]
    return reverse_arr(arr, left + 1, right - 1)

# print(reverse_arr(arr, 0, len(arr) - 1))

arr = [1, 2, 3, 131, 5, 6, 7]
def find_max(arr, left, right):
    if left == right:
        return arr[left]
    if right == left + 1:
        if arr[left] > arr[right]:
            return arr[left]
        else:
            return arr[right]
    mid = (left + right) // 2
    max_el = max(find_max(arr, left, mid), find_max(arr, mid + 1, right))
    return max_el

print(find_max(arr, 0, len(arr) - 1))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(5))

def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)

# print(sum_of_digits(325))

def is_palindrome(s, left, right):
    if left == right:
        return True
    if right == left + 1:
        if s[left] == s[right]:
            return True
        else:
            return False
    if s[left] == s[right]:
        return is_palindrome(s, left + 1, right - 1)
    else:
        return False
    
s = "racecar"
# print(is_palindrome(s, 0, len(s) - 1))

def calculate_power(x, n):
    if n == 0:
        return 1
    
    if n % 2 == 0:
        return calculate_power(x, n//2) ** 2
    else:
        return x * calculate_power(x, n - 1)

# print(calculate_power(3, 4))

def merge_sorted_arrs(arr1, arr2):
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    merged = []
    if arr1[0] < arr2[0]:
        merged = [arr1[0]] + merge_sorted_arrs(arr1[1:], arr2)
    else:
        merged = [arr2[0]] + merge_sorted_arrs(arr1, arr2[1:])

    return merged

# print(merge_sorted_arrs([1, 2, 5], [4, 6, 9]))

def unique_paths(m, n):
    if m == 1 or n == 1:
        return 1
    return unique_paths(m, n - 1) + unique_paths(m - 1, n)

# print(unique_paths(3, 5))

def find_sum(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    return find_sum(arr, left, mid) + find_sum(arr, mid + 1, right)

arr3 = [1, 2, 4, 3]

# print(find_sum(arr3, 0, len(arr3) - 1))

def greater_than(arr, value, left, right):
    if left == right:
        if arr[left] > value:
            return 1
        else:
            return 0
    
    mid = (left + right) // 2
    return greater_than(arr, value, left, mid) + greater_than(arr, value, mid + 1, right)

arr4 = [5, 2, 7, 9, 10, 23, 6, 1, 655, 3]
# print(greater_than(arr4, 1, 0, len(arr4) - 1))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

def merge(left, right):
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

# print(merge_sort(arr4))

def kth_smallest(arr, k):
    if len(arr) <= 1:
        return arr
    
    # Come back to this

def fibonacci(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range (2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# print(fibonacci(9))

arr5 = [4, 5, 19, 3, 1, 2, 4546, 6]

def max_difference(arr, left, right):
    if left == right:
        return 0
    if right == left + 1:
        return max(0, arr[right] - arr[left])
    
    mid = (left + right) // 2

    max_left = max_difference(arr, left, mid)
    max_right = max_difference(arr, mid + 1, right)
    max_crossing = max_elt(arr, mid + 1, right) - min_elt(arr, left, mid)

    return max(max_left, max_right, max_crossing)

def max_elt(arr, left, right):
    maximum = float("-inf")
    for i in range(left, right + 1):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum

def min_elt(arr, left, right):
    minimum = float("inf")
    for i in range(left, right + 1):
        if arr[i] < minimum:
            minimum = arr[i]
    return minimum

# print(max_difference(arr5, 0, len(arr5) - 1))

def quick_sort(arr, left, right):
    if left < right:
        pivot_idx = partition(arr, left, right)
    
        quick_sort(arr, left, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, right)
    
def partition(arr, left, right):
    pivot = arr[right]

    i = left - 1

    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    
    return i + 1