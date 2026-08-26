class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #reverse the list
        # reverse firt k nums
        # reverse n-k nums
        k = k % len(nums)
        self.reverse(nums)
        nums[:k] = self.reverse(nums[:k])
        nums[k:] = self.reverse(nums[k:])
    
    
    def reverse(self, arr):
        n = len(arr)

        left = 0
        right = n-1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        
        return arr
        