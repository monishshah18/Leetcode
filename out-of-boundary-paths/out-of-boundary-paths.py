class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[-1]*(maxMove+1) for _ in range(n+1)] for _ in range(m+1)]
        
        def solveRecursion(i, j, maxMove):
            if maxMove < 0:
                return 0
            if i < 0 or i >=m or j < 0 or j >= n:
                return 1
            if dp[i][j][maxMove] != -1:
                return dp[i][j][maxMove]
            a = solveRecursion(i-1,j,maxMove-1)
            b = solveRecursion(i+1,j,maxMove-1)
            c = solveRecursion(i,j-1,maxMove-1)
            d = solveRecursion(i,j+1,maxMove-1)
            
            dp[i][j][maxMove] = a+b+c+d
            return dp[i][j][maxMove]
        
        return solveRecursion(startRow,startColumn,maxMove) % 1000000007