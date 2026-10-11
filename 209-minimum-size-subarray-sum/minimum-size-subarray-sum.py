class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        minLength = float('inf')
        start = 0
        curr_sum = 0
        for end in range(n):
            curr_sum += nums[end]
            while curr_sum >= target:
                curr_sum -= nums[start]
                minLength = min(minLength, end-start+1)
                start += 1
        
        return 0 if minLength == float('inf') else minLength
