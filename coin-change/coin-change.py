class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = []
        for i in range(amount+1):
            dp.append(-1)
        dp[0] = 0
        n = len(coins)
        for i in range(n):
            for j in range(coins[i], amount+1):
                if dp[j-coins[i]] > -1:
                    if dp[j] == -1:
                        dp[j] = dp[j-coins[i]] + 1
                    else:
                        dp[j] = min(dp[j], dp[j-coins[i]] + 1)
        return dp[amount]
        