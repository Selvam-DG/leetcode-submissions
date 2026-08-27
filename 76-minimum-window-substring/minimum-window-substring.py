class Solution:
    def minWindow(self, s: str, t: str) -> str:

        
        need_count = dict()
        for char in t:
            need_count[char] = 1 + need_count.get(char, 0)
        window_count = dict()
        required = len(need_count)
        formed = 0
        left = 0
        best_length = -1
        best_start = 0

        for right in range(len(s)):
            char = s[right]
            window_count[char] = 1 + window_count.get(char, 0)
            if char in need_count and window_count[char] == need_count[char]:
                formed += 1

            while formed == required:
                if (best_length == -1) or (right-left+1)< best_length:
                    best_length = right - left + 1
                    best_start = left
                lchar = s[left]
                window_count[lchar] -= 1
                if lchar in need_count and window_count[lchar] < need_count[lchar]:
                    formed -= 1
                left += 1
                
        if best_length == -1:
            return ""
        return s[best_start: best_start+best_length]
        
