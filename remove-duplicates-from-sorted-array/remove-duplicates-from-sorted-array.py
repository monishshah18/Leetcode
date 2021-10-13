class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            p = i+1
            if nums[i]==nums[p]:
                del nums[p]
            else:
                i += 1
        return len(nums)