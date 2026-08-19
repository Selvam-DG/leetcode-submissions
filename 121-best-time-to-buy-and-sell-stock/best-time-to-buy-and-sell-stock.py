class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        buy = prices[0]
        for i in range(n):
            buy = min(buy, prices[i])
            profit = prices[i] - buy
            max_profit = max(profit, max_profit)
        
        return max_profit
