class Solution:
    def numTilings(self, n: int) -> int:
        a,b,c = 0,1,1
        for i in range(n-1):
            a,b,c = b,c,(c+c+a)%int(10**9+7)
        return c