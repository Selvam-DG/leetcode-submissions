class Solution:
    def checkValidString(self, s: str) -> bool:
        minRange = 0
        maxRange = 0

        for ch in s:
            if ch == '(':
                minRange += 1
                maxRange += 1
            elif ch == ')':
                minRange -= 1
                maxRange -= 1
            else:
                minRange -= 1
                maxRange += 1
            
            if maxRange < 0:
                return False
            minRange = max(minRange, 0)
        
        return minRange == 0