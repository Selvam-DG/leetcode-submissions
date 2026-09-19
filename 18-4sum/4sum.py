class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        result = []
        if not nums:
            return result
        
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                left = j + 1
                right = n-1

                while left < right:
                    sum4 = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum4 > target:
                        right -= 1
                    elif sum4 < target:
                        left += 1
                    else:
                        result.append([nums[i] , nums[j] , nums[left] , nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
        
        return result
                    