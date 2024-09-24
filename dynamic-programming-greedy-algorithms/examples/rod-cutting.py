# C(i) = max(Vk) + C(i-k) for all k

T = 8
prices = [1, 5, 8, 9, 10, 17, 17, 20]

def rod_cutting(T, prices):
    dp = {}
    dp[0] = 0
    for i in range(1, T + 1):
        dp[i] = max(prices[k - 1] + dp[i - k] for k in range(1, i+1))
    print(dp)
    return dp[T]

print(rod_cutting(T, prices))

# C(i) = min(1 + (C (i - Vk))) for all k

def coin_changing(target, coins):
    dp = {}
    dp[0] = 0
    for i in range(1, target + 1):
        dp[i] = min(1 + dp[i - coins[j]] for j in range(len(coins)) if i - coins[j] >= 0)
    # print(dp)
    return dp[target]

print(coin_changing(2, [1, 2, 5, 10, 20]))