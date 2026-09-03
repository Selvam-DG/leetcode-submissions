class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_num = min(nums1)

        if min_num % 2:
            return True
        
        for num in nums1:
            if num % 2 == 1:
                return False
        return True