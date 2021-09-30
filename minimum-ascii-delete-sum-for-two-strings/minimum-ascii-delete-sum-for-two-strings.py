class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m,n = len(s1),len(s2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + ord(s1[i-1])
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        total = 0
        for i in s1:
            total += ord(i)
        for i in s2:
            total += ord(i)
        return total - dp[m][n]*2
            