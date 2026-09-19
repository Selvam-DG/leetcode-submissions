class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        curr_sum = 0
        remainders = {0:-1}

        for i, num in enumerate(nums):
            curr_sum += num
            remainder = curr_sum % k
            if remainder in remainders:
                if i - remainders[remainder] >= 2:
                    return True
            else:
                remainders[remainder] = i
        return False