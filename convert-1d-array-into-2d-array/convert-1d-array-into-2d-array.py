class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        k = len(original)
        if m*n != k:
            return []
        matrix = [[0 for _ in range(n)] for _ in range(m) ]
        for i in range(k):
            row = i//n
            col = i%n
            matrix[row][col] = original[i]
        return matrix