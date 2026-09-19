class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        element = None
        count = 0

        for num in nums:
            if count == 0:
                element = num
                count += 1
            elif element == num:
                count += 1
            else:
                count -= 1
        temp = 0
        for num in nums:
            if num == element:
                temp += 1
            if temp > n//2:
                return element
