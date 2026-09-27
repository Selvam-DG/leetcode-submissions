class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = {}
        stack = []

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch ==')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
        
        ans = []
        i  = 0
        direction = 1

        while i < n:
            if s[i] == '(' or s[i] == ')':
                i = pair[i]
                direction *= -1
            else:
                ans.append(s[i])
            i += direction
        
        return ''.join(ans)