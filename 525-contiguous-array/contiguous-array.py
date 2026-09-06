class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {0:-1}
        balance = 0
        ans =0
        for i, num in enumerate(nums):
            if num == 0:
                balance -=1
            else:
                balance += 1
            if balance in freq:
                ans = max(ans, i-freq[balance])
            else:
                freq[balance]=i
        return ans
        