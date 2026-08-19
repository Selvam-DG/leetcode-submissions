class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float('-inf')
        curr_sum = float('-inf')

        for i in range(n):
            curr_sum = max(nums[i], curr_sum+nums[i])
            max_sum = max(max_sum, curr_sum)
        
        return max_sum