class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount

        for coin in coins:
            for a in range(coin, amount+1):
                dp[a] = dp[a] + dp[a-coin]
        
        return dp[amount]