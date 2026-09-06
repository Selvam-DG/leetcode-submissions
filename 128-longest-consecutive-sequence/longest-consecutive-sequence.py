class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set()
        for num in nums:
            unique.add(num)
        
        longest = 0
        for num in unique:
            if (num-1) not in unique:
                length = 0
                while num in unique:
                    num += 1
                    length += 1
                longest = max(longest, length)
        
        return longest
