class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        start = 0
        currSum = 0
        maxSum = 0
        seen = set()
        for end in range(n):
            while nums[end] in seen:
                currSum -= nums[start]
                seen.remove(nums[start])
                start += 1
            seen.add(nums[end])
            currSum += nums[end]
            maxSum = max(maxSum, currSum)
        
        return maxSum