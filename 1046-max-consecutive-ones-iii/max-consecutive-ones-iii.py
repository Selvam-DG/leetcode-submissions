class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)

        start = 0
        zeroCount = 0
        max_length = 0
        for end in range(n):
            if nums[end] == 0:
                zeroCount += 1
            
            while zeroCount > k:
                if nums[start] == 0:
                    zeroCount -=1
                start += 1
            
            max_length = max(max_length, end-start+1)
        
        return max_length