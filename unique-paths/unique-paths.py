class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        return self.memo(dp, m-1,n-1,{})
    def memo(self, dp, i, j, grid):
        if i < 0 or j < 0 or i >= len(dp) or j >= len(dp[0]):
            return 0
        if dp[i][j] == 1:
            return 1
        if (i,j) in grid:
            return grid[(i,j)]
        grid[(i,j)] = self.memo(dp,i-1,j,grid)+self.memo(dp,i,j-1,grid)
        return grid[(i,j)]