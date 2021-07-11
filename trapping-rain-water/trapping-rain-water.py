class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res, n = 0, len(height)
        left_max, right_max = [height[0]], [height[-1]]
        
        for i in range(1, n):
            left_max.append(max(left_max[i-1],height[i]))
            right_max.append(max(right_max[i-1], height[n-i-1]))
        right_max.reverse()
        return sum(min(left_max[i], right_max[i])-height[i] for i in range(1, n))