class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = []
        for num in nums:
            squares.append(num*num)
        
        squares = sorted(squares)

        n = len(nums)
        negative_count = n//2
        return sum(squares[negative_count:])-sum(squares[:negative_count])