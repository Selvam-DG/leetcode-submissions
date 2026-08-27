class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        for i in range(len(strs[0])):
            curr_char = strs[0][i]

            for word in strs:
                if i == len(word) or word[i] != curr_char:
                    return strs[0][0:i]
        return strs[0]
        