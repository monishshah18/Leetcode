class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(nums[i]*nums[i]*a+nums[i]*b+c)
        res.sort()
        return res