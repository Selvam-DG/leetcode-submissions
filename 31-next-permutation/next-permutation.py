class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(arr, i,j):
            arr[i], arr[j] = arr[j], arr[i]
            return arr
        def reverse(arr, a, b):
            while a < b:
                arr[a], arr[b] =arr[b], arr[a]
                a += 1
                b -= 1
            return arr
        n = len(nums)
        i = n-2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i >= 0:
            j = n-1
            while nums[j] <= nums[i]:
                j -= 1
            nums = swap(nums, i, j)
        
        nums = reverse(nums, i+1, n-1)
        