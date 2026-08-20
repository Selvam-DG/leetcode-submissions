class Solution:
    def climbStairs(self, n: int) -> int:
        count = [0] * (n+1)
        def dp(n):
            if n <= 1:
                return 1
            if count[n] != 0:
                return count[n]
            count[n] =  dp(n-1) + dp(n-2)
            return count[n]
        
        return dp(n)