class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        for i, char in enumerate(s):
            idx = ord(char) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i
        
        result = []
        prev_end = -1

        for i in range(n):
            idx = ord(s[i]) - ord('a')

            if first[idx] != i:
                continue
            
            end = last[idx]
            j = i
            valid = True

            while  j <= end:
                x = ord(s[j]) - ord('a')

                if first[x] < i:
                    valid = False
                    break
                
                end = max(end, last[x])

                j += 1
            
            if not valid:
                continue
            
            if i > prev_end:
                result.append(s[i:end+1])
            else:
                result[-1] = s[i:end+1]
            
            prev_end = end
        
        return result