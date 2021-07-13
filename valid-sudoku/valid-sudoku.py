class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in [Counter(board[i]), Counter([board[q][i] for q in range(9)]), Counter([board[((i % 3) * 3) + q % 3][((i // 3) * 3) + q // 3] for q in range(9)])]:
                j.pop('.')
                if not all([t<=1 for t in j.values()]):
                    return False
        return True
        