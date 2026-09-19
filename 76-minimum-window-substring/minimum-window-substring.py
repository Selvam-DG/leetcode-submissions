class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        count_t = dict()
        for char in t:
            count_t[char] = 1 + count_t.get(char, 0)
        
        need = len(count_t)
        curr_count = dict()
        left = 0
        matched = 0
        best_length = -1
        best_start = 0

        for right in range(n):
            char = s[right]
            curr_count[char] = 1 + curr_count.get(char, 0)
            if char in count_t and curr_count[char] == count_t[char]:
                matched += 1
            
            while matched == need:
                leave_char = s[left]
                if best_length == -1 or (right-left+1) < best_length:
                    best_length = right-left+1
                    best_start = left
                curr_count[leave_char] -= 1
                if leave_char in count_t and curr_count[leave_char] < count_t[leave_char]:
                    matched -= 1
                left += 1
        if best_length == -1:
            return ""
        return s[best_start:best_start+best_length]

                    
                

