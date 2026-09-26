class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        replace = dict()
        for i in range(len(knowledge)):
            key, value = knowledge[i]
            replace[key] = value
        
        ans = ''
        n = len(s)
        r = 0
        while r < n:
            while r < n and s[r] != '(':
                ans += s[r]
                r += 1
            if r <n and s[r] == '(':
                key = ''
                r += 1
                start = r
                while r< n and s[r] != ')':
                    r += 1
                end = r
                key = s[start:end]
                if key in replace:
                    ans += replace[key]
                else:
                    ans += '?'
                r += 1
        return ans
