class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        m,n = len(heightMap), len(heightMap[0])
        heap = []
        result = 0
        visited = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0 or i==m-1 or j==n-1:
                    heapq.heappush(heap, (heightMap[i][j],i,j))
                    visited[i][j] = 1
        while heap:
            height,i,j = heapq.heappop(heap)
            for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    result += max(0, height - heightMap[x][y])
                    heapq.heappush(heap, (max(height,heightMap[x][y]),x,y))
                    visited[x][y] = 1
        return result