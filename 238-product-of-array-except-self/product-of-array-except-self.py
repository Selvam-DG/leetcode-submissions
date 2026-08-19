class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = [1] * n
        prefix = 1

        for i in range(1, n):
            product[i] = nums[i-1] * prefix
            prefix = product[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            product[i] *= suffix
            suffix *= nums[i]
        
        return product