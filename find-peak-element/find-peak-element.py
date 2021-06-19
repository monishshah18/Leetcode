class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return (nums.index(sorted(nums)[-1]))
        