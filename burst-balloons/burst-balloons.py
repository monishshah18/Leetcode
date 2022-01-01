class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums, n = [1] + nums + [1], len(nums) + 2
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n-2, -1, -1):
            for j in range(i+2, n):
                dp[i][j] = max(nums[i]*nums[k]*nums[j] + dp[i][k] + dp[k][j] for k in range(i+1, j))
        return dp[0][n-1]