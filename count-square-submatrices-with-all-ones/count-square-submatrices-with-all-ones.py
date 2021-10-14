class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix is None or len(matrix)==0:
            return 0
        res = 0
        row,cols = len(matrix), len(matrix[0])
        for r in range(row):
            for c in range(cols):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0:
                        res += 1
                    else:
                        cell_val = min(matrix[r-1][c],matrix[r][c-1],matrix[r-1][c-1])+matrix[r][c]
                        res += cell_val
                        matrix[r][c] = cell_val
        return res