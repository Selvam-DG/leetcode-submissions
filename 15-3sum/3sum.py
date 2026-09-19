class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        result = []
        if not nums:
            return result
        
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            left = i+1
            right = n-1

            while left < right:
                sum3 = nums[i] + nums[left] + nums[right]
                if sum3 > 0:
                    right -= 1
                elif sum3 < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        
        return result
