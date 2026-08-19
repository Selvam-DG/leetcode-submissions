class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        [1,1,2,6]
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]
        # [24,12,4,1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        result = [1] * n
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        
        return result