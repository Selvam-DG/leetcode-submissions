class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()

        l = 0
        longest = 0
        for r in range(n):
            char = s[r]
            while char in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(char)
            longest = max(longest, r-l+1)
        
        return longest