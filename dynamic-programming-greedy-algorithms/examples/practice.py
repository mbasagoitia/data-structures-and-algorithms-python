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

arr = [1, 2, 3, 4, 5]
# print(find_sum([1, 2, 3, 4, 5], 0, len(arr) - 1))

def get_count(arr, left, right):
    