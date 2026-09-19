class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        basket = dict()
        max_fruits = 0
        l = 0
        for r in range(n):
            basket[fruits[r]] = 1 + basket.get(fruits[r], 0)
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
            max_fruits = max(max_fruits, r-l+1)
        
        return max_fruits