import sys

def coinChange(coins, amount):
    memo = {}

    def dp(rem):
        if rem < 0:
            return sys.maxsize
        if rem == 0:
            return 0
        if rem in memo:
            return memo[rem]

        min_coins = sys.maxsize
        for coin in coins:
            res = dp(rem - coin)
            if res != sys.maxsize:
                min_coins = min(min_coins, res + 1)

        memo[rem] = min_coins
        return min_coins

    result = dp(amount)
    return result if result != sys.maxsize else -1

coins = [1, 2, 5]
amount = 11
print(coinChange(coins, amount))  # Output: 3
