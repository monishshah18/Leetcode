class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def FindPath(height, i, j, visited):
            if not visited[i][j] and grid[i][j]<=height:
                visited[i][j] = 1
                if i-1 >= 0:
                    FindPath(height, i-1, j, visited)
                if i+1 < n:
                    FindPath(height, i+1, j, visited)
                if j-1 >= 0:
                    FindPath(height, i, j-1, visited)
                if j+1 < n:
                    FindPath(height, i, j+1, visited)
        def BinarySearch(l,r):
            while l < r:
                mid = (l+r)//2
                visited = [[0]*m for _ in range(n)]
                FindPath(mid, 0, 0, visited)
                if visited[n-1][m-1]:
                    r = mid
                else:
                    l = mid + 1
            return l
                
        n,m = len(grid), len(grid[0])
        l, r = 0, max(max(x) for x in grid)
        return BinarySearch(l,r)
        