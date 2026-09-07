class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = dict()
        for char in t:
            freq_t[char] = 1 + freq_t.get(char,0)
        n = len(s)
        curr_freq = dict()
        best_length = -1
        best_start = 0
        l=0
        formed = 0
        for r in range(n):
            char = s[r]
            curr_freq [char] = 1 + curr_freq.get(char, 0)

            if char in freq_t and freq_t[char] == curr_freq[char]:
                formed += 1
            
            while formed == len(freq_t):
                if best_length == -1 or (r-l+1) < best_length:
                    best_length = r-l+1
                    best_start = l
                
                lchar = s[l]
                curr_freq[lchar] -= 1
                if lchar in freq_t and curr_freq[lchar] < freq_t[lchar]:
                    formed -= 1
                l += 1
        
        if best_length == -1:
            return ""
        return s[best_start: best_start+best_length]

