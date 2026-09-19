class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_pointer = 0

        n = len(nums)
        for r in range(n):
            if nums[r] != 0:
                nums[non_zero_pointer] = nums[r]
                non_zero_pointer += 1
        
        for i in range(non_zero_pointer, n):
            nums[i] = 0
        
    