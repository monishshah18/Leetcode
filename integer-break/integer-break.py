class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        res = 0
        for i in range(2, (n//2)+1):
            a,b = divmod(n,i)
            val = pow(a,i-b)*pow(a+1,b)
            res = max(val,res)
        return res
        