def coinChange(coins, amount):
    memo = {}

    def minCoins(remain):
        if remain == 0:

            return 0
        if remain < 0:
            return float("inf")
        if remain in memo:
            return memo[remain]
        min_count = float("inf")
        for coin in coins:

            res = minCoins(
                remain - coin,
            )
            if res != float("inf"):
                min_count = min(min_count, 1 + res)
        memo[remain] = min_count
        return min_count

    ans = minCoins(amount)
    return -1 if ans == float("inf") else ans


coins = [1, 2, 5]
amount = 3
# print(coinChange(coins, amount))


def coinChangeBottomUp(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            print("ANTES:", dp)
            print(dp[x], dp[x - coin] + 1, coin)
            dp[x] = min(dp[x], dp[x - coin] + 1)
            print("DESPU:", dp)
    return dp[amount] if dp[amount] != float("inf") else -1


coins = [1, 2, 5]
amount = 3
print(coinChangeBottomUp(coins, amount))
