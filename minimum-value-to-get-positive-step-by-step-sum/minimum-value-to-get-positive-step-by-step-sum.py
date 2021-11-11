class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        res = 1
        for i in range(len(nums)-1,-1,-1):
            res = res - nums[i]
            if res <= 0:
                res = 1
        return res