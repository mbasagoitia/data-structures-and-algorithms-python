# C(i) = max(Vk) + C(i-k) for all k

T = 8
prices = [1, 3, 7, 8, 9, 10, 11, 15]

def rod_cutting(T, prices):
    dp = {}
    dp[0] = 0
    for i in range(1, T + 1):
        dp[i] = max([prices[k - 1] + dp[i - k] for k in range(1, i)])

    return dp[T]

print(rod_cutting(T, prices))