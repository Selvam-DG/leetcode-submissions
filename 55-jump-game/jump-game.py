class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        farthest_marked = 0
        for i in range(n):
            if not dp[i]:
                continue
            reach = min(n-1, i+nums[i])

            for j in range(farthest_marked + 1, reach+1):
                dp[j] = True
            
            farthest_marked = max(farthest_marked, reach)

            if dp[n-1]:
                return True
                
        return dp[n-1]