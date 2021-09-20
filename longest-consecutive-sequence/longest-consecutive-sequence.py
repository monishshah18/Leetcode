class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        @lru_cache(None)
        def dp(x):
            if x-1 in nums_set:
                return dp(x-1)+1
            return 1
        ans = 0
        for i in nums_set:
            ans = max(ans, dp(i))
        return ans