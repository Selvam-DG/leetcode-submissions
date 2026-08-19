class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        result = float('inf')
        while left <= right:
            mid = left + (right-left) // 2
            if nums[left] <= nums[right]:
                result = min(result, nums[left])
                break

            if nums[left] <= nums[mid]:
                result = min(result, nums[left])
                left = mid + 1
            else:
                result = min(result, nums[mid])
                right = mid -1
            
        return result

