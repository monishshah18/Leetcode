class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        notHold,hold, notHold_cooldown = 0, float('-inf'),float('-inf')
        for p in prices:
            notHold, hold, notHold_cooldown = max(notHold, notHold_cooldown), max(hold, notHold-p), p+hold
        return max(notHold,notHold_cooldown)