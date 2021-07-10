class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        preMin, preMax = 1,1
        maxProduct = nums[0]
        for x in (nums):
            preMin, preMax = min(x, x*preMin, x*preMax), max(x,x*preMin,x*preMax)
            maxProduct = max(maxProduct, preMax)
        return maxProduct