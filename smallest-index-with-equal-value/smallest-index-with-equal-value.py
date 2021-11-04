class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        res = -1
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                res = i
                return res
        return -1
            