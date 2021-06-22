class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp, dp1, dp2 = 0,0,0
        for i in range(2, len(cost)+1):
            onestep = dp1 + cost[i-1]
            twostep = dp2 + cost[i-2]
            dp = min(onestep, twostep)
            dp1, dp2 = dp, dp1
        return dp1