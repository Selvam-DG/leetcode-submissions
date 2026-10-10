class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = dict()#
        result = 0
        max_freq = 0
        start = 0
        for end in  range(len(s)):
            char = s[end]
            freq[char] = 1 + freq.get(char, 0)
            max_freq = max(max_freq, freq[char])

            while ((end-start+1)- max_freq) > k:
                freq[s[start]] -= 1
                start += 1
            result = max(result, end-start+1)
        
        return result
