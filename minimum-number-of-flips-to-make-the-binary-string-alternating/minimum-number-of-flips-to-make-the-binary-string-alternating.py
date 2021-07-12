class Solution:
    def minFlips(self, s: str) -> int:
        def func(st):
            dp = [0]
            x = len(st)//2
            for i in range(len(st)):
                if i%2 != int(st[i]):
                    dp.append(dp[-1]+1)
                else:
                    dp.append(dp[-1])
            dp.pop(0)
            maxi = 0
            mini = x+10
            for i in range(x, 2*x):
                val = dp[i]-dp[i%x]
                mini = min(mini, val)
                maxi = max(maxi, val)
            return min(mini, x-maxi)
        return func(s+s)
        