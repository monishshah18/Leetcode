class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1': return False
        if minJump <= len(s)-1 <= maxJump: return True
        dp = [1]*minJump
        for i in range(minJump, len(s)):
            reach = 0
            if s[i]=='0':
                reach = dp[i-minJump]-(dp[i-maxJump-1] if i-maxJump > 0 else 0)
            if reach > 0:
                dp.append(dp[-1]+1)
            else:
                dp.append(dp[-1])
        return reach > 0