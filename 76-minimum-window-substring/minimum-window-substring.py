class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        if len(s) < len(t):
            return ""
        need = dict()
        for char in t:
            need[char] = 1 + need.get(char, 0)
        required = len(need)


        window = dict()
        formed =0 
        start = 0
        best_start = 0
        min_best_length = float('inf')
        for end in range(len(s)):
            window[s[end]] = 1 + window.get(s[end], 0)
            if s[end] in need and window[s[end]] == need[s[end]]:
                formed += 1
            
            while formed == required:
                if (end-start+1 < min_best_length):
                    best_start = start
                    min_best_length = end-start+1
                leaving_char = s[start]
                window[leaving_char] -= 1
                if leaving_char in need and window[leaving_char] < need[leaving_char]:
                    formed -= 1
                start += 1
        return "" if min_best_length == float('inf') else s[best_start:best_start+ min_best_length]

