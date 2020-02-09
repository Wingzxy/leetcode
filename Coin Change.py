class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('Inf')] * (amount + 1)
        dp[0] = 0

        for coin in (coins):
            for amt in range(coin, amount + 1):
                dp[amt] = min(dp[amt], dp[amt - coin] + 1)
        return dp[amount] if dp[amount] != float('Inf') else -1
