class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k == 0:
            return 0
        n = len(nums)
        start = 0
        product = 1
        count = 0
        for end in range(n):
            product *= nums[end]

            while start <= end and product >= k:
                product /= nums[start]
                start += 1
            
            count += end-start+1
        
        return count