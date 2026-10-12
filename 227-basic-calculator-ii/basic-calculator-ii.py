class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        operator = '+'
        num = 0
        for i, char in enumerate(s):
            if char.isnumeric():
                num = num*10 + int(char)
            if (not char.isnumeric() and char != ' ') or i == n-1:
                if operator == '+' :
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '*':
                    stack.append(stack.pop()*num)
                elif operator =='/':
                    prev = stack.pop()
                    quotient = abs(prev) // num
                    stack.append(quotient if prev > 0 else -quotient)
                num = 0
                operator= char
        result = 0
        for num in stack:
            result += num
        return result
