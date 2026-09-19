class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        result = []
        pointer = n-1

        while pointer >= 0:

            while pointer >= 0 and s[pointer] == ' ':
                pointer -= 1
            if pointer < 0:
                break

            end = pointer
            while pointer >= 0 and s[pointer] != ' ':
                pointer -= 1

            start = pointer+1
        
            result.append(s[start:end+1])
        
        return ' '.join(result)