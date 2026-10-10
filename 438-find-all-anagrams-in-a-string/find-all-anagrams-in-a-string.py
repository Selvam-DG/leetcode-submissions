class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = []
        if len(p) > len(s):
            return result
        
        need = [0]* 26
        for char in p:
            need[ord(char)-ord('a')] += 1
        current = [0] * 26
        start = 0
        for end in range(len(s)):
            current[ord(s[end])-ord('a')] += 1

            while (end-start+1) > len(p):
                current[ord(s[start]) - ord('a')] -= 1
                start += 1
            
            if (end-start+1 == len(p) and current == need):
                result.append(start)
        
        return result