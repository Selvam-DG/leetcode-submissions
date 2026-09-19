class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        n = len(s)
        seen = set()
        l = 0
        r = 0

        while r < n:
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            result = max(result, (r-l+1))

            r += 1
        return result

        