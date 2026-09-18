class Solution:
    def climbStairs(self, n: int) -> int:
        prev2 = 1
        prev1 = 1

        for _ in range(2,n+1):
            prev2, prev1 = prev1, prev1+prev2
        
        return prev1