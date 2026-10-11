class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0:-1}
        n = len(nums)
        curr_sum = 0
        maxLength = 0
        for i, num in enumerate(nums):
            curr_sum += -1 if num == 0 else 1
            if curr_sum in seen:
                maxLength = max(maxLength, i - seen[curr_sum])
            else:
                seen[curr_sum] = i
        
        return maxLength
