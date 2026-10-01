class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_paren = {'(', '[', '{'}
        parentheses = {')':'(', ']':'[', '}':'{'}
        
        for char in s:
            if char in open_paren:
                stack.append(char)
            else:
                if not stack or stack.pop() != parentheses[char]:
                    return False
        return not stack