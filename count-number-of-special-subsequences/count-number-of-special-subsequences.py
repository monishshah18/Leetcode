class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        dp = [1,0,0,0]
        for i in nums:
            dp[i+1] += dp[i]+dp[i+1]
        return dp[-1]%(10**9+7)