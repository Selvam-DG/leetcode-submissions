class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        sorted_s = ''.join(sorted(s))

        if n == 1 or s == sorted_s:
            return 0
        if n == 2:
            return -1
        
        if s[0] == sorted_s[0] or s[-1] == sorted_s[-1]:
            return 1
        
        if s[0] > max(s[1:-1]) and s[-1] < min(s[1:-1]):
            return 3

        return 2
