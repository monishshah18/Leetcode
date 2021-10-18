class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left_max,right_max = [height[0]],[height[-1]]
        res = 0
        n = len(height)
        for i in range(1, n):
            left_max.append(max(left_max[i-1],height[i]))
            right_max.append(max(right_max[i-1],height[n-i-1]))
        right_max.reverse()
        return sum(min(right_max[i],left_max[i])-height[i] for i in range(1,n))