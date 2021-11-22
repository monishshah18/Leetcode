class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i,j in enumerate(heights):
            start = i
            while stack and stack[-1][1] > j:
                index,height = stack.pop()
                maxArea = max(maxArea, height*(i - index))
                start = index
            stack.append((start, j))
        for i,j in stack:
            maxArea = max(maxArea, j*(len(heights)-i))
        return maxArea