class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        maxSteps = nums[0]
        for i in range(len(nums)-1):
            if maxSteps <= 0:
                return False
            maxSteps = max(maxSteps-1, nums[i])
            if maxSteps <= 0:
                return False
        return True