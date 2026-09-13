class Solution:
    def reverseWords(self, s: str) -> str:
        
        n = len(s)-1
        result = []
        while n >= 0:
            while  n >= 0 and s[n] == ' ':
                n -= 1
            if n < 0:
                break
            end = n
            while n >= 0 and s[n] != ' ':
                n -= 1
            start = n+1
            word = s[start:end+1]
            result.append(word)
        return ' '.join(result)