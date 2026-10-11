class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        start = 2
        
        for end in range(2, n):
            if nums[end] != nums[start-2]:
                nums[start] = nums[end]
                start += 1
        return min(start, n)