class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_gain = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                profit_gain += (prices[i+1] - prices[i])
        return profit_gain