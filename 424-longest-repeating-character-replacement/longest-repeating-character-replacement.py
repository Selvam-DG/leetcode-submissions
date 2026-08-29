class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        char_freq = [0] * 26
        window_start = 0
        max_freq = 0
        longest = 0

        for i in range(n):
            char = s[i]
            index = ord(char) - ord('A')
            char_freq[index] += 1

            max_freq = max(max_freq, char_freq[index])


            while (i - window_start + 1) - max_freq > k:
                idx = ord(s[window_start])-ord('A')
                char_freq[idx] -= 1
                window_start += 1
            
            longest = max(longest, i-window_start+1)
        
        return longest
