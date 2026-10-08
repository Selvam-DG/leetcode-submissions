class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        result = ''
        for i, char in enumerate(s):
            if char =='(':
                if stack:
                    result += char
                stack.append(char)
            else:
               
                stack.pop()
                if stack:
                    result += char
            
        return result