class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        stack = []
        curr = 0
        for i,ch in enumerate(s):
            if ch == '(':
                curr += 1
                stack.append(ch)
            elif ch == ')':
                stack.pop()
                curr -= 1
            ans = max(ans, curr)
        
        return ans
                
            
