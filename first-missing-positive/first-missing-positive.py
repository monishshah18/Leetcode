class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        ans = 1
        for i in range(len(nums)):
            if nums[i] > 0 and ans != nums[i]:
                continue
            elif nums[i] > 0:
                ans += 1
            if ans == nums[-1]:
                ans += 1
        return ans
        