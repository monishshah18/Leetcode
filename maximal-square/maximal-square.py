class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        res = 0
        temp = [[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]=='1':
                    temp[i][j] = 1 + min(temp[i-1][j], temp[i][j-1], temp[i-1][j-1])
                    res = max(res, temp[i][j])
        return res**2