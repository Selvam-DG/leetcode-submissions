class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum_count = {0:1}
        count = 0
        curr_sum = 0

        for i in range(n):
            curr_sum += nums[i]
            if (curr_sum - k) in prefix_sum_count:
                count += prefix_sum_count[curr_sum - k]
            
            prefix_sum_count[curr_sum] = 1 + prefix_sum_count.get(curr_sum, 0)
        
        return count