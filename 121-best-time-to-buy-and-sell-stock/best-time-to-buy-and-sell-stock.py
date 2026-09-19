class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        buy = prices[0]
        for price in prices:
            buy = min(price, buy)
            max_profit = max(max_profit, price-buy)
        
        return max_profit