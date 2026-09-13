class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}
        def solve(idx, remaining):
            if  remaining == 0:
                return 1
            if idx ==n or remaining < 0:
                return 0
            if (idx, remaining) in memo:
                return memo[(idx, remaining)]
            
            take = solve(idx, remaining-coins[idx])
            skip = solve(idx+1, remaining)
            memo[(idx, remaining)] = take + skip
            return memo[(idx, remaining)]
        
        return solve(0, amount)
