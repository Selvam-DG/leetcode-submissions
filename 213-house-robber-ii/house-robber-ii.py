class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(start, end):
            prev2 = 0
            prev1 = 0

            for i in range(start, end):
                temp = prev1
                prev1 = max(prev1, prev2+nums[i])
                prev2 = temp
            
            return prev1
        n = len(nums)
        if n == 1:
            return nums[0]
        if n== 2:
            return max(nums)
        return max(solve(0, n-1), solve(1, n))