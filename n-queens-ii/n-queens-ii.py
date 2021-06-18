class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = []
        board = [['.'] * n for _ in range(n)]
        
        def place(i: int, vert: int, ldiag: int, rdiag:int) -> None:
            if i == n:
                ans.append(["".join(row) for row in board])
                return
            for j in range(n):
                vmask, lmask, rmask = 1 << j, 1 << (i+j), 1 << (n-i-1+j)
                if vert & vmask or ldiag & lmask or rdiag & rmask: continue
                board[i][j] = 'Q'
                place(i+1, vert | vmask, ldiag | lmask, rdiag | rmask)
                board[i][j] = '.'
            
        place(0,0,0,0)
        return len(ans)
        