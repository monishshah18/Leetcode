class Solution:
    def numOfWays(self, n: int) -> int:
        dp1, dp2 = 6,6
        for i in range(2, n+1):
            dp1, dp2 = dp1*3+dp2*2,2*dp1+2*dp2
        return (dp1+dp2)%(10**9+7)
        