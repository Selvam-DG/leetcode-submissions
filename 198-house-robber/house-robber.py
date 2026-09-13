class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def solve(idx):
            if idx >= n:
                return 0
            if idx in memo:
                return memo[idx]

            # skip
            skip = solve(idx+1)

            # take
            take = nums[idx] + solve(idx+2)
            memo[idx] = max(skip, take)
            return max(skip, take)
        
        return solve(0)
