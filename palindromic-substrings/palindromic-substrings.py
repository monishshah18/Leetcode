class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False]*len(s) for _ in range(len(s))]
        count = 0
        for i in range(len(s)):
            for j in range(i):
                if s[i]==s[j] and (i-j+1 <= 3 or dp[i-1][j+1]):
                    count += 1
                    dp[i][j] = True
        return count + len(s)