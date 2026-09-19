class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        i = n-2

        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        print(i)
        if i >= 0:
            j = n-1
            while nums[j] <= nums[i]:
                j -= 1
            swap(i, j)
        
        reverse(i+1,n-1)