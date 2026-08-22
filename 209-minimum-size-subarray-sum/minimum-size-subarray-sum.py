class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        l = 0
        length = float('inf')
        curr_sum = 0
        for r in range(n):
            curr_sum += nums[r]
            while curr_sum >= target:
                length = min(length, r-l+1)
                curr_sum -= nums[l]
                
                l += 1
        if length == float('inf'):
            return 0
        return length