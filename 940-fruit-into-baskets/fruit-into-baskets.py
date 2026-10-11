class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n = len(fruits)
        result = 0
        count = dict()
        start  = 0

        for end in range(n):
            count[fruits[end]] = 1 + count.get(fruits[end], 0)

            while len(count) > 2:
                count[fruits[start]] -= 1
                if count[fruits[start]] == 0:
                    del count[fruits[start]]
                start += 1
            
            result = max(result, end-start+1)
        
        return result