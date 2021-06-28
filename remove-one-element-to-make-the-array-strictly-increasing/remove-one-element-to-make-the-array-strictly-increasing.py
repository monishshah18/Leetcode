class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        nums = [0] + nums
        removed = False
        for i in range(2, len(nums)):
            if nums[i] <= nums[i-1]:
                if removed:
                    return False
                if nums[i] > nums[i-2]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                removed = True
        return True
        