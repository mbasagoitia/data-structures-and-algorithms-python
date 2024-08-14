# Approach with memoization

def rod_cutting_memoization(prices, n, memo={}):
    if n in memo:
        return memo[n]
    
    if n == 0:
        return 0
    
    max_revenue = float('-inf')
    for i in range(1, n + 1):
        max_revenue = max(max_revenue, prices[i - 1] + rod_cutting_memoization(prices, n - i, memo))
    
    memo[n] = max_revenue
    return max_revenue

# Approach with tabulation

def rod_cutting_tabulation(prices, n):
    dp = [0] * (n + 1)
    
    for j in range(1, n + 1):
        max_revenue = float('-inf')
        for i in range(1, j + 1):
            max_revenue = max(max_revenue, prices[i - 1] + dp[j - i])
        dp[j] = max_revenue
    
    return dp[n]
