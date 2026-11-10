class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        # to reach step1 the cost is cost[1] + (j-i)**2
        # to reach step2 min(cost to reach from 0 to 2, step1+step2)
        # to reach step3 min(0 to 3, 0 to 1 and 1 to 3, 1to2to3)
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            for jump in range(1,4):
                prev = i - jump
                if prev >= 0:
                    dp[i] = min(dp[i], dp[prev]+costs[i-1]+jump**2)
        
        return dp[n]

