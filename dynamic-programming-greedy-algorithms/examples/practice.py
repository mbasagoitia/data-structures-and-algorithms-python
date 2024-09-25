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



print(min_cost_path(grid))

T = 12
coins = [1, 2, 5, 10]

def coin_change(T, coins):
    dp = [float("inf")] * (T + 1)
    dp[0] = 0 

    for i in range(1, T + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[T] if dp[T] != float("inf") else -1


print(coin_change(T, coins))