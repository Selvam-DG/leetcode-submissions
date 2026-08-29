class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # only 2 baskets
        # no limit on amount of fruit in each basket
        #
        basket = dict()
        n = len(fruits)
        window_start = 0

        max_fruit = 0

        for window_end in range(n):
            basket[fruits[window_end]] = 1 + basket.get(fruits[window_end], 0)

            while len(basket) > 2:
                basket[fruits[window_start]] -= 1
                if basket[fruits[window_start]] == 0:
                    del basket[fruits[window_start]]
                window_start += 1
            max_fruit = max(max_fruit, window_end-window_start+1)
        
        return max_fruit
                 