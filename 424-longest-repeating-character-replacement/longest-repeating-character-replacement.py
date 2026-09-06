class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        char_freq = dict()
        l = 0
        max_freq = 0
        res = 0
        for r in range(n):
            char = s[r]
            char_freq[char] = 1 + char_freq.get(char, 0)
            max_freq = max(max_freq, char_freq[char])

            while (r-l+ 1) - max_freq > k:
                char_freq[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res

