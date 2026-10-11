class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set()
        for num in nums:
            unique.add(num)
        
        longest = 0
        for num in unique:
            
            if (num-1) not in unique:
                start = num
                count = 1
                while (num+1) in unique:
                    count += 1
                    num += 1
                longest = max(longest, count)
        
        return longest