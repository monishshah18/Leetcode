class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] or (i==0 and j==0):
                    continue
                dp[i][j] = (dp[i-1][j] if i else 0) + (dp[i][j-1] if j else 0)
        return dp[m-1][n-1]