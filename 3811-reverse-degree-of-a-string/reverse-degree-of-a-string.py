class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            result += (i+1)*(26 - (ord(s[i])- ord('a')))
        
        return result