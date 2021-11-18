class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = j = nums[0]
        for x in range(1, len(nums)):
            i = max(nums[x], i+nums[x])
            j = max(i,j)
        return j