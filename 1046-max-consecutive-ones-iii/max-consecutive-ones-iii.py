class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        longest = 0
        zero_count = 0
        l = 0
        for r in range(n):
            if nums[r] == 0:
                zero_count += 1
            
            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1
            longest = max(longest, r-l+1)
        
        return longest
