def coin_changing(target, coins):
    dp = {}
    dp[0] = 0
    for i in range(1, target + 1):
        dp[i] = min(1 + dp[i - coins[j]] for j in range(len(coins)) if i - coins[j] >= 0)
    print(dp)
    return dp[target]

print(coin_changing(2, [1, 2, 5, 10, 20]))

def minCoinsBottomUpMemoTable(lst,x):
    n = len(lst)
    # Create a memo table with (x+1) rows and (n+1) columns
    memoTbl =  [ [0 for i in range(0,n+1) ] for j in range(0,x+1) ]
    solutionTbl = [[ -1 for i in range(0,n+1)] for j in range(0,x+1)]
    # No need to fill in the 0s in the table
    for y in range(1,x+1):
        memoTbl[y][0] = 1000000
        for j in range(1,n+1):
            cj = lst[j-1]
            if (y < cj):
                memoTbl[y][j] = memoTbl[y][j-1]
                solutionTbl[y][j] = 0
            else:
                pj = int(y/cj)
                assert(pj > 0)
                minValue= 1000000
                bestOption = -1
                for i in range(0,pj+1):
                    l = i+memoTbl[y-i*cj][j-1]
                    if (l < minValue):
                        minValue = l
                        bestOption = i
                #Update memo table and solution tables
                memoTbl[y][j] = minValue
                solutionTbl[y][j] = bestOption
    # Done
    print('Minimum number of coins needed:', memoTbl[x][n])
    # Extracting solution
    j = n
    y = x
    while (y > 0 and j >= 0):
        k = solutionTbl[y][j]
        print('Coin:', lst[j-1], ' # Times:', k)
        y = y - k * lst[j-1]
        j = j -1
 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Top-down (memoization) approach
        coins.sort()
        memo = {0:0}

        def min_coins(amt):
            if amt in memo:
                return memo[amt]

            min = float('inf')
            for coin in coins:
                diff = amt - coin
                if diff < 0:
                    break
                min = min(min, 1 + min_coins(diff))
            
            memo[amt] = min
            return memo[amt]

        result = min_coins(amount)
        if result < float('inf'):
            return result
        else:
            return -1
        
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Bottom-up (tabulation) approach
        coins.sort()
        memo = {0:0}
        # Include 0
        dp = [0] * amount + 1

        for i in range (1, amount + 1):
            min = float('inf')

            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break
                min = min(min, dp[diff] + 1)
            
            dp[i] = min
        
        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1