class Solution:
    def maxArea(self, height: List[int]) -> int:
        start,end = 0,len(height)-1
        maxArea = float('-inf')
        while start < end:
            currArea = min(height[start],height[end])*(end-start)
            maxArea = max(maxArea, currArea)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return maxArea