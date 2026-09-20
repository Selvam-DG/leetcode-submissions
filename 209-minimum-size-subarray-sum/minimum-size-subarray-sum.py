class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        INF = float('inf')
        n = len(nums)
        curr_sum = 0
        l = 0
        result = INF
        for r in range(n):
            curr_sum += nums[r]
            while curr_sum >= target:
                result = min(result, r-l+1)
                curr_sum -= nums[l]
                l += 1
        
        return 0 if result == INF else result
            