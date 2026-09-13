class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = dict()

        for char in t:
            freq_t[char] = 1 + freq_t.get(char, 0)
        
        needed = len(freq_t)
        
        freq_s = dict()
        actual = 0
        start_idx = 0
        best_length = 0
        l = 0

        for r in range(len(s)):
            char = s[r]
            freq_s[char] = 1 + freq_s.get(char, 0)
            if char in freq_t and freq_s[char] == freq_t[char]:
                actual += 1
            
            while needed == actual:
                if best_length == 0 or (r-l+1) < best_length:
                    start_idx = l
                    best_length = r-l+1

                leaving_char = s[l]
                freq_s[leaving_char] -= 1
                if leaving_char in freq_t and freq_s[leaving_char] < freq_t[leaving_char]:
                    actual -= 1
                
                l += 1
        
        return s[start_idx: start_idx+best_length]
                    
