class Solution:
    def minInsertions(self, s: str) -> int:
        count_open = 0
        count_close = 0
        result = 0

        for char in s:
            if char == '(':
                if count_close == 1:
                    result += 1
                    count_close = 0
                    if count_open:
                        count_open-=1
                    else:
                        result += 1

                count_open += 1
            elif char == ')':
                count_close +=1
                if count_close == 2:
                    if count_open:
                        count_open -= 1
                    else:
                        result += 1
                    count_close = 0
        
        if count_close == 1:
            result += 1
            if count_open:
                count_open -= 1
            else:
                result += 1
        
        return result + 2*count_open
        

            
