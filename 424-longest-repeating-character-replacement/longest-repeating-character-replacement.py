class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = dict()
        max_freq = 0
        l = 0
        longest = 0
        for r in range(n):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            max_freq = max(max_freq, freq[s[r]])

            while (r-l+1) - max_freq > k:
                freq[s[l]] -=1
                l += 1
            longest = max(longest, r-l+1)
        return longest