class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n =len(strs)
        group = dict()
        for word in strs:
            key = tuple(self.word2Vec(word))
            if key not in group:
                group[key] = []
            group[key].append(word)
        
        result = []

        for key, words in group.items():
            temp = []
            for word in words:
                temp.append(word)
            
            result.append(temp)
        
        return result   
    def word2Vec(self, s: str):
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')]  += 1
        
        return count