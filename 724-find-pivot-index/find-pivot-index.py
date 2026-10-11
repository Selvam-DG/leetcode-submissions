class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        totalSum = 0
        for num in nums:
            totalSum += num
        
        leftSum = 0
        for i, num in enumerate(nums):
            if num == (totalSum - leftSum) - leftSum:
                return i
            leftSum += num
        return -1