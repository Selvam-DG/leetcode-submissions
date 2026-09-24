class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            temp = 0
            for digit in str(num):
                temp += int(digit)
            if temp == i:
                return i
        
        return -1
        