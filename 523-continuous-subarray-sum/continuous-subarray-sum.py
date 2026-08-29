class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_indices = dict()
        remainder_indices[0] = -1

        curr_sum = 0

        for i, num in enumerate(nums):
            curr_sum += num
            remainder = curr_sum % k

            if remainder in remainder_indices:
                if i - remainder_indices[remainder] > 1:
                    return True
            else:
                remainder_indices[remainder] = i

        
        return False