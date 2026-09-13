class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        def solve(arr): 
            n = len(arr)
            dp = [0] * (n+2)

            for i in range(n-1, -1, -1):
                dp[i] = max(dp[i+1], arr[i]+dp[i+2])
            
            return dp[0]
        
        take_first_house = solve(nums[:-1])
        skip_first_house = solve(nums[1:])

        return max(take_first_house, skip_first_house)