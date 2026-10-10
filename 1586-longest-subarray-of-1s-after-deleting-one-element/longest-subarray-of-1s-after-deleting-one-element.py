class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        zeroCount = 0
        start = 0
        result = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                zeroCount += 1
            
            while zeroCount > 1:
                if nums[start] == 0:
                    zeroCount -= 1
                start += 1
            
            result = max(result, end-start)
        
        return result
