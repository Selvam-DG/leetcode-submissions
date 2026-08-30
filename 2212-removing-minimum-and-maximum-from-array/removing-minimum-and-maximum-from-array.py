class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        minimum_idx = 0
        minimum = float('inf')
        maximum_idx = 0
        maximum = float('-inf')
        result = 0

        for i, num in enumerate(nums):
            if num <= minimum:
                minimum = num
                minimum_idx = i
            
            if num >= maximum:
                maximum = num
                maximum_idx = i

        
        left = min(minimum_idx, maximum_idx)
        right = max(minimum_idx, maximum_idx)
        remove_left = right + 1
        remove_right = n - left
        remove_both_sides = (left + 1) + (n-right)

        return min(remove_left, remove_right, remove_both_sides)

