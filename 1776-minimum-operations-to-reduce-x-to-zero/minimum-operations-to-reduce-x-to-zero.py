class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        target = total - x

        if target < 0:
            return -1
        
        if target == 0:
            return len(nums)
        
        l = 0
        curr_sum = 0
        longest = -1

        for r in range(n):
            curr_sum +=  nums[r]

            while curr_sum > target:
                curr_sum -= nums[l]
                l += 1
            
            if curr_sum == target:
                longest = max(longest, r-l+1)
            
        
        return -1 if longest == -1 else n-longest
        
        