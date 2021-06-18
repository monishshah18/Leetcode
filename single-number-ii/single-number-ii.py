class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = [i for i in nums if nums.count(i) == 1]
        return res[0]