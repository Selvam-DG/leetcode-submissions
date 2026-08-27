class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if not s or not t:
            return False
        if not s and not t:
            return True
        
        return ''.join(sorted(s)) == ''.join(sorted(t))