class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        min_product = max_product = result = nums[0]

        for i in range(1, n):
            num = nums[i]
            if num < 0:
                min_product, max_product = max_product, min_product
            
            min_product = min(num, min_product*num)
            max_product = max(num, max_product*num)

            result = max(result, max_product)
        
        return result
        