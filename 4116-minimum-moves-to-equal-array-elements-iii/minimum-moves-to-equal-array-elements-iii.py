class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        maximum = max(nums)
        moves = 0

        for num in nums:
            moves += abs(maximum - num)
        
        return moves