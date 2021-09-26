class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        min_ = nums[0]
        for i in nums[1:]:
            if i <= min_:
                min_ = i
            else:
                res = max(res, i-min_)
        return res
            