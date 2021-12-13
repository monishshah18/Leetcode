class Solution:
    def maxPower(self, s: str) -> int:
        count = ans = 1
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                count += 1
                ans = max(count, ans)
            else:
                count = 1
        return ans
        