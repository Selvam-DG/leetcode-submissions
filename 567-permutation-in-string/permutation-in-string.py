class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False
        
        s1_count = dict()
        for char in s1:
            s1_count[char] = 1 + s1_count.get(char, 0)
        
        window_count = dict()
        l = 0
        for r in range(m):
            window_count[s2[r]] = 1 + window_count.get(s2[r], 0)
            while r-l+1 > n:
                window_count[s2[l]] -= 1
                if window_count[s2[l]] == 0:
                    del  window_count[s2[l]]
                l +=1

            if window_count == s1_count:
                return True
            
        return False
