class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
            
        ans = 0
        i = 1
        while i < n:
            curr = 1
            while i < n and nums[i] > nums[i-1]:
                curr += 1
                i += 1
            ans = max(ans, curr)
            i += 1
        
        j = 1
        while j < n:
            curr = 1
            while j < n and nums[j] < nums[j-1]:
                curr += 1
                j += 1
            ans = max(ans, curr)
            j += 1
        
        return ans
