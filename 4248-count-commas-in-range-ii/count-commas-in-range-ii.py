class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        start = 1_000
        commas = 1

        while start <= n:
            end = min(n, (start*1_000-1))
            total += (end-start+1)*commas
            commas += 1
            start *= 1_000
        
        return total
