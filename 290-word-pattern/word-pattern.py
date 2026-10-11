class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        
        char2Word = dict()
        word2Char = dict()

        for i in range(len(pattern)):
            word = words[i]
            char = pattern[i]
            if char in char2Word and char2Word[char] != word:
                return False
            if word in word2Char and word2Char[word] != char:
                return False
            char2Word[char] = word
            word2Char[word] = char
        
        return True