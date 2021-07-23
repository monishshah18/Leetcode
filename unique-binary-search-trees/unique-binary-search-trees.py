class Solution:
    def numTrees(self, n: int) -> int:
        dp = [[None]*(n+1) for _ in range(n+1)]
        def count(start,end):
            if start >= end:
                return 1
            if dp[start][end]:
                return dp[start][end]
            total = 0
            for i in range(start, end+1):
                total += count(start,i-1)*count(i+1,end)
            dp[start][end] = total
            return dp[start][end]
        res = count(1,n)
        return res