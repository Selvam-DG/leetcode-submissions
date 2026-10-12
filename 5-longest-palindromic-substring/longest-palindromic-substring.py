class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandFromCenter(s, left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right-left-1
        length = 0
        bestLength = 0
        bestStart = 0
        for i in range(len(s)):
            oddL = expandFromCenter(s, i ,i)
            evenL = expandFromCenter(s,i, i+1)
            length = max(oddL, evenL)

            if length > bestLength:
                bestLength = length
                bestStart = i - (length-1)//2
            
        
        return s[bestStart:bestStart+bestLength]
        