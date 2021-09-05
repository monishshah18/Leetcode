class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        temp = 0
        for i in range(len(nums)):
            if temp == s - temp - nums[i]:
                return i
            temp += nums[i]
        return -1