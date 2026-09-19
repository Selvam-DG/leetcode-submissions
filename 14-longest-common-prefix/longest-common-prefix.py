class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs[0])
        temp_word = strs[0]
        result = ''
        for i in range(n):
            char = temp_word[i]
            for word in strs:
                if i == len(word) or word[i] != char:
                    return result
            result += char
        
        return result
