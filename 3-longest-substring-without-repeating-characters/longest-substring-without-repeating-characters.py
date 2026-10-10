class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        start = 0
        result = 0
        for end in range(n):
            while s[end] in seen:
                seen.remove(s[start])
                start += 1
            seen.add(s[end])
    
            result = max(result, end-start+1)
        return result