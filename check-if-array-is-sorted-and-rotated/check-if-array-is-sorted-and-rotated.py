class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        old_array = nums.copy()
        nums.sort()
        for i in range(0, len(nums)):
            nums.insert(len(nums), nums.pop(0))
            if nums==old_array:
                return True
        return False
        