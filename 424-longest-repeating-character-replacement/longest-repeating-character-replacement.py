class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = dict()
        max_freq = 0
        longest = 0
        l = 0
        for r in range(n):
            char = s[r]
            freq[char] = 1 + freq.get(char, 0)
            max_freq = max(max_freq, freq[char])
            while  (r-l+1) - max_freq > k:
                freq[s[l]] -= 1
                l +=1
            print(freq)
            longest = max(longest, r-l+1)
        
        return longest