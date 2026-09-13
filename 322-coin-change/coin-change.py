class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        INF  = float('inf')

        def solve(idx, remaining):
            if remaining == 0:
                return 0
            if idx < 0 or remaining < 0:
                return INF
            
            if (idx, remaining) in memo:
                return memo[(idx, remaining)]
            
            take = INF

            if coins[idx] <= remaining:
                take = 1 +  solve(idx, remaining-coins[idx])
            
            skip = solve(idx-1, remaining)

            memo[(idx, remaining)] = min(take, skip)

            return memo[(idx, remaining)]
        
        ans = solve(len(coins)-1, amount)
        return -1 if ans == INF else ans