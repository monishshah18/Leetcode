class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row,cols,box = [[0]*9 for i in range(9)],[[0]*9 for i in range(9)],[[0]*9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                temp = i//3 * 3 + j//3
                temp1 = int(board[i][j]) - 1
                row[i][temp1], cols[j][temp1], box[temp][temp1] = 1,1,1
        def dfs(board, r, c):
            if r==9: return True
            next_r, next_c = (r,c+1) if c!=8 else(r+1,0)
            if board[r][c].isnumeric(): return dfs(board, next_r, next_c)
            box1 = r//3 * 3 + c//3
            for i in range(9):
                if row[r][i] or cols[c][i] or box[box1][i]:continue
                row[r][i], cols[c][i], box[box1][i] = 1,1,1
                board[r][c] = str(i+1)
                if dfs(board, next_r, next_c):return True
                board[r][c] = "."
                row[r][i], cols[c][i], box[box1][i] = 0,0,0
                
        dfs(board,0,0)