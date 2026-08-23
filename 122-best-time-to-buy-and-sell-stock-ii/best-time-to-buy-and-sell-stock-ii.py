class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        result = 0
        i = 0

        while i < n-1:

            while i < n-1 and prices[i] >= prices[i+1]:
                i += 1
            buy = prices[i]

            while i < n-1 and prices[i] <= prices[i+1]:
                i += 1
            sell = prices[i]
            result += sell-buy
            
        return result