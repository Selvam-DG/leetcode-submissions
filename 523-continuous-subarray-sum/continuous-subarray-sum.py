class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        remainder = dict()
        remainder[0] = -1
        curr_sum = 0

        for i, num in enumerate(nums):
            curr_sum += num
            rem = curr_sum % k
            if rem in remainder :
                if  i - remainder[rem] >= 2:
                    return True
            else:
                remainder[rem] = i
        
        return False