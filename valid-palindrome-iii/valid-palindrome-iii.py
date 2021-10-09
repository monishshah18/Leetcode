class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(n+1):
                if not i or not j:
                    dp[i][j] = i or j
                elif s[i-1]==s[n-j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1])+1
        return dp[n][n] <= 2*k