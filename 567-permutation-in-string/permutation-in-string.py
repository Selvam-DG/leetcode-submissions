class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need = [0] * 26

        for char in s1:
            need[ord(char) - ord('a')] += 1
        
        start = 0
        window = [0] * 26
        for end in range(len(s2)):
            window[ord(s2[end]) - ord('a')] += 1
            if end-start+1 > len(s1):
                window[ord(s2[start]) - ord('a')] -= 1
                start += 1

            if (end-start+1) == len(s1) and window == need:
                return True
        
        return False
            
            

