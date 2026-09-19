class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        count_p = dict()
        for char in p:
            count_p[char] = 1 + count_p.get(char, 0)
        m = len(p)
        n = len(s)
        if m > n:
            return []
        window_count = dict()
        result = []
        
        l = 0

        for r in range(n):
            window_count[s[r]] = 1 + window_count.get(s[r], 0)
            while r-l+1 > m:
                window_count[s[l]] -= 1
                if window_count[s[l]] == 0:
                    del window_count[s[l]]
                l += 1
            if window_count == count_p:
                result.append(l)
        
        return result