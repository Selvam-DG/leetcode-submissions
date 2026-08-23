class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        left = [0] * n
        buy = prices[0]
        for i in range(1, n):
            buy = min(buy, prices[i])
            left[i] = max(left[i-1], prices[i] - buy)
        right = [0] * n
        sell = prices[-1]
        for i in range(n-2, -1, -1):
            sell = max(sell, prices[i])
            right[i] = max(right[i+1], sell-prices[i])
        
        result = 0
        for i in range(n):
            result = max(result, left[i]+right[i])
        
        return result
