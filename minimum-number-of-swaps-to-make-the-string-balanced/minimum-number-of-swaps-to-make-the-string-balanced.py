class Solution:
    def minSwaps(self, s: str) -> int:
        res, ans = 0,0
        for i in s:
            if i == '[':
                res += 1
            else:
                res -= 1
            ans = min(res, ans)
        return (-ans+1)//2