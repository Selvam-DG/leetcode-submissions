class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        prefix_sum = 0
        remainder_freq = {0:1}

        for i in range(n):
            prefix_sum += nums[i]
            remainder = prefix_sum % k

            count += remainder_freq.get(remainder, 0)

            remainder_freq[remainder] = 1 + remainder_freq.get(remainder, 0)

        return count