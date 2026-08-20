class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        l = 0
        hset = set()
        longest = 0
        for r in range(n):
            while s[r] in hset:
                hset.remove(s[l])
                l += 1
            hset.add(s[r])

            longest = max(longest, r-l+1)
        
        return longest