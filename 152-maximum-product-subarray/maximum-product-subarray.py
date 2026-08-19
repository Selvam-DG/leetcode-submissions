class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = 1
        suffix = 1
        result = nums[0]
        for i in range(n):
            if prefix == 0:
                prefix = 1
            elif suffix == 0:
                suffix = 1
            prefix *= nums[i]
            suffix *= nums[n-i-1]

            result = max(result, max(prefix, suffix))
        
        return result
