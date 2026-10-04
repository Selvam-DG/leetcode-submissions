class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        buy = prices[0]
        maxProfit = 0
        for price in prices:
            buy = min(price, buy)
            maxProfit = max(maxProfit, price-buy)
        
        return maxProfit