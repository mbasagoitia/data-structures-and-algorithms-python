# Coin-Changing Problem

Given a list of coin denominations and a target value, make optimal change (fewest number of coins from the list of denominations) for the target value.

## Optimal Substructure

After making the first coin choice, the remaining amount leaves us with the same goal of choosing the optimal amount of coins for that new value. We have a sequence of decisions to make.

## Recurrence

T = target
C1 .... Cn = different coin denominations

minCoins(T) = 

- Base case: when T = 0, return 0 (no coins for 0 cents); when T < 0, return infinity (overshot target, positive since we are minimizing)
- Recursive case: min(1 + minCoins(T - C1), 1 + minCoins(T - C2), ... 1 + minCoins(T - Cn))

## Memo Table

Table Tbl of length 0 ... T

for i = 0 to T:
    Tbl[i] = min(1 + Tbl[i = C1], ... min(1 + Tbl[i - Cn]))

For every value in the table, we are calculating the local minimum number of coins for each target, that is why i = T 

Table S that records value at each step which case gives you the minimum (S[i] = j).