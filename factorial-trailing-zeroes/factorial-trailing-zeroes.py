class Solution:
    def trailingZeroes(self, n: int) -> int:
        x = 5
        res = 0
        while(x <= n):
            res += n//x
            x *= 5
        return res
        