class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        curr_min = prices[0]
        profits = []
        max_profit = 0
        for p in prices:
            curr_min = min(curr_min, p)
            max_profit = max(max_profit, p - curr_min)
            profits.append(max_profit)
        max_profit,total_profit = 0,0
        curr_max = prices[-1]
        for p in range(len(prices)-1,-1,-1):
            curr_max = max(curr_max,prices[p])
            max_profit = max(max_profit, curr_max - prices[p])
            total_profit = max(total_profit, max_profit + profits[p])
        return total_profit