class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j]==word[0]:
                    if self.helper(board,i,j,0,word)==True:
                        return True
        return False
    
    def helper(self, board, row, cols, ind, word):
        if len(word)==ind:
            return True
        if row < 0 or row >= len(board) or cols < 0 or cols >= len(board[0]):
            return False
        if board[row][cols]!=word[ind]:
            return False
        temp = board[row][cols]
        board[row][cols] = '.'
        up = self.helper(board, row, cols+1, ind+1, word)
        down = self.helper(board, row, cols-1,ind+1,word)
        left = self.helper(board, row+1, cols, ind+1, word)
        right = self.helper(board, row-1, cols, ind+1, word)
        found = (left or right or up or down)
        board[row][cols] = temp
        
        return found