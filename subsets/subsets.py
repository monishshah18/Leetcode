class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in sorted(nums):
            res += [item+[i] for item in res]
        return res