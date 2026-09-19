class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seen = dict()
        seen[0] = 1
        curr_sum = 0
        count = 0

        for r in range(n):
            curr_sum += nums[r]
            need = curr_sum - k
            if need in seen:
                count += seen[need]
            seen[curr_sum] = 1 + seen.get(curr_sum, 0)
        
        return count