class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:

        count = [0] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1
        
        prefix = []
        n = len(s)

        i = 0

        while i < n:
            idx = ord(target[i]) - ord('a')
            if count[idx] > 0:
                prefix.append(target[i])
                count[idx] -= 1
                i += 1
            else:
                break
        
        while True:
            if i < n:
                curr = ord(target[i]) - ord('a')

                for j in range(curr+1, 26):
                    if count[j] > 0:
                        count[j] -= 1

                        suffix = []

                        for c in range(26):
                            suffix.append(chr(c + ord('a')) * count[c])
                        
                        return ''.join(prefix)+chr(j + ord('a')) + ''.join(suffix)

            if not prefix:
                return ""
            
            i-=1

            removed = prefix.pop()
            count[ord(removed)-ord('a')] += 1