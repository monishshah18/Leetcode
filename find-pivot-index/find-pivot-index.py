class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rSum = sum(nums)
        lSum = 0
        for i,j in enumerate(nums):
            rSum -= j
            if lSum == rSum:
                return i
            lSum += j
        return -1
        