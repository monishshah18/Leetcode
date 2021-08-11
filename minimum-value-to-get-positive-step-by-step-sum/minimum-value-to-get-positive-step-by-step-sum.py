class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        smallSum, temp = nums[0], nums[0]
        for i in nums[1:]:
            temp += i
            smallSum = min(temp, smallSum)
        return max(1-smallSum,1)