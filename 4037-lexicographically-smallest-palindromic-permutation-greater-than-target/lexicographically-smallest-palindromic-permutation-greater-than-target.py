class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        
        odd = 0
        middle = ""

        for i in range(26):
            if freq[i] %2 == 1:
                odd += 1
                middle = chr(i + ord('a'))
        
        if odd > 1: 
            return ""
        
        half_count = [x//2  for x in freq]

        half_len = n //2
        target_half = target[:half_len]

        prefix  = []
        i = 0

        while i < half_len:
            idx = ord(target_half[i]) - ord('a')

            if half_count[idx] > 0:
                prefix.append(target_half[i])
                half_count[idx] -= 1
                i += 1
        
            else:
                break
        
        while True:
            if i< half_len:
                curr = ord(target_half[i])-ord('a')

                for j in range(curr+1, 26):
                    if half_count[j]> 0:
                        half_count[j]-= 1

                        suffix= []
                        for c in range(26):
                            suffix.append(chr(c+ord('a')) * half_count[c])
                        
                        left = ''.join(prefix)+ chr(j+ord('a')) + ''.join(suffix)

                        return self.buildPalindrome(left, middle)
            else:
                left = ''.join(prefix)
                candidate = self.buildPalindrome(left, middle)

                if candidate > target:
                    return candidate
            
            if not prefix:
                return ""
            
            i -= 1
            removed = prefix.pop()
            half_count[ord(removed)-ord('a')] += 1
    
    def buildPalindrome(self, left, middle):
        return left + middle+ left[::-1]