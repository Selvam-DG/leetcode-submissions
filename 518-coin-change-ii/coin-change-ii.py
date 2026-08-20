class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # take that coin or not
        n = len(coins)
        memo = {}
        def recursive(curr, index):
            
            if curr > amount or index >= len(coins):
                return 0
            if curr == amount:
                return 1
            if (curr, index) in memo:
                return memo[(curr, index)]
            take = recursive(curr + coins[index], index)
            not_take = recursive(curr, index+1)
            memo[(curr, index)] = take + not_take
            return memo[(curr, index)]
        
        return recursive(0,0)