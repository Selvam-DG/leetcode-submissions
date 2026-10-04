class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        result = float('-inf')
        current_sum = float('-inf')

        for num in nums:
            current_sum = max(num, current_sum+num)
            result= max(result, current_sum)
        
        return result