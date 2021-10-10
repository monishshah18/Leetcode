class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        i,j = 0,len(nums)-1
        ans = -1
        nums = sorted(nums)
        while i < j:
            if nums[i]+nums[j] < k:
                ans = max(ans, nums[i]+nums[j])
                i += 1
            else:
                j -= 1
        return ans