class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix)==0: return 0
        m,n = len(matrix), len(matrix[0])
        dp = [0] * n
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="1":
                    dp[j] += 1
                else:
                    dp[j] = 0
                   
            maxArea = max(maxArea, self.maxHistogram(dp))
        return maxArea
    def maxHistogram(self, heights):
        n = len(heights)
        maxArea = 0
        stack = [-1]
        for i in range(n):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                currentHeight = heights[stack.pop()]
                currentWidth = i - stack[-1] - 1
                maxArea = max(maxArea, currentWidth * currentHeight)
            stack.append(i)
        while stack[-1] != -1:
            currentHeight = heights[stack.pop()]
            currentWidth = n - stack[-1] - 1
            maxArea = max(maxArea, currentWidth * currentHeight)
        return maxArea
            