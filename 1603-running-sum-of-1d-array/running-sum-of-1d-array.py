class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = [0] * len(nums)
        curr_sum = 0

        for i, num in enumerate(nums):
            curr_sum += num
            result[i] = curr_sum
        
        return result