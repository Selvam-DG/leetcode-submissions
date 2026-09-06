class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        freq = {0:1}
        curr_sum = 0
        count = 0
        for i in range(n):
            curr_sum += nums[i]

            if (curr_sum - goal) in freq:
                count += freq[curr_sum - goal]
            freq[curr_sum] = 1 + freq.get(curr_sum, 0)

        
        return count