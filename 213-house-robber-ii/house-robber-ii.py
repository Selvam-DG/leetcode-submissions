class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        def helper(arr):
            m = len(arr)
            dp = [0] * (m)

            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, m):
                take = arr[i] + dp[i-2]
                skip = dp[i-1]

                dp[i] = max(take, skip)
            return dp[-1]
        
        case1 = helper(nums[1:])
        case2 = helper(nums[:-1])

        return max(case1, case2)
