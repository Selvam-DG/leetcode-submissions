class Solution:
    def rob(self, nums: List[int]) -> int:
        # skip  idx+1
        n = len(nums)
        dp = [0] * (n+2)

        for i in range(n-1, -1, -1):
            take = nums[i] + dp[i+2]
            skip = dp[i+1]

            dp[i] = max(take, skip)
        
        return dp[0]
