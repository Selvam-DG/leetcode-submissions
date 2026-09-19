class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        def word2Vec(word):
            count = [0] * 26
            for char in word:
                count[ord(char)-ord('a')] += 1
            
            return count
        group = dict()
        for word in strs:
            key = tuple(word2Vec(word))

            if key not in group:
                group[(key)] = []
            
            group[key].append(word)
        
        return list(group.values())