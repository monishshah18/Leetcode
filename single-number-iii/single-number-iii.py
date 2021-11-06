class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums_count = Counter(nums)
        res = []
        for i,j in nums_count.items():
            if j == 1:
                res.append(i)
        return res